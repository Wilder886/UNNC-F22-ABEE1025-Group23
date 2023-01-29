import tkinter as tk
from bar import SingleFrame,MultipleFrame,HistoryFrameS,HistoryFrameM,GuideFrame,AboutFrame
# This is the main UI page of this calculator, the bar is the function menu
# The functions are made in bar.py

class MainPage:
    def __init__(self, master: tk.Tk):
        self.root = master
        self.root.title('Simple U-value calculator v1.0')
        self.root.geometry('700x500')
        self.root.attributes("-alpha", 0.9)
        self.create_page()

    # create main page
    def create_page(self):
        self.single_frame = SingleFrame(self.root)
        self.multiple_frame = MultipleFrame(self.root)
        self.history_frameS = HistoryFrameS(self.root)
        self.history_frameM = HistoryFrameM(self.root)
        self.guide_frame = GuideFrame(self.root)
        self.about_frame = AboutFrame(self.root)


        menubar = tk.Menu(self.root, tearoff=False)

        menubar.add_command(label='Single',command=self.show_single)
        menubar.add_command(label='Multiple',command=self.show_multiple)

        historymenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='History', menu=historymenu)
        historymenu.add_command(label='historyS',command=self.show_historyS)
        historymenu.add_separator()
        historymenu.add_command(label='historyM',command=self.show_historyM)

        menubar.add_command(label='Guide',command=self.show_guide)
        menubar.add_command(label='About', command=self.show_about)

        self.root['menu'] = menubar


    def show_single(self):
        self.single_frame.pack()
        self.multiple_frame.pack_forget()
        self.history_frameS.pack_forget()
        self.history_frameM.pack_forget()
        self.guide_frame.pack_forget()
        self.about_frame.pack_forget()


    def show_multiple(self):
        self.single_frame.pack_forget()
        self.multiple_frame.pack()
        self.history_frameS.pack_forget()
        self.history_frameM.pack_forget()
        self.guide_frame.pack_forget()
        self.about_frame.pack_forget()


    def show_historyS(self):
        self. single_frame.pack_forget()
        self.multiple_frame.pack_forget()
        self.history_frameS.pack()
        self.history_frameM.pack_forget()
        self.guide_frame.pack_forget()
        self.about_frame.pack_forget()


    def show_historyM(self):
        self. single_frame.pack_forget()
        self.multiple_frame.pack_forget()
        self.history_frameS.pack_forget()
        self.history_frameM.pack()
        self.guide_frame.pack_forget()
        self.about_frame.pack_forget()


    def show_guide(self):
        self.single_frame.pack_forget()
        self.multiple_frame.pack_forget()
        self.history_frameS.pack_forget()
        self.history_frameM.pack_forget()
        self.guide_frame.pack()
        self.about_frame.pack_forget()


    def show_about(self):
        self.single_frame.pack_forget()
        self.multiple_frame.pack_forget()
        self.history_frameS.pack_forget()
        self.history_frameM.pack_forget()
        self.guide_frame.pack_forget()
        self.about_frame.pack()



if __name__ == '__main__':
    root = tk.Tk()
    MainPage(root)
    root.mainloop()