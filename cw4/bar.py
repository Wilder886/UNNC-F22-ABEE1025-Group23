import json
import tkinter as tk
from tkinter import ttk
from history import historydata
from isfloat import isfloat
from tkinter import messagebox
from datetime import datetime
import os

class SingleFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        tk.Label(self, text='Calculate monolayer or single material U-value').grid()
        self.name = tk.StringVar()
        self.K_value = tk.StringVar()
        self.Thickness = tk.StringVar()
        self.U_value = tk.StringVar()
        self.result = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()


    def create_page(self):
        tk.Label(self).grid(row=1,pady=10)

        tk.Label(self, text='Material Name : ').grid(row=2, column=0, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=2, column=1, pady=10)

        tk.Label(self, text='K-value(W/mK) : ').grid(row=3, column=0, pady=10)
        tk.Entry(self, textvariable=self.K_value).grid(row=3, column=1, pady=10)

        tk.Label(self, text='Thickness(m) : ').grid(row=4, column=0, pady=10)
        tk.Entry(self, textvariable=self.Thickness).grid(row=4, column=1, pady=10)

        tk.Label(self, text='U-value(m^2*K/W) : ').grid(row=6, column=0, pady=10)
        tk.Label(self, textvariable=self.result).grid(row=6, column=1, pady=10)


        tk.Button(self, text='Confirm', command=self.confirm).grid(row=5, column=1, pady=10)

        tk.Button(self, text='Save', command=self.save).grid(row=7, column=1, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=8, column=1, pady=10)


# calculate the U-value
    def confirm(self):
        if isfloat(self.K_value.get()) == 1 and isfloat(self.Thickness.get()) == 1:
            self.U_value = float(self.K_value.get())/float(self.Thickness.get())
            self.U_value = str(self.U_value)
            self.result.set(self.U_value)
# remind the user the entry type is wrong
        else:
            messagebox.showerror(title='Error', message='The value should be float')


    def save(self):
        self.U_value = float(self.U_value)
        material = {'Name': self.name.get(), 'K_value': self.K_value.get(), ''
                    'Thickness': self.Thickness.get(), 'U_value': self.U_value}
        historydata.insert(material)
        # The history.json should have a specified initial line.
        # If not, it will get an error.

        self.status.set('Save successfully')


class MultipleFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        tk.Label(self, text='Calculate multilayer material U-value').grid()
        self.Element_name = tk.StringVar()
        self.K_value = tk.DoubleVar()
        self.Thickness = tk.DoubleVar()
        self.R_value = tk.DoubleVar()
        self.result = tk.StringVar()
        self.result1 = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()
        self.next()
        self.next_material()






    def create_page(self):
        tk.Label(self).grid(row=1, pady=10)

        tk.Label(self, text='Element name : ').grid(row=2, column=0, pady=10)
        tk.Entry(self, textvariable=self.Element_name).grid(row=2, column=1, pady=10)

        tk.Label(self, text='K-value(W/mK) : ').grid(row=3, column=0, pady=10)
        tk.Entry(self, textvariable=self.K_value).grid(row=3, column=1, pady=10)

        tk.Label(self, text='Thickness(m) : ').grid(row=4, column=0, pady=10)
        tk.Entry(self, textvariable=self.Thickness).grid(row=4, column=1, pady=10)

        tk.Button(self, text='Next layer', command=self.next) .grid(row=5, column=1, pady=10)

        tk.Label(self, textvariable=self.result).grid(row=6, column=1, pady=10)
        tk.Label(self, text='R-value(m^2*k/W) : ').grid(row=6, column=0, pady=10)

        tk.Button(self, text='Confirm', command=self.confirm).grid(row=7, column=1, pady=10)

        tk.Label(self, text='U-value(m^2*K/W) : ').grid(row=8, column=0, pady=10)
        tk.Label(self, textvariable=self.result1).grid(row=8, column=1, pady=10)

        tk.Button(self, text='Next material', command=self.next_material).grid(row=9, column=1, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=10, column=1, pady=10)




    def next(self):
        if isfloat(self.K_value.get()) != 1 and isfloat(self.Thickness.get()) != 1:
            messagebox.showerror(title='Error', message='The value should be float')
        else:
            # to judge the k-value default. If the k-value==0, there will be an error.
            K_value1 = self.K_value.get()
            if K_value1 == 0:
                print('')
            else:
                self.R_value = self.Thickness.get() / self.K_value.get()
                self.R_value = str(self.R_value)
                self.result.set(self.R_value)


        f = open('historyM.text','a+',encoding='utf-8')
        f.write('\n'+str(self.R_value))
        f.readlines()
        f.close()

        time = datetime.now().strftime('%Y%m%d%H%M%S')

        d = open('data.text','a+', encoding='utf-8')
        d.write('\r'+time)
        d.write('\r'+'Element_name:'+str(self.Element_name.get()))
        d.write('\r'+'K_value:'+str(self.K_value.get()))
        d.write('\r'+'Thickness:'+str(self.Thickness.get()))
        d.write('\r'+'R_value:'+str(self.R_value))
        d.close()

# To refresh the entry
        self.Element_name.set("")
        self.K_value.set("")
        self.Thickness.set("")

    def confirm(self):

        with open('historyM.text', encoding='utf-8') as file:
            content = file.read().splitlines()

        list = []
# Open the software , it will show 'PY_VAR9' in historyM.txt
# To delete it
        for i in content:
            if i == 'PY_VAR9' or i == '':
                print('')
                # calculate the final u-value
            else:
                list.append(i)
                sum=0
                for item in list:
                    item=float(item)
                    sum += item
                    U_value = 1 / sum

        U_value = str(U_value)
        self.result1.set(U_value)

        print(list)
        print(U_value)



    def next_material(self):
        self.status.set('You can entry next material information after push the above button.')
        f=open('historyM.text','r+')
        f.truncate()
        f.close()


class HistoryFrameS(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.checkfile()
        self.table_view = tk.Frame()
        self.table_view.pack()
        self.create_page()

# try to make sure the json file is not blank

    def checkfile(self):
        with open('history.json','w') as f:
            if f == '':
                messagebox.showerror(title='Error', message='Please check the file history.json')
                f.write(json.dumps([{"Name": "None", "K_value": "0.0", "Thickness": "0.0", "U_value": 0.0}]))
            else:
                pass


    def create_page(self):
        columns = ('Name', 'K-value', 'Thickness', 'U-value')
        columns_values = ('Name', 'K-value(W/mK)', 'Thickness(m)', 'U-value(m^2*K/W)')

        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('Name', width=140, anchor='center')
        self.tree_view.column('K-value', width=140, anchor='center')
        self.tree_view.column('Thickness', width=140, anchor='center')
        self.tree_view.column('U-value', width=140, anchor='center')

        self.tree_view.heading('Name', text='Name')
        self.tree_view.heading('K-value', text='K-value(W/mK)')
        self.tree_view.heading('Thickness', text='Thickness(m)')
        self.tree_view.heading('U-value', text='U-value(m^2*K/W)')
        self.tree_view.pack(fill=tk.BOTH, expand=True)

        self.show_data_frame()

        tk.Button(self, text='Refresh', command=self.show_data_frame).pack(anchor=tk.E, pady=5)



    def show_data_frame(self):
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        history1 = historydata.all()
        index = 0
        for material in history1:
            print(material)
            self.tree_view.insert('', index + 1, values=(material['Name'], material['K_value'],
            material['Thickness'],material['U_value']))



class HistoryFrameM(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.status = tk.StringVar()
        tk.Label(self,text='').pack()
        tk.Label(self, text='Check the calculation by read the file ').pack()
        tk.Label(self, text='').pack()
        tk.Button(self, text='Open the file',command=self.openfile).pack()
        tk.Label(self, text='').pack()
        tk.Button(self, text='Delete the all data saved',command=self.delete).pack()
        tk.Label(self, textvariable=self.status).pack()

    def openfile(self):
        os.startfile('data.text')

    def delete(self):
        f = open('data.text', 'r+')
        f.truncate()
        f.close()
        os.startfile('data.text')
        self.status.set('Delete successfully, please reopen the file')


class GuideFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        tk.Label(self, text='1.--Single--for monolayer material U-value calculation').pack()
        tk.Label(self, text='You can save the U-values and check them in --historyS-- treeview').pack()
        tk.Label(self, text='').pack()
        tk.Label(self, text='2.--Multiple--for multilayer material U-value calculation').pack()
        tk.Label(self, text='You need entry the material information one by one by pushing the button -next layer-').pack()
        tk.Label(self, text='All material information will be saved if you push the button -Confirm-').pack()
        tk.Label(self, text='And you will get the final U-value of this element').pack()
        tk.Label(self, text='You can check each material information in --historyM-- by checking the datafile').pack()


class AboutFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        tk.Label(self, text='Simple U-value calculator v1.0 ').pack()
        tk.Label(self, text='').pack()
        tk.Label(self, text='Producer information: ').pack()
        tk.Label(self, text='Student ID: 20413387').pack()
        tk.Label(self, text='Name: Dinghan WANG').pack()