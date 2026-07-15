import json

from utils.loader import load_json

def booking_agent(state):

    data = load_json("data/bookings.json")

    booking = {

        "booking_id":
            f"BK{
            1000 +
            len(
                data["bookings"]
            ) + 1
            }",

        "customer":
            state["customer"]["name"],

        "movie":
            state["movie"]["title"],

        "amount":
            state["bill"]["final_amount"]
    }

    data["bookings"].append(booking)

    with open(
        "data/bookings.json",
        "w"
    ) as file:

        json.dump(data, file, indent=4)

    state["booking"] = booking

    return state