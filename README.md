# DATA-MINING-Algorithms

[![Generic badge](https://img.shields.io/badge/DATA-MINING-<BLUE>.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/MACHINE-LEARNING-<BLUE>.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/LANGUAGE-PYTHON-<BLUE>.svg)](https://shields.io/)

## Algorithms Discussed:

We have discussed the following algorithms:

* Apriori algorithm
* Decision tree ID3 algorithm
* FP Growth Algorithm
* Bayesian Classification Algorithm
* Web Crawling Problem
* KNN Algorithm
* Linear Regression with One variable
* Linear Regression with Multiple Variables
* Support Vector Machine Model
* BIRCH Algorithm
* DBSCAN Algorithm
* K-Mean Algorithm
* PAM Algorithm
* Decision tree using C4.5 and CART algorithm
* Hierarchical Clustering Algorithm
* OPTICS Algorithm 

## Problem Statements

## Algorithm-1:
Dataset used: weather.csv <br/>

Perform the following operations on the weather dataset using Pandas.<br/>
* Reading a dataset into a dataframe.<br/>
* Dropping rows with missing(”NaN”) values.<br/>
* Dropping columns with missing(”NaN”) values.<br/>
* Filling the ”Nan” values with mean, median.<br/>
* Split data set by row and column wise.<br/>

## Algorithm-2:
Dataset used: data folder(chess.dat, mushroom.txt,retail.dat, FILE1.txt, FILE2.txt) <br/>

Implement Apriori algorithm for association rules. Run the algorithm with two different support and confidence level defined by you. (Chees, Mushroom, Retail dataset can be used.)<br/>
* Print closed itemset.<br/>
* Print closed frequent itemset.<br/>

Note: Let Y ⊆ I and X ⊆ Y<br/>
If the X is an infrequent itemset, then Y is also an infrequent itemset. On that basis apply the Apriori algorithm.<br/>

## Algorithm-3:
Dataset used: car.data.txt <br/>

Implement decision tree ID3 algorithm for the given dataset for Car Evaluation Database. <br/>
* Attribute Information: Six input attributes: buying, maint, doors, persons, lugboot, safety <br/>
* Class Values: unacc, acc, good, vgood <br/>
* Attributes: <br/>
    ∗ buying: vhigh, high, med, low. <br/>
    ∗ maint: vhigh, high, med, low. <br/>
    ∗ doors: 2, 3, 4, 5,more. <br/>
    ∗ persons: 2, 4, more. <br/>
    ∗ lug-boot: small, med, big. <br/>
    ∗ safety: low, med, high. <br/>

## Algorithm-4:<br>
Dataset used: Online Retail.xlxs <br/>

Implement FP Growth algorithm on the given dataset.

## Algorithm-5(i):<br>
Dataset used: DATASET.xlsx <br/>  

Using Baysian classfication, predict the class (Target wait) for the following sample. <br/>
X=(alt=T, Bat=T, Fri=F, Hun=T, Pat=Some, Price=$$$, Rain=T,Res=T, Type=Italian, Est>60).<br/>

## Algorithm-5(ii):<br>

The task is a web crawling problem.<br/>  
* Write a program to stream web page, http://en.wikipedia.org/wiki/India.<br/>  
* Count the number of hyperlinks in this page.<br/>  
* Provide a unique number to each link.<br/>  
* Select a link from the found links and repeat the steps from 1 to 3.<br/>  
* Repeat above steps at least two times and generate an adjacency matrix.<br/>  

## Algorithm-6(i):<br>
Dataset used: DATASET.xlsx <br/>  

Using Baysian classfication, predict the class (Target wait) for the following sample. <br/>
X= (alt = T, Bat = T, Fri = F, Hun = T, Pat = Some, Price = $$$, Rain = T, Res = T, Type = Italian, Est > 60).<br/> 

## Algorithm-6(ii):<br>
Dataset used: data_sheet.xlsx <br/>  

Predict a class label using naïve Bayesian classification for the tuple: <br/>
X = {age = “<= 30”, income = “medium”, student = “yes”, credit rating = “fair”} <br/>

## Algorithm-7:<br>
Dataset used: iris-dataset.csv , iris-test.csv <br/>  

Implementation the KNN algorithm for classification purpose in Python using the following instructions: <br/>
* The Iris data set is bundled for test, however you are free to use any data set of your choice provided that it follows the specified format. <br/>
Data set format: <br/>
* Attributes can be integer or real values. <br/>
* List attributes first, and add response as the last parameter in each row. <br/>
    * E.g. [4.5, 7, 2.6, "Orange"], where the first 3 numbers are values of attributes and "Orange" is one of the response classes. <br/>
    * Another example can be [1.2, 4.3, 3], in this case, there are 2 attributes while the response class is the integer 3. <br/>
* Responses can be integer, real or categorical. <br/>

## Algorithm-8(i):<br>
Dataset used: ex1data1.txt <br/>  

Implement the linear regression with one variable to predict profits for a food truck.<br/>
Suppose you are the CEO of a restaurant franchise and are considering different cities for opening a new outlet. The chain already has trucks in various cities and you have data for profits and populations from the cities.
You would like to use this data to help you select which city to expand to next. The file ex1data1.txt contains the dataset for our linear regression problem. The first column is the population of a city and the second column is the profit of a food truck in that city. A negative value for profit indicates a loss.

## Algorithm-8(i):<br>
Dataset used: ex1data2.txt <br/>  

Implement the linear regression with multiple variables to predict the prices of houses.<br/>
Suppose you are selling your house and you want to know what a good market price would be. One way to do this is to first collect information on recent houses sold and make a model of housing prices. The file ex1data2.txt contains a training set of housing prices in Portland, Oregon. The first column is the size of the house (in square feet), the second column is the number of bedrooms, and the third column is the price of the house.

## Algorithm-9(i):<br>
Dataset used: data.xlsx <br/>  

Write a program to train a linear SVM using the dataset given in file data.xlsx and test it using some unseen data. (Don’t use library function of SVM)

## Algorithm-9(ii):<br>
Dataset used: ionosphere.data <br/>  

Train an SVM for ionosphere dataset. Divide the dataset into training and testing sets and find accuracy of SVM.

## Algorithm-10:<br>
Dataset used: Dataset.txt <br/>  

Perform the BIRCH algorithm for the dataset.

## Algorithm-11:<br>
Dataset used: Dataset.txt <br/>  

Perform the DBSCAN algorithm for the dataset.

## Algorithm-12(i):<br>
Dataset used: Absenteeism_at_work.xls <br/>  

Perform the K-Mean algorithm for the dataset.

## Algorithm-12(ii):<br>
Dataset used: Absenteeism_at_work.xls <br/>  

Perform the PAM algorithm for the dataset.

## Algorithm-13:<br>
Dataset used: car.data.txt <br/>

Implement decision tree using C4.5 and CART algorithm for the for Car Evaluation Dataset. <br/>
* Attribute Information: Six input attributes: buying, maint, doors, persons, lug boot, safety <br/>
* Class Values: unacc, acc, good, vgood  <br/>
* Attributes:  <br/>
    Buying: vhigh, high, med, low.  <br/>
    Maint: vhigh, high, med, low.  <br/>
    Doors: 2, 3, 4, 5more.  <br/>
    Persons: 2, 4, more.  <br/>
    Lug boot: small, med, big. <br/> 
    Safety: low, med, high.  <br/>
    
## Algorithm-14:
Dataset used: qla.csv , matrix.xlsx <br/>

Implement Hierarchical clustering algorithm and apply it on the qla.xlxs dataset. Also, show the resulting dendograms after applying average linkage approach.

## Algorithm-15:
Dataset used: data1.xlsx, data2.xlsx <br/>

Implement OPTICS algorithm and apply it on datasets (for this epsilon = 0.02, minPts = 500) and output each point's reachability distance, core distance and order of points in the reachability graph.

## Algorithm-16:
Dataset used: Dataset Manual.txt <br/>
Code: PCA Folder<br/>

Implement Face detection algorithm using Principle Component Analysis(PCA).

## Algorithm-17:
Dataset used: dataset <br/>

Implement Face detection algorithm using Linear Discriminant Analysis(LDA).

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)











