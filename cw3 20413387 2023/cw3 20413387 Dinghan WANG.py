import csv
import json
import pandas as pd
import os
import numpy as np
from StaticEplusEngine import run_eplus_model, convert_json_idf

# Explanation1: The cases need are at the bottom as creating the two objects, you can just run this .py
'''Explanation2: I do not use the getter and setter, because I think when you need test other case, you can not 
 always only change one or two of the attributes to change the path and vals. 
 And there is no need to lock certain attributes in this cw.
 Just use copy and paste to crate a new object is faster for this cw'''
'''And of course i can writer this like: 

  self.__parameter_key = None
 @Property
 def parameter_key(self):
    return self.__parameter_key
 @parameter_key.setter(self, key):
    self.__parameter_key = key
    
Param_1.key = ''
 
But i think this is not better for using these methods.
'''


class Param:
    def __init__(self, eplus_run_path,idf_path,output_dir,
                    parameter_key, parameter_val):
        self.eplus_run_path = eplus_run_path
        self.idf_path = idf_path
        self.output_dir = output_dir
        self.parameter_key = parameter_key
        self.parameter_val = parameter_val


    def RunOneSimulation(self, eplus_run_path, idf_path, output_dir,
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

        return output_dir + '/eplusout.csv'


    def OneParameterParametric(self,eplus_run_path, idf_path, output_dir,
                               parameter_key, parameter_vals):
        res_dict = {}

        if not os.path.isdir(output_dir):
            os.mkdir(output_dir)

        for parameter_val in parameter_vals:
            this_output_dir = output_dir + f'/{parameter_val}'
            this_res_path = self.RunOneSimulation(eplus_run_path, idf_path, this_output_dir,
                                             parameter_key, parameter_val)

            res_dict[parameter_val] = this_res_path

        return res_dict

    def Run(self,eplus_run_path, idf_path, output_dir,
                 parameter_key, parameter_vals,parameter_vals_view,parameter_key_view):

        output_paths = self.OneParameterParametric(eplus_run_path, idf_path, output_dir,
                                              parameter_key, parameter_vals)

        list = []
        for parameter_key in output_paths.keys():
            this_path = output_paths[parameter_key]
            data = pd.read_csv(this_path, usecols=[8])
            data = np.array(data)
            sum_data = sum(data)
            value = sum_data / 25
            list.append(value)
            print(this_path)

        max_value = max(list)
        with open('optimal_value.csv','a',encoding='utf_8')as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['Parameter'])
            csv_writer.writerow(parameter_key_view)
            csv_writer.writerow(parameter_vals_view)
            csv_writer.writerow(['optimal_value(ZN001:WALL001:Surface Inside Face Temperature [C)'])
            csv_writer.writerow([max_value])

# These are 2 object cases for the test need

eplus_run_path = './energyplus9.5/energyplus'
idf_path = './1ZoneUncontrolled_win_1.idf'
parameter_vals_1 = [0.25+i*0.02 for i in range(25)]
parameter_vals_2 = [1.0+i*0.06 for i in range(25)]
output_dir_1 = 'param_exp_1'
output_dir_2 = 'param_exp_2'
parameter_key_1 = ['WindowMaterial:SimpleGlazingSystem','SimpleWindow:DOUBLE PANE WINDOW','solar_heat_gain_coefficient']
parameter_key_2 = ['WindowMaterial:SimpleGlazingSystem','SimpleWindow:DOUBLE PANE WINDOW','u_factor']

# Due to parameter_value and parameter_key are not str
# These are used for creating output easily without transition and freely.

parameter_vals_view_1 = ['0.25 - 0.25+25*0.02']
parameter_vals_view_2 = ['1.0 - 0.1+25*0.06']
parameter_key_view_1 = ['WindowMaterial:SimpleGlazingSystem''SimpleWindow:DOUBLE PANE WINDOW'' solar_heat_gain_coefficient']
parameter_key_view_2 = ['WindowMaterial:SimpleGlazingSystem''SimpleWindow:DOUBLE PANE WINDOW'' u_factor']


Param_1 = Param(eplus_run_path,idf_path,output_dir_1,parameter_key_1,parameter_vals_1)
Param_2 = Param(eplus_run_path,idf_path,output_dir_2,parameter_key_2,parameter_vals_2)


Param_1.Run(eplus_run_path,idf_path,output_dir_1,parameter_key_1,parameter_vals_1,parameter_vals_view_1,parameter_key_view_1 )

Param_2.Run(eplus_run_path,idf_path,output_dir_2,parameter_key_2,parameter_vals_2,parameter_vals_view_2,parameter_key_view_2)






