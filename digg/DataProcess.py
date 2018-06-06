#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'TaoKee'
__mtime__ = '2018/6/4'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import numpy as np





def SplitData(url):
    Split_Net={}
    Net_Dict={}
    for line in open(url):
        if len(line.split())>3:
            n1=line.split()[0]
            n2=line.split()[1]
            timestr=line.split()[3]
            # if Split_Net.has_key(timestr):
            if timestr not in Split_Net.keys():
                Split_Net[timestr]=[]
            Split_Net[timestr].append([n1, n2,timestr])

    Sort_by_Time = sorted(Split_Net.items(), key=lambda d: d[0])
    step_time=int(len(Sort_by_Time)/10)
    print("统计完毕")
    kk=0
    for i in range(10):
        Net_arr=[]
        for s in range(step_time):
            arr_temp=Sort_by_Time[i*step_time+s][1]
            for arr in arr_temp:
                Net_arr.append(arr)
        Net_Dict[i]=Net_arr
    print("开始保存")
    Save_Complete_Dict(Net_Dict)
    Save_Incream_Dict(Net_Dict)
    # print(Net_Dict)

def Save_Incream_Dict(Net_Dict):
    for i in range(10):
        output = open('inc/G_link_'+str(i)+',txt', 'w')
        arrs=Net_Dict[i]
        for s in range(len(arrs)):
            for j in range(len(arrs[s])):
                output.write(str(arrs[s][j]) + ' ')
            output.write('\n')

def Save_Complete_Dict(Net_Dict):
    arrs=[]
    for i in range(10):
        output = open('com/G_link_'+str(i)+',txt', 'w')
        # arrs=Net_Dict[i]
        for arr in Net_Dict[i]:
            arrs.append(arr)

        for s in range(len(arrs)):
            for j in range(len(arrs[s])):
                output.write(str(arrs[s][j]) + ' ')
            output.write('\n')

Data_Dict={'digg_meta':'out.digg-friends'}
SplitData(Data_Dict['digg_meta'])

