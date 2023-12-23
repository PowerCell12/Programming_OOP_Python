from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):

        if username in [h.username for h in self.users_collection]:
            raise Exception("User already exists!")

        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."


    def upload_movie(self, username: str, movie: Movie):

        if username not in [h.username for h in self.users_collection]:
            raise Exception("This user does not exist!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user = None
        for us in self.users_collection:
            if us.username == username:
                user = us
                break

        if movie in self.movies_collection or movie in user.movies_owned:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."



    def edit_movie(self, username: str, movie: Movie, **kwargs):

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")


        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")


        for key,value in kwargs.items():

            if key == "title":
                movie.title = value
            elif key == "year":
                movie.year = value
            elif key == "age_restriction":
                movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."



    def delete_movie(self, username: str, movie: Movie):

        if movie not in self.movies_collection: ## if error check
            raise Exception(f"The movie {movie.title} is not uploaded!")


        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        movie.owner.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."



    def like_movie(self, username: str, movie: Movie):

        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        user = None
        for us in self.users_collection:
            if us.username == username:
                user = us
                break


        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."


    def dislike_movie(self, username: str, movie: Movie):

        user = None
        for us in self.users_collection:
            if us.username == username:
                user = us
                break

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."


    def display_movies(self): ## check if error
        if not self.movies_collection:
            return "No movies found."

        y = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        return "\n".join([m.details() for m in y])


    def __str__(self):

        list = []
        if not self.users_collection:
            list.append("All users: No users.")
        else:
            list.append(f"All users: {', '.join([u.username for u in self.users_collection])}")

        if not self.movies_collection:
            list.append("All movies: No movies.")
        else:
            list.append(f"All movies: {', '.join([m.title for m in self.movies_collection])}")

        return "\n".join(list)
