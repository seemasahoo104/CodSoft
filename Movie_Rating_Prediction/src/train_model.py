from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

def train(df):

    X = df['Features']
    y = df['Rating']

    vectorizer = TfidfVectorizer(stop_words='english')

    X_vectorized = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_vectorized,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=10,
        random_state=42
    )

    model.fit(X_train, y_train)
    joblib.dump(model, "movie_rating_model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Mean Absolute Error:", mae)
    print("R2 Score:", r2)

    return model, vectorizer