from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from roomCard import RoomCard

class RoomSelectionPage(QWidget): 
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        grid = QHBoxLayout()
        

        self.junior = RoomCard("Assets/junior.jpeg", "King bed", "Wifi, Free Breakfast", "$170", self.stacked_widget)
        self.standard = RoomCard("Assets/junior.jpeg", "Queen bed", "Wifi", "$120", self.stacked_widget)
        self.couple = RoomCard("Assets/junior.jpeg", "Double bed", "Wifi", "$210", self.stacked_widget)
        self.family = RoomCard("Assets/junior.jpeg", "Suite bed", "Wifi", "$280", self.stacked_widget)
        #CHANGED
        self.junior_txt = self.junior.currentText()
        self.standard_txt = self.standard.currentText()
        self.couple_txt = self.couple.currentText()
        self.family_txt = self.family.currentText()


        grid.addWidget(junior)
        grid.addWidget(standard)
        grid.addWidget(couple)
        grid.addWidget(family)

        self.setLayout(grid)


    #def go_to_reservation_form(self):
     #   self.stacked_widget.setCurrentIndex(2)