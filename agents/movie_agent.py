from utils.loader import load_json

def movie_agent(state):

    data = load_json("data/movies.json")

    movie_name = state["customer"]["movie"]

    for movie in data["movies"]:

        if movie_name.lower() in movie["title"].lower():
            state["movie"] = movie

            print(f"\nMovie Found : {movie['title']}")

            return state

    print("\nMovie Not Found")

    state["movie"] = {}

    return state