# Movie Rating Prediction using Machine Learning

## Overview

This project predicts movie ratings based on features such as Genre, Director, and Actors using Machine Learning techniques. The model analyzes historical movie data and estimates the rating a movie may receive from users or critics.

The project demonstrates the complete machine learning workflow, including data preprocessing, feature engineering, visualization, model training, evaluation, and prediction.

## Dataset

**Dataset:** IMDb Movies India Dataset

**Features Used:**

* Genre
* Director
* Actor 1
* Actor 2
* Actor 3

**Target Variable:**

* Rating

## Features

* Data preprocessing and cleaning
* Handling missing values
* Feature engineering
* Data visualization
* TF-IDF vectorization
* Random Forest Regression
* Model evaluation using MAE and R² Score
* Movie rating prediction
* Model saving using Joblib

## Visualizations

The project includes:

1. Distribution of Movie Ratings
2. Top 10 Genres
3. Top 10 Directors
4. Top 10 Actors
5. Box Plot of Ratings
6. Movies Released Per Year
7. Year vs Rating Scatter Plot
8. Correlation Heatmap

## Libraries Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib

## Run the Project

```bash
python main.py
```

## Example Input

```
Enter Genre: Action
Enter Director: Rohit Shetty
Enter Actor 1: Ajay Devgn
Enter Actor 2: Kareena Kapoor
Enter Actor 3: Arjun Kapoor
```

## Example Output

```
Predicted Rating: 5.0
```

## Evaluation Metrics

* Mean Absolute Error (MAE)
* R² Score

Example:

```
Mean Absolute Error: 0.97
R2 Score: 0.15
```

## Saved Files

* movie_rating_model.pkl
* vectorizer.pkl

## Future Improvements

* Compare multiple machine learning models
* Hyperparameter tuning
* Build a Streamlit web application
* Deploy the model
* Add a recommendation system

