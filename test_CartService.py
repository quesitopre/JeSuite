import unittest #The test framework
from cart_Service import CartService, CartItem
from room import Room
from datetime import datetime
from roomSearch import roomSearch

class TestCartService(unittest.TestCase):

    def setUp(self):
        self.cartService = CartService()
        self.roomChoices = roomSearch()

    def printIt(self):
        print(self.cartService.cartItems) 

    def test_addItem1(self):
        cart = CartService()
        check_in = datetime.strptime("12/02/2025", "%m/%d/%Y")
        check_out = datetime.strptime("12/07/2025", "%m/%d/%Y")
        item1 = CartItem(self.roomChoices.single_king, check_in, check_out) #create a new cart item
        self.cartService.addCartItem(item1,check_in, check_out)

        self.assertEqual(len(self.cartService.cartItems),1)


    def test_addItem2(self):
        check_in = datetime.strptime("12/03/2025", "%m/%d/%Y")
        check_out = datetime.strptime("12/05/2025", "%m/%d/%Y")
        item2 = CartItem(self.roomChoices.single_queen, check_in, check_out)
        
        self.cartService.addCartItem(item2,check_in,check_out)

        self.assertEqual(len(self.cartService.cartItems),1)

       
    def test_removeItem(self):
        check_in = datetime.strptime("12/02/2025", "%m/%d/%Y")
        check_out = datetime.strptime("12/07/2025", "%m/%d/%Y")
        item1 = CartItem(self.roomChoices.single_king, check_in, check_out) #create a new cart item
        self.cartService.addCartItem(item1,check_in,check_out)
    
        self.cartService.removeCartItem(0)
        self.assertEqual(len(self.cartService.cartItems),0)

    if __name__ == '__main__':
        unittest.main()