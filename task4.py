# Sample movie dataset
movies = {
    'The Shawshank Redemption': ['Drama'],
    'The Godfather': ['Crime', 'Drama'],
    'The Dark Knight': ['Action', 'Crime', 'Drama'],
    'Pulp Fiction': ['Crime', 'Drama'],
    'The Lord of the Rings: The Return of the King': ['Adventure', 'Fantasy'],
    'Forrest Gump': ['Drama', 'Romance'],
    'The Matrix': ['Action', 'Sci-Fi'],
    'Inception': ['Action', 'Adventure', 'Sci-Fi'],
    'Interstellar': ['Adventure', 'Drama', 'Sci-Fi'],
    'The Silence of the Lambs': ['Crime', 'Drama', 'Thriller']
}

# Function to recommend movies based on user preferences
def recommend_movies(user_preferences, movies):
    recommended_movies = []
    for movie, genres in movies.items():
        # Calculate similarity score based on genre overlap
        genre_overlap = set(genres) & set(user_preferences)
        similarity_score = len(genre_overlap) / len(user_preferences)
        recommended_movies.append((movie, similarity_score))
    
    # Sort recommended movies by similarity score in descending order
    recommended_movies.sort(key=lambda x: x[1], reverse=True)
    
    return recommended_movies

# Example user preferences
user_preferences = ['Drama', 'Crime']

# Get recommended movies based on user preferences
recommended_movies = recommend_movies(user_preferences, movies)

# Print the top N recommended movies
N = 5
print(f"Top {N} recommended movies based on your preferences:")
for i in range(N):
    movie, similarity_score = recommended_movies[i]
    print(f"{movie} (Similarity Score: {similarity_score:.2f})")
