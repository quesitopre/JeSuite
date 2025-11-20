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
        

        king = RoomCard("Assets/King_room.jpg", "1 King bed", "Max Occupancy: 3", "$170", self.stacked_widget)
        queen = RoomCard("Assets/Queen_room.avif", "1 Queen bed", "Max Occupancy: 2", "$120", self.stacked_widget)
        double = RoomCard("Assets/Double_room.avif", "Double bed(2 Queen)", "Max Occupancy: 4", "$210", self.stacked_widget)
        suite = RoomCard("Assets/Suite_room.jpg", "Suite bed(2 King)", "Max Occupancy: 4", "$280", self.stacked_widget)

        #self.king_txt = self.king.currentText()
        #self.queen_txt = self.queen.currentText()
        #self.double_txt = self.double.currentText()
        #self.suite_txt = self.suite.currentText()

        
        grid.addWidget(king)
        grid.addWidget(queen)
        grid.addWidget(double)
        grid.addWidget(suite)

        self.setLayout(grid)


    #def go_to_reservation_form(self):
     #   self.stacked_widget.setCurrentIndex(2)