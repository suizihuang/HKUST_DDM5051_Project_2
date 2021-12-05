#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 17:23:25 2021

@author: cuiyang

Last modify: 12/05/2021 20:44:07 by Cynthia Guan
"""

import pandas as pd
import datetime

col_dict = {0:0, 1:1, 2:2, 3: 3, 4: 4, 5: 6}

def search_by_time(data, col_num, time_range):
    col = col_dict[col_num]
    time_range = time_range.split('-')
    if time_range[0]:
        strt = datetime.datetime.strptime(time_range[0], "%Y/%m/%d %H:%M:%S")
        data = data[data[col] >= strt]
    if time_range[1]:
        strt = datetime.datetime.strptime(time_range[1], "%Y/%m/%d %H:%M:%S")
        data = data[data[col] <= strt]
    return data

def search_by_value(data, col_num, value):
    col = col_dict[col_num]
    data = data[data[col] == value]
    return data


def Search(sheet, searchlist):
    df1 = sheet
 #   df1 = sheet.head(300)
    df1[1] = pd.to_datetime(df1[1])
    df1[3] = pd.to_datetime(df1[3])

    search_condition = {}

    for i in range(6):
        if not searchlist[i]:
            continue
        search_condition[i] = searchlist[i]

    if 0 in search_condition:
        search_condition[0] = int(search_condition[0])

    for i in range(6):
        if i in search_condition:
            if i == 1 or i == 3:
                df1 = search_by_time(df1, i, search_condition[i])
                continue
            df1 = search_by_value(df1, i, search_condition[i])

    return df1