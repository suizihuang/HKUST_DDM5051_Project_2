# -*- coding: utf-8 -*-
# Author    : Cynthia Guan
# Create    : 12/05/2021  03:34:36
# Final Edit: 12/05/2021  03:34:36
# Software: PyCharm

import pandas as pd


class Sheet:
    def __init__(self):
        self.file_path = r'.\data\TDCS_M06A_20190830_080000.csv'
        self.sheet = pd.read_csv(self.file_path)