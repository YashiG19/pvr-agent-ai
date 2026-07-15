from utils.loader import load_json

def food_agent(state):

    food = load_json("data/food.json")

    tickets = state["customer"]["tickets"]

    recommended = []

    for item in food["food"]:

        if tickets <= 2:

            if item["item_name"] in [
                "Large Popcorn",
                "Coke"
            ]:
                recommended.append(item)

        elif tickets <= 4:

            if item["item_name"] in [
                "Combo 1",
                "Nachos",
                "Coke"
            ]:
                recommended.append(item)

        else:

            if item["item_name"] in [
                "Combo 2",
                "Large Popcorn"
            ]:
                recommended.append(item)

    state["food"] = recommended

    print("\nRecommended Food")

    for item in recommended:
        print(item["item_name"], "₹", item["price"])

    return state