# -*- coding: utf-8 -*-
# Author    : Cynthia Guan
# Create    : 12/05/2021  03:34:36
# Final Edit: 12/05/2021  03:34:36
# Software: PyCharm

import pandas as pd


class Sheet:
    def __init__(self):
        self.file_path = r'.\data\TDCS_M06A_20190830_080000.csv'
        self.sheet = pd.read_csv(self.file_path, header=None)

    def get_vehichle_type(self):
        vt = [i for i in self.sheet[0].value_counts().index]
        vt.sort()
        vt = list(map(lambda x: str(x), vt))
        return vt

    def get_gantry_id_o(self):
        go = [i for i in self.sheet[2].value_counts().index]
        go.sort()
        return go

    def get_gantry_id_d(self):
        gd = [i for i in self.sheet[4].value_counts().index]
        gd.sort()
        return gd

    def add_row(self, row: dict):
        self.sheet.append(row)

    def get_row(self, idx):
        return self.sheet.loc[idx]

    def drop_row(self, idx: int):
        self.sheet.drop(idx, inplace=True)