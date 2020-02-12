# Copyright 2019 Okera Inc. All Rights Reserved.
#
# Some integration tests for auth in PyOkera
#
# pylint: disable=global-statement
# pylint: disable=no-self-use
# pylint: disable=no-else-return


import datetime
import json
import warnings

import pytest
import numpy

import requests

from okera import context

API_URL = "http://localhost:5000"

def get_scan_as_json(conn, dataset):
    data = conn.scan_as_json(
        dataset, strings_as_utf8=True,
        max_records=10, max_client_process_count=1)
    return data

def get_scan_as_pandas(conn, dataset):
    def convert_types(datum):
        if isinstance(datum, datetime.datetime):
            return datum.replace(tzinfo=None).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        elif isinstance(datum, numpy.int64):
            return int(datum)
        elif isinstance(datum, dict):
            for key, value in datum.items():
                datum[key] = convert_types(value)
            return datum
        elif isinstance(datum, list):
            return [convert_types(child) for child in datum]

        return datum

    data = conn.scan_as_pandas(
        dataset, strings_as_utf8=True,
        max_records=10, max_client_process_count=1)
    data = data.replace({numpy.nan: None})
    data = data.to_dict('records')
    return convert_types(data)

def get_scan_from_rest(dataset):
    headers = {'content-type': 'application/json'}
    query = {'query': 'SELECT * FROM %s' % dataset}
    response = requests.post(
        API_URL + '/api/scan?records=10',
        json=query, headers=headers)
    result = json.loads(response.text)
    return result

def format(data):
    return json.dumps(data, sort_keys=True, indent=1)

@pytest.mark.parametrize("dataset", [
    'rs_complex.array_struct_array',
    'rs_complex.array_struct_t',
    'rs_complex.array_t',
    'rs_complex.avrotbl',
    'rs_complex.bytes_type',
    'rs_complex.bytes_type_file',
    'rs_complex.enum_type',
    'rs_complex.enum_type_default',
    'rs_complex.map_t',
    'rs_complex.market_decide_single_avro',
    'rs_complex.market_v20_single',
    'rs_complex.market_v30_single',
    'rs_complex.multiple_structs_nested',
    'rs_complex.strarray_t',
    'rs_complex.strarray_t_view',
    'rs_complex.struct_array_struct',
    'rs_complex.struct_nested',
    'rs_complex.struct_nested_s1',
    'rs_complex.struct_nested_s1_f1',
    'rs_complex.struct_nested_s1_s2',
    'rs_complex.struct_nested_view',
    'rs_complex.struct_t',
    'rs_complex.struct_t2',
    'rs_complex.struct_t3',
    'rs_complex.struct_t_id',
    'rs_complex.struct_t_s1',
    'rs_complex.struct_t_view',
    'rs_complex.struct_t_view2',
    'rs_complex.user_phone_numbers',
    'rs_complex.user_phone_numbers_map',
    'rs_complex.users',
    'rs_complex.view_over_multiple_structs',
    'rs_complex_parquet.array_struct_array',
    'rs_complex_parquet.array_struct_t',
    'rs_complex_parquet.array_struct_t2',
    'rs_complex_parquet.array_t',
    'rs_complex_parquet.bytes_type',
    'rs_complex_parquet.enum_type',
    'rs_complex_parquet.map_array',
    'rs_complex_parquet.map_array_t2',
    'rs_complex_parquet.map_struct_array_t',
    'rs_complex_parquet.map_struct_array_t_view',
    'rs_complex_parquet.map_struct_t',
    'rs_complex_parquet.map_struct_t_view',
    'rs_complex_parquet.map_t',
    'rs_complex_parquet.strarray_t',
    'rs_complex_parquet.struct_array_struct',
    'rs_complex_parquet.struct_nested',
    'rs_complex_parquet.struct_nested_s1',
    'rs_complex_parquet.struct_nested_s1_f1',
    'rs_complex_parquet.struct_nested_s1_s2',
    'rs_complex_parquet.struct_nested_view',
    'rs_complex_parquet.struct_t',
    'rs_complex_parquet.struct_t2',
    'rs_complex_parquet.struct_t3',
    'rs_complex_parquet.struct_t_id',
    'rs_complex_parquet.struct_t_s1',
    'rs_complex_parquet.struct_t_view',
    'rs_complex_parquet.struct_t_view2',
    # # The ones below don't work because the /scan API returns the wrong value
    # # for decimals
    # 'rs_complex_parquet.spark_all_mixed_compression',
    # 'rs_complex_parquet.spark_gzip',
    # 'rs_complex_parquet.spark_snappy',
    # 'rs_complex_parquet.spark_snappy_part',
    # 'rs_complex_parquet.spark_uncompressed',
    # 'rs_complex_parquet.spark_uncompressed_legacy_format',
    'customer.zd277_complex',
    'rs_json_format.complex_c1_case_sensitive',
    'rs_json_format.complex_c1_usecase',
    'rs_json_format.complex_nike_usecase',
    # NOT WORKING array of arrays is not allowed, scan error
    # 'rs_json_format.json_array_arrays',
    'rs_json_format.json_array_struct',
    'rs_json_format.json_arrays_test',
    # # These tables don't work because Pandas and JSON don't serialize to the
    # # exact same types (e.g. float vs int), even though the overall data is correct)
    # 'rs_json_format.json_inferred',
    # 'rs_json_format.json_primitives',
    # 'rs_json_format.json_primitives_inferred',
    'rs_json_format.json_struct',
    'rs_json_format.json_struct_array',
    'rs_json_format.json_struct_nested',
    'rs_json_format.primitives_with_array',
])
def test_basic(dataset):
    warnings.filterwarnings("ignore", message="numpy.dtype size changed")
    ctx = context()
    with ctx.connect(host='localhost', port=12050) as conn:
        json_data = get_scan_as_json(conn, dataset)
        pandas_data = get_scan_as_pandas(conn, dataset)
        rest_data = get_scan_from_rest(dataset)
        assert format(json_data) == format(pandas_data)
        assert format(json_data) == format(rest_data)
