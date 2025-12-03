# Cart service
'''cart_Service Module manages the shopping cart functionality after a customer selects rooms to book.
Through these functionalities a customer may add, remove, or clear their cart. the cart will also calculate 
their total with taxes.

made by Citlalli Martinez 11/08/2025. '''

from typing import List,Dict, Optional
from datetime import datetime

class CartItem:
    """ Class to represent an item in the shoppping cart.

    Attributes:
        room: The room object being added to the cart.
        check_in(datetime): The check-in date for the room booking.
        check_out(datetime): The check-out date for the room booking.
        nights(int): The number of nights for the booking.
    """
    @property
    def __init__(self,room, check_in,check_out):
        """A constructor to initialize a cart item with room and check-in & check-out dates.

        Args:
            room (room): The type of room(double, king, queen, suite) to add to the cart.
            check_in (datetime): The check-in date.
            check_out (datetime): The check-out date.
        """
        self.room = room 
        self.check_in = check_in
        self.check_out = check_out
        self.nights = (check_out - check_in).days

        def getItemTotal(self)-> float:
            """ Calculate the total price for this cart item.""""
            return self.room.price_per_night * self.nights

class CartService:
    """''Class to manage the shopping cart functionality for hotel room bookings.

    Attributes:
        cartItems (List[CartItem]): A list to hold items added to the cart.
        tax_rate (float): The tax rate applied to the total price.
    """
    def __init__(self):
        """constructor to initialize an empty cart and set the tax rate to 10%"""
        self.cartItems: List[CartItem] = []  # List to hold cart items
        self.tax_rate: float = 0.1  #tax rate of 10%
        self.initialized = True 

#cart function to add item to cart
    def addCartItem(self, room,check_in:datetime, check_out:datetime):
       #Need an append() function here
        """Add a room to the shopping cart.

        Args:
            room (room): A room object to add to the cart.
            check_in (datetime): The check-in date.
            check_out (datetime): The check-out date.
        """
        new_cartItem = CartItem(room, check_in, check_out) #create a new cart item
        self.cartItems.append(new_cartItem)


#cart function to remove item from cart
def removeCartItem( self,index: int)-> bool: #boolean to indicate if item was removed sucessfully or not
    """Removes an item from the cart by its index position.

    Args:
        index (int): The index of the item to be removed from the cart.

    Returns:
        bool:  True if the item was successfully removed or else false.
    """
    if 0 <= index < len(self.cartItems):
        del self.cartItems[index]
        return True
    return False


#cart function to clear ALL items in the cart
def clearCart(self):    
    """Remove all items from the shopping cart with .clear() function.
    """
    '''Clear all items from the cart.'''
    self.cartItems.clear() #clear list of items  in cart
    
def isCartEmpty(self) -> bool:
    """Check if the cart is empty."""
    return len(self.cartItems) == 0 #return true if cart is empty


def calculateCartTotal(self) -> float:
    """Calculate the total price of all items in the cart with tax.

    Iterates through all the cart items and multiplies the price of the room with 
    the number of nights and the tax of 10%. Each iteration adds to the subtotal. Which is 
    rounded to 2 decimal places.

    Returns:
        float:  The total price of items in the cart including tax.
    """
    '''Calculate the total price of items in the cart including tax'''
    subtotal = 0.0 #counter for subtotal
    for item in self.cartItems:
        subtotal +=item.room.price_per_night * item.nights* (1 + self.tax_rate)
    return round(subtotal, 2) #round to 2 decimal places

def getItemCount(self) -> int:
    """Get the number of items in the cart.

    Returns:
        int: The number of items currently in the cart.
    """
    return len(self.cartItems)

