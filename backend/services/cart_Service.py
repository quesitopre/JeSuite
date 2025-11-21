# Cart service
'''cart_Service manages the shopping cart functionality after a customer selects rooms to book.
mad by Citlalli Martinez '''

from typing import List,Dict, Optional
from datetime import datetime

class CartItem:
    '''constructor for cart item'''
    def __init__(self,room, check_in,check_out):
        self.room = room 
        self.check_in = check_in
        self.check_out = check_out
        self.nights = (check_out - check_in).days
        self.cart_items: List[Dict]= [] #Empty list to hold items in cart
'''class to manage the shopping cart functionality'''
class CartService:
    def __init__(self):
        '''initialize the cart'''
        self.cartItems: List[CartItem] = []  # List to hold cart items
        self.tax_rate: float = 0.1  #tax rate of 10%
        self.initialized = True 

#cart function to add item to cart
    def addCartItem(self, room,check_in:datetime, check_out:datetime):
       #Need an append() function here
       '''add a room to the cart'''
       new_cartItem = CartItem(room, check_in, check_out) #create a new cart item
       self.cartItems.append(new_cartItem)


#cart function to remove item from cart
def removeCartItem( self,index: int)-> bool: #boolean to indicate if item was removed sucessfully or not 
    '''Remove an item from thge cart by index'''
    if 0 <= index < len(self.cartItems):
        del self.cartItems[index]
        return True
    return False


#cart function to clear ALL items in the cart
def clearCart(self):    
    '''Clear all items from the cart'''
    self.cartItems.clear() #clear list of items  in cart
    
# cart function to calculate the total price of items in the cart
def calculateCartTotal(self) -> float:
    '''Calculate the total price of items in the cart including tax'''
    subtotal = 0.0 #counter for subtotal
    for item in self.cartItems:
        subtotal +=item.room.price_per_night * item.nights* (1 + self.tax_rate)
    return round(subtotal, 2) #round to 2 decimal places

# need to return number of items in cart and details of items in cart