from utils.loader import load_json

def show_agent(state):
    shows_data = load_json("data/shows.json")
    screens = load_json("data/screens.json")
    
    movie_id = state["movie"]["movie_id"]
    
    # Get all shows for this movie
    movie_shows = [s for s in shows_data["shows"] if s["movie_id"] == movie_id]
    
    if not movie_shows:
        print("\n❌ No Shows Available for this movie!")
        state["show"] = {}
        return state
        
    # Get unique dates
    unique_dates = sorted(list(set(s["show_date"] for s in movie_shows)))
    
    print("\n========== 📅 SELECT DATE ==========\n")
    for i, date in enumerate(unique_dates):
        print(f"  {i+1}. {date}")
        
    while True:
        try:
            date_choice = int(input("\nChoose Date Number: ").strip())
            if 1 <= date_choice <= len(unique_dates):
                selected_date = unique_dates[date_choice - 1]
                break
            print("Invalid choice! Try again.")
        except ValueError:
            print("Please enter a number.")
            
    # Now get shows for this date
    available_shows = []
    for show in movie_shows:
        if show["show_date"] == selected_date:
            for screen in screens["screens"]:
                if screen["screen_id"] == show["screen_id"]:
                    temp = show.copy()
                    temp["screen_name"] = screen["screen_name"]
                    available_shows.append(temp)
                    
    print(f"\n========== 🕒 SHOWS ON {selected_date} ==========\n")
    for i, show in enumerate(available_shows):
        print(f"  {i+1}. Time: {show['start_time']} | Screen: {show['screen_name']}")
        
    while True:
        try:
            show_choice = int(input("\nChoose Show Number: ").strip())
            if 1 <= show_choice <= len(available_shows):
                selected_show = available_shows[show_choice - 1]
                break
            print("Invalid choice! Try again.")
        except ValueError:
            print("Please enter a number.")
            
    state["show"] = selected_show
    print(f"\n✅ Selected Show: {selected_show['start_time']} on {selected_show['show_date']} ({selected_show['screen_name']})")
    
    return state