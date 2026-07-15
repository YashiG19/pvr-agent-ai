from utils.loader import load_json

def theatre_agent(state):

    theatres = load_json("data/theatres.json")

    city = state["customer"]["city"]

    available = []

    for theatre in theatres["theatres"]:

        if theatre["city"].lower() == city.lower():

            available.append(theatre)

    if len(available) == 0:

        print("No Theatre Found")

        state["theatre"] = {}

        return state

    print("\nAvailable Theatres\n")

    for i, theatre in enumerate(available):

        print(i + 1, theatre["theatre_name"])

    choice = int(input("\nSelect Theatre : "))

    state["theatre"] = available[choice - 1]

    return state