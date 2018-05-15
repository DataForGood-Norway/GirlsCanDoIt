#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 14:11:02 2018

@author: emmascala
"""

""" Importing the libraries
"""
#import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd


""" Data preprocessing
"""
# Importing the dataset
original = pd.read_csv('datasets/gapminder_2007.csv',index_col = 0)
health_spend = pd.read_csv('datasets/health_spend_2007.csv',encoding = 'latin1',index_col = 0)
pop_density = pd.read_csv('datasets/pop_density_2007.csv',encoding = 'latin1',index_col = 0)
democracy_score = pd.read_csv('datasets/democracy_2007.csv',encoding = 'latin1',index_col = 0)

all = pd.concat([original,health_spend,pop_density,democracy_score], axis = 1, join = "inner")

dataset = all.iloc[:,[0,2,3,4,5,6,7]]
dataset.to_csv('datasets/gapminder_2007_emma.csv',index_label = 'country')