#this is the booking/checkout class
from dataclasses import dataclass, field
from typing import List, Optional
from homepage import CalendarPopUp, HomePage
from room import Room
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
        print(f"Customer object created: {first_name} {last_name}")
        self.save_to_csv()

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
    

    def save_to_csv(self, filename="customers.csv"):
        file_exists = os.path.isfile(filename)
        print("save_to_csv() called")

        with open(filename, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow([
                    "First Name","Last Name","Phone","Email",
                    "Address","City","State","Zipcode",
                    "Card Number","Expir Month","Expir Year","CVV","Billing Zip"
                ])
            writer.writerow([
                self.first_name, self.last_name, self.phone, self.email,
                self.address, self.city, self.state, self.zipcode,
                self.card_num, self.expir_month, self.expir_year,
                self.cvv, self.billing_zip
            ])

    
