from dataclasses import dataclass, field
from typing import List, Optional
from homepage import CalendarPopUp, MainWindow
from backend.room import Room

class roomSearch:
    def __init__(self):
        self.single_queen = Room()
        self.single_queen.set_room("Queen", 1, 120.0, 209, True)

        self.single_king = Room()
        self.single_king.set_room("King", 1, 170.0, 167, True)

        self.double = Room()
        self.double.set_room("Queen", 2, 210.0, 38, True)

        self.suite = Room()
        self.suite.set_room("King", 2, 280.0, 412, True)
#add in the buttons later for popup
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
            return {self.single_queen, self.single_king, self.suite, self.double}
