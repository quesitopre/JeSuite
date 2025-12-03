#this is the booking/checkout class
from dataclasses import dataclass, field
from typing import List, Optional
from homepage import CalendarPopUp, HomePage
from room import Room
from backend.customer import Customer
from roomSearch import roomSearch
import os
import csv
import pydoc

class Booking:

    '''
    a) Class Booking
    b) 11/17
    c) Angela Fernandez
    d) The booking class is used to evaluate the items in the cart classes and 
    returns it
    It collects the variable from customer and returns them
    It also calculates the total that the customer owes for the room/s
    e) They are stated in the code below, on top of each method.
    

    '''
    
    '''
    The __init__ holds the variables that we get from the rooms added to cart
    '''
    def __init__(self):
        #make protected
        #use in email class later
        self.booking_id = 123
        self.payment_approved = True
        self.customer = Customer
        self.room = Room
        self.roomSearch = roomSearch

    '''
    The info_getter retrieves the vars from other classes
    '''

    def info_getter(self) -> dict:
        return{
            "first_name": self.customer_first_name,
            "last_name": self.customer_last_name,
            "email": self.customer_email,
            "cart_items": [item.room.room_type for item in self.cart_service.cartItems],
            "total_amount": self.calculate_total(),
            "booking_id": self.booking_id
        }
    '''
    The update_availability method changes the availability from true to false if it
    is detected in the cart
    '''
    def bookingItems(self):
        #Return cart items separately depending on how many there are.
        self.items = self.cart_service.cartItems
        self.count = len(self.items)

        if self.count == 0:
            return "No items in cart."
        elif self.count == 1:
            # Return details of the single item
            self.item = self.items[0]
            return {
                "room_type": self.item.room.room_type,
                "check_in": self.item.check_in.strftime("%Y-%m-%d"),
                "check_out": self.item.check_out.strftime("%Y-%m-%d"),
                "nights": self.item.nights,
                "price_per_night": self.item.room.price_per_night
            }
        else:
            # Return details of both items separately
            return [
                {
                    "room_type": self.items[0].room.room_type,
                    "check_in": self.items[0].check_in.strftime("%Y-%m-%d"),
                    "check_out": self.items[0].check_out.strftime("%Y-%m-%d"),
                    "nights": self.items[0].nights,
                    "price_per_night": self.items[0].room.price_per_night
                },
                {
                    "room_type": self.items[1].room.room_type,
                    "check_in": self.items[1].check_in.strftime("%Y-%m-%d"),
                    "check_out": self.items[1].check_out.strftime("%Y-%m-%d"),
                    "nights": self.items[1].nights,
                    "price_per_night": self.items[1].room.price_per_night
                }
            ]
        

    def update_availability(self):
        #Mark rooms in cart as unavailable.
        for item in self.cart_service.cartItems:
            item.room.is_available = False  # assumes Room has an 'available' attribute

    def confirm_payment(self):
        #Simulate payment approval.
        if len(self.cart_service.cartItems) == 0:
            return ValueError("Cart is empty. Cannot confirm booking.")
        self.payment_approved = True
        return f"Payment confirmed for booking {self.booking_id}"
   


