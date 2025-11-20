from backend.customer import Booking
import csv
import os
from datetime import datetime
from homepage import CalendarPopUp, MainWindow
from backend.customer import Customer
from roomSearch import roomSearch

#booking service to create, read and write CSV file for bookings
class BookingService:
    def __init__(self, booking_file = 'bookings.csv'):
        self.booking_file = booking_file 
        self._initialize_file()
        self.total_bookings = []
        self.booking_id = 123
        self.nights = self.start_date - self.end_date
        self.payment_approved = True

    def info_getter(self):
        return{self.customer_first_name,
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

    def calculate_total(self):
        return self.rooms_total + self.calculate_tax()
    
    def calculate_tax(self):
        return self.rooms_total * .0925
    
    def _initialize_file(self):
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
       #Must generate a unique booking ID
       bookings = self.loadBookings()
       if not bookings:
           return "BK001"
       last_id = bookings[-1].get('booking_id', 'BK000')
       number = int(last_id.replace('BK','')) + 1
       return f'BK{number:03d}'
    
#clear "cart" after booking is complete


    def saveBooking(self, booking)-> str:
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
        # find a specific booking ID 
        bookings = self.getAllBookings()
        for booking in bookings:
            if booking['booking_id'] == booking_id:
                return booking
            
        return None