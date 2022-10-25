#demo2 on Ubuntu

#copy from demo1 to import
def run_one_parameter_parametric(self):
	from StaticEplusEngine import run_eplus_model
	eplus_exe_path = './energyplus9.5/energyplus'
	eplus_model_path = './1ZoneUncontrolled_win_1.idf'
	res_dir = './result2'

	run_eplus_model(eplus_exe_path, eplus_model_path, res_dir)

	a=[0.1,0.2,0.3,0.4,0.5]
	a=str=[str(i) for i in a]
	hate_list=[]
	for i in a_str:
		shutil.copyfile('./1ZoneUncontrolled_win_1.idf','./1ZoneUncontrolled_win_1(copy).idf')

		lines=[]
		with open('./1ZoneUncontrolled_win_1.idf','r') as f:
			for line in f:
				lines.append(line)

		new_lines=lines[:248]
		new_lines.append(lines[248].replace('0.763',i))
		new_lines.extend(lines[248:])

		with open('./1ZoneUncontrolled_win_1.idf','w') as f:
			for line in new_lines:
			    f.write(line)

		import csv
		content=[]
		with open('./1ZoneUncontrolled_win_1.csv','r',encoding='utf-8') as csvfile:
			read = csv.reader(csvfile)
			for i in read:
				content.append(i)
		hate=content[1][2]
		hate_list.append(hate)

		return()