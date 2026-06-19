# Titanic Survival Prediction using Machine Learning

## Overview
This project aims to predict whether a passenger on the Titanic survived or not using Machine Learning techniques. The model is trained on the famous Titanic dataset, which contains information such as passenger age, gender, ticket class, fare, and family details.

This is a beginner-friendly classification project and one of the most popular introductory Machine Learning projects.

## Objective

To build a classification model capable of predicting passenger survival based on historical data from the Titanic dataset.

## Dataset

The dataset contains information about individual passengers, including:

* Passenger Class ("Pclass")
* Gender ("Sex")
* Age
* Number of Siblings/Spouses Aboard ("SibSp")
* Number of Parents/Children Aboard ("Parch")
* Fare
* Embarkation Port ("Embarked")
* Survival Status ("Survived")

### Target Variable

* **0** — Did Not Survive
* **1** — Survived

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn

## Methodology

### Data Preprocessing

* Handled missing values.
* Removed unnecessary features.
* Encoded categorical variables.
* Prepared feature and target variables.

### Exploratory Data Analysis

* Survival distribution analysis.
* Gender-wise survival analysis.
* Passenger class analysis.
* Age and fare distribution visualization.

### Model Development

* Split the dataset into training and testing sets.
* Trained a Logistic Regression model.
* Generated predictions on unseen data.

### Model Evaluation

The model performance was evaluated using:

* Accuracy Score
* Confusion Matrix
* Classification Report

## Results

The Logistic Regression model achieved an accuracy of approximately **80%**, demonstrating its effectiveness in predicting passenger survival.

## Key Learnings

* Data Cleaning and Preprocessing
* Handling Missing Values
* Feature Engineering
* Exploratory Data Analysis
* Logistic Regression
* Model Evaluation Techniques
* Binary Classification

## Conclusion

This project provides a practical introduction to Machine Learning and demonstrates how predictive models can be used to solve real-world classification problems. Through effective preprocessing and Logistic Regression, the model achieved reliable performance in predicting passenger survival.

