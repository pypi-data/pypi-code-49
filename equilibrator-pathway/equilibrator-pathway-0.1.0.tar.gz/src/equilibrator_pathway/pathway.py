"""analyze pathways using thermodynamic models."""
# The MIT License (MIT)
#
# Copyright (c) 2013 Weizmann Institute of Science
# Copyright (c) 2018-2020 Institute for Molecular Systems Biology,
# ETH Zurich
# Copyright (c) 2018-2020 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import csv
import logging
import warnings
from typing import Callable, Dict, Iterable, List, TextIO, Tuple

import numpy as np
import pandas as pd
from equilibrator_api import (
    Q_,
    Compound,
    R,
    ccache,
    default_I,
    default_pH,
    default_pMg,
    default_T,
    search_reaction,
)
from equilibrator_api.component_contribution import ComponentContribution
from equilibrator_api.phased_reaction import PhasedReaction
from equilibrator_cache.reaction import (
    create_stoichiometric_matrix_from_reactions,
)
from sbtab import SBtab

from .bounds import Bounds
from .thermo_models import PathwayMDFData, PathwayThermoModel


class Pathway(object):
    """A pathway parsed from user input.

    Designed for checking input prior to converting to a stoichiometric model.
    """

    def __init__(
        self,
        reactions: List[PhasedReaction],
        fluxes: np.ndarray,
        standard_dg_primes: np.ndarray = None,
        dg_sigma: np.ndarray = None,
        bounds: Bounds = None,
        config_dict: Dict[str, str] = None,
    ) -> object:
        """Initialize.

        :param reactions: a list of gibbs.reaction.Reaction objects.
        :param fluxes: numpy.array of relative fluxes in same order as
        reactions.
        :param standard_dg_primes: reaction energies (in kJ/mol)
        :param dg_sigma: square root of the uncertainty covariance matrix
        (in kJ/mol)
        :param bounds: bounds on metabolite concentrations. Uses default
        bounds if None provided.
        """
        self.reactions = reactions
        Nr = len(reactions)

        if bounds is None:
            self._bounds = Bounds.GetDefaultBounds().Copy()
        else:
            self._bounds = bounds.Copy()

        self.p_h = default_pH
        self.p_mg = default_pMg
        self.ionic_strength = default_I
        self.temperature = default_T
        self.config_dict = config_dict or dict()
        self.configure()

        # make sure the bounds on Water are (1, 1)
        self._bounds.SetBounds(ccache.water, Q_(1.0, "M"), Q_(1.0, "M"))

        self.S = create_stoichiometric_matrix_from_reactions(
            reactions, ccache.is_proton, ccache.is_water, ccache.water
        )

        assert fluxes.unitless or fluxes.check("[concentration]/[time]")
        self.fluxes = fluxes.flatten()
        assert self.fluxes.shape == (Nr,)

        self.comp_contrib = None
        if standard_dg_primes is None:
            assert dg_sigma is None, (
                "If standard_dg_primes are not "
                "provided, dg_sigma must also be None"
            )
            self.update_standard_dgs()
        else:
            assert standard_dg_primes.check("[energy]/[substance]")
            assert standard_dg_primes.shape == (Nr,)
            # dGr should be orthogonal to nullspace of S
            # If not, dGr is not contained in image(S) and then there
            # is no consistent set of dGfs that generates dGr and the
            # first law of thermo is violated by the model.
            S_T = self.S.T.values
            S_inv = np.linalg.pinv(S_T)
            null_proj = np.eye(self.S.shape[1]) - S_T @ S_inv
            projected = null_proj @ standard_dg_primes.T
            assert (projected < Q_("1e-8 kJ/mol")).all(), (
                "Supplied reaction standard deltaG values are inconsistent "
                "with the stoichiometric matrix."
            )

            self.standard_dg_primes = standard_dg_primes

            if dg_sigma is None:
                self.dg_sigma = None
            else:
                assert dg_sigma.shape == (Nr, Nr)
                self.dg_sigma = dg_sigma

        # Set the compound names by to their default strings, these names can
        # be changed later using the same function (set_compound_names)
        self.compound_names = None
        self.set_compound_names(str)

    def configure(self) -> None:
        if "p_h" in self.config_dict:
            self.p_h = Q_(self.config_dict["p_h"])
            assert self.p_h.check(""), "pH must be given without units"

        if "p_mg" in self.config_dict:
            self.p_mg = Q_(self.config_dict["p_mg"])
            assert self.p_mg.check(""), "pMg must be given without units"

        if "ionic_strength" in self.config_dict:
            self.ionic_strength = Q_(self.config_dict["ionic_strength"])
            assert self.ionic_strength.check(
                "[concentration]"
            ), "ionic_strength must be given in concentration units"

        if "temperature" in self.config_dict:
            self.temperature = Q_(self.config_dict["temperature"])
            assert self.temperature.check(
                "[temperature]"
            ), "temperature must be given in Kalvin"

        # this is the factor by which the STDEV matrix is multiplied to create
        # the confidence margins for the Gibbs energies of reaction
        self.stdev_factor = float(self.config_dict.get("stdev_factor", "0"))

    def update_standard_dgs(self,) -> None:
        """Set the aqueous conditions and recalculate the standard dG' values.
        """
        if self.comp_contrib is None:
            self.comp_contrib = ComponentContribution(
                p_h=self.p_h,
                p_mg=self.p_mg,
                ionic_strength=self.ionic_strength,
                temperature=self.temperature,
            )
        else:
            self.comp_contrib.p_h = self.p_h
            self.comp_contrib.p_mg = self.p_mg
            self.comp_contrib.ionic_strength = self.ionic_strength
            self.comp_contrib.temperature = self.temperature

        (
            self.standard_dg_primes,
            self.dg_sigma,
        ) = self.comp_contrib.standard_dg_prime_multi(self.reactions)

    def set_compound_names(self, mapping: Callable[[Compound], str]) -> None:
        """Use alternative compound names for outputs such as plots.

        :param mapping: a dictionary mapping compounds to their names in the
        model
        """
        self.compound_names = list(map(mapping, self.S.index))

    @property
    def bounds(self) -> Tuple[Iterable[float], Iterable[float]]:
        """Get the concentration bounds.

        The order of compounds is according to the stoichiometric matrix index.
        :return: tuple of (lower bounds, upper bounds)
        """
        return self._bounds.GetBounds(self.S.index)

    @property
    def ln_conc_lb(self) -> np.array:
        """Get the log lower bounds on the concentrations.

        The order of compounds is according to the stoichiometric matrix index.
        :return: a NumPy array of the log lower bounds
        """
        return np.array(
            list(map(float, self._bounds.GetLnLowerBounds(self.S.index)))
        )

    @property
    def ln_conc_ub(self) -> np.array:
        """Get the log upper bounds on the concentrations.

        The order of compounds is according to the stoichiometric matrix index.
        :return: a NumPy array of the log upper bounds
        """
        return np.array(
            list(map(float, self._bounds.GetLnUpperBounds(self.S.index)))
        )

    @staticmethod
    def get_compounds(reactions: Iterable[PhasedReaction]) -> List[Compound]:
        """Get a unique list of all compounds in all reactions.

        :param reactions: an iterator of reactions
        :return: a list of unique compounds
        """
        compounds = set()
        for r in reactions:
            compounds.update(r.keys())

        return sorted(compounds)

    def calc_mdf(self) -> PathwayMDFData:
        """Calculate the Max-min Driving Force.

        :param stdev_factor: the factor by which to multiply the uncertainties
        :return: a PathwayMDFData object with the results
        """
        return PathwayThermoModel(self, self.stdev_factor).FindMDF()

    @property
    def reaction_ids(self) -> Iterable[str]:
        """Iterate through all the reaction IDs.

        :return: the reaction IDs
        """
        return map(lambda rxn: rxn.rid, self.reactions)

    @property
    def reaction_formulas(self) -> Iterable[str]:
        """Iterate through all the reaction formulas.

        :return: the reaction formulas
        """
        return map(str, self.reactions)

    @property
    def net_reaction(self) -> PhasedReaction:
        """Calculate the sum of all the reactions in the pathway.

        :return: the net reaction
        """
        net_rxn_stoich = self.S @ self.fluxes.magnitude
        net_rxn_stoich = net_rxn_stoich[net_rxn_stoich != 0]
        sparse = net_rxn_stoich.to_dict()
        return PhasedReaction(sparse)

    @classmethod
    def from_csv(
        cls,
        f: TextIO,
        bounds: Bounds = None,
        p_h: float = default_pH,
        p_mg: float = default_pMg,
        ionic_strength: float = default_I,
        temperature: float = default_T,
    ) -> object:
        """Parse a CSV file and return a Pathway object.

        Caller responsible for closing f.

        :param f: file-like object containing CSV data describing the pathway
        :param bounds: a Bounds object
        :param p_h:
        :param p_mg:
        :param ionic_strength:
        :param: temperature:
        :return: a Pathway object
        """
        reactions = []
        fluxes = []

        for row in csv.DictReader(f):
            rxn_formula = row.get("ReactionFormula")

            flux = float(row.get("Flux", 0.0))
            logging.debug("formula = %f x (%s)", flux, rxn_formula)

            rxn = search_reaction(rxn_formula)
            rxn.is_balanced(ignore_atoms=["H"])

            reactions.append(rxn)
            fluxes.append(flux)

        v = np.array(fluxes)

        config_dict = {
            "p_h": str(p_h),
            "p_mg": str(p_mg),
            "ionic_strength": str(ionic_strength),
            "temperature": str(temperature),
        }
        pp = Pathway(reactions, v, bounds=bounds, config_dict=config_dict)
        return pp

    @staticmethod
    def from_sbtab(sbtabdoc: SBtab.SBtabDocument) -> object:
        """Parse and SBtabDocument and return a Pathway.

        :param sbtabdoc: an SBtabDocument defining the pathway
        :return: a Pathway object
        """

        # Read the configuration table if it exists
        config_sbtab = sbtabdoc.get_sbtab_by_id("Configuration")
        if config_sbtab:
            config_df = config_sbtab.to_data_frame()
            assert (
                "Option" in config_df.columns
            ), "Configuration table must have an Option column"
            assert (
                "Value" in config_df.columns
            ), "Configuration table must have an Value column"
            config_dict = config_df.set_index("Option").Value.to_dict()
        else:
            config_dict = dict()

        table_ids = ["Compound", "ConcentrationConstraint", "Reaction", "Flux"]
        dfs = []

        for table_id in table_ids:
            sbtab = sbtabdoc.get_sbtab_by_id(table_id)
            if sbtab is None:
                tables = ", ".join(map(lambda s: s.table_id, sbtabdoc.sbtabs))
                raise ValueError(
                    f"The SBtabDocument must have a table "
                    f"with the following ID: {table_id}, "
                    f"however, only these tables were "
                    f"found: {tables}"
                )
            dfs.append(sbtab.to_data_frame())

        compound_df, bounds_df, reaction_df, flux_df = dfs

        # Read the Compound table
        # -----------------------
        # use equilibrator-cache to build a dictionary of compound IDs to
        # Compound objects
        compound_df.set_index("ID", inplace=True)

        # legacy option, KEGG IDs could be provided without the namespace
        # when the column title  explicitly indicated that they were from KEGG
        if "Identifiers:kegg.compound" in compound_df.columns:
            compound_df["Identifiers"] = (
                "kegg:" + compound_df["Identifiers:kegg.compound"]
            )

        # Now, by default, we assume the namespaces are provided as part of the
        # reaction formulas
        if "Identifiers" not in compound_df.columns:
            raise KeyError(
                "There is no column of Identifiers in the Compound table"
            )

        compound_df["Compound"] = compound_df["Identifiers"].apply(
            ccache.get_compound
        )

        if pd.isnull(compound_df.Compound).any():
            accessions_not_found = compound_df.loc[
                pd.isnull(compound_df.Compound), "Identifiers"
            ]
            error_msg = str(accessions_not_found.to_dict())
            raise KeyError(
                f"Some compounds not found in equilibrator-cache: "
                f"{error_msg}"
            )

        # Read the ConcentrationConstraints table
        # ---------------------------------------
        # convert compound IDs in the bounds table to Compound objects
        name_to_compound = compound_df.Compound.to_dict()
        bounds_df["Compound"] = bounds_df.Compound.apply(name_to_compound.get)
        bounds_df.set_index("Compound", inplace=True)

        bounds_sbtab = sbtabdoc.get_sbtab_by_id("ConcentrationConstraint")
        try:
            bounds_unit = bounds_sbtab.get_attribute("Unit")
            lbs = bounds_df["Min"].apply(lambda x: Q_(float(x), bounds_unit))
            ubs = bounds_df["Max"].apply(lambda x: Q_(float(x), bounds_unit))
        except SBtab.SBtabError:
            # if the unit is not defined in the header, we assume it is given
            # next to each bound individually
            lbs = bounds_df["Min"].apply(Q_)
            ubs = bounds_df["Max"].apply(Q_)

        bounds = Bounds(lbs.to_dict(), ubs.to_dict())
        bounds._check_bounds()

        # Read the Reaction table
        # -----------------------
        reactions = []
        reaction_ids = []
        for row in reaction_df.itertuples():
            rxn = PhasedReaction.parse_formula(
                name_to_compound.get, row.ReactionFormula
            )
            rxn.rid = row.ID
            if not rxn.is_balanced(ignore_atoms=("H",)):
                warnings.warn(f"Reaction {rxn.rid} is not balanced")
            reactions.append(rxn)
            if row.ID in reaction_ids:
                raise KeyError(
                    f"Reaction IDs must be unique, but you have "
                    f"{row.ID} twice"
                )
            reaction_ids.append(row.ID)

        # Read the Flux table
        # ---------------------------
        flux_sbtab = sbtabdoc.get_sbtab_by_id("Flux")
        fluxes = (
            flux_df.set_index("Reaction")
            .loc[reaction_ids, "Value"]
            .apply(float)
        )

        fluxes = np.array(fluxes.values, ndmin=2, dtype=float).T

        try:
            # convert fluxes to M/s if they are in some other absolute unit
            flux_unit = flux_sbtab.get_attribute("Unit")
            fluxes *= Q_(1.0, flux_unit)
        except SBtab.SBtabError:
            # otherwise, assume these are relative fluxes
            fluxes *= Q_("dimensionless")

        thermo_sbtab = sbtabdoc.get_sbtab_by_id("Thermodynamics")
        if thermo_sbtab:
            rid2dg0 = Pathway.ReadThermodynamics(thermo_sbtab, config_dict)

            # make sure all reactions have a standard Gibbs energy
            assert set(reaction_ids).issubset(rid2dg0.keys()), (
                "Not all reactions have a equilibrium constant or gibbs energy "
                "in the 'Thermodynamics' table."
            )
            standard_dg_primes = np.array(
                [rid2dg0[rid].m_as("kJ/mol") for rid in reaction_ids]
            ) * Q_("1 kJ/mol")

            pp = Pathway(
                reactions,
                fluxes=fluxes,
                standard_dg_primes=standard_dg_primes,
                dg_sigma=None,
                bounds=bounds,
                config_dict=config_dict,
            )
        else:
            pp = Pathway(
                reactions, fluxes=fluxes, bounds=bounds, config_dict=config_dict
            )

        # override the compound names with the ones in the SBtab
        compound_to_name = dict(map(reversed, name_to_compound.items()))
        pp.set_compound_names(compound_to_name.get)
        return pp

    @staticmethod
    def ReadThermodynamics(
        thermo_sbtab: SBtab.SBtabTable, config_dict: Dict[str, str]
    ) -> Dict[str, Q_]:

        try:
            std_conc = thermo_sbtab.get_attribute("StandardConcentration")
            assert Q_(std_conc) == Q_(
                "1 M"
            ), "We only support a standard concentration of 1 M."
        except SBtab.SBtabError:
            pass

        if "temperature" in config_dict:
            temperature = Q_(config_dict["temperature"])
            assert temperature.check("[temperature]")
        else:
            temperature = default_T

        thermo_df = thermo_sbtab.to_data_frame()
        cols = ["QuantityType", "Value", "Compound", "Reaction", "Unit"]

        rid2dg0 = dict()
        for i, row in thermo_df.iterrows():
            try:
                typ, val, cid, rid, unit = [row[c] for c in cols]
                val = Q_(float(val), unit)

                if typ == "equilibrium constant":
                    assert val.check(
                        ""
                    ), f"equilibrium constants must have no units"
                    rid2dg0[rid] = -np.log(val.m_as("")) * R * temperature
                elif typ == "reaction gibbs energy":
                    assert val.check(
                        "[energy]/[substance]"
                    ), f"Gibbs energies must be in kJ/mol (or equivalent)"
                    val.ito("kJ/mol")
                    rid2dg0[rid] = val
                else:
                    raise AssertionError(
                        "unrecognized Rate Constant Type: " + typ
                    )
            except AssertionError:
                raise ValueError(
                    "Syntax error in Parameter table, row %d - %s" % (i, row)
                )

        return rid2dg0
