#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 12:06:12 2018

@author: emmascala
"""
""" Importing the libraries
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


"""
# Importing the datasets"""
# Original Gapminder 2007 data
dataset = pd.read_csv('gapminder_2007.csv')
X = dataset.iloc[:,[0,1,4,5]].values
y = dataset.iloc[:, 3].values

# Health expenditure perc of GDP
health_gdp = pd.read_csv('indicator total health expenditure perc of GDP - Export.csv')
health_gdp_2007 = health_gdp.iloc[:,[0,3]].values
health_gdp_new = []
for item in health_gdp_2007:
    country = ""
    for char in item[0]:
        if char != '"':
            country = country + char
    if country in X:
        health_gdp_new.append([country,item[1]])

i = 0
j = 0
X_list = []
for item in X:
    if  X[i][0]== health_gdp_new[j][0]:
        item=np.insert(item,4,health_gdp_new[j][1])
        X_list.append([item[0],item[1],item[2],item[3],health_gdp_new[j][1]])
        j = j + 1
    i = i + 1
X_new = np.array(X_list)

#Replace missing values
#sklearn contains libraries for preprocessing data
#now importing Imputer class
from sklearn.preprocessing import Imputer
#Create object
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
#Fit imputer object to feature X
imputer = imputer.fit(X_new[:,2:5])
#Replace missing data with replaced values
X_new[:,2:5] = imputer.transform(X_new[:,2:5])


# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# Firstly assign the categorical variables a unique number using LabelEncoder
labelencoder_X_new = LabelEncoder()
# Country names are in column zero
# Each country will get a number 1-142 (for the full dataset) 
X_new[:, 0] = labelencoder_X_new.fit_transform(X_new[:, 0])
# Continent names are in column 1
# Assign each continent a number 0-4
X_new[:, 1] = labelencoder_X_new.fit_transform(X_new[:, 1])
# Each continent now gets an idividual column, with a 0 or 1
# depending on if the country is in that continent
onehotencoder = OneHotEncoder(categorical_features = [1])
X_new = onehotencoder.fit_transform(X_new).toarray()

#Finally the first column is dropped (dummy variable trap)
X_new = X_new[: , 1:]


#train the regressor
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_new,y)

#Make predictions
y_pred = regressor.predict(X_test)
import statsmodels.formula.api as sm
#Start backward elimination
X_opt = X_new[ : ,[0,1,2,3,7]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
