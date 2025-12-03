import unittest #The test framework
from cart_Service import CartService, CartItem
from room import Room
from datetime import datetime
from roomSearch import roomSearch

class TestCartService:

    def __init__(self):
        self.cartService = CartService()
        self.roomChoices = roomSearch()
    
    def printIt(self):
        print(self.cartService.cartItems) 
    
    def addItem1(self):
        check_in = datetime.strptime("12/02/2025", "%m/%d/%Y")
        check_out = datetime.strptime("12/07/2025", "%m/%d/%Y")
        self.item1 = CartItem(self.roomChoices.single_king, check_in, check_out) #create a new cart item
        self.cartService.cartItems.append(self.item1)

    def addItem2(self):
        check_in = datetime.strptime("12/03/2025", "%m/%d/%Y")
        check_out = datetime.strptime("12/05/2025", "%m/%d/%Y")
        self.item2 = CartItem(self.roomChoices.single_queen, check_in, check_out)
        self.cartService.cartItems.append(self.item2)

    def removeItem(self, index):
        removed = self.cartService.removeCartItem(index)


test = TestCartService()
test.printIt()
test.addItem1()
test.printIt()
test.addItem2()
test.printIt()
test.removeItem(0)
test.printIt()


cart = CartService()
