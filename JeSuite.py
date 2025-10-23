import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout, QComboBox, 
    QVBoxLayout, QLabel, QCalendarWidget
) 
from PyQt5.QtGui import QPixmap


# Subclass QMainWindow to customize your application's main window
class MainWindow(QWidget): 
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(1000,500)
        self.setStyleSheet("background-color: lightblue;")

        main_layout = QVBoxLayout()
        header = self.create_header()
        filters = self.create_categories()

        main_layout.addLayout(header)

        #background
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("Assets/landingpage_image.jpeg")
        self.label.setPixmap(pixmap.scaled(1000, 500)) 

    
        main_layout.addWidget(self.label)
        main_layout.addLayout(filters)
        self.setLayout(main_layout)

    def create_header(self):
        header_layout = QHBoxLayout()

        company_logo = QLabel("Hotel logo")
        home_text = QLabel("Home")
        about_text = QLabel("About Us")
        services_text = QLabel("Services")
        memebership_text = QLabel("Membership")
        contact_text = QLabel("Contact Us")
        sign_in_button = QPushButton("Sign In")
        sign_up_button = QPushButton("Sign Up")

        header_layout.addWidget(company_logo)
        header_layout.addWidget(home_text)
        header_layout.addWidget(about_text)
        header_layout.addWidget(services_text)
        header_layout.addWidget(memebership_text)
        header_layout.addWidget(contact_text)
        header_layout.addWidget(sign_in_button)
        header_layout.addWidget(sign_up_button)

        return header_layout

    
    def create_categories(self):
        
        #hold all layouts and lays them out horizontally
        filter_layout = QHBoxLayout()

        #individual layouts for each filter
        location_layout = QVBoxLayout()
        #guest_layout = QVBoxLayout()
        #room_layout = QVBoxLayout()
        #guestandroom_layout = QVBoxLayout()
        people_layout = QVBoxLayout()
        #checkin_layout = QVBoxLayout()
        #checkout_layout = QVBoxLayout()
        ##calendar_layout = QVBoxLayout()

        

        #location
        location_label = QLabel("Location:")
        location_combo = QComboBox()
        location_combo.addItems(["Los Angeles, California", "Santa Monica, California", "Beverly Hill, California"])

        #guest
        #guest_label = QLabel("Guest:")
        #guest_combo = QComboBox()
        #guest_combo.addItems(["1", "2", "3", "4", "5"])

        #room
        #room_label = QLabel("Room:")
        #room_combo = QComboBox()
        #room_combo.addItems(["1", "2", "3", "4", "5"])

        #guestandroom
        #guestandroom_label = QLabel("Guest and Room:")
        #guestandroom_combo = QComboBox()
        #guestandroom_combo.addItems(["1 guest, 1 room", "2 guests, 1 room", "3 guests, 1 room", "4 guests, 1 room", "5 guests, 2 rooms"])

        #calendar checkin
        ##checkin_label = QLabel("Check In Date:")
        ##self.checkin_calendar = QCalendarWidget(self)
        ##self.checkin_calendar.setGridVisible(True)
        #self.checkin_calendar.setCalendar(QDate.currentDate())
        #self.checkin_calendar.setCalendarPopup(True)


        #calendar checkout
         #checkout_label = QLabel("Check Out Date:")     
         #self.checkout_calendar = QCalendarWidget(self)
         #self.checkout_calendar.setGridVisible(True)
        #self.checkout_calendar.setCalendar(QDate.currentDate().addDay(1))
        #self.checkout_calendar.setCalendarPopup(True)


        #people
        people_label = QLabel("People:")
        people_combo = QComboBox()
        people_combo.addItems(["1 guest, 1 room", "2 guests, 1 room", "3 guests, 1 room", "4 guests, 1 room", "5 guests, 2 rooms", "6 guests, 2 rooms"])


        #searchbutton
        search_button = QPushButton("Search")

        #adding location layout to filter layout
        location_layout.addWidget(location_label)
        location_layout.addWidget(location_combo)
        filter_layout.addLayout(location_layout)

        #adding guest layout to filter layout
        #guest_layout.addWidget(guest_label)
        #guest_layout.addWidget(guest_combo)
        #filter_layout.addLayout(guest_layout)

        #adding room layout to filter layout
        #room_layout.addWidget(room_label)
        #room_layout.addWidget(room_combo)
        #filter_layout.addLayout(room_layout)

        #adding guestandroom layout to filter layout
        #guestandroom_layout.addWidget(guestandroom_label)
        #guestandroom_layout.addWidget(guestandroom_combo)
        #filter_layout.addLayout(guestandroom_layout)

        #adding people layout to filter layout
        people_layout.addWidget(people_label)
        people_layout.addWidget(people_combo)
        filter_layout.addLayout(people_layout)

        #adding calendar check_in layout to filter layout
        ##calendar_layout.addWidget(checkin_label)
        ##calendar_layout.addWidget(self.checkin_calendar)
        ##filter_layout.addLayout(calendar_layout)

        #adding calendar check_out layout to filter layout
        #calendar_layout.addWidget(checkout_label)
        #calendar_layout.addWidget(self.checkout_calendar)
        #filter_layout.addLayout(calendar_layout)


        filter_layout.addWidget(search_button)
        #filter_layout.addWidget(self.label)
        
        return filter_layout
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

