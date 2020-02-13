from copy import deepcopy
from logging import getLogger
from os.path import join, exists, splitext, dirname

import numpy as np
import pandas as pd
from pymagicc.io import (
    convert_magicc_to_openscm_regions,
    convert_magicc7_to_openscm_variables,
    MAGICCData,
)
from scipy.io import loadmat
from scmdata import df_append, ScmDataFrame

from .distributions import Uniform, Normal
from .finder import PointEstimateFinder
from .parameterset import KeyedParameterSet

logger = getLogger(__name__)


def _lookup_param_col(df, param, model_code):
    try:
        v = df.set_index("purpose").at[param, model_code]
    except KeyError:
        return None
    return _maybe_as_float(v)


def _maybe_as_float(v):
    if isinstance(v, list):
        return list(map(_maybe_as_float, v))

    try:
        v_as_float = float(v)
        if v_as_float != int(v):
            return v_as_float
    except ValueError:
        pass

    try:
        return int(v)
    except ValueError:
        return v


def _get_var_info(p):
    if p["name"] == "CARBONCYCLE":
        return {"variable": "CARBONCYCLE_" + p["colcode"], "region": "World"}
    else:
        if p["colcode"].startswith("BOX"):
            p["colcode"] = p["colcode"][3:]
        return {
            "variable": p["name"],
            "region": convert_magicc_to_openscm_regions(p["colcode"])
            if p["colcode"]
            else None,
        }


def _handle_simcap_varnames(p, fname):
    """
    Interpret variable/region data from simcap naming convention
    """
    res = _get_var_info(p)

    if "_WITHIN_" in fname:
        v, fname = fname.split("_WITHIN_")
        res["file_variable"] = v
    elif p["name"] == "CARBONCYCLE":
        res["file_variable"] = p["colcode"]
    else:
        res["file_variable"] = p["name"]
    if '|' in fname:
        fname, region = fname.split('|')
        res["file_region"] = convert_magicc_to_openscm_regions(region)
    res["file"] = fname

    return res


def get_target(tuning_data, data_dir=None):
    weights = []
    data = []

    for sce in tuning_data:
        for t in tuning_data[sce]:
            if 'data' in t:
                df = t['data']
                assert len(df['variable'].unique()) == 1
                err_msg = "No valid data for scenario {}".format(sce)
            else:
                variable = t["file_variable"]
                region = t.get("region", "World")
                file_name = t["file"]
                if data_dir is not None:
                    file_name = join(data_dir, file_name)

                err_msg = "Could not find data for scenario {}, variable {} and region {} in {}".format(
                    sce, variable, region, file_name
                )

                _, file_ext = splitext(file_name.lower())
                if file_ext == ".mat":
                    logger.error(".mat files are no longer supported")
                    continue
                elif file_ext == ".mag":
                    df = MAGICCData(file_name)
                elif file_ext == ".csv":
                    df = ScmDataFrame(
                        pd.read_csv(file_name)
                    )  # read as a normal SCM Dataframe
                    if len(df["scenario"].unique()) > 1:
                        # if there are more th
                        df = df.filter(scenario=sce)
                        if not len(df):
                            logger.error(err_msg)
                            continue
                    else:
                        # If only one scenario is present assume that it is correct
                        if sce not in df["scenario"].values:
                            logger.error(
                                "Scenario {} was not found in {}. Assuming data from scenario".format(
                                    sce, file_name
                                )
                            )

                else:
                    raise ValueError(
                        "Unknown file extension encountered: {}".format(file_ext)
                    )

                if variable in df["variable"].values:
                    df = df.filter(variable=variable, region=region)
                elif convert_magicc7_to_openscm_variables(variable) in df["variable"].values:
                    df = df.filter(
                        variable=convert_magicc7_to_openscm_variables(variable),
                        region=region,
                    )
                else:
                    if len(df['variable'].unique()) == 1:
                        logger.warning("Could not find variable name {}. Assuming single variable file".format(variable))
                        df = df.filter(
                            region=t["region"],
                        )
                    else:
                        logger.error(err_msg)
                        continue

            if len(df):
                # scmcallib only uses year , and ignores month, day
                df["time"] = df["year"]
                df["scenario"] = sce
                if "variable" in t:
                    v = t["variable"]
                    if t["variable"].startswith("DAT_"):
                        # Check if the openscm name can be parsed
                        v = convert_magicc7_to_openscm_variables(t["variable"][4:])
                    df["variable"] = v
                data.append(df)

                # Copy the df and setup the weights
                w = deepcopy(df)
                w._data.loc[:, :] = t["weight"] if "weight" in t else 1.0
                weights.append(w)
            else:
                logger.error(err_msg)

    return df_append(data), df_append(weights)


def read_scenset(fname):
    if fname is None or not exists(fname):
        logger.warning("Not using scensets data")
        return None, []

    if fname.lower().endswith(".mat"):
        logger.warning("Using .mat file for SCENSETS. Please update to .csv format")
        scenset = loadmat(fname, struct_as_record=False, squeeze_me=True)["SCENSETS"]
        sces = []
        for sce in scenset._fieldnames:
            assert sce.startswith("SCENSET_")
            inner = getattr(scenset, sce)
            res = {k: getattr(inner, k) for k in inner._fieldnames}
            res["scenario"] = sce[len("SCENSET_"):]
            sces.append(res)
        df = pd.DataFrame(sces).set_index("scenario")

    elif fname.lower().endswith(".csv"):
        df = pd.read_csv(fname, index_col=0)
        df = df.drop(["COMMENTS", "UPPERNAME"], axis=1)
        df.index = [d.upper() for d in df.index]

        # All other missing values are empty strings
        # The SCENSETS's don't contain any nan float/int parameters
        df = df.fillna("")

        def group_cols(f):
            # The FILE_EMISSCEN_X shouldn't be grouped together
            if f.startswith('FILE_EMISSCEN'):
                return f

            toks = f.split('_')
            try:
                int(toks[-1])
                return '_'.join(toks[:-1])
            except:
                return f

        def convert_to_lists(df):
            if df.shape[1] > 1:
                col_name = '_'.join(df.columns[0].split('_')[:-1])

                # Sort the columns (Can't do it using sort_index as the int values arenot right aligned integers)
                sorted_order = np.argsort([int(x.split('_')[-1]) for x in df.columns])
                df = df.iloc[:, sorted_order]
                return pd.Series(df.values.tolist(), index=df.index, name=col_name)
            return df.iloc[:, 0]

        # This converts the FGAS_FILES_CONC_X into a list
        df = df.groupby(group_cols, axis=1).apply(convert_to_lists)
    else:
        raise ValueError('Cannot read xtrasens file {}'.format(fname))

    return df


def get_scenario_params(scensets, s, model_name, variant):
    if scensets is not None and s.upper() in scensets.index:
        p = scensets.loc[s.upper()].dropna().to_dict()
    else:
        p = {}
        logger.error("Could not find scenset values for {}".format(s))

    # format any flags which have braces in them
    for k in p:
        if isinstance(p[k], str):
            if '{' in p[k]:
                model_variant = "{}_{}".format(model_name, variant)
                p[k] = p[k].format(
                    MODEL=model_name,
                    VARIANT=variant,
                    MODELVARIANT=model_variant
                ).upper()
        else:
            p[k] = _maybe_as_float(p[k])
    return p


def read_csv_tuningcore(
    fname,
    data_dir=None,
    scensets_fname="SCENSETS.csv",
    sep=";",
):
    """
    Read in a tuning core file

    Parameters
    ----------
    fname: str
        Name of the file to read
    data_dir: str
        Where the SCENSETS files are located. If no directory is provided it defaults to the same directory as the
        tuningcore
    scensets_fname: str
        Filename of the scensets file
    sep: {',', ';'}
        Separator used in the csv file

    Returns
    -------
    dict
        A dict containing the information parsed from the tuning file
    """
    df = pd.read_csv(fname, sep=sep, skiprows=4, header=None)
    res = {"runs": []}

    if data_dir is None:
        data_dir = dirname(fname)

    # We are referencing specific col/row numbers as that is how simcap also does it

    model_info = df.iloc[5:, 1:5]
    model_info.columns = pd.Index(["code", "name", "descr", "do_tuning"])

    parameters = df.iloc[:, 5:].T

    # Not needed, but helps with my sanity
    cols = ["name", "scenario", "colcode", "purpose", "description"] + [
        str(v) for v in model_info["code"]
    ]
    parameters.columns = pd.Index(cols)

    scenarios = parameters["scenario"].dropna().unique()

    scensets = read_scenset(join(data_dir, scensets_fname))

    for _, m in model_info.iterrows():
        # Header info
        model = {
            "code": m["code"],
            "name": m["name"],
            "description": m["descr"],
            "do_tuning": True if m["do_tuning"] == "1" else False,
            "fixed_parameters": [],
            "free_parameters": [],
            "scenarios": [],
            "transforms": [],
        }
        model_name = m["code"]

        scenario_info = {}

        # Get the scenario data from the SCENSET file
        for s in scenarios:
            p = get_scenario_params(scensets, s, model_name=model_name, variant=model["name"])

            scenario_info[s] = {
                "tuning_data": [],
                "parameters": p
            }

        # Handle each column in the order which it is added
        for _, p in parameters.iterrows():
            if p["purpose"] == "FIXEDVALUE":
                # Fixed parameter
                model["fixed_parameters"].append(
                    {"name": p["name"], "value": _maybe_as_float(p[model_name])}
                )
            elif p["purpose"] == "STARTVALUE":
                # Free parameter
                parameter_cols = parameters[parameters["name"] == p["name"]]

                val = _maybe_as_float(p[model_name])
                parameter = {"name": p["name"], "value": val}

                v = _lookup_param_col(parameter_cols, "MIN", model_name)
                if v is not None:
                    parameter["min"] = v

                v = _lookup_param_col(parameter_cols, "MAX", model_name)
                if v is not None:
                    parameter["max"] = v

                v = _lookup_param_col(parameter_cols, "DISTRIBUTION", model_name)
                if v is not None:
                    parameter["distribution"] = v
                else:
                    parameter["distribution"] = "uniform"

                model["free_parameters"].append(parameter)
            elif p["purpose"] == "DATSOURCE":
                # Figure out the different file format which simcap specifies
                # Namely, interpret a variable and region from name and colcode
                d = _handle_simcap_varnames(p, p[model_name])
                parameter_cols = parameters[
                    (parameters["name"] == p["name"])
                    & (parameters["scenario"] == p["scenario"])
                    & (parameters["colcode"] == p["colcode"])
                    ]
                weight = _lookup_param_col(parameter_cols, "WEIGHT", model_name)
                if weight is not None:
                    d["weight"] = weight
                scenario_info[p["scenario"]]["tuning_data"].append(d)
            elif p["purpose"] == "TRANSFORM":
                d = _get_var_info(p)
                d["scenario"] = p["scenario"]
                transform = {"transform": p[model_name]}
                # Remove any empty strings
                for k in d:
                    if d[k]:
                        transform[k] = d[k]
                model["transforms"].append(transform)
            elif p["purpose"] == "XTRASCENSETTING":
                # We now ignore XTRASCENSETTING flags as the SCENSET can now have scenario_specific namings
                pass

        # Flatten the scenarios object
        model["scenarios"] = [
            {
                "name": s,
                "tuning_data": scenario_info[s]["tuning_data"],
                "parameters": scenario_info[s]["parameters"],
            }
            for s in scenario_info
        ]
        res["runs"].append(model)

    return res


def _check_if_local(k, v, data_dir=None):
    if data_dir is None or not isinstance(v, str):
        return v

    if v and exists(join(data_dir, v)):
        v = join(data_dir, v)
        logger.info("Using {} for {}".format(v, k))

    return v


def create_point_model(model, data_dir=None, **kwargs):
    """

    Create a new model point estimate model instance from a configuration dict

    Note that a tuning core file may specify multiple calibration models. This function expects a single dict

    Parameters
    ----------
    model : dict
        Required keys (fixed_parameters, free_parameters)

        scenario: List of scenario definitions
            name : Name of the scenario
            parameters: List of fixed parameters for a given scenario
            tuning_data: List of scenario specific tuning_data
    data_dir: str or path
        All data are loaded relative to this path
    Returns
    -------
    An instance of a PointEstimateFinder which has its parameter's and target's set

    """

    assert isinstance(model, dict)

    # Quick validation
    required_keys = ["fixed_parameters", "free_parameters"]
    for k in required_keys:
        if k not in model:
            raise ValueError('The model dict didnt contain a "{}" key'.format(k))
    scenarios = model.get("scenarios", [])

    config_dimensions = {
            "scenario": [s["name"] for s in scenarios]
        }
    if "extra_dimensions" in model:
        config_dimensions = {**config_dimensions, **model["extra_dimensions"]}

    params = KeyedParameterSet(config_dimensions)

    for p in model["fixed_parameters"]:
        params.set_config(p["name"], _check_if_local(p["name"], p["value"], data_dir))

    for p in model["free_parameters"]:
        if p["distribution"] == "uniform":
            dist = Uniform(lower=p["min"], upper=p["max"])
        elif p["distribution"] == "normal":
            dist = Normal(mu=p["mean"], sd=p["sd"])
        else:
            raise ValueError("Unknown distribution {}".format(p["distribution"]))
        params.set_tune(p["name"], dist, x0=p.get("value", None))

    # Find all the scenario parameters used
    sce_param_names = set()
    for sce in scenarios:
        for p in sce["parameters"]:
            sce_param_names.add(p)

    for p in sce_param_names:
        items = {
            (sce["name"],): _check_if_local(sce["name"], sce["parameters"].get(p, None), data_dir)
            for sce in scenarios
        }
        params.set_config(p, items, dims=("scenario",))

    m = PointEstimateFinder(params, **kwargs)

    # Load the data
    data, weights = get_target({sce["name"]: sce["tuning_data"] for sce in scenarios}, data_dir=data_dir)
    m.set_target(data, iter_over=config_dimensions.keys(), weights=weights)

    # Check if there are any transforms on the tuning data
    for sce in scenarios:
        for d in sce["tuning_data"]:
            if "transform" in d:
                v = d["variable"]
                if d["variable"].startswith("DAT_"):
                    # Check if the openscm name can be parsed
                    v = convert_magicc7_to_openscm_variables(d["variable"][4:])
                m.apply_transform(d["transform"], filters={
                    "scenario": sce["name"],
                    "variable": v,
                    "region": d["region"]
                })

    if "transforms" in model:
        for t in model["transforms"]:
            transform = t.pop("transform")
            m.apply_transform(transform, filters=t)

    return m
