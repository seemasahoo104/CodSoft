def predict_rating(model, vectorizer):

    genre = input("Enter Genre: ")
    director = input("Enter Director: ")
    actor1 = input("Enter Actor 1: ")
    actor2 = input("Enter Actor 2: ")
    actor3 = input("Enter Actor 3: ")

    movie = [f"{genre} {director} {actor1} {actor2} {actor3}"]

    movie_vector = vectorizer.transform(movie)

    prediction = model.predict(movie_vector)

    print("Predicted Rating:", round(prediction[0],2))
   