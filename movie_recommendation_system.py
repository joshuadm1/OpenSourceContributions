# movie_recommendation_system.py

class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def __str__(self):
        return f"{self.title} ({self.genre})"


class User:
    def __init__(self, name):
        self.name = name
        self.ratings = {}

    def rate_movie(self, movie, rating):
        self.ratings[movie] = rating
        print(f"Movie '{movie.title}' rated as {rating} by {self.name}.")

    def get_recommendations(self, movies, min_rating):
        recommended_movies = []
        for movie in movies:
            if movie not in self.ratings or self.ratings[movie] < min_rating:
                recommended_movies.append(movie)
        return recommended_movies

# Usage example
movie1 = Movie("The Shawshank Redemption", "Drama")
movie2 = Movie("Inception", "Action")
movie3 = Movie("The Dark Knight", "Action")
movie4 = Movie("Pulp Fiction", "Crime")
movie5 = Movie("Fight Club", "Drama")

user1 = User("John")
user2 = User("Alice")

user1.rate_movie(movie1, 5)
user1.rate_movie(movie2, 4)
user1.rate_movie(movie4, 3)

user2.rate_movie(movie2, 5)
user2.rate_movie(movie3, 4)
user2.rate_movie(movie5, 5)

movies = [movie1, movie2, movie3, movie4, movie5]

recommended_movies_user1 = user1.get_recommendations(movies, 4)
recommended_movies_user2 = user2.get_recommendations(movies, 4)

print(f"Recommended movies for {user1.name}:")
for movie in recommended_movies_user1:
    print(movie)

print(f"\nRecommended movies for {user2.name}:")
for movie in recommended_movies_user2:
    print(movie)
