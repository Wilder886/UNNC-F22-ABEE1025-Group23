def run_one_simulation_helper(eplus_run_path, idf_path, out_dir, parameter_key, parameter_vals):
    run_eplus_model(eplus_run_path, idf_path, out_dir, parameter_key, parameter_vals)
    import csv
    import os.path
    from pathlib import Path
    import os
    import json
    import pandas as pd
    import numpy as np
    import math
    import copy
    from numpy import array
    from StaticEplusEngine import run_eplus_model, convert_json_idf
    convert_json_idf(eplus_run_path, idf_path)
    epjson_path = idf_path.split('.idf')[0] + '.epJSON'
    with open(epjson_path) as epJSSON:
        epjson_dict = json.load(epJSON)

    convert_json_idf(eplus_run_path, epjson_path)

    inner_dict = epjson_dict
    for i in range(len(parameter_key)):
        if i < len(parameter_key) - 1:
            inner_dict = inner_dict[parameter_key[i]]
    inner_dict[parameter_key[-1]] = parameter_val

    with open(epjson_path, 'w') as epjson:
        jspn.dump(epjson_dict, epjson)
    convert_json_idf(eplus_run_path, epjson_path)
    run_eplus_model(eplus_run_path, idf_path, out_dir)


def run_one_parametric(eplus_run_path, idf_path, output_dir, parameter_key, parameter_vals):
    return (None)










