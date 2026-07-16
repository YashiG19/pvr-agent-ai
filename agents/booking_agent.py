import json
from utils.loader import load_json

def booking_agent(state):

    data = load_json("data/bookings.json")

    booking_id = f"BK{1000 + len(data['bookings']) + 1}"
    
    booking = {
        "booking_id": booking_id,
        "customer": state["customer"]["name"],
        "city": state["customer"]["city"],
        "movie": state["movie"]["title"],
        "date": state["show"]["show_date"],
        "time": state["show"]["start_time"],
        "screen": state["show"]["screen_name"],
        "seats": [s["seat_number"] for s in state["seats"]],
        "food": [f["item_name"] for f in state["food"]],
        "amount": round(state["bill"]["final_amount"], 2)
    }

    data["bookings"].append(booking)

    with open("data/bookings.json", "w") as file:
        json.dump(data, file, indent=4)

    state["booking"] = booking

    return state