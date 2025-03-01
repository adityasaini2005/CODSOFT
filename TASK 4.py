import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_movies(movie_title, movies_df, num_recommendations=5):
    # Ensure case-insensitive matching
    movie_title = movie_title.lower()
    
    # Check if the movie exists in the dataset
    idx = movies_df[movies_df['title'].str.lower() == movie_title].index
    if idx.empty:
        return f"Movie '{movie_title}' not found in the dataset."
    
    idx = idx[0]  # Get the first index
    
    # Convert genres into a TF-IDF matrix
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies_df['genres'].fillna(''))
    
    # Compute cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
    
    # Ensure the number of recommendations does not exceed available movies
    num_recommendations = min(num_recommendations, len(movies_df) - 1)
    
    # Get recommended movie titles
    movie_indices = [i[0] for i in sim_scores]
    return movies_df['title'].iloc[movie_indices].tolist()

# Extended dataset with 40 movies (Hollywood + Indian)
movies_data = {
    'title': [
        # Hollywood Movies
        "Inception", "Interstellar", "The Dark Knight", "The Matrix", "Avatar",
        "Titanic", "The Shawshank Redemption", "The Godfather", "Jurassic Park", "Forrest Gump",
        "Gladiator", "The Avengers", "The Lion King", "Pulp Fiction", "The Social Network",
        "The Silence of the Lambs", "Schindler's List", "Fight Club", "The Departed", "The Prestige",
        "Django Unchained", "The Wolf of Wall Street", "Mad Max: Fury Road", "Black Panther", "Parasite",
        "John Wick", "Deadpool", "The Conjuring", "It", "A Quiet Place",
        
        # Indian Movies
        "3 Idiots", "Dangal", "Zindagi Na Milegi Dobara", "Sholay", "Drishyam",
        "Gangs of Wasseypur", "Baahubali: The Beginning", "KGF: Chapter 1", "Kabir Singh", "Tumbbad"
    ],
    'genres': [
        # Hollywood Genres
        "Sci-Fi Thriller", "Sci-Fi Adventure", "Action Crime Thriller", "Sci-Fi Action", "Fantasy Adventure",
        "Romance Drama", "Drama Crime", "Crime Drama", "Sci-Fi Adventure", "Drama Romance",
        "Action Drama", "Action Sci-Fi", "Animation Adventure", "Crime Drama Thriller", "Drama Biography",
        "Horror Thriller", "Historical Drama", "Psychological Thriller", "Crime Thriller", "Sci-Fi Mystery",
        "Western Action Drama", "Crime Comedy Drama", "Action Adventure Sci-Fi", "Action Fantasy", "Thriller Drama",
        "Action Thriller", "Action Comedy", "Horror Mystery", "Horror Thriller", "Horror Sci-Fi",
        
        # Indian Genres
        "Comedy Drama", "Sports Drama", "Comedy Adventure", "Action Drama", "Mystery Thriller",
        "Crime Action", "Epic Fantasy", "Action Thriller", "Romance Drama", "Horror Fantasy"
    ]
}
movies_df = pd.DataFrame(movies_data)

# Show available movies
print("\n📌 Available movies:")
for idx, title in enumerate(movies_df['title'], start=1):
    print(f"{idx}. {title}")

# Get user input
while True:
    try:
        choice = int(input("\nEnter the number of the movie you like: "))
        if 1 <= choice <= len(movies_df):
            user_movie = movies_df.loc[choice - 1, 'title']
            break
        else:
            print("❌ Invalid number. Please select from the list.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Print recommendations
print(f"\n🎬 You selected: {user_movie}")
print("💡 Recommended movies:", recommend_movies(user_movie, movies_df))
