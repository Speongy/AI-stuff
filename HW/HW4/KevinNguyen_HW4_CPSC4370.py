#Dr. Sinan Kockara @2022
#Lamar University
#AI class: Logistic Regression
'''
Kevin Nguyen
HW4
CPCS 4350
Kockara
Fall 2020
'''

'''
Instead of covering many algorithms quickly at a high-level and using AI/ML algorithm libraries (e.g. Scikit-learn),
this course aims to explain important AI/ML algorithms in-depth. It is meant to prepare you to be a computer scientist
who develops new tools and algorithms rather than being a programmer who simply just uses available APIs or tools but
unaware on what is going on behind the scene. This class is designed to be a top class in the AI/Machine Learning Skills
Pyramid. I would like you to become a computer scientist who cannot only apply existing AI/ML algorithms but improve
existing algorithms or innovate/create new algorithms!
'''

import numpy as np
from numpy import log, dot, exp, shape
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# to compare our model's accuracy with sklearn model
from sklearn.linear_model import LogisticRegression

def standardize(X_tr):  # (x-Mean(x))/std(X) Normalizes data
    for i in range(shape(X_tr)[1]):
        X_tr[:, i] = (X_tr[:, i] - np.mean(X_tr[:, i])) / np.std(X_tr[:, i])
    return X_tr

def sigmoid(z):#Sigmoid/Logistic function
    sig = 1 / (1 + exp(-z))
    return sig

def cost(theta, X, y):#Cost calculation in Logistic Regression
    z = dot(X, theta)
    cost0 = y.T.dot(log(sigmoid(z)))
    cost1 = (1 - y).T.dot(log(1 - sigmoid(z)))
    cost = -((cost1 + cost0)) / len(y)
    return cost

def initialize(X):#Initializing X feature matrix and Theta vector
    thetas = np.zeros((shape(X)[1] + 1, 1))
    X = np.c_[np.ones((shape(X)[0], 1)), X]  # adding 691 rows of ones as the first column in X
    return thetas, X

def fit(X, y, alpha=0.001, iter=400):  # Gradient Descent
    thetas, X = initialize(X)
    '''
    as we increase alpha value, we can see the plot jumping around more.
    if the alpha is greater than one, all of our plots disappear 
    
    as we decrease the alpha value, the graph becomes more linear
    '''
    #making sure that their shapes match
    print("thetas.shape: ", thetas.shape)
    print("X.shape: ", X.shape)
    print("y.shape: ", y.shape)
    cost_list = np.zeros(iter, )
    for i in range(iter):#gradient descent iterations
        #derivative of J(Theta)= (1/m)*(X^T . (h(x)-y))
        thetas = thetas - alpha * dot(X.T, (sigmoid(dot(X, thetas)) - np.reshape(y, (len(y), 1))))#making y a column vector
        cost_list[i] = cost(thetas, X, y)#putting each iteration's cost in a list to display later
    global gthetas#not a good way of programming but works for now:))
    gthetas = thetas
    return cost_list

def predict(X):
    X = np.c_[np.ones((shape(X)[0], 1)), X]  # adding # rows of ones as the first column in X
    z = dot(X, gthetas)
    sig = sigmoid(z)
    lis = []
    for i in sig:
        if i > 0.5:#notice that boundary included in class 0
            lis.append(1)
        else:
            lis.append(0)
    # Another, more elegant way is: lis = np.where( sig >= 0.5, 1, 0 ) in this case boundary included in class 1
    return lis

def compare(Y_test, Y_pred, Y_pred1):
    # measure performance
    correctly_classified = 0
    correctly_classified1 = 0
    # counter
    count = 0
    for count in range(np.size(Y_pred)):
        if Y_test[count] == Y_pred[count]:
            correctly_classified = correctly_classified + 1
        if Y_test[count] == Y_pred1[count]:
            correctly_classified1 = correctly_classified1 + 1
        count = count + 1
    print("Accuracy on test set by our model       :  ", (
            correctly_classified / count) * 100)
    print("Accuracy on test set by sklearn model   :  ", (
            correctly_classified1 / count) * 100)

def main():
    df = pd.read_csv('Social_Network_Ads.csv')
    df['Gender'].replace(['Female', 'Male'], [0,1], inplace=True)
    # df['Gender'].replace( [0,1], ['Female', 'Male'], inplace=True)
    X = df.iloc[:, :-1].values 
    print(X)    
    '''
    #todo what if we add userid?
    with userid, it changes shape and raises accuracy to 65.8%? theta shape is (5,1)
    without userid, the accuracy for both models is 34.2% theta shape is (4,1)
    raises accuracy for both models
    i think it would be wise to include userid because because it raises our accuracy very high
    '''

    y = df.iloc[:, -1:].values  # take all rows in the last column

    X_tr, X_te, y_tr, y_te = train_test_split(X, y, 
        test_size=.3, random_state=0)#max test size is 1
    
    '''
    So when testing size is one, we don't have any data for training. Training 
    data is essential for building a model, so without it we dont have anything 
    to make a model.  

    so more training means we have barely anything to test against our model and 
    more testing means we have barely anything to make our model

    with userid and test_size 1, we get 100 accuracy
    at .6 is the lowest and then it goes back up as we increase
    at .9 both of the accuracies are different
    
    #todo increasing random state will also randomize accuracy 
    #todo changing test size changes shape of the graph and makes mor accurate
    #todo changing the test size to one brings the accuracy to 0 and drastically
    #todo changes the shape
    #todo decreasing the test size to 0.001 also brings the accuracy to 0
    '''
    
    
    X_tr = standardize(X_tr)
    
    '''
        #todo if we turn off standardize, our model becomes highly inaccurate 
        #todo sklearn model becomes more accurate
        #todo nothing is shown on the plot
        #todo our model seems to converge much faster than the sklearn model
        We standardize our data because we have features of different degrees and magnitude, so standardization
        makes sure the gradient descent converges smoother. 
    '''

    plt.title("Alpha Value = 8")
    cost_list = fit(X_tr, y_tr)
    plt.scatter(range(len(cost_list)), cost_list, c="blue")
    plt.show()

    y_pred = predict(X_te)#predicting with our own Logistic Regression implementation
    # Predicting with scikit learn's LogisticRegression() implementation
    model1 = LogisticRegression()
    model1.fit(X_tr, y_tr)
    y_pred1 = model1.predict(X_te)

    compare(y_te, y_pred, y_pred1)

main()#main driving function call


'''

#TODO Can we replace gradient descent with Normal Equation for logistic regression? Explain your reasoning!

Well not likely, only one discriminative method in classification theory,
linear regression... (linear discriminant analysis/fischer discriminant are
generative, and even they have a closed form solution due to the extreme
simplicity of the distributions fitted).
So, what made Normal Equation so successful in linear regression?
Because once you've computed your derivatives, you'll find that the
outcome is a set of linear equations, m equations with m variables, which
we know can be solved directly using matrix inversions (and other
techniques). When logistic regression costs are differentiated, the
resultant issue is no longer linear... it is convex (thus global optimum), but
not linear, and as a result, present mathematics does not offer us with
tools powerful enough to identify the optimum in closed form solution
'''