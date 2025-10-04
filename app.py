import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout, QComboBox, QVBoxLayout


# Subclass QMainWindow to customize your application's main window
class MainWindow(QWidget): 
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(1000,500)

        main_layout = QVBoxLayout()

        filters = self.create_categories()
        main_layout.addLayout(filters)

        self.setLayout(main_layout)
    
    def create_categories(self):
        filter_layout = QHBoxLayout()

        #location
        location_combo = QComboBox()
        location_combo.addItems(["Los Angeles, California", "Santa Monica, California", "Beverly Hill, California"])

        #guest
        guest_combo = QComboBox()
        guest_combo.addItems(["1", "2", "3", "4", "5"])

        #room
        room_combo = QComboBox()
        room_combo.addItems(["1", "2", "3", "4", "5"])

        #searchbutton
        search_button = QPushButton("Search")

        filter_layout.addWidget(location_combo)
        filter_layout.addWidget(guest_combo)
        filter_layout.addWidget(room_combo)
        filter_layout.addWidget(search_button)
        
        return filter_layout
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

