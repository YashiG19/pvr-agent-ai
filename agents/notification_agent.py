def notification_agent(state):
    print("\n==========================================")
    print("🎉 BOOKING CONFIRMED 🎉")
    print("==========================================\n")
    print(f"🎫 Booking ID : {state['booking']['booking_id']}")
    print(f"👤 Customer   : {state['customer']['name']} ({state['customer']['city']})")
    print(f"🎬 Movie      : {state['movie']['title']}")
    print(f"📅 Date       : {state['show']['show_date']}")
    print(f"🕒 Time       : {state['show']['start_time']}")
    print(f"📺 Screen     : {state['show']['screen_name']}")
    
    seat_details = ", ".join([s["seat_number"] for s in state["seats"]])
    print(f"💺 Seats      : {seat_details}")
    
    if state["food"]:
        food_details = ", ".join([f["item_name"] for f in state["food"]])
        print(f"🍿 Food       : {food_details}")
    else:
        print(f"🍿 Food       : None")
        
    if state["offer"]:
        print(f"🎁 Offer      : {state['offer']['offer_name']}")
        
    print(f"\n💵 Final Amount : ₹ {round(state['bill']['final_amount'],2)}")
    print("\n==========================================\n")
    
    state["message"] = "Booking Successful!"
    return state