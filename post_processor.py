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
    fig. axs = plt.subplots(1,1, figsize=(20,10))
    fontsize = 20
    for item in paramter_vals:
       this_path=['eplusout.csv']
       this_df = pd.read_csv(this_path)
       this_df['Date/Time'] = '2002' + this_df['Date/Time']
       this_df['Date/Time'] = this_df['Date/Time'].apply(eplus_to_datetime)
       data_st_date = this_df.iloc[0]['Date/Time']
       date_ed_date = this_df.iloc[-1]['Date/Time']
       date_list = this_df['Date/Time']
       this_y = this_df[plot_column_name].values
       axs.plpt(date_list,this_y,alpha=0.7,linestyle='--',linewidth =2,label=itme)
       axs.set_title(plot_title)
       axs.set_ylabel(y_axis_title)
       axs.set_xlabel('Time (%s to %s)'%(date_st_date, date_ed_date),fontsize =fontsize)
       axs.lengend(fontsize=fontsize)
       show()
