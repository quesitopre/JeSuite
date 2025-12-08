from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from customer import Customer
import pydoc

""""" Creates class TextInputField that encapsulates a labeled text input field. """
class TextInputField(QWidget):
   
    def __init__ (self, label_text, placeholder=""):
        """ creates labeled text input field with specified label and placeholder text """
        super().__init__()
        self.label_text = label_text
        self.placeholder = placeholder
        self.initUI()


    def initUI(self):
        """ Initialize the UI components for the input fields creation of vertical layout containing:
          - Descriptive QLabel for field
            - QLineEdit for user input and placeholder text
         The layout is set as the widget layout. """
        layout = QVBoxLayout()
        self.label = QLabel(self.label_text)
        self.input = QLineEdit()
        self.input.setPlaceholderText(self.placeholder)
        self.input.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: black;
                border: 1px solid #c4c4c4;
                border-radius: 6px;
                padding: 6px;
                font-size: 14px;
            }
            QLineEdit::placeholder {
                color: #666666;
            }
        """)
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        self.setLayout(layout)
    def get_value(self):
        """Return text entered in the input field"""
        return self.input.text()
    def set_value(self,text):
        """Set text in the input field"""
        self.input.setText(text)

""" Reservation Page Class"""
class ReservationPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        """Initialize input fields to None"""
        self.first_name_field = None
        self.last_name_field = None

        self.initUI()


    def initUI(self):

        """ Defines the layout and structure of the reservation page UI."""
        layout = QVBoxLayout()
        layout.setSpacing(10)
       


        """Main Header label: Complete Your Reservation"""


        self.header_label = QLabel("Complete Your Reservation")
        self.header_label.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("font-size: 20px; font-weight: bold; color: black;")
        layout.addWidget(self.header_label)
       
        '''Create Subheader: Guest Information'''
        self.subheader = QLabel ("Guest Information")
        self.subheader.setAlignment (Qt.AlignLeft)
        self.setStyleSheet("font-size: 15px; color: black;")
        layout.addWidget(self.subheader)
       

        """Creates and adds input fields to the reservation page layout
         for first name, last name and are arranged horizontally in a 
         shared QHBoxLayoutso they appear side by side. """
       ####Input Fields####
        self.first_name_field = TextInputField("First Name", "Enter your first name")
        self.last_name_field = TextInputField("Last Name", "Enter your last name")
        name_layout = QHBoxLayout()
        name_layout.addWidget(self.first_name_field)
        name_layout.addWidget(self.last_name_field)
        layout.addLayout(name_layout)



        """Creates and adds input fields to the reservation page layout for phone number and 
       email and are arranged horizontally in a shared QHBoxLayout so they appear side by side"""
        ##Contact Field##
        self.phone_field = TextInputField("Phone Number", "Enter your phone number")
        self.email_field = TextInputField("Email","Enter your email address")
        contact_layout = QHBoxLayout()
        contact_layout.addWidget(self.phone_field)
        contact_layout.addWidget(self.email_field)
        layout.addLayout(contact_layout)    


        '''Create Address Subheader: Address'''
        self.address_header = QLabel ("Address")
        self.address_header.setAlignment (Qt.AlignLeft)
        self.setStyleSheet("font-size: 15px; color: black;")
        layout.addWidget(self.address_header)

        """Create a horizontal layout containing input fields for Zipcode and State. 
        This groups related address information side-by-side to improve form readability."""
        ####address field####
        self.addressline_field = TextInputField("Adress Line ", "Enter your address")
        self.city_field = TextInputField("City", "Enter your City")
        address_layout = QHBoxLayout()
        address_layout.addWidget(self.addressline_field)
        address_layout.addWidget(self.city_field)
        layout.addLayout(address_layout)
       

        """Create the Zipcode and State input fields and arrange them horizontally.
         The two TextInputField widgets are placed inside an HBox layout so the user
        can enter both values side by side. The combined layout is then added to
         the main form layout."""
        ###address field####
        self.zipcode = TextInputField("Zipcode", "Enter your zipcode")
        self.state = TextInputField("State", "Enter your state")
        zipstate_layout = QHBoxLayout()
        zipstate_layout.addWidget(self.zipcode)
        zipstate_layout.addWidget(self.state)
        layout.addLayout(zipstate_layout)


        '''Create Credit Info Subheader'''
        self.credit_subheader = QLabel ("Credit/Debit Information")
        self.credit_subheader.setAlignment (Qt.AlignLeft)
        self.setStyleSheet("font-size: 15px; color: black;")
        layout.addWidget(self.credit_subheader)


        """Creates and configures the credit/debit  input fields. The exipiration date and year
          field uses a narrowfixed width because it contains a short numeric value,
         while the Card number field is given a slightly
         larger width. All fields are added to the main layout
           to appear horizontal in the form."""


        ###credit/debit fields####
   
        self.card_num = TextInputField("Credit/Debit", "Enter your Card Number")
        self.card_num.setFixedWidth(250)
        self.expir_month = TextInputField("Expiration Month", "Enter expiration month")
        self.expir_month.setFixedWidth(150)
        self.expir_year = TextInputField("Expiration Year", "Enter expiration year")
        self.expir_year.setFixedWidth(150)
        card_layout = QHBoxLayout()
        card_layout.addWidget(self.card_num)
        card_layout.addWidget(self.expir_month)
        card_layout.addWidget(self.expir_year)
        layout.addLayout(card_layout)


        """Creates and configures the CVV and Billing 
        Zipcode input fields. The CVV field uses a narrow
          fixed width because it contains a short numeric value,
         while the Billing Zipcode field is given a slightly
         larger width. Both fields are added to the main layout
           to appear vertically in the form."""

        self.CVV = TextInputField("CVV", "Enter CVV")
        self.CVV.setFixedWidth(100)
        self.billing_zip = TextInputField("Billing Zipcode", "Enter billing zip")
        self.billing_zip.setFixedWidth(150)
        cvv_layout = QVBoxLayout()
        layout.addWidget(self.CVV)
        layout.addWidget(self.billing_zip)
        layout.addLayout(cvv_layout)


        self.setLayout(layout)



        """Create and configure the Confirm Reservation button."""
        self.confirm_button = QPushButton("Confirm Reservation")
        self.confirm_button.setStyleSheet("""
            QPushButton {
                background-color: #8c6d3d;
                color: white;
            }
            QComboBox {
                background-color: #8c6d3d;
            }
        """)
        self.confirm_button.clicked.connect(self.confirm_reservation)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

   
    def confirm_reservation(self):
        """Handle reservation confirmation logic"""
        customer = Customer(
            first_name=self.first_name_field.get_value(),
            last_name=self.last_name_field.get_value(),
            phone=self.phone_field.get_value(),
            email=self.email_field.get_value(),
            address=self.addressline_field.get_value(),
            city=self.city_field.get_value(),
            state=self.state.get_value(),
            zipcode=self.zipcode.get_value(),
            card_num=self.card_num.get_value(),
            expir_month=self.expir_month.get_value(),
            expir_year=self.expir_year.get_value(),
            cvv=self.CVV.get_value(),
            billing_zip=self.billing_zip.get_value()
        )

    # ✅ Customer.__init__ already calls save_to_csv()
        print(f"Reservation confirmed and saved for: {customer.first_name} {customer.last_name}")
   
    def get_guestinfo(self):
        """Return guest information as a dictionary"""
        return {
            "first_name": self.first_name_field.get_value(),
            "last_name": self.last_name_field.get_value()
        }
    
    
pydoc.writedoc("reservationPage")
