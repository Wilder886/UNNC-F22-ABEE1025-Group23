import json
import copy
import os
from StaticEplusEngine import run_eplus_model, convert_json_idf


def run_one_simulation_helper(eplus_run_path, idf_path, output_dir,
                              parameter_key, parameter_val):


    convert_json_idf(eplus_run_path, idf_path)
    epjson_path = idf_path.split('.idf')[0] + '.epJSON'


    with open(epjson_path) as epJSON:
        epjson_dict = json.load(epJSON)

    inner_dict = epjson_dict
    for i in range(len(parameter_key)):
        if i < len(parameter_key) - 1:
            inner_dict = inner_dict[parameter_key[i]]
    inner_dict[parameter_key[-1]] = parameter_val


    with open(epjson_path, 'w') as epjson:
        json.dump(epjson_dict, epjson)

    convert_json_idf(eplus_run_path, epjson_path)

    run_eplus_model(eplus_run_path, idf_path, output_dir)

    return output_dir +'/eplusout.csv'


def run_one_parameter_parametric(eplus_run_path, idf_path, output_dir,
                                 parameter_key, parameter_vals):
    res_dict={}

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    for parameter_val in parameter_vals:
        this_output_dir = output_dir + f'/{parameter_val}'
        this_res_path = run_one_simulation_helper(eplus_run_path, idf_path,this_output_dir, parameter_key,parameter_val)

        res_dict[parameter_val]=this_res_path

    return res_dict