from enum import Enum


class Type(Enum):
    TRANSIT = 'Boarding pass or transit ticket'
    COUPON = 'Coupon'
    EVENT = 'Ticket for an event'
    CARD = 'Loyalty or another type of card'
    OTHER = 'Other'
