# this is the room file
from dataclasses import dataclass, field
from typing import List, Optional
from homepage import CalendarPopUp, MainWindow

class Room:

    '''
    a) Room class
    b) 11/08
    c) Angela Fernandez
    d) The room class holds the var default names and creates the cinstructor for 
    the room objects for guest selection; queen, king, suite, and double
    e) They are stated in the code below, on top of each method.

    '''
    
    '''
    The __init__ gives the default room variables and hard codes variables
    that dont change from room to room like amenities for room and hotel
    '''
    def __init__(self, bed_type, num_beds, price_per_night, room_num, is_available):
        self.room_number = 0
        self.room_type = ["Suite", "Double", "Single_Queen", "Single_King"]
        self.price_per_night = 0.0
        self.hotel_amenities = ["Pool", "Gym", "Free Breakfast", "Wifi", "Free Parking", "Office Area", "Laundry"]
        self.room_amenitites = ["Kitchen", "TV", "Room Service"]
        self.is_available = True
        self.check_in_date = None
        self.check_out_date = None

    '''
    The setroom def creates the constructor for the objects in the roomSearch class
    I did it this way since it is more simple and efficient than writing 4 seperate methods
    '''
    def set_room(self, bed_type, num_beds, price_per_night, room_num, is_available):
        self.bed_type = bed_type
        self.num_beds = num_beds
        self.price_per_night = price_per_night
        self.room_num = room_num
        self.is_available = is_available

    


        




       
    


