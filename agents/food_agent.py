from utils.loader import load_json

def food_agent(state):

    food = load_json("data/food.json")

    tickets = state["customer"]["tickets"]

    recommended = []

    # AI Recommendation
    if tickets <= 2:

        for item in food["food"]:

            if item["item_name"] in [
                "Large Popcorn",
                "Coke"
            ]:
                recommended.append(item)

    elif tickets <= 4:

        for item in food["food"]:

            if item["item_name"] in [
                "Combo 1",
                "Nachos"
            ]:
                recommended.append(item)

    else:

        for item in food["food"]:

            if item["item_name"] in [
                "Combo 2",
                "Large Popcorn"
            ]:
                recommended.append(item)

    print("\n========== AI FOOD RECOMMENDATION ==========\n")

    for item in recommended:

        print(
            f"{item['food_id']}. "
            f"{item['item_name']} - ₹{item['price']}"
        )

    print("\n1. Accept Recommendation")
    print("2. Customize Order")
    print("3. Skip Food")

    choice = int(input("\nEnter Choice: "))

    # ------------------------------------
    # Accept Recommendation
    # ------------------------------------

    if choice == 1:

        state["food"] = recommended

        print("\nFood Added Successfully!")

    # ------------------------------------
    # Customize
    # ------------------------------------

    elif choice == 2:

        print("\nAvailable Food:\n")

        for item in food["food"]:

            print(
                f"{item['food_id']}. "
                f"{item['item_name']} - ₹{item['price']}"
            )

        ids = input(
            "\nEnter Food IDs "
            "(comma separated): "
        )

        selected = []

        ids = [
            int(x.strip())
            for x in ids.split(",")
        ]

        for item in food["food"]:

            if item["food_id"] in ids:

                selected.append(item)

        state["food"] = selected

    # ------------------------------------
    # Skip
    # ------------------------------------

    else:

        state["food"] = []

        print("\nNo Food Selected.")

    return state