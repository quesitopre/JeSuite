import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout, QComboBox, 
    QVBoxLayout, QLabel, QCalendarWidget, QSizePolicy
) 
from PyQt5.QtGui import QPixmap
from header import Header

import pydoc

#calendar popup class
class CalendarPopUp(QCalendarWidget):
    '''
    Popup calendar for selecting start and end dates.
    Calls a callback function with the selected dates.
    '''
    def __init__(self, parent=None, callback=None):
        '''
        Initializes the CalendarPopUp widget.

        Params:
            parent: QWidget, the parent widget.
            callback: function, a function to call with (start_date, end_date).

        Returns:
            None
        '''
        super().__init__(parent)
        self.callback = callback
        self.setWindowFlags(Qt.Popup)
        self.clicked.connect(self.on_date_selected)
        self.start_date = None

    def on_date_selected(self, date):
        '''
        Handles date selection. Stores the start date first, then the end date.
        Ensures the start date is before the end date. Calls the callback function 
        if defined and closes the popup.

        Params:
            date: QDate, the date clicked.

        Returns:
            None
        '''

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


class HomePage(QWidget):
    '''
    The landing page of the hotel reservation system. 
    Displays header, filters, background image, and search functionality.
    '''
    def __init__(self, stacked_widget):
        '''
        Initializes the HomePage widget with header, filters, and background.

        Params:
            stacked_widget: QStackedWidget, used for navigation between pages.

        Returns:
            None
        '''
        super().__init__()
        self.stacked_widget = stacked_widget

        self.setStyleSheet("""
            QLabel {
                color: black;          
            }
            QPushButton {
                background-color: #8c6d3d;
            }
            QComboBox {
                background-color: #8c6d3d;
            }
            QDateEdit{
                background-color: #a07e45;
                color: white;
            }          
            QCalendarWidget QWidget {
                background-color: white;  
                color: #a07e45;       
            }
            QCalendarWidget QAbstractItemView {
                selection-background-color: #f2c94c;
            }  
        """)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)
        header = self.create_header()
        filters = self.create_categories()
       
        main_layout.addLayout(header)

        #background
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("Assets/landingpage_image.jpeg")
        self.label.setPixmap(pixmap.scaled(1000, 300)) 

    
        main_layout.addWidget(self.label)
        main_layout.addLayout(filters)
        main_layout.addStretch() 
        self.setLayout(main_layout)

        self.calendar_popUp = None
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    
    def create_header(self):
        '''
        Creates the header layout with navigation labels and sign-in/up buttons.

        Params:
            None

        Returns:
            QHBoxLayout containing the header widgets.
        '''
        header_layout = QHBoxLayout()

        # add hotel logo 
        self.logo = QLabel(self)
        self.logo.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("Assets/logo.png")
        self.logo.setPixmap(pixmap.scaled(100, 100)) 
        header_layout.addWidget(self.logo)
        #company_logo = QLabel("Hotel logo")
        home_text = QLabel("Home")
        about_text = QLabel("About Us")
        services_text = QLabel("Services")
        memebership_text = QLabel("Membership")
        contact_text = QLabel("Contact Us")
        sign_in_button = QPushButton("Sign In")
        sign_up_button = QPushButton("Sign Up")

        #header_layout.addWidget(company_logo)
        header_layout.addWidget(home_text)
        header_layout.addWidget(about_text)
        header_layout.addWidget(services_text)
        header_layout.addWidget(memebership_text)
        header_layout.addWidget(contact_text)
        header_layout.addWidget(sign_in_button)
        header_layout.addWidget(sign_up_button)

        return header_layout
    

    def create_categories(self):
        '''
        Creates search filters for location, people, and calendar dates, 
        along with a search button.

        Params:
            None

        Returns:
            QHBoxLayout containing filter widgets and search button.
        '''
        
        #hold all layouts and lays them out horizontally
        filter_layout = QHBoxLayout()

        #individual layouts for each filter
        location_layout = QVBoxLayout()
        people_layout = QVBoxLayout()
        calendar_layout = QVBoxLayout()


        #location
        location_label = QLabel("Location:")
        location_combo = QComboBox()
        location_combo.addItems(["Los Angeles, California", "Santa Monica, California", "Beverly Hill, California", "Malibu, California"])
        self.location_combo = location_combo.currentText()

        #people
        people_label = QLabel("People:")
        people_combo = QComboBox()
        people_combo.addItems(["1 guest, 1 room", "2 guests, 1 room", "3 guests, 1 room", "4 guests, 1 room", "5 guests, 2 rooms", "6 guests, 2 rooms"])
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

        #adding location layout to filter layout
        location_layout.addWidget(location_label)
        location_layout.addWidget(location_combo)
        filter_layout.addLayout(location_layout)

        #adding people layout to filter layout
        people_layout.addWidget(people_label)
        people_layout.addWidget(people_combo)
        filter_layout.addLayout(people_layout)

        #adding calendar check in, check out layout to filter layout
        calendar_layout.addWidget(calendar_label)
        calendar_layout.addWidget(self.date_button)
        filter_layout.addLayout(calendar_layout)


        filter_layout.addWidget(search_button)
        #filter_layout.addWidget(self.label)
        
        return filter_layout
    
    def show_calendar_popup(self):
        '''
        Displays a popup calendar for selecting check-in and check-out dates.

        Params:
            None

        Returns:
            None
        '''
        if self.calendar_popUp and self.calendar_popUp.isVisible():
            self.calendar_popUp.close()
            return
        self.calendar_popUp= CalendarPopUp(self, self.set_selected_dates)
        button_pos =self.date_button.mapToGlobal(self.date_button.rect().bottomLeft())
        self.calendar_popUp.move(button_pos)
        self.calendar_popUp.show()

    def set_selected_dates(self, start_date, end_date):
        '''
        Updates the date button text with selected start and end dates.

        Params:
            start_date: QDate, selected start date
            end_date: QDate, selected end date

        Returns:
            None
        '''
        self.date_button.setText(
            f"{start_date.toString('MM/dd/yyyy')} - {end_date.toString('MM/dd/yyyy')}"
            )
        
    def go_to_room_selection(self):
        '''
        Switches the stacked widget to the room selection page.

        Params:
            None

        Returns:
            None
        '''
        self.stacked_widget.setCurrentIndex(1)

pydoc.writedoc("homepage")
