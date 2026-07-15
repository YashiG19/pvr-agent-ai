# 🎬 PVR-Agent-AI

An AI-inspired multi-agent movie booking application built using **Python** and **LangGraph**. The system simulates a real-world movie ticket booking workflow similar to PVR/BookMyShow by utilizing multiple agents that collaborate to perform tasks such as movie selection, show booking, seat reservation, food recommendation, offer application, bill generation, and booking confirmation.

---

## 🚀 Features

- Movie Discovery
- Show Selection
- Dynamic Seat Booking
- Automatic Food Recommendations
- Best Offer Selection
- Bill Generation
- Booking Confirmation
- Multi-Agent Workflow using LangGraph
- JSON-based Data Management

---

## 🏗️ Project Architecture

```text
Customer Agent
      │
      ▼
Movie Agent
      │
      ▼
Show Agent
      │
      ▼
Seat Agent
      │
      ▼
Food Agent
      │
      ▼
Offer Agent
      │
      ▼
Bill Agent
      │
      ▼
Booking Agent
      │
      ▼
Notification Agent
      │
      ▼
END
```

---

## 🛠️ Tech Stack

- Python
- LangGraph
- JSON
- Git & GitHub

---

## 📂 Project Structure

```text
PVR/
│
├── agents/
│   ├── customer_agent.py
│   ├── movie_agent.py
│   ├── show_agent.py
│   ├── seat_agent.py
│   ├── food_agent.py
│   ├── offer_agent.py
│   ├── bill_agent.py
│   ├── booking_agent.py
│   └── notification_agent.py
│
├── data/
│   ├── movies.json
│   ├── shows.json
│   ├── screens.json
│   ├── seats.json
│   ├── food.json
│   ├── offers.json
│   └── bookings.json
│
├── utils/
│   └── loader.py
│
├── app.py
├── state.py
└── README.md
```

---

## ⚙️ How It Works

1. The customer enters:
   - Name
   - City
   - Movie Name
   - Date
   - Number of Tickets
   - Seat Type

2. The Movie Agent searches for the requested movie.

3. The Show Agent displays available shows for the selected date.

4. The Seat Agent reserves seats based on availability.

5. The Food Agent recommends food items automatically.

6. The Offer Agent selects the best available offer.

7. The Bill Agent calculates:
   - Ticket Cost
   - Food Cost
   - Discount
   - Final Amount

8. The Booking Agent generates a booking ID.

9. The Notification Agent displays the final booking details.

## 🎯 Future Enhancements

- MySQL Integration
- Email Notifications
- WhatsApp Notifications
- Payment Gateway Integration
- Seat Recommendation System
- Conditional LangGraph Workflows
- LLM-based Movie Recommendations
- Real-time Seat Availability
- Web Interface using Streamlit/Flask
