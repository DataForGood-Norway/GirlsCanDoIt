""" Importing the libraries
"""
import numpy as np
import pandas as pd
from plot_functions import make_plot


""" Data preprocessing
"""
# Importing the dataset
dataset = pd.read_csv('datasets/gapminder_2007_emma.csv')
dataset = dataset.loc[dataset['continent'].isin(['Asia','Americas','Europe','Oceania'])]
X = dataset.iloc[:,[0,3,4,5,6,7]].values
y = dataset.iloc[:, 2].values
cont = dataset.iloc[:,1].values


# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# Firstly assign the categorical variables a unique number using LabelEncoder
labelencoder_X = LabelEncoder()
# Country names are in column zero
# Each country will get a number 1-136 (for the full dataset) 
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
cont = labelencoder_X.fit_transform(cont)

# Fix the "NaNs" - replace with the average of that column
#Replace missing values
#sklearn contains libraries for preprocessing data
#now importing Imputer class
from sklearn.preprocessing import Imputer
#Create object
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
#Fit imputer object to feature X
imputer = imputer.fit(X[:,1:])
#Replace missing data with replaced values
X[:,1:] = imputer.transform(X[:,1:])

#Add a column of ones to the begining.  
#This is because the following procedure 
#will otherwise not have a constant in the regression model
X = np.append(arr = np.ones((len(X),1)).astype(int), values = X, axis = 1)



onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test, cont_train, cont_test = train_test_split(X, y, cont, test_size = 0.2, random_state = 0)


"""Start the training
"""

#train the regressor
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)
#Make predictions
y_pred = regressor.predict(X_train)

#plot the results
make_plot('GDP per cap',X_train[:,3],y_train,y_pred,cont_train)

#Start backward elimination
import statsmodels.formula.api as sm
X_opt = X_train[ : , [0,1,2,3,4,5,6]]
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()

# Drop country name (as it makes no sense)
X_opt = X_train[ : , [0,2,3,4,5,6]]
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()

#Drop populaton density
X_opt = X_train[ : , [0,2,3,4,6]]
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()

# Drop population
X_opt = X_train[ : , [0,3,4,6]]
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()

# Drop demoocracy rating
X_opt = X_train[ : , [0,3,4]]
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()

# Drop demoocracy rating
X_opt = X_train[ : , [0,3]]
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()


regressor_new = LinearRegression()
regressor_new.fit(X_opt,y_train)
#Make predictions
y_pred2 = regressor_new.predict(X_opt)


#plot the results
make_plot('GDP per cap',X_train[:,3],y_train,y_pred2,cont_train)
