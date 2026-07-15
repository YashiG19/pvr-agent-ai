def customer_agent(state):

    print("\n========== PVR BOOKING ==========\n")

    name = input("Enter Your Name : ")
    city = input("Enter City : ")
    movie = input("Movie Name : ")
    date = input("Date (YYYY-MM-DD): ")

    tickets = int(input("Number of Tickets : "))

    seat_type = input("Seat Type (Silver/Gold/Recliner): ")

    state["customer"] = {
        "name": name,
        "city": city,
        "movie": movie,
        "date": date,
        "tickets": tickets,
        "seat_type": seat_type
    }
    print("\nCustomer Details Saved Successfully\n")

    return state