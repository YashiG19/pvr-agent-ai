def bill_agent(state):

    ticket_total = 0

    for seat in state["seats"]:
        ticket_total += float(seat["price"])

    food_total = 0

    for item in state["food"]:
        food_total += float(item["price"])

    subtotal = ticket_total + food_total

    discount = 0

    if state["offer"]:

        discount = (
            subtotal *
            state["offer"]["discount_percent"]
        ) / 100

    final = subtotal - discount

    state["bill"] = {

        "ticket_total": ticket_total,

        "food_total": food_total,

        "subtotal": subtotal,

        "discount": discount,

        "final_amount": final
    }

    return state