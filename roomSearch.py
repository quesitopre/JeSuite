from dataclasses import dataclass, field
from typing import List, Optional
from homepage import HomePage , CalendarPopUp
from backend.room import Room
import pydoc

class roomSearch:

    '''
    a) Room Search
    b) 11/08
    c) Angela Fernandez
    d) The room search class uses the objects and determines which rooms show
    depending on how many people/rooms are selected
    e) They are stated in the code below, on top of each method.
    

    '''

    '''
    This __init__ has the objects that we created from the room class
    '''
    def __init__(self):
        self.single_queen = Room()
        self.single_queen.set_room("Queen", 1, 120.0, 209, True)

        self.single_king = Room()
        self.single_king.set_room("King", 1, 170.0, 167, True)

        self.double = Room()
        self.double.set_room("Queen", 2, 210, 38, True)

        self.suite = Room()
        self.suite.set_room("King", 2, 280, 412, True)

    '''
    This def, selected_people uses the homepage

    It determines which button was selceted in the front end where the user decides
    how many people and rooms they want

    It selects by treating it like an array and returning certain rooms depeding on
    the button(index of the array) selected

    Users who choose 1-4 guests must select one room
    Users who choose 5-6 guests must select two rooms

    '''
    def selected_people(self):
        if self.people_combo.currentIndex() == 0:
            return {self.single_queen, self.single_king, self.suite}
        elif self.people_combo.currentIndex() == 1:
            return {self.single_queen, self.single_king, self.suite, self.double}
        elif self.people_combo.currentIndex() == 2:
            return {self.single_queen, self.single_king, self.suite, self.double}
        elif self.people_combo.currentIndex() == 3:
            return {self.single_queen, self.single_king, self.suite, self.double}
        elif self.people_combo.currentIndex() == 4:
            print("Must select 2 rooms")
            return {self.single_queen, self.single_king, self.suite, self.double}
        else: 
            print("Must select 2 rooms")
            return {self.single_queen, self.single_king, self.suite, self.double}\
    
    


