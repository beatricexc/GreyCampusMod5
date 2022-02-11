# K-Nearest Neighbour (K-NN)
# wW are going to predict if each user is buying something or not 

#Importing the library

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing the datset
dataset = pd.read_csv(r"C:\Users\beatricexc\Downloads\Social_Network_Ads.csv")
X = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:,4].values

# Splitting the dataset into the Training set and the Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state= 42)
# random_state = provides deterministic outcome, meaning each time I run the test, the outcome
# will be fixed ( will not change)

# Feature Scaling (Data Pre-processing Technique)
from sklearn.preprocessing import StandardScaler #standardising the values 
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#Fitting the KNN to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2) 
# p Power parameter for the Minkowski metric.
# When p = 1, this is equivalent to using manhattan_distance (l1),
 #and euclidean_distance (l2) for p = 2. For arbitrary p, minkowski_distance (l_p) is used.
classifier.fit(X_train, y_train)

# Predicting on the Test set
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix to compare the results
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Plotting the confusion matrix 
ax = sns.heatmap(cm, annot = True, cmap = 'Blues')
ax.set_title('Confusion Matrix with labels \n\n')
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Valules')

plt.show()
