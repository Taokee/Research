#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'TaoKee'
__mtime__ = '2018/6/7'
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
import os


Data_Dict={'digg':{'digg_meta':'out.digg-friends','num':3}
    ,'':''}
# line.exe -train Slashdot090216/Slashdot090216_Data_For_Embedding_0.txt -output Slashdot090216/emb/or2/Slashdot090216_Embedding_Result5_0.txt -binary 0 -size 100 -order 2 -negative 5 -samples 10 -rho 0.025 -threads 5

dataname='digg'
for i in range(Data_Dict[dataname]['num']):
    inputstr='../../'+dataname+'/com/G_link_'+str(i)+'.txt'
    outputstr='../'+dataname+'/2/Embresult_'+str(i)+'.txt'
    cmdstr='line.exe -train '+inputstr+' -output '+outputstr+' -binary 0 -size 100 -order 2 -negative 5 -samples 10 -rho 0.025 -threads 5'
    os.system(cmdstr)
