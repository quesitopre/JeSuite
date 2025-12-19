#this is the booking/checkout class

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
        self.booking_data = { 
        'location': None,
        'check_in': None,
        'check_out': None,
        'guests': None,
        'rooms': None,
        'room_price':None,
        'nights': None,
        'customer _first_name': None,
        'room_type': None
        }

    def set_search_filters(self, location, check_in, check_out, guests, rooms):
        '''Store data from hompepage search'''
        self.booking_data['location'] = location #store location
        self.booking_data['check_in'] = check_in #store check-in date
        self.booking_data['check_out'] = check_out #store check-out date
        self.booking_data['guests'] = guests #store number of guests
        self.booking_data['rooms'] = rooms #store number of rooms
       
    def set_room_selection(self, room_type, room_price):
        '''Store data from room selection page'''
        self.booking_data['room_type'] = room_type  #store room type
        self.booking_data['room_price'] = room_price #store room price

    def set_customer_info(self, first_name, last_name, email):
       self.booking_data['customer_first_name'] = first_name #store first name
       self.booking_data['customer_last_name'] = last_name   #store last name
       self.booking_data['customer_email'] = email #store email

    def get_booking_data(self):
       '''Return all collected booking data.'''
       return self.booking_data
    
    def clear_data(self):
       self.booking_data = {
        'location': None,
        'check_in': None,
        'check_out': None,
        'guests': None,
        'rooms': None,
        'room_price':None,
        'nights': None,
        'customer _first_name': None,
        'room_type': None
        }
  