# Credit Card Fraud Detection using Machine Learning

## Overview

This project aims to detect fraudulent credit card transactions using Machine Learning techniques. Due to the highly imbalanced nature of the dataset, SMOTE (Synthetic Minority Oversampling Technique) is used to balance the classes and improve model performance.

The project uses the Random Forest Classifier to classify transactions as either fraudulent or genuine and evaluates the model using various performance metrics.

## Dataset

The dataset used in this project is the Credit Card Fraud Detection dataset from Kaggle.

Dataset link:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud


## Dataset Information

The dataset contains credit card transactions made by European cardholders.

* Total Transactions: **284,807**
* Genuine Transactions (Class = 0): **284,315**
* Fraudulent Transactions (Class = 1): **492**

### Features

* Time
* Amount
* V1, V2, V3, ..., V28 (anonymized features obtained using PCA)
* Class

  * 0 → Genuine Transaction
  * 1 → Fraudulent Transaction

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Imbalanced-learn (SMOTE)
* Pickle

## Exploratory Data Analysis

The following visualizations were performed:

* Class Distribution Plot
* Pie Chart of Fraud vs Genuine Transactions
* Correlation Heatmap
* Transaction Amount Distribution
* Boxplots
* Scatter Plots
* Feature Importance Plot

## Data Preprocessing

* Loaded the dataset
* Checked missing values
* Feature scaling using StandardScaler
* Train-Test Split
* Handled class imbalance using SMOTE

## Machine Learning Model

### Random Forest Classifier

```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

## Model Evaluation

The model performance was evaluated using:

* Classification Report
* Precision
* Recall
* F1-Score
* Confusion Matrix

## Model Saving

The trained model was saved using Pickle:

```python
import pickle

with open("fraud_model.pkl", "wb") as file:
    pickle.dump(rf, file)
```

## Results

The Random Forest model successfully detected fraudulent transactions with high accuracy and achieved strong Precision, Recall, and F1-Score values.

## Sample Visualizations

* Correlation Heatmap
* Confusion Matrix
* Feature Importance Plot
* Class Distribution Graph

## Conclusion

This project demonstrates how Machine Learning can be used to detect fraudulent credit card transactions effectively. Since the dataset is highly imbalanced, SMOTE was applied to balance the classes. A Random Forest Classifier was trained and evaluated using precision, recall, F1-score, and confusion matrix. The trained model was finally saved using Pickle for future use.
