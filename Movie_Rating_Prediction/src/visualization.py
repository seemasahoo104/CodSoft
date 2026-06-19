import matplotlib.pyplot as plt
import seaborn as sns
def visualize_data(df):
    # 1. Rating Distribution
    plt.figure(num="Figure 1: Rating Distribution", figsize=(8,5))
    plt.hist(df['Rating'],bins=20)
    plt.title("Distribution of Movie Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.show()

    # 2. Top 10 Genres
    plt.figure(num="Figure 2: Top 10 Genres", figsize=(8,5))
    df['Genre'].value_counts().head(10).plot(kind='bar')
    plt.title("Top 10 Genres")
    plt.xlabel("Genre")
    plt.ylabel("Number of Movies")
    plt.xticks(rotation=45)
    plt.show()

    # 3. Top 10 Directors
    plt.figure(num="Figure 3: Top 10 Directors", figsize=(8,5))
    df['Director'].value_counts().head(10).plot(kind='bar')
    plt.title("Top 10 Directors")
    plt.xlabel("Director")
    plt.ylabel("Number of Movies")
    plt.xticks(rotation=45)
    plt.show()

    # 4. Top 10 Actors
    plt.figure(num="Figure 4: Top 10 Actors", figsize=(8,5))
    df['Actor 1'].value_counts().head(10).plot(kind='bar')
    plt.title("Top 10 Actors")
    plt.xlabel("Actor")
    plt.ylabel("Number of Movies")
    plt.xticks(rotation=45)
    plt.show()

    # 5. Box Plot of Ratings
    plt.figure(num="Figure 5: Box Plot of Ratings", figsize=(8,5))
    plt.boxplot(df['Rating'])
    plt.title("Box Plot of Ratings")
    plt.ylabel("Rating")
    plt.show()

    # 6. Movies Released Per Year
    plt.figure(num="Figure 6: Movies Released Per Year", figsize=(8,5))
    df['Year'].value_counts().sort_index().plot()
    plt.title(" Movies Released Per Year")
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.show()

    # 7. Scatter Plot: Year vs Rating
    plt.figure(num="Figure 7: Year vs Rating", figsize=(8,5))
    plt.scatter(df['Year'],df['Rating'])
    plt.title("Year vs Rating")
    plt.xlabel("Year")
    plt.ylabel("Rating")
    plt.xticks(rotation=45)
    plt.show()

    # 8. Correlation Heatmap
    plt.figure(num="Figure 8: Correlation Heatmap", figsize=(8,5))
    sns.heatmap(df.corr(numeric_only=True),
                annot=True,
                cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()
     
    
