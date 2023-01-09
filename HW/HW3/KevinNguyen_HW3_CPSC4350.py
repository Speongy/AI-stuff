'''
Kevin Nguyen
HW3
CPSC4350
Kockara
Fall2022
'''
#TODO linear regression model with multiple features
#TODO Visualize data with scatter plot from matplotlib
#TODO After training linera regression model, test on data set

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import metrics

bikerentals = pd.read_csv('bikes.csv')
x = bikerentals[['temperature','humidity','windspeed']]
y = bikerentals['rentals']

#!split training set
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.001, random_state= 0) 
#? if test_size is 0.001 and random_state=0, we get good coefficients

mlg = LinearRegression()
mlg.fit(x_train, y_train) #train the model

#! intercept and coeff
print('intercept: ',mlg.intercept_)
# print('coefficient: ',mlg.coef_)
# print(pd.DataFrame(mlg.coef_, x.columns, columns = ['Coeff']))
print('coeff: ',list(zip(x, mlg.coef_)))

#! test prediction
y_pred = mlg.predict(x_test)
x_pred = mlg.predict(x_train)
print("prediction for test set: {}".format(y_pred), '\n')

#! actual value and pred value
mlr_diff = pd.DataFrame({'ActValue': y_test, 'PredValue': y_pred})
print(mlr_diff, '\n')

#! model performance evaluation
meanAbErr = metrics.mean_absolute_error(y_test, y_pred)
meanSqErr = metrics.mean_squared_error(y_test, y_pred)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred))

print('R sqrd: {:.2f}'.format(mlg.score(x,y)*100))
print('mean absol error:', meanAbErr)
print('mean square error:', meanSqErr)
print('Root mean square error:', rootMeanSqErr)

#! plot ===========================================================================
bikerentals.plot(kind= 'scatter', x = 'temperature', y = 'rentals', color = 'red')
#? more bike rentals when it's warmer
bikerentals.plot(kind= 'scatter', x = 'humidity', y = 'rentals', color = 'blue')
#? more bike rentals when it's not as windy
bikerentals.plot(kind= 'scatter', x = 'windspeed', y = 'rentals', color = 'green')
#? more bike rentals when it's not as humid
plt.show()


