from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QPushButton, QWidget, QHBoxLayout, QLabel
) 
from PyQt5.QtGui import QPixmap

class Header(QWidget):
    def __init__(self, bool=True):
       
        super().__init__()
        self.initUI()
    
    def initUI(self):
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
        home_text = QLabel("       Home")
        about_text = QLabel("About Us")
        services_text = QLabel("Services")
        memebership_text = QLabel("Membership")
        contact_text = QLabel("Contact Us")

        #header_layout.addWidget(company_logo)
        header_layout.addWidget(home_text)
        header_layout.addWidget(about_text)
        header_layout.addWidget(services_text)
        header_layout.addWidget(memebership_text)
        header_layout.addWidget(contact_text)

        if bool == True:
            sign_in_button = QPushButton("Sign In")
            sign_up_button = QPushButton("Sign Up")
            header_layout.addWidget(sign_in_button)
            header_layout.addWidget(sign_up_button)
            
        #admin butto

        
        self.setLayout(header_layout)
    