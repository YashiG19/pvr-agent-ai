from typing import TypedDict

class PVRState(TypedDict):
    customer: dict
    movie: dict
    theatre: dict
    show: dict
    seats: list
    food: list
    offer: dict
    bill: dict
    booking: dict
    message: str