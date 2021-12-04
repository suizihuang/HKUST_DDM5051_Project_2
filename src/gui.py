# -*- coding: utf-8 -*-
# Author    : Cynthia Guan
# Create    : 12/04/2021  14:54:36
# Final Edit: 12/04/2021  14:54:36
# Software: PyCharm
"""
The whole GUI should look like this:
master_frame--------------------------------------------------------------------------------------
    |                                                                                             |
    |  Search(LabelFrame)----------------------------------------------------------------------   |
    |  |   Type(cbox)-   DT_O(tbox)-   GID_O(cbox)-   DT_D(tbox)-   GID_D(cbox)-   TE(bool)-   |  |
    |  |  |           | |  (2 tbox) | |            | | (2 tbox)  | |            | |         |  |  |
    |  |   -----------   -----------   ------------   -----------   ------------   ---------   |  |
    |  ----------------------------------------------------------------------------------------   |
    |                                                                                             |
    |  Sort(LabelFrame)------------------------------------------------------------------------   |
    |  |   Type(LbFm)----   DT_O(LbFm)----   GID_O(LbFm)---   DTD(LbFm)-----  GID_D(LbFm)----  |  |
    |  |  |    tick      | |      tick    | |      tick    | |      tick    | |      tick    | |  |
    |  |  | ascend(bool) | | ascend(bool) | | ascend(bool) | | ascend(bool) | | ascend(bool) | |  |
    |  |   --------------   --------------   --------------   --------------   --------------  |  |
    |                                                                                             |
     ---------------------------------------------------------------------------------------------
"""

import tkinter as tk
import tkinter.ttk as ttk


class GUI:
    def __init__(self):
        root_window = tk.Tk()
        root_window.title('5051 project2')
        # root_window.minsize(100, 50)
        root_window.geometry('1200x600')

        box1 = tk.LabelFrame(root_window, text="Search", font=30)
        box1.pack(expand=1, fill=tk.X)
        vehicle_type = NamedCombobox(box1, "Vehicle Type", ['a', 'b'])
        dtime_O = Namedtimetextbox(box1, "First Detection Time")


        root_window.mainloop()


class NamedCombobox:
    def __init__(self, master, name, valuelist):
        frame = tk.Frame(master)
        label = tk.Label(frame,text = name, font = 30)
        label.pack(expand=1)
        combo = ttk.Combobox(frame, state='readonly')
        combo['values'] = valuelist
        combo.pack(expand=1)
        frame.pack(side=tk.LEFT, expand=1)


class Namedtimetextbox:
    def __init__(self, master, name):
        frame = tk.Frame(master)
        label = tk.Label(frame, text=name, font=30)
        label.pack(expand=1)
        subframe = tk.Frame(frame)
        start = tk.Label(subframe, text="Between")
        start.pack(side=tk.LEFT, expand=1)
        s_time = tk.Entry(subframe)
        s_time.pack(side=tk.LEFT, expand=1)
        end = tk.Label(subframe, text="and")
        end.pack(side=tk.LEFT, expand=1)
        e_time = tk.Entry(subframe)
        e_time.pack(side=tk.LEFT, expand=1)
        subframe.pack(expand=1)
        frame.pack(side=tk.LEFT, expand=1)



###TEST###
if __name__ == '__main__':
    GUI()
