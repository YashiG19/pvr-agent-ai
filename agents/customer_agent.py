def customer_agent(state):
    print("\n========== 🎟️ PVR BOOKING ==========\n")
    name = input("Enter Your Name : ").strip()
    city = input("Enter City : ").strip()
    
    state["customer"] = {
        "name": name,
        "city": city
    }
    print("\n✅ Welcome, " + name + "!")
    return state