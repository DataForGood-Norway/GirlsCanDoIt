""" Importing the libraries
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


""" Data preprocessing
"""
# Importing the dataset
dataset = pd.read_csv('gapminder_2007.csv')
X = dataset.iloc[:,[0,1,2,4,5]].values
y = dataset.iloc[:, 3].values

# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# Firstly assign the categorical variables a unique number using LabelEncoder
labelencoder_X = LabelEncoder()
# Country names are in column zero
# Each country will get a number 1-142 (for the full dataset) 
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
# Continent names are in column 1
# Assign each continent a number 0-4
X[:, 1] = labelencoder_X.fit_transform(X[:, 1])
# Each continent now gets an idividual column, with a 0 or 1
# depending on if the country is in that continent
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()

#Finally the first colum is dropped (dummy variable trap)
X = X[: , 1:]

import statsmodels.formula.api as sm
#Add a column of ones to the begining.  
#This is because the following procedure 
#will otherwise not have a constant in the regression model
X = np.append(arr = np.ones((len(X),1)).astype(int), values = X, axis = 1)

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


"""Start the training
"""

#train the regressor
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)
#Make predictions
y_pred = regressor.predict(X_test)

#plot the results
plt.scatter(X_train[:,8],y_train, c = X_train[:,5])
plt.scatter(X_train[:,8],regressor.predict(X_train), c = X_train[:,5], marker = 'x')
#plt.scatter(X_test[:,7],y_test, color = 'green')
plt.title('GDP per capita vs. life expectancy')
plt.xlabel('GDP per Capita')
plt.ylabel('Life expectancy')
plt.show()



## In case the above has been run more than once
#X_train = X_train[: , 1:]

#plot the results
plt.scatter(X_train[:,8],y_train, c = X_train[:,5])
plt.scatter(X_train[:,8],regressor.predict(X_train), c = X_train[:,5], marker = 'x')
#plt.scatter(X_test[:,7],y_test, color = 'green')
plt.title('GDP per capita vs. life expectancy')
plt.xlabel('GDP per Capita')
plt.ylabel('Life expectancy')
plt.show()


#Start backward elimination
X_opt = X_train[ : ,[0]]
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()


