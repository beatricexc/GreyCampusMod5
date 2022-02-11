# GreyCampusMod5

## KNN
K-Nearest Neighbour can be used for both classification and regression predictive problems. It uses the concept principal or the similarity principal also known as the distance or proximity/ closeness. Best used in *Recommendation Engine*. 

K should be odd number: K = odd , the best K number is the one that renders the smallest error of them all.

Depending on the model we're using, KNN returns differnt parameters : 

- regression : it returns the mean of the K labeles;
- classification : it returns the mode of the labels;

**Usage**: to classify the new cases based on all the available nearest neighbouring cases.

**Assumptions**: 
- KNN assumes that the data is in a feature space
- meaning, the data points are in a metric space
- the data can be scalars or even multidimensional vectors 

3 important reasons to choose KNN
1. Ease of interpretation
2. Calculation time
3. Predictive power

**Disadvantages** : 
- no insight into the importance/role of each predictor;
- it is prone to over-fitting ( it needs a test set)
- can be computationally heavy for large K
- it needs a lot of DATA


## Types of Measures in KNN

Hamming Distance

Euclidian Distance

![image](https://user-images.githubusercontent.com/72341578/153647825-4004923f-8578-436a-9cca-24ee93455674.png)

Manhattan Distance (Taxicab or City Block)

Minkowski Distance
