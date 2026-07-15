from langgraph.graph import StateGraph, START, END

from state import PVRState

from agents.customer_agent import customer_agent
from agents.movie_agent import movie_agent
from agents.show_agent import show_agent
from agents.seat_agent import seat_agent
from agents.food_agent import food_agent
from agents.offer_agent import offer_agent
from agents.bill_agent import bill_agent
from agents.booking_agent import booking_agent
from agents.notification_agent import notification_agent


# -----------------------------
# Conditional Functions
# -----------------------------

def check_movie(state):

    if state["movie"]:
        return "show"

    return "end"


def check_seats(state):

    if state["seats"]:
        return "food"

    return "end"

def check_show(state):

    if state["show"]:
        return "seat"

    return "end"
# -----------------------------
# Graph Builder
# -----------------------------

builder = StateGraph(PVRState)

# Nodes
builder.add_node("customer", customer_agent)
builder.add_node("movie", movie_agent)
builder.add_node("show", show_agent)
builder.add_node("seat", seat_agent)
builder.add_node("food", food_agent)
builder.add_node("offer", offer_agent)
builder.add_node("bill", bill_agent)
builder.add_node("booking", booking_agent)
builder.add_node("notification", notification_agent)

# -----------------------------
# Workflow
# -----------------------------

builder.add_edge(START, "customer")

builder.add_edge("customer", "movie")

# Movie Check
builder.add_conditional_edges(
    "movie",
    check_movie,
    {
        "show": "show",
        "end": END
    }
)

builder.add_conditional_edges(
    "show",
    check_show,
    {
        "seat": "seat",
        "end": END
    }
)

# Seat Check
builder.add_conditional_edges(
    "seat",
    check_seats,
    {
        "food": "food",
        "end": END
    }
)

builder.add_edge("food", "offer")
builder.add_edge("offer", "bill")
builder.add_edge("bill", "booking")
builder.add_edge("booking", "notification")
builder.add_edge("notification", END)

# -----------------------------
# Compile
# -----------------------------

workflow = builder.compile()

# -----------------------------
# Initial State
# -----------------------------

initial_state = {

    "customer": {},
    "movie": {},
    "theatre": {},
    "show": {},
    "seats": [],
    "food": [],
    "offer": {},
    "bill": {},
    "booking": {},
    "message": ""

}

# -----------------------------
# Run
# -----------------------------

result = workflow.invoke(initial_state)

print("\n")
print("=" * 50)
print(result.get("message", "Workflow Finished"))
print("=" * 50)