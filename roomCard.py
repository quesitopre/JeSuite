from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import pydoc

class RoomCard(QWidget):
    '''
    Represents an individual hotel room card, showing the room image, 
    name, capacity, price, and a 'Book Now!' button.
    '''
    def __init__(self, image_path, suite_name, capacity, price, stacked_widget = None):
        '''
        Initializes the RoomCard widget with image, name, capacity, price, 
        and optional stacked widget for navigation.

        Parameters:
            image_path (str): Path to the room image.
            suite_name (str): Name of the suite.
            capacity (str): Maximum occupancy description.
            price (str): Room price as a string.
            stacked_widget (QStackedWidget, optional): For page navigation.

        Returns:
            None
        '''
        super().__init__()

        self.image = image_path
        self.name = suite_name
        self.capacity = capacity
        self.price = price
        self.stacked_widget = stacked_widget

        self.initUI()
        
    def initUI(self):
        '''
        Sets up the RoomCard UI with image, labels, and a 'Book Now!' button.
        Styles the card and arranges components vertically.

        Parameters:
            None

        Returns:
            None
        '''
        self.setObjectName("RoomCard")
        self.setFixedSize(300,380)
        self.setStyleSheet("""
            QLabel {
                color: #333333;
                font-family: Arial;
            }
            QPushButton {
                background-color: #a07e45;
                color: white;
                border-radius: 8px;
                padding: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #8c6d3d;
            }
            #RoomCard {
                background-color: white;
                border: 1px solid #000000;
                border-radius: 12px;
                padding: 10px;
            }
            #RoomCard:hover {
                border: 1px solid #a07e45;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            }
        """)

    
        layout = QVBoxLayout()

        info_layout = QVBoxLayout()

        # image 
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(self.image)
        self.label.setPixmap(pixmap.scaled(250, 300)) 
        info_layout.addWidget(self.label)

        # name 
        name_label = QLabel(self.name)
        name_label.setAlignment(Qt.AlignCenter)
        info_layout.addWidget(name_label)

        # capacity 
        cap_label = QLabel(self.capacity)
        cap_label.setAlignment(Qt.AlignCenter)
        info_layout.addWidget(cap_label)

        # price
        price_label = QLabel(self.price)
        price_label.setAlignment(Qt.AlignCenter)
        info_layout.addWidget(price_label)

        # book button 
        self.book_button = QPushButton("Book Now!")
        self.book_button.clicked.connect(self.go_to_reservation_page)
        info_layout.addWidget(self.book_button)        

        layout.addLayout(info_layout)

        self.setLayout(layout)

    def go_to_reservation_page(self):
        '''
        Navigates to the reservation page by changing the stacked widget index.

        Parameters:
            None

        Returns:
            None
        '''
        self.stacked_widget.setCurrentIndex(2)

pydoc.writedoc("roomCard")

