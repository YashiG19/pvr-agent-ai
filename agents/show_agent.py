from utils.loader import load_json

def show_agent(state):

    shows = load_json("data/shows.json")
    screens = load_json("data/screens.json")

    movie_id = state["movie"]["movie_id"]

    date = state["customer"]["date"]

    available_shows = []

    # Find matching shows
    for show in shows["shows"]:

        if (
            show["movie_id"] == movie_id
            and show["show_date"] == date
        ):

            for screen in screens["screens"]:

                if screen["screen_id"] == show["screen_id"]:

                    temp = show.copy()

                    temp["screen_name"] = screen["screen_name"]

                    available_shows.append(temp)

    # No shows found
    if len(available_shows) == 0:

        print("\nNo Shows Available!")

        state["show"] = {}

        return state

    # Display shows
    print("\n========== AVAILABLE SHOWS ==========\n")

    for i, show in enumerate(available_shows):

        print(
            f"{i+1}. "
            f"Date: {show['show_date']} | "
            f"Time: {show['start_time']} | "
            f"Screen: {show['screen_name']}"
        )

    # User selects a show
    while True:

        choice = int(input("\nChoose Show Number: "))

        if 1 <= choice <= len(available_shows):
            break

        print("Invalid Choice! Try Again.")

    state["show"] = available_shows[choice - 1]

    print("\nSelected Show:")

    print(
        f"{state['show']['start_time']} "
        f"on {state['show']['show_date']}"
    )

    return state