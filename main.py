import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from homepage import HomePage
from roomSelection import RoomSelectionPage
#from roomCard import RoomCard
from shoppingCartPage import ShoppingCartPage
from reservationPage import ReservationPage
from confirmationPage import ConfirmationPage
from booking import Booking 

import pydoc

class MainWindow(QMainWindow):

    def __init__(self):
        '''
        Initializes the main window with title, size, style, and sets up 
        the stacked widget with all pages: HomePage, RoomSelectionPage, 
        ShoppingCartPage, and ReservationPage.
        
        Params:
            None

        Returns:
            None
        '''
        super().__init__()
        self.setWindowTitle("JeSuite Hotel Reservation")
        self.resize(1292, 924)
        self.setMinimumSize(800, 600)
        self.setMaximumSize(1920, 1080)
        self.statusBar().setSizeGripEnabled(True) # make window resizable
        #self.setStyleSheet("background-color: lightblue;")
        self.setStyleSheet("""
            MainWindow{
                background-color: white;          
            }
        """)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.booking_manager = Booking() #booking manager reference

        #Initialize pages
        home = HomePage(self.stack,self.booking_manager)
        shopping_cart = ShoppingCartPage(self.stack)
        room_selection = RoomSelectionPage(self.stack,shopping_cart)
        reservation = ReservationPage(self.stack, self.booking_manager,shopping_cart) 
        shopping_cart = ShoppingCartPage(self.stack, self.booking_manager)
        confirmation_text = ConfirmationPage(self.stack)

        #Add pages to stacked widget
        self.stack.addWidget(home)
        self.stack.addWidget(room_selection)
        self.stack.addWidget(shopping_cart)
        self.stack.addWidget(reservation)
        self.stack.addWidget(confirmation_text)

if __name__ == "__main__":
    '''
    Entry point of the application. Creates a QApplication, initializes 
    MainWindow, shows it, and starts the event loop.
    
    Params:
        None

    Returns:
        None
    '''
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_() # bring window to front
    window.activateWindow() # bring window to front
    sys.exit(app.exec_())

pydoc.writedoc("main")
