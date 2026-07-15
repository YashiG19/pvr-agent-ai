from utils.loader import load_json

def offer_agent(state):

    offers = load_json("data/offers.json")

    ticket_price = 0


    food_price = 0

    for seat in state["seats"]:
        ticket_price += float(seat["price"])

    for item in state["food"]:
        food_price += float(item["price"])
        
    total = ticket_price + food_price

    best_offer = None

    max_discount = 0

    for offer in offers["offers"]:

        if total >= float(offer["minimum_amount"]):

            if offer["discount_percent"] > max_discount:

                max_discount = offer["discount_percent"]

                best_offer = offer

    state["offer"] = best_offer

    return state