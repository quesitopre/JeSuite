import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout, QComboBox, 
    QVBoxLayout, QLabel, QCalendarWidget
) 
from PyQt5.QtGui import QPixmap

#calendar popup class
class CalendarPopUp(QCalendarWidget):
    #Popup calendar for selecting start and end dates
    def __init__(self, parent=None, callback=None):
        super().__init__(parent)
        self.callback = callback
        self.setWindowFlags(Qt.Popup)
<<<<<<< HEAD
        self.clicked.connect(self.on_date_selected)#typo fixed
=======
        self.clicked.connect(self.on_date_selected)
>>>>>>> bc63d033fffcf9646a9120805637a6f6e7a0151c
        self.start_date = None #The first click

    def on_date_selected(self, date):
        #Select the starting and ending dates, then close ze popup
        if not self.start_date:
            self.start_date = date
        else:
            end_date = date
            #verify date order
            if end_date <self.start_date:
                self.start_date, end_date = end_date, self.start_date
            if self.callback:
                self.callback(self.start_date,end_date)
                self.close( )


<<<<<<< HEAD
        



# Subclass QMainWindow to customize your application's main window
class MainWindow(QWidget): 
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(1000,500)
        self.setStyleSheet("background-color: lightblue;")
=======
class HomePage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
>>>>>>> bc63d033fffcf9646a9120805637a6f6e7a0151c

        main_layout = QVBoxLayout()
        header = self.create_header()
        filters = self.create_categories()
<<<<<<< HEAD

=======
       
>>>>>>> bc63d033fffcf9646a9120805637a6f6e7a0151c
        main_layout.addLayout(header)

        #background
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("Assets/landingpage_image.jpeg")
        self.label.setPixmap(pixmap.scaled(1000, 500)) 

    
        main_layout.addWidget(self.label)
        main_layout.addLayout(filters)
        self.setLayout(main_layout)

        self.calendar_popUp = None

<<<<<<< HEAD
=======

>>>>>>> bc63d033fffcf9646a9120805637a6f6e7a0151c
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
<<<<<<< HEAD

    
=======
    

>>>>>>> bc63d033fffcf9646a9120805637a6f6e7a0151c
    def create_categories(self):
        
        #hold all layouts and lays them out horizontally
        filter_layout = QHBoxLayout()

        #individual layouts for each filter
        location_layout = QVBoxLayout()
<<<<<<< HEAD
        #guest_layout = QVBoxLayout()
        #room_layout = QVBoxLayout()
        #guestandroom_layout = QVBoxLayout()
        people_layout = QVBoxLayout()
        #checkin_layout = QVBoxLayout()
        #checkout_layout = QVBoxLayout()
        calendar_layout = QVBoxLayout()

        
=======
        people_layout = QVBoxLayout()
        calendar_layout = QVBoxLayout()

>>>>>>> bc63d033fffcf9646a9120805637a6f6e7a0151c

        #location
        location_label = QLabel("Location:")
        location_combo = QComboBox()
<<<<<<< HEAD
        location_combo.addItems(["Los Angeles, California", "Santa Monica, California", "Beverly Hill, California"])
        
        #CHANGED
        self.location_combo = location_combo.currentText()

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


        #calendar
        calendar_label = QLabel("Calendar:")
        calendar_combo = QComboBox()
        calendar_combo.addItems(["Check-in and Check-out Dates"])
        

=======
        location_combo.addItems(["Los Angeles, California", "Santa Monica, California", "Beverly Hill, California", "Malibu, California"])
        self.location_combo = location_combo.currentText()

>>>>>>> bc63d033fffcf9646a9120805637a6f6e7a0151c
        #people
        people_label = QLabel("People:")
        people_combo = QComboBox()
        people_combo.addItems(["1 guest, 1 room", "2 guests, 1 room", "3 guests, 1 room", "4 guests, 1 room", "5 guests, 2 rooms", "6 guests, 2 rooms"])
<<<<<<< HEAD
        #CHANGED
        self.people_combo = people_combo.currentText()

        #datebutton
        self.date_button = QPushButton("Select Dates")
        self.date_button.clicked.connect(self.show_calendar_popup)
        #searchbutton
        search_button = QPushButton("Search")
=======
        self.people_combo = people_combo.currentText()

        #calendar
        calendar_label = QLabel("Calendar:")
        calendar_combo = QComboBox()
        calendar_combo.addItems(["Check-in and Check-out Dates"])
        self.calendar_combo = calendar_combo.currentText()
        
        #datebutton
        self.date_button = QPushButton("Select Dates")
        self.date_button.clicked.connect(self.show_calendar_popup)
        
        #searchbutton
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.go_to_room_selection)
>>>>>>> bc63d033fffcf9646a9120805637a6f6e7a0151c

        #adding location layout to filter layout
        location_layout.addWidget(location_label)
        location_layout.addWidget(location_combo)
        filter_layout.addLayout(location_layout)

<<<<<<< HEAD
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

=======
>>>>>>> bc63d033fffcf9646a9120805637a6f6e7a0151c
        #adding people layout to filter layout
        people_layout.addWidget(people_label)
        people_layout.addWidget(people_combo)
        filter_layout.addLayout(people_layout)

<<<<<<< HEAD
        #adding calendar check_in layout to filter layout
        calendar_layout.addWidget(calendar_label)
        calendar_layout.addWidget(self.date_button) #bug fixed
        filter_layout.addLayout(calendar_layout)

        #adding calendar check_out layout to filter layout
        #calendar_layout.addWidget(checkout_label)
        #calendar_layout.addWidget(self.checkout_calendar)
        #filter_layout.addLayout(calendar_layout)


=======
        #adding calendar check in, check out layout to filter layout
        calendar_layout.addWidget(calendar_label)
        calendar_layout.addWidget(self.date_button)
        filter_layout.addLayout(calendar_layout)

>>>>>>> bc63d033fffcf9646a9120805637a6f6e7a0151c

        filter_layout.addWidget(search_button)
        #filter_layout.addWidget(self.label)
        
        return filter_layout
    
    def show_calendar_popup(self):
        if self.calendar_popUp and self.calendar_popUp.isVisible():
            self.calendar_popUp.close()
            return
        self.calendar_popUp= CalendarPopUp(self, self.set_selected_dates)
        button_pos =self.date_button.mapToGlobal(self.date_button.rect().bottomLeft())
        self.calendar_popUp.move(button_pos)
        self.calendar_popUp.show()

    def set_selected_dates(self, start_date, end_date):
        self.date_button.setText(
            f"{start_date.toString('MM/dd/yyyy')} - {end_date.toString('MM/dd/yyyy')}"
            )
<<<<<<< HEAD

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

=======
        
    def go_to_room_selection(self):
        self.stacked_widget.setCurrentIndex(1)
>>>>>>> bc63d033fffcf9646a9120805637a6f6e7a0151c
