from src.preprocessing import load_data
from src.train_model import train
from src.predict import predict_rating
from src.visualization import visualize_data

print("Loading data...")
df = load_data()
print("Data loaded successfully!")
visualize_data(df)

print("Training model...")
model, vectorizer = train(df)
print("Model trained successfully!")

print("Predicting...")
predict_rating(model, vectorizer)

print("Done!")