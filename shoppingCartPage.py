from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import pydoc

# Cart Item Model
class CartItem(QWidget):
    def __init__(self, room_name, price, quantity=1):
        self.room_name = room_name
        self.price = price
        self.quantity = quantity

# Shopping Cart Page
class ShoppingCartPage(QWidget):
    '''
    Represents the shopping cart page where users can review selected rooms 
    and proceed to the reservation page.
    '''
    def __init__(self, stacked_widget):
        '''
        Initializes the ShoppingCartPage and sets up the UI components.

        Parameters:
            stacked_widget (QStackedWidget): Used to navigate between pages.

        Returns:
            None
        '''
        super().__init__()
        self.stacked_widget = stacked_widget
        self.cart = []   # list of CartItem objects
        self.initUI()

    def initUI(self):
        '''
        Sets up the UI for the shopping cart page, including a label 
        and a button to go to the reservation page.

        Parameters:
            None

        Returns:
            None
        '''
        layout = QVBoxLayout()
        self.setLayout(layout)

        title = QLabel("Your Shopping Cart")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; color: black;")
        layout.addWidget(title)

        self.cart_list = QListWidget()
        self.cart_list.setStyleSheet("background-color: white; color: black")
    
        layout.addWidget(self.cart_list)

        self.total_label = QLabel("Total: $0.00")
        self.total_label.setStyleSheet("font-size: 15px; color: black;")
        layout.addWidget(self.total_label)

        self.button = QPushButton("Confirm Reservation")
        self.button.setStyleSheet("""
            QLabel {
                color: black;
            }
            QPushButton {
                background-color: #8c6d3d;
            }
            QComboBox {
                background-color: #8c6d3d;
            }
        """)
        self.button.clicked.connect(self.go_to_reservation)
        layout.addWidget(self.button)

        self.refresh_cart()


    # Cart Logic
    def add_room(self, room_name, price):
        for item in self.cart:
            if item.room_name == room_name:
                item.quantity += 1
                self.refresh_cart()
                return

        self.cart.append(CartItem(room_name, price))
        self.refresh_cart()

    def get_total(self):
        return sum(item.price * item.quantity for item in self.cart)
    
    # UI Updates
  
    def refresh_cart(self):
        self.cart_list.clear()

        for item in self.cart:
            widget = self.create_cart_item_row(item)
            list_item = QListWidgetItem()
            list_item.setSizeHint(widget.sizeHint())
            self.cart_list.addItem(list_item)
            self.cart_list.setItemWidget(list_item, widget)

        self.total_label.setText(f"Total: ${self.get_total():.2f}")

    def create_cart_item_row(self, item):
        container = QWidget()
        layout = QHBoxLayout(container)

        label = QLabel(f"{item.room_name} — ${item.price:.2f}")
        label.setMinimumWidth(200)
        layout.addWidget(label)

        minus_btn = QPushButton("-")
        minus_btn.clicked.connect(lambda: self.update_quantity(item, -1))
        layout.addWidget(minus_btn)

        qty_label = QLabel(str(item.quantity))
        qty_label.setAlignment(Qt.AlignCenter)
        qty_label.setMinimumWidth(30)
        layout.addWidget(qty_label)

        plus_btn = QPushButton("+")
        plus_btn.clicked.connect(lambda: self.update_quantity(item, 1))
        layout.addWidget(plus_btn)

        return container

    def update_quantity(self, item, change):
        item.quantity += change
        if item.quantity <= 0:
            self.cart.remove(item)
        self.refresh_cart()
    
    def go_to_reservation(self):
        '''
        Navigates to the reservation page by changing the stacked widget index.

        Parameters:
            None

        Returns:
            None
        '''
        self.stacked_widget.setCurrentIndex(3)

pydoc.writedoc("shoppingCartPage")

