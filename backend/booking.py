#this is the booking/checkout class
from dataclasses import dataclass, field
from typing import List, Optional
from homepage import CalendarPopUp, MainWindow
from backend.room import Room

def __init__(self):
    #make protected
    #use in email class later
    self.customer_first_name = "Button Customer first name"
    self.customer_last_name = "Button customer last name"
    self.credit_card_num = "Button credit card number"
    self.credit_card_cvc = "Button credit card cvc"
    self.billing_zip_code = "Button billing zip code"
    self.customer_email = "Button customer email"
    self.check_in_date = "txt from check in button"
    self.check_out_date = "txt from check out button"


