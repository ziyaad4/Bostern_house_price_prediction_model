Boston House Price Prediction


This repository contains a machine learning model developed to predict housing prices in Boston based on various neighborhood and property features. The project leverages regression techniques to estimate the median value of homes, assisting stakeholders in understanding the factors influencing housing prices.

Project Overview


The primary objective of this project was to build an accurate predictive model that utilizes the Boston housing dataset to estimate home prices. The project involved data preprocessing, feature engineering, model selection, and evaluation using performance metrics such as Mean Squared Error (MSE).

Dataset
The model was trained on the Boston housing dataset, which includes the following features:

CRIM: Crime rate by town

ZN: Proportion of residential land zoned for lots over 25,000 sq. ft.

INDUS: Proportion of non-retail business acres per town

CHAS: Charles River dummy variable (1 if tract bounds river; 0 otherwise)

NOX: Nitrogen oxide concentration (parts per 10 million)

RM: Average number of rooms per dwelling

AGE: Proportion of owner-occupied units built before 1940

DIS: Weighted distances to employment centers

RAD: Index of accessibility to radial highways

TAX: Full-value property tax rate per $10,000

PTRATIO: Pupil-teacher ratio by town

B: Calculated as 1000(Bk - 0.63)^2, where Bk is the proportion of Black residents by town

LSTAT: Percentage of lower-status population

MEDV: Median value of owner-occupied homes (target variable)


Installation

Clone the repository:

git clone https://github.com/yourusername/boston-house-price-prediction.git

Install the required packages:
pip install -r requirements.txt

Usage

Ensure the dataset (HousingData.csv) is in the root directory.

Run the PREDICTION.PY file to preprocess the data, train the model, and make predictions:

python PREDICTION.PY

Modify the script as needed to evaluate the model on new data or test additional metrics.

Methodology

Data Preprocessing: Handled missing values, normalized data, and prepared features for model training.

Feature Engineering: Selected and engineered relevant features based on domain knowledge and correlation analysis.

Model Selection: Compared multiple regression models, including linear regression and ensemble methods.

Model Evaluation: Assessed model performance using Mean Squared Error (MSE) and R-squared.

Results

The final model achieved an MSE of X and an R-squared of Y, demonstrating its accuracy in predicting Boston housing prices.


