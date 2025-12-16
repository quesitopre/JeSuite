import csv
from fileinput import filename
import os
from datetime import datetime

class AdminBackend:
    def __init__(self):
        self.customers_file = 'customers.csv'
        self.bookings_file = 'bookings.csv'

    def read_csv(self, filename):
        data = []
        if not os.path.exists(filename):
            print(f"File {filename} does not exist.")
            return data
    
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = list(reader)
        except Exception as e:
            print(f"Error reading {filename}: {e}")
        return data

    
    def get_all_customers(self):
        return self.read_csv(self.customers_file)
    
    def get_all_bookings(self):
        return self.read_csv(self.bookings_file)
    
    def get_stats(self):
        customers = self.get_all_customers()
        bookings = self.get_all_bookings()
        
        total_customers = len(customers)
        total_bookings = len(bookings)
        
        revenue = 0.0
        canceled = 0
        active = 0

        for booking in bookings:
            status = booking.get('status', '').lower()
            if status == 'canceled':
                canceled += 1
            elif status == 'confirmed':
                active += 1
            
            try:
                price = float(booking.get('price', 0))
                if status == 'confirmed':
                    revenue += price
            except (ValueError, TypeError):
                pass

        return {
            'total_bookings': total_bookings,
            'total_customers': total_customers,
            'active_bookings': active,
            'canceled_bookings': canceled,
            'total_revenue': revenue
        }