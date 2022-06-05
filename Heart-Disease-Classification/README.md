# Heart-Disease-Classification
## Machine Learning Classification Model to Predict Heart Disease

> This notebook looks into using various Python-based libraries in an attempt to build a machine learning model capable of predicting whether of not someone has heart disease based on specific medical attributes.

### We are going to take the following approach

1. Problem definition
2. Data
3. Evaluation
4. Features
5. Modelling
6. Experimentation

#### 1. Problem Definition:
Given clinical parameters about a patient, can we predict whether of not a patient has heart disease.

#### 2. Data
The original data comes from the Cleveland UCI Machine Learning Repository. https://archive.ics.uci.edu/ml/datasets/heart+disease

Verison also available on Kaggle. https://www.kaggle.com/ronitf/heart-disease-uci

#### 3. Evaluation
If we can reach 95% accuacy at predicting whether of not a patient has heart disease during the proof of concept, well pursue the project

#### 4. Features
> Create a data dictionary

* age
* sex(1 = male, 0 = female)
* chest pain type (4 values)
* resting blood pressure
* serum cholestoral in mg/dl
* fasting blood sugar > 120 mg/dl
* resting electrocardiographic results (values 0,1,2)
* maximum heart rate achieved
* exercise induced angina
* oldpeak = ST depression induced by exercise
* relative to rest
* the slope of the peak exercise ST segment
* number of major vessels (0-3) colored by flourosopy
* thal: 3 = normal; 6 = fixed defect; 7 = reversable *defect

#### 5. Model
> Linear Regression
>> Hyperparameters that give us the best score with 2 iterations of RandomizedRearchCV: C = 0.1082636733874054, solver = 'liblinear' 
#### Final Metrics
![alt text](https://github.com/vbgupta/Heaart-Disease-Classification/blob/main/download.png?raw=true)

![alt text](https://github.com/vbgupta/Heaart-Disease-Classification/blob/main/download%20(1).png?raw=true)


