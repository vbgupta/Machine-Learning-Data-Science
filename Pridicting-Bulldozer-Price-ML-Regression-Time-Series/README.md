# Pridicting-Bulldozer-Price-ML-Regression-Time-Series-.ipynb
> Predicting Bulldozer 🚜 Price Using Machine Learning - Regression

### 1. Problem Definition
> How well can we predict the future sale price of a bulldozer, given its characteristics and previously given examples and is the sale price similar?

### 2. Data
> The data is downloaded from Kaggle Blue Book for Bulldozers: https://www.kaggle.com/c/bluebook-for-bulldozers/

> The data for this competition is split into three parts:

* Train.csv is the training set, which contains data through the end of 2011.
* Valid.csv is the validation set, which contains data from January 1, 2012 - April 30, 2012 You make predictions on this set throughout the majority of the competition. Your score on this set is used to create the public leaderboard.
* Test.csv is the test set, which won't be released until the last week of the competition. It contains data from May 1, 2012 - November 2012. Your score on the test set determines your final rank for the competition.

### 3. Evaluation
> The evaluation metrics for this is the RMSLE - Root Mean Squared Log Error - between predicted and auctioned prices.

> The goal for this machine learning project is to build a model that minimizes the RMSLE.

### 4. Features
**The key fields are in train.csv are:**

* SalesID: the uniue identifier of the sale
* MachineID: the unique identifier of a machine. A machine can be sold multiple times
* saleprice: what the machine sold for at auction (only provided in train.csv) saledate: the date of the sale


#### Conclusion:
> The Kaggle Competition needs the RMSLE score: 0.48851205767382017
![alt text](https://github.com/vbgupta/Pridicting-Bulldozer-Price-ML-Regression-Time-Series-.ipynb/blob/main/RMSLE%20SCORE.JPG?raw=true)

> The Kaggle Competiton need the predicted scores in a dataframe with the SaleID 
![alt text](https://github.com/vbgupta/Pridicting-Bulldozer-Price-ML-Regression-Time-Series-.ipynb/blob/main/Dataframe.JPG?raw=true)
