import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

dataset = pd.read_csv('possalary.csv')
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2].values

lg = LinearRegression()
lg.fit(X,Y)

poly = PolynomialFeatures(degree = 10)
X_poly = poly.fit_transform(X)
lg2 = LinearRegression()
lg2.fit(X_poly, Y)

plt.scatter(X, Y, color = 'red') #!dataset points

plt.plot(X, lg.predict(X), color = 'green')#!linReg1

plt.plot(X, lg2.predict(poly.fit_transform(X)), color = 'blue')#!LinReg2

plt.title("Linear Regression")
plt.xlabel("Years of Exp")
plt.ylabel("Salary")
plt.show()
