#this is the booking/checkout class
from dataclasses import dataclass, field
from typing import List, Optional
from homepage import CalendarPopUp, HomePage
from room import Room
from reservationPage import TextInputField, ReservationPage
import os
import csv


class Customer:
    """
    Represents a customer making a reservation.
    """

    def __init__(self, first_name: str, last_name: str, phone: str, email: str,
                 address: str, city: str, state: str, zipcode: str,
                 card_num: str, expir_month: str, expir_year: str,
                 cvv: str, billing_zip: str):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.card_num = card_num
        self.expir_month = expir_month
        self.expir_year = expir_year
        self.cvv = cvv
        self.billing_zip = billing_zip

    def get_contact_info(self) -> dict:
        #Return safe customer contact info
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "email": self.email,
            "address": f"{self.address}, {self.city}, {self.state} {self.zipcode}"
        }

    def get_payment_info(self) -> dict:
        #Return payment info
        return {
            "card_num": self.card_num,
            "expir_month": self.expir_month,
            "expir_year": self.expir_year,
            "cvv": self.cvv,
            "billing_zip": self.billing_zip
        }
def confirm_reservation(self):
    #Handle reservation confirmation logic

    customer = Customer(
        first_name=self.first_name_field.get_value(),
        last_name=self.last_name_field.get_value(),
        phone=self.phone_field.get_value(),
        email=self.email_field.get_value(),
        address=self.addressline_field.get_value(),
        city=self.city_field.get_value(),
        state=self.state.get_value(),
        zipcode=self.zipcode.get_value(),
        card_num=self.card_num.get_value(),
        expir_month=self.expir_month.get_value(),
        expir_year=self.expir_year.get_value(),
        cvv=self.CVV.get_value(),
        billing_zip=self.billing_zip.get_value()
    )

    
