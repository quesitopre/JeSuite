""" Booking Service Module 
Module manages functionality for creating, fetching, and inputting booking data to a csv file.

Made by Citlalli Martinez 11/08/2025.
"""
from backend.booking import Booking
import csv
import os
from datetime import datetime
#booking service to create, read and write CSV file for bookings
''' BookingService class to handle booking operations to save and retrieve customer booking info into a csv file'''
class BookingService: 

    def __init__(self, booking_file = 'bookings.csv'):
        """constructor to initialize the booking service with a CSV file.

        Args:
            booking_file = 'bookings.csv': The path to the CSV file to store booking data.
            """
        self.booking_file = booking_file 
        self._initialize_file()
    
    def _initialize_file(self): 
        """ Create  the CSV file if it does not exists. 
        
        This method  sets up the file structure for storing booking information and initializes
          the CSV file with  the appropriate column headers.
        """
        #Create a CSV file and folder.
        os.makedirs(os.path.dirname(self.booking_file), exist_ok=True) # create a directory if it doesn't exist
        if not os.path.exists(self.booking_file):
            with open(self.booking_file,'w',newline = '') as file:
                write = csv.writer(file)

                write.writerow([
                    'booking_id',
                    'customer_first_name',
                    'customer_last_name',
                    'customer_email',
                    'credit_card_num',
                    'credit_card_cvc',
                    'billing_zip_code',
                    'room_id',
                    'room_price',
                    'nights'
                    'total_amount',
                    'status',
                ])

    def generateBookingID(self)-> str:
        """Generate a unique booking ID for the reservation.

        This method reads from CSV file to generate a new unique booking ID if it does
        not already exist. Starting from numerical value BK001 and increments by 1 for 
        each new booking.

        Returns:
            str:  A unique booking ID in the format BK000( 000 a 3 digit number).
        """
       #Must generate a unique booking ID
        bookings = self.loadBookings()
        if not bookings:
             return "BK001"
        last_id = bookings[-1].get('booking_id', 'BK000')
        number = int(last_id.replace('BK','')) + 1
        return f'BK{number:03d}'
    
    def saveBooking(self, booking:Booking)-> str:
        """Save a new booking  to the CSV file. 
        
        This method appends a new booking record to the CSV file.

        Args:
            booking (Booking): A Booking object containing the booking details.

        Returns:
            str: The unique booking ID is returned.
        """
        #save a booking to the CSV file
        booking_id = self.generateBookingID()
        with open(self.booking_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                booking_id,
                booking.customer_first_name,
                booking.customer_last_name,
                booking.customer_email,
                booking.credit_card_num,
                booking.credit_card_cvc,
                booking.billing_zip_code,
                getattr(booking, 'room_id',''),
                getattr(booking,' nights',''), 
                getattr(booking,total_amount,'')
            ])
        

        print(f"booking confirmed{booking_id}")
        return booking_id
    
    def getAllBookings(self):
        """Retrieve all bookings from the CSV file. 

        This method reads the CSV file and returns the booking information as a 
        list of dictionaries.

        Returns:
            bookings = list[dict[str,str]]: A list of dictionaries, each representing a booking record.
        """
        #get all bookings from CSV as a list of dictionaries
        bookings = list[dict[str,str]] = []
        try: 
            with open(self.booking_file, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    bookings.list(reader)
        except FileNotFoundError:
            self._initialize_file() # if file does not exist then create it

        return bookings
    
    def getBookingByID(self, booking_id):
        """Find and retrieve a specific booking by its ID.
         This method searches through the bookings that match the desired booking ID.

        Args:
            booking_id (str): The unique ID of the booking to retrieve.

        Returns:
            dict[str,str] | None: A dictionary representing the booking record if found
            or None if no matching booking is found.
        """
        # find a specific booking ID 
        bookings = self.getAllBookings()
        for booking in bookings:
            if booking['booking_id'] == booking_id:
                return bookings
            
        return None 
    
    