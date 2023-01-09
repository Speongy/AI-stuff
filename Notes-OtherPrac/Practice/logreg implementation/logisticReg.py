#Let's learn more about logistic regression!!!!!!!!!!!!!

'''
#?What's the difference between logistic and linear regression?

The outcome

linear is continuous
logistic is discrete

wtf is a continuous and discrete output

okay, so if we predict the value of the share, it's continuous
    - predicted Y can exceed 0 and 1 range

if we predict if an indivdual has diabetes or not, that's discrete
    - predicted Y is in between 0 and 1 range

#! Three types of logistic regression

#? Binary Logistic Regression
    - only TWO possible types for an outcome value
    - 1 or 0

#? Multinomial Logistic Regression
    - THREE or MORE possible tpes for an outcome
    - NOT ordered
    - For example, the weather. Possible outcomes include rainy, sunny, windy, cloudy, etc.

#? Ordinal Logistic Regression
    - THREE or MORE possible tpes for an outcome
    - ORDERED
    - For example, on a scale from 1 - 10, with 1 being the worst and 10 being the best.

#? Applications of Logistic Regression
    - Predicting if email is spam or not
    - Seeing if a patient has diabetes or not
    - Predicting heart attacks

#! How does LogReg work?

Sigmoid or logistic is implemented as a cost function
For predicting probabilities, the sigmoid can be used

#! MATH OF LOG REG

F(z) = 1 / (1-e^(-z))
z = w0 + w1x1 + w2x2 + ... + wnxn

w0, w1, w2, w3,... is used to represent the regression of the coefficient
x0, x1, x2, x3,... is used to represent the features or independent variables

'''

#TODO Let's implement Logistic Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset =  pd.read_csv("diabetes.csv")

feature_columns = ['Pregnancies','Glucose','Blood Pressure','Skin Thickness','Insulin','BMI','Diabetes Pedigree Function', 'Age']

x = dataset[feature_columns]
y = dataset.target

from sklearn.model_selection import train_test_split
x_train, y_train, x_test, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LogisticRegression

logReg = LogisticRegression()
logReg.fit(x_train, y_train)

y_pred = logReg(x_test)

from sklearn import metrics

confusion = metrics.confusion_matrix(y_test, y_pred)    
