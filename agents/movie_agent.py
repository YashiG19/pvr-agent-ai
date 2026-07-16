from utils.loader import load_json

def movie_agent(state):

    data = load_json("data/movies.json")

    # Display Now Showing movies
    now_showing = [
        m for m in data["movies"]
        if m["status"] == "Now Showing"
    ]

    print("\n========== 🎬 NOW SHOWING ==========\n")

    for i, movie in enumerate(now_showing):

        print(
            f"  {i+1}. {movie['title']} "
            f"({movie['language']}) | "
            f"{movie['genre']} | "
            f"{movie['duration']} min | "
            f"Rating: {movie['rating']}"
        )

    # Coming Soon
    coming_soon = [
        m for m in data["movies"]
        if m["status"] == "Coming Soon"
    ]

    if coming_soon:

        print("\n---------- Coming Soon ----------\n")

        for movie in coming_soon:

            print(
                f"  ★ {movie['title']} "
                f"({movie['language']}) | "
                f"Releasing: {movie['release_date']}"
            )

    print("\n" + "=" * 40)

    # User selects movie by number or name
    while True:

        choice = input(
            "\nSelect Movie (number or name): "
        ).strip()

        # Try number first
        if choice.isdigit():

            idx = int(choice)

            if 1 <= idx <= len(now_showing):

                state["movie"] = now_showing[idx - 1]

                print(
                    f"\n✅ Movie Selected : "
                    f"{state['movie']['title']}"
                )

                return state

            print("Invalid number! Try again.")
            continue

        # Try name match
        for movie in now_showing:

            if choice.lower() in movie["title"].lower():

                state["movie"] = movie

                print(
                    f"\n✅ Movie Selected : "
                    f"{movie['title']}"
                )

                return state

        print("Movie Not Found! Try again.")

    state["movie"] = {}

    return state