#parametric_somulation
import json
import copy
import os
import re
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

    return output_dir


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

#post
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import csv
import pandas as pd
import datetime as dt

def eplus_to_datetime(date_str):
    if date_str[-8:-6]!='24':
        dt_obj =pd.to_datetime(date_str)
    else:
        date_str = date_str[0: -8] + '00' + date_str[-6:]
        dt_obk = pd.to_datetime(date_str) + dt.timedelta(days=1)
    return dt_obj


def plot_1D_results(output_paths,plot_column_name,plot_title):
    fig.axs = plt.subplots(1,1, figsize=(20,10))
    fontsize = 20
    for parameter_key in output_paths.keys():
       this_path=output_paths[parameter_key]
       this_df = pd.read_csv(this_path)
       this_df['Date/Time'] = '2002' + this_df['Date/Time']
       this_df['Date/Time'] = this_df['Date/Time'].apply(eplus_to_datetime)
       data_st_date = this_df.iloc[0]['Date/Time']
       date_ed_date = this_df.iloc[-1]['Date/Time']
       date_list = this_df['Date/Time']
       this_y = this_df[plot_column_name].values
       axs.plpt(date_list,this_y,alpha=0.7,linewidth =2,label=parameter_key)
    datetime_ax_loc=mdates.HourLocator()
    datetime_ax_fmt=mdates.DateFormatter('%H;%M')
    axs.xaxis.set_major_locator(datetime_ax_loc)
    axs.xaxis.set_major_formatter(datetime_ax_fmt)
    for tick in axs.xaxis.get_major_ticks():
        tick.label.set_fontsize(fontsize^0.8)
    for tick in axs.yaxis.get_major_ticks():
        tick.label.set_fontsize(fontsize ^ 0.8)
    axs.tick_params('x',laberotation=45)
    asx.set_xlabel('Time(%s to %s)'%(date_st_date,date_ed_date))
    axs.set_title(plot_title)
    axs.set_ylabel(y_axis_title)
    axs.set_xlabel('Time (%s to %s)'%(date_st_date, date_ed_date),fontsize =fontsize)
    axs.lengend(fontsize=fontsize)

#main

from parametric_simulation_for_cw1_part3 import run_one_parameter_parametric
from post_for_cw1_part3 import plot_1D_results


#choice one parmetric simulation
def main():
    while True:
        menm()
        choice = int(input('choice parametric simulation type '))
        list_1 = [1, 2, 3, 4]
        if choice not in list_1:
            print('wrong,please try again')
            break
        elif choice ==1:
            parametric_simulation_wall_insulation_thickness()
        elif choice ==2:
            parametric_simulation_window_U_value()
        elif choice ==3:
            parametric_simulation_room_height()
        elif choice ==4:
            parametric_simulation_room_length()
# 4 types
def menm():
    print('1.wall_insulation_thickness')
    print('2.window_U_value')
    print('3.room_height')
    print('4.room_length')

#run helper

def parametric_simulation_wall_insulation_thickness (eplus_run_path, idf_path,output_dir, parameter_key, parameter_vals,plot_column_name,y_axis_title,plot_title ):
    eplus_run_path = './energyplus9.5/energyplus'
    output_dir = 'param_exp_wall_insulation_thickness'

    idf_path_1 = input(str('your_idf_path,please with\'\' '))
    idf_path = idf_path_1

    parameter_key_1=input(str('your_parameter_key,please with\'\''))
    parameter_key=parameter_key_1

    parameter_vals_1 = input(str('your_parameter_key,please with\'\''))
    parameter_vals = parameter_vals_1

    plot_column_name_1=input(str('your_plot_column_name,please with\'\''))
    plot_column_name=plot_column_name_1

    y_axis_title_1=input(str('your_y_axis_title,please with\'\''))
    y_axis_title=y_axis_title_1

    plot_title_1=input(str('your_plot_title,please with\'\''))
    plot_title=plot_title_1

    output_paths = run_one_parameter_parametric(eplus_run_path, idf_path, output_dir, parameter_key, parameter_vals)
    print(output_paths)



def parametric_simulation_window_U_value (eplus_run_path, idf_path,output_dir, parameter_key, parameter_vals,plot_column_name,y_axis_title,plot_title ):
    eplus_run_path = './energyplus9.5/energyplus'
    output_dir = 'param_exp_window_U_value '

    idf_path_2 = input(str('your_idf_path,please with\'\' '))
    idf_path = idf_path_2

    parameter_key_2 = input(str('your_parameter_key,please with\'\''))
    parameter_key = parameter_key_2

    parameter_vals_2 = input(str('your_parameter_key,please with\'\''))
    parameter_vals = parameter_vals_2

    plot_column_name_2 = input(str('your_plot_column_name,please with\'\''))
    plot_column_name = plot_column_name_2

    y_axis_title_2 = input(str('your_y_axis_title,please with\'\''))
    y_axis_title = y_axis_title_2

    plot_title_2 = input(str('your_plot_title,please with\'\''))
    plot_title = plot_title_2

    output_paths = run_one_parameter_parametric(eplus_run_path, idf_path, output_dir, parameter_key, parameter_vals)
    print(output_paths)



def parametric_simulation_room_height(eplus_run_path, idf_path,output_dir, parameter_key, parameter_vals,plot_column_name,y_axis_title,plot_title ):
    eplus_run_path = './energyplus9.5/energyplus'
    output_dir = 'param_exp_room_height  '

    idf_path_3 = input(str('your_idf_path,please with\'\' '))
    idf_path = idf_path_3

    parameter_key_3= input(str('your_parameter_key,please with\'\''))
    parameter_key = parameter_key_3

    parameter_vals_3 = input(str('your_parameter_key,please with\'\''))
    parameter_vals = parameter_vals_3

    plot_column_name_3 = input(str('your_plot_column_name,please with\'\''))
    plot_column_name = plot_column_name_3

    y_axis_title_3 = input(str('your_y_axis_title,please with\'\''))
    y_axis_title = y_axis_title_3

    plot_title_3 = input(str('your_plot_title,please with\'\''))
    plot_title = plot_title_3

    output_paths = run_one_parameter_parametric(eplus_run_path, idf_path, output_dir, parameter_key, parameter_vals)
    print(output_paths)

def parametric_simulation_room_length(eplus_run_path, idf_path, output_dir, parameter_key, parameter_vals, y_axis_title, plot_title):
    eplus_run_path = './energyplus9.5/energyplus'
    output_dir = 'param_exp_room_length'

    idf_path_4 = input(str('your_idf_path,please with\'\' '))
    idf_path = idf_path_4

    parameter_key_4 = input(str('your_parameter_key,please with\'\''))
    parameter_key = parameter_key_4

    parameter_vals_4 = input(str('your_parameter_key,please with\'\''))
    parameter_vals = parameter_vals_4

    plot_column_name_4 = input(str('your_plot_column_name,please with\'\''))
    plot_column_name = plot_column_name_4

    y_axis_title_4 = input(str('your_y_axis_title,please with\'\''))
    y_axis_title = y_axis_title_4

    plot_title_4 = input(str('your_plot_title,please with\'\''))
    plot_title = plot_title_4

    output_paths = run_one_parameter_parametric(eplus_run_path, idf_path, output_dir, parameter_key, parameter_vals)
    print(output_paths)

if __name__ == '__main__':
    main()