def notification_agent(state):

    print("\n===========================")
    print("BOOKING CONFIRMED")
    print("===========================\n")

    print("Booking ID :", state["booking"]["booking_id"])

    print("Customer :", state["customer"]["name"])

    print("Movie :", state["movie"]["title"])

    print("Screen :", state["show"]["screen_id"])

    print("Time :", state["show"]["start_time"])

    print("Seats :")

    for seat in state["seats"]:
        print(seat["seat_number"])

    print("\nFood")

    for item in state["food"]:
        print(item["item_name"])

    if state["offer"]:

        print(
            "\nOffer Applied :",
            state["offer"]["offer_name"]
        )

    print(
        f"\nFinal Amount : ₹ "
        f"{round(state['bill']['final_amount'],2)}"
    )

    state["message"] = "Booking Successful"

    return state