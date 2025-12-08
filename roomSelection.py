from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from roomCard import RoomCard
from header import Header
from roomAmenities import RoomAmenities

class RoomSelectionPage(QWidget):
    """
    Displays all rooms. Connects RoomCard signals to ShoppingCartPage.
    """
    def __init__(self, stacked_widget, cart_page):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.cart_page = cart_page  # reference to ShoppingCartPage

        layout = QVBoxLayout()

        # Header
        layout.addWidget(Header(False))
        layout.addWidget(RoomAmenities())

        # Room cards layout
        grid = QHBoxLayout()
        rooms = [
            ("Assets/King_room.jpg", "1 King bed", "Max Occupancy: 3", "$170"),
            ("Assets/Queen_room.avif", "1 Queen bed", "Max Occupancy: 2", "$120"),
            ("Assets/Double_room.avif", "Double bed(2 Queen)", "Max Occupancy: 4", "$210"),
            ("Assets/Suite_room.jpg", "Suite bed(2 King)", "Max Occupancy: 4", "$280")
        ]

        for img, name, cap, price in rooms:
            card = RoomCard(img, name, cap, price, self.stacked_widget)
            # Connect the signal to add_room in the cart
            card.added_to_cart.connect(self.cart_page.add_room)
            grid.addWidget(card)

        layout.addLayout(grid)
        self.setLayout(layout)
