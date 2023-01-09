#Let's try to gain a better knowledge of polynomial regression

'''
poly regression is where we analyze the relationship between the independent var 
and dependent var, in which we model them in the nth degree polynomial

we usually fit them using the least squares method

special case of linear regression, where we fit the polynomial eq. on the data with
a curved line between the variables

we use linear quadratic and cubic polynomials

dependent variable's behavior is based on linear or curvilinear lines. 
additive relationship between the dependent vars and a set of k independent vars.
(xi, i = 1 to k)

relationship between dependent vars and any independent vars is linear or curvilinear
(polynomials)

independent vars are independent of each other
errors are independent and they are distributed with mean zero and a constant variance

'''

'''
#!our model sucks
#!when we observe actual value and best fit line, the actual value has a curve 
#! and it's no where near the mean of points
#?polynomial regression predicts the best fit line to follow the data curve

#!polynomial reg doesn't need relationship between independent and dependent vars to be linear
#? unlike linear regression

polynomial regression is normally used when data points are not captured by the lin reg model
and when it fails in describing the best result clearly

# as we increase the degree in the model, it tends to increase the performance of the model
# however, increasing the degrees of the model also increase the risk of over-fitting
and under-fitting the data.

'''

'''
#? How to find the right degree of the equation?
#! Either forward selection or Backward selection. This increases or decreases the degree until it is
#! significant enough to define the best model
'''

'''
linear regression is first degree polynomial

#! Simple linear regression => y = b0 + b1x1
#! Multiple linear regression => y = b0 + b1x1 + b2x2 + ... + bnxn
#! polynomial linear regression => b0 + b1x1 + b2x1^2 + ... bnx1^n

The value of b is found thru matrix multiplication
#! for a better understanding 
#!  behind the math  http://polynomialregression.drque.net/math.html

'''

''''
Cost Function of poly reg

cost function - measures performance of ML model for given data
cost is average of errors in n-samples, loss is the error for individual data point
cost ==> entire training set
loss ==> one training example

cost fn of poly can be taken to be #! Mean Squared Error with a slight change

J = (1/n) Summation of n as i=1 of (pred(i) - y(i))^2

#!cost fn of linear reg
J = 1/n * sum(square(pred - y))
or
J = 1/n * sum(square(pred - (b0 + b1x1)))

#! cost fn of polynomial reg
#? instead of y we have b0 + b1x + b2x^2, ...

J = 1/n * sum(squared(pred - (b0 + b1x + b1x^2 + b3bx^3 + ... + bnbx^n)))

#? polynomial regression can reduce costs returned by cost fn. gives regression line curvilinear shape and makes it fit underlying data.
#! higher order polynomial = better regression line fit

'''

'''#!Gradient Descent for polynomial reg
- optimization algo for finding values of parameters of a fn that minimizes the cost fn
    -Jason Brownlee's Blog: https://machinelearningmastery.com/gradient-descent-for-machine-learning/

#TODO Steps followed by gradient descent to lower cost fn
- values of m and b will be 0
- learning rate will be introduced to the fn and very small (0.001 - 0.01)
- partial derivative is calculated for the cost fn equation in terms of:
    - slope (m)
    
- derivatives are calculated with respect to:
    - intercept (b)

- after derivatives are calculated, the slope and intercept are updated with the following equation:
    - m = m - \alpha(learning rate) * derivative of m
    - b = b - \alpha(learning rate) * derivative of b

#? learn intuition behind gradient descent and how it tries to reach the global optima(Lowset cost fun value)

- updating the values of m and b goes on until fn raches value or 0 or close
- values of m and b are now optimal to describe the best fit line
'''

#TODO Let's implement polynomial regression!

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

dataset = pd.read_csv("possalary.csv")

X = dataset.iloc[:, 1:2].values     #data preprocessing
Y = dataset.iloc[:, 2].values

'''
since we don't have that many observations, we don't
need to split set
'''

linReg = LinearRegression()     #fitting lin reg model to dataset
linReg.fit(X,Y)

plt.scatter(X, Y, color='red')      #Linear reg plot
plt.plot(X, linReg.predict(X), color = 'blue')
# plt.title("Linear")
# plt.xlabel("Position Level")
# plt.ylabel("Salary")

polyReg = PolynomialFeatures(degree = 4)
xPoly = polyReg.fit_transform(X)
linReg2 = LinearRegression()
linReg2.fit(xPoly, Y)

plt.plot(X, linReg2.predict(polyReg.fit_transform(X)), color = 'red')
plt.title("Polynomial Reg")
plt.xlabel("Pos")
plt.ylabel("Salary")

plt.show()
