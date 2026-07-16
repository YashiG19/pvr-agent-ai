from utils.loader import load_json
import json

def seat_agent(state):
    seats_data = load_json("data/seats.json")
    screen_id = state["show"]["screen_id"]
    
    while True:
        try:
            tickets = int(input("\n🎟️ How many tickets do you want? ").strip())
            if tickets > 0:
                break
            print("Please enter a valid number greater than 0.")
        except ValueError:
            print("Please enter a valid number.")
            
    # Get all seats for this screen
    screen_seats = [s for s in seats_data["seats"] if s["screen_id"] == screen_id]
    
    print(f"\n========== 🎭 SEAT MAP (Screen {screen_id}) ==========\n")
    seat_types_order = ["Silver", "Gold", "Platinum", "Recliner"]
    
    available_seats_map = {}
    
    for stype in seat_types_order:
        type_seats = [s for s in screen_seats if s["seat_type"] == stype]
        if not type_seats: continue
        price = type_seats[0]["price"]
        print(f"  {stype.upper()} (₹{price}):")
        
        row = []
        for seat in type_seats:
            symbol = "✅" if seat["status"] == "Available" else "❌"
            if seat["status"] == "Available":
                available_seats_map[seat["seat_number"].lower()] = seat
            row.append(f"[{seat['seat_number']} {symbol}]")
            if len(row) == 4:
                print("    " + "  ".join(row))
                row = []
        if row:
            print("    " + "  ".join(row))
        print()
        
    print("  ✅ = Available  |  ❌ = Booked")
    print("=" * 45)
    
    selected_seats = []
    
    while len(selected_seats) < tickets:
        seat_input = input(f"\nEnter {tickets} comma-separated seat numbers (e.g. A1, B2): ").strip()
        seat_ids = [s.strip().lower() for s in seat_input.split(",") if s.strip()]
        
        if len(seat_ids) != tickets:
            print(f"❌ Please enter exactly {tickets} seats.")
            continue
            
        valid = True
        temp_selected = []
        
        # Check for duplicates in input
        if len(set(seat_ids)) != len(seat_ids):
             print(f"❌ You entered duplicate seats.")
             continue
             
        for sid in seat_ids:
            if sid not in available_seats_map:
                print(f"❌ Seat {sid.upper()} is either invalid or already booked!")
                valid = False
                break
            temp_selected.append(available_seats_map[sid])
            
        if valid:
            selected_seats = temp_selected
            
    print(f"\n✅ Seats Booked:\n")
    for seat in selected_seats:
        print(f"  🎫 {seat['seat_number']} ({seat['seat_type']}) - ₹{seat['price']}")
        
        # Mark booked in the global list
        for s in seats_data["seats"]:
            if s["seat_id"] == seat["seat_id"]:
                s["status"] = "Booked"
                break
                
    # Save once after all bookings
    with open("data/seats.json", "w") as file:
        json.dump(seats_data, file, indent=4)
        
    state["seats"] = selected_seats
    return state