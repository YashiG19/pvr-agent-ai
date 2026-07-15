from utils.loader import load_json
import json

def seat_agent(state):

    seats = load_json("data/seats.json")

    screen_id = state["show"]["screen_id"]

    seat_type = state["customer"]["seat_type"]

    tickets = state["customer"]["tickets"]

    selected = []

    for seat in seats["seats"]:

        if (
            seat["screen_id"] == screen_id
            and seat["seat_type"].lower() == seat_type.lower()
            and seat["status"] == "Available"
        ):

            selected.append(seat)

            if len(selected) == tickets:
                break

    if len(selected) < tickets:
        print(
            f"\nOnly {len(selected)} "
            f"{seat_type} seats are available."
        )

        state["seats"] = []

        return state

    print("\nSeats Booked\n")

    for seat in selected:

        print(seat["seat_number"])

        # Mark booked
        seat["status"] = "Booked"

        with open("data/seats.json", "w") as file:
            json.dump(seats, file, indent=4)

    state["seats"] = selected

    return state