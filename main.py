import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from homepage import HomePage
from roomSelection import RoomSelectionPage
#from roomCard import RoomCard
from shoppingCartPage import ShoppingCartPage
from reservationPage import ReservationPage
from confirmationPage import ConfirmationPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JeSuite Hotel Reservation")
        self.resize(1000, 500)
        #self.setStyleSheet("background-color: lightblue;")
        self.setStyleSheet("""
            MainWindow{
                background-color: white;          
            }
        """)


        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        home = HomePage(self.stack)
        room_selection = RoomSelectionPage(self.stack)
        shopping_cart = ShoppingCartPage(self.stack)
        reservation = ReservationPage(self.stack)
        confirmation_text = ConfirmationPage(self.stack)


        self.stack.addWidget(home)
        self.stack.addWidget(room_selection)
        self.stack.addWidget(shopping_cart)
        self.stack.addWidget(reservation)
        self.stack.addWidget(confirmation_text)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
