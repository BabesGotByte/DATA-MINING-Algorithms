# Package imports

import matplotlib.pyplot as plt
import numpy as np
import os 
import sys
from PIL import Image
import random
import cv2
import functools
from copy import deepcopy

height = 64
width = 64
original = os.path.join('dataset','photos')
new = os.path.join('dataset','compressed')
files=os.listdir(original)

#resize images 
for file in files:    
    path =  os.path.join(original,file)
    new_path = os.path.join(new, file)
    image = Image.open(path)
    image = image.resize((height,width), Image.ANTIALIAS)   
    image.save(new_path)

# get all images from the reduced dataset, and construct the dataset
Y = [] # output
Yid = {} # name to number Y_values
Yname = {} # nuber to name Y_inverse_values 

X = [] # training dataset R
files=os.listdir(new)

for file in files:    
    # for X
    image_path=os.path.join(new, file)
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image.flatten()
    X.append(image)
    # for Y
    name = file.split("_")[0]
    if(name not in Yid) :
        val = len(Yid) + 1
        Yid[name] = val
        Yname[val] = name
    Y.append(Yid[name])
        
X = np.array(X)
Y = np.array(Y)

#mean_intensities
u = np.mean(X, axis=0)


# split into training and testing data
X_train = []
X_test = []
Y_train = []
Y_test = []

percent = 80 
sample_size = int((percent / float(100)) * X.shape[0])
training_indices = random.sample(range(0, X.shape[0]), sample_size)
for i in range(X.shape[0]) :
    if(i in training_indices) :
        X_train.append(X[i])
        Y_train.append(Y[i])
    else :
        X_test.append(X[i])
        Y_test.append(Y[i])
        
X_train = np.array(X_train)
Y_train = np.array(Y_train)
X_test = np.array(X_test)
Y_test = np.array(Y_test)

#noralising training dataset
utrain = np.mean(X_train,axis=0)
X_train = X_train - utrain

#normlaising testing dataset
X_test_original = deepcopy(X_test)
utest = np.mean(X_test,axis=0)
X_test = X_test - utest

# finding covariance matrix 
covariance = (1 / float(X_train.shape[0])) * np.dot(np.transpose(X_train), X_train)

# finding best K values
u, s, v = np.linalg.svd(covariance)
totalsum = 0
for i in range(s.shape[0]) :
    totalsum = totalsum + s[i]
sm = 0
for i in range(s.shape[0]) :
    sm = sm + s[i]
    val = float(sm) / float(totalsum)
    if(val >= 0.99) :
        K=i+1
        break

#calculating eigen vectors
EigenVectors = []
for i in range(K) :
    EigenVectors.append(u[:,i])
EigenVectors = np.array(EigenVectors)

EigenVectors

X_train.shape

# getting the eigen faces
eigen_faces = np.dot(X_train, np.transpose(EigenVectors))

# for testing data => already done mean normalization
projected_data = np.dot(X_test, np.transpose(EigenVectors))

X_train = eigen_faces
X_test = projected_data

#predictions
predictions = []

for i in range(X_test.shape[0]) :
    min_distance = -1
    for j in range(X_train.shape[0]) :
        distance = np.linalg.norm(X_train[j] - X_test[i]) 
        if(min_distance == -1 or min_distance > distance) :
            min_distance = distance
            label = Y_train[j]
    predictions.append(label)

predictions

Y_test

#actual v/s prediction
for i in range(X_test.shape[0]):
    print("actual: " +Yname[Y_test[i]] +" , predictions: " + Yname[predictions[i]])

correct=0
for i in range(X_test.shape[0]):
    if predictions[i]==Y_test[i]:
        correct+=1
print("correct Predictions: " ,(correct) , " Out of: ",(X_test.shape[0]))
print("percentage accuracy: ", (correct / X_test.shape[0]) * 100)



