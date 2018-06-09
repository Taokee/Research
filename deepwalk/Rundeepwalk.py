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
# deepwalk --input wiki_Data_For_Embedding_unweight_0.txt --number-walks 3 --representation-size 100 --walk-length 10 --window-size 4 --workers 3 --output wiki_Embedding_Result_iter.txt

dataname='digg'
for i in range(Data_Dict[dataname]['num']):
    inputstr='../'+dataname+'/com/G_link_'+str(i)+'.txt'
    outputstr=dataname+'/Embresult_'+str(i)+'.txt'
    cmdstr='deepwalk --input '+inputstr+' --number-walks 3 --representation-size 100 --walk-length 5 --window-size 1 --workers 3 --output '+outputstr
    os.system(cmdstr)

