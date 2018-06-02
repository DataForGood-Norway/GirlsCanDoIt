""" Importing the libraries
"""
import numpy as np
import pandas as pd
from plot_functions import make_plot


""" Data preprocessing
"""
# Importing the dataset
dataset = pd.read_csv('datasets/gapminder_2007_emma.csv')
#dataset = dataset.loc[dataset['continent'].isin(['Asia','Americas','Europe','Oceania'])]
X = dataset.iloc[:,[0,1,3,4,5,6,7]].values
X[:,3] = np.log(dataset.iloc[:,4].values)
y = dataset.iloc[:, 2].values
cont = dataset.iloc[:,1].values

# Fix the "NaNs" - replace with the average of that column
#Replace missing values
#sklearn contains libraries for preprocessing data
#now importing Imputer class
from sklearn.preprocessing import Imputer
#Create object
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
#Fit imputer object to feature X
imputer = imputer.fit(X[:,2:])
#Replace missing data with replaced values
X[:,2:] = imputer.transform(X[:,2:])

# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# Firstly assign the categorical variables a unique number using LabelEncoder
labelencoder_X = LabelEncoder()
# Country names are in column zero
# Each country will get a number 1-136 (for the full dataset) 
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
X[:, 1] = labelencoder_X.fit_transform(X[:, 1])
cont = labelencoder_X.fit_transform(cont)
# if excluding Africa
#cont = cont + 1
# one hot encode continenets
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
#Remove a continent (dummy variable trap)
# The obvious one to drop is Africa as it's the first column
# However this is also the most interesting
# so dropping Oceania instead
X = X[:,[0,1,2,3,5,6,7,8,9,10]]

#Add a column of ones to the begining.  
#This is because the following procedure 
#will otherwise not have a constant in the regression model
X = np.append(arr = np.ones((len(X),1)).astype(int), values = X, axis = 1)

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test, cont_train, cont_test = train_test_split(X, y, cont, test_size = 0.2, random_state = 0)

"""
Columns are now
0: constant, 1:is Africa 2: is Americas 3: is Asia 4:is Europe
5: country 6:population 7:log(GDP per cap) 
8:health spend 9:pop density 10: dempocracy score
"""


"""Start the training
"""

#train the regressor
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)
#Make predictions
y_pred = regressor.predict(X_train)

#plot the results
gdp_per_cap = np.exp(X_train[:,7])
make_plot('GDP per cap',gdp_per_cap,y_train,y_pred,cont_train)
#plot the results
# make_plot('Health spend',X_train[:,8],y_train,y_pred,cont_train)

#Start backward elimination
import statsmodels.formula.api as sm
X_opt = X_train[ : , [0,1,2,3,4,5,6,7,8,9,10]]
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()

# Drop country name (as it makes no sense)
X_opt = X_train[ : , [0,1,2,3,4,6,7,8,9,10]]
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()

#Drop population
X_opt = X_train[ : , [0,1,2,3,4,7,8,9,10]]
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()

# Drop democracy index
X_opt = X_train[ : , [0,1,2,3,4,7,8,9]]
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()

# Drop population density
X_opt = X_train[ : , [0,1,2,3,4,7,8]]
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()

# Drop health spend
X_opt = X_train[ : , [0,1,2,3,4,7]]
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()


regressor_new = LinearRegression()
regressor_new.fit(X_opt,y_train)
#Make predictions
y_pred2 = regressor_new.predict(X_opt)


#plot the results
gdp_per_cap = np.exp(X_train[:,7])
make_plot('GDP per cap',gdp_per_cap,y_train,y_pred2,cont_train)
make_plot('Health spend',X_train[:,8],y_train,y_pred2,cont_train)

X_test_opt = X_test[:,[0,1,2,3,4,7]]
y_pred_test = regressor_new.predict(X_test_opt)
#plot the results
gdp_per_cap = np.exp(X_test[:,7])
make_plot('GDP per cap',gdp_per_cap,y_test,y_pred_test,cont_test)
make_plot('Health spend',X_test[:,8],y_test,y_pred_test,cont_test)
