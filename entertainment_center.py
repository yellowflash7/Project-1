import fresh_tomatoes
import media

# Following are some of my favourite movies
fast_furious = media.Movie(
    "The Fast and Furious",
    "The Fast and the Furious (also known as Fast & Furious) is an American \
    franchise based on a series of action films ",
    "https://upload.wikimedia.org/wikipedia/en/8/8f/"
    "Fast_and_Furious_Poster.jpg",
    "https://www.youtube.com/watch?v=Gf1RToVnDeQ")
# print(toy_story.storyline)


jumper = media.Movie(
    "Jumper",
    "Jumper is a 2008 American science fiction action film loosely based on \
    the 1992 science fiction novel of the same name written by Steven Gould	",
    "https://upload.wikimedia.org/wikipedia/en/thumb/3/37/"
    "Jumperposter.jpg/215px-Jumperposter.jpg",
    "https://www.youtube.com/watch?v=2PQi5ueqig4")

Transformers = media.Movie(
    "Transformers",
    "Transformers is a movie about alien robots coming from space.",
    "https://upload.wikimedia.org/wikipedia/en/2/26/"
    "Transformers_The_Last_Knight_poster.jpg",
    "https://www.youtube.com/watch?v=yCOvcyfRPRk")

inception = media.Movie(
    "Inception",
    "The film stars Leonardo DiCaprio as a professional thief who \
    steals information by infiltrating the subconscious",
    "https://upload.wikimedia.org/wikipedia/en/2/2e/"
    "Inception_%282010%29_theatrical_poster.jpg",
    "https://www.youtube.com/watch?v=66TuSJo4dZM")

beautiful_creatures = media.Movie(
    "Beautiful Creatures",
    "In Gatlin, South Carolina, Ethan Wate awakens from a recurring \
    dream of a girl he does not know.",
    "https://upload.wikimedia.org/wikipedia/en/2/23/"
    "Beautiful_creatures_poster.jpg",
    "https://www.youtube.com/watch?v=r9rjhB7KWEc")

thor = media.Movie(
    "Thor",
    "Thor is a fictional superhero appearing in American comic books \
    published by Marvel Comics",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
    "https://www.youtube.com/watch?v=v7MGUNV8MxU")

"""This array consists of all of my favourite movies"""
movies = [
    fast_furious,
    jumper,
    Transformers,
    inception,
    beautiful_creatures,
    thor]
fresh_tomatoes.open_movies_page(movies)  # Passes movies to open_movies_page
