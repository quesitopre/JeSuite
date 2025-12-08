from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# -------------------------
# Cart Item Model
# -------------------------
class CartItem:
    def __init__(self, room_name, price, quantity=1):
        self.room_name = room_name
        self.price = price
        self.quantity = quantity

# -------------------------
# Shopping Cart Page
# -------------------------
class ShoppingCartPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.cart = []  # list of CartItem objects
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Title
        title = QLabel("Your Shopping Cart")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)

        # Cart List
        self.cart_list = QListWidget()
        layout.addWidget(self.cart_list)

        # Total Label
        self.total_label = QLabel("Total: $0.00")
        self.total_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(self.total_label)

        # Confirm Button
        self.button = QPushButton("Confirm Reservation")
        self.button.clicked.connect(self.go_to_reservation)
        layout.addWidget(self.button)

        self.refresh_cart()

    # -------------------------
    # Cart Logic
    # -------------------------
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

    # -------------------------
    # UI Updates
    # -------------------------
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

        # Room Label
        label = QLabel(f"{item.room_name} — ${item.price:.2f}")
        label.setMinimumWidth(200)
        layout.addWidget(label)

        # Minus Button
        minus_btn = QPushButton("-")
        minus_btn.clicked.connect(lambda _, i=item: self.update_quantity(i, -1))
        layout.addWidget(minus_btn)

        # Quantity Label
        qty_label = QLabel(str(item.quantity))
        qty_label.setAlignment(Qt.AlignCenter)
        qty_label.setMinimumWidth(30)
        layout.addWidget(qty_label)

        # Plus Button
        plus_btn = QPushButton("+")
        plus_btn.clicked.connect(lambda _, i=item: self.update_quantity(i, 1))
        layout.addWidget(plus_btn)

        return container

    def update_quantity(self, item, change):
        item.quantity += change
        if item.quantity <= 0:
            self.cart.remove(item)
        self.refresh_cart()

    def go_to_reservation(self):
        self.stacked_widget.setCurrentIndex(3)
