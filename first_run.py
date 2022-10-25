#demo1 on Ubuntu

from StaticEplusEngine import run_eplus_model

eplus_exe_path = './energyplus9.5/energyplus'
eplus_model_path = './1ZoneUncontrolled_win_1.idf'
res_dir = './result1'

run_eplus_model(eplus_exe_path, eplus_model_path, res_dir)
