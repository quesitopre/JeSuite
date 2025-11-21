#this is the booking/checkout class
from dataclasses import dataclass, field
from typing import List, Optional
from homepage import CalendarPopUp, MainWindow
from backend.room import Room
import os
import csv

class Booking:

    
    '''
    The __init__ holds the variables that we get from the rooms added to cart
    '''
    def __init__(self):
        #make protected
        #use in email class later
        self.room_one = room_one_price
        self.room_two = room_two_price
        self.total_amount = calculate_total
        self.booking_id = 123
        self.nights = self.start_date - self.end_date
        self.payment_approved = True

    '''
    The info_getter retrieves the vars from other classes
    '''

    def info_getter(self):
        return{
            self.customer_first_name,
            self.customer_last_name,
            self.credit_card_num, 
            self.credit_card_cvc, 
            self.billing_zip_code, 
            self.customer_email, 
            self.check_in_date,
            self.check_out_date,
            self.location_combo,
            self.cart_items
            }

    '''
    The update_availability method changes the availability from true to false if it
    is detected in the cart
    '''

    def update_availability(self):
        for room in self.cart_items:
            if self.single_queen in self.cart_items:
                self.single_queen.set_room("Queen", 1, 120.0, 209, False)
            elif self.single_king in self.cart_items:
                self.single_king.set_room("King", 1, 170.0, 167, False)
            elif self.double in self.cart_items:
                self.double.set_room("Queen", 2, 210.0, 38, False)
            else:
                self.suite.set_room("King", 2, 280.0, 412, False)

    '''
    The calculate_total takes the previously calculated tax and adds it to the 
    room_total to give back the total for everything
    '''

    def calculate_total(self):
        return self.rooms_total + self.calculate_tax()
    

    '''
    The calculate tax gets the total of the rooms, whether it be one or 
    two rooms in the cart and multiplies it by the tax to return how much tax
    will be
    '''

    def calculate_tax(self):
        return self.rooms_total * .0925




