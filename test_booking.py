import unittest
from datetime import datetime
from cart_Service import CartService, CartItem
from room import Room

class TestBookingItems(unittest.TestCase):

    def setUp(self):
        # Create a CartService and dummy rooms for testing
        self.cart_service = CartService()
        self.room1 = Room("King", 1, 170.0, 101, True)
        self.room2 = Room("Queen", 1, 120.0, 102, True)


        self.cart_service.bookingItems = self.bookingItems.__get__(self.cart_service)

    #method copied from booking
    def bookingItems(self):
        self.items = self.cartItems
        self.count = len(self.items)

        if self.count == 0:
            return "No items in cart."
        elif self.count == 1:
            self.item = self.items[0]
            return {
                "room_type": self.item.room.bed_type,
                "check_in": self.item.check_in.strftime("%Y-%m-%d"),
                "check_out": self.item.check_out.strftime("%Y-%m-%d"),
                "nights": self.item.nights,
                "price_per_night": self.item.room.price_per_night
            }
        else:
            return [
                {
                    "room_type": self.items[0].room.bed_type,
                    "check_in": self.items[0].check_in.strftime("%Y-%m-%d"),
                    "check_out": self.items[0].check_out.strftime("%Y-%m-%d"),
                    "nights": self.items[0].nights,
                    "price_per_night": self.items[0].room.price_per_night
                },
                {
                    "room_type": self.items[1].room.bed_type,
                    "check_in": self.items[1].check_in.strftime("%Y-%m-%d"),
                    "check_out": self.items[1].check_out.strftime("%Y-%m-%d"),
                    "nights": self.items[1].nights,
                    "price_per_night": self.items[1].room.price_per_night
                }
            ]

    def test_empty_cart(self):
        result = self.cart_service.bookingItems()
        self.assertEqual(result, "No items in cart.")

    def test_single_item(self):
        check_in = datetime.strptime("12/02/2025", "%m/%d/%Y")
        check_out = datetime.strptime("12/07/2025", "%m/%d/%Y")
        item = CartItem(self.room1, check_in, check_out)
        self.cart_service.cartItems.append(item)

        result = self.cart_service.bookingItems()
        self.assertEqual(result["room_type"], "King")
        self.assertEqual(result["nights"], 5)
        self.assertEqual(result["price_per_night"], 170.0)

    def test_two_items(self):
        check_in1 = datetime.strptime("12/02/2025", "%m/%d/%Y")
        check_out1 = datetime.strptime("12/07/2025", "%m/%d/%Y")
        item1 = CartItem(self.room1, check_in1, check_out1)

        check_in2 = datetime.strptime("12/03/2025", "%m/%d/%Y")
        check_out2 = datetime.strptime("12/05/2025", "%m/%d/%Y")
        item2 = CartItem(self.room2, check_in2, check_out2)

        self.cart_service.cartItems.extend([item1, item2])

        result = self.cart_service.bookingItems()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["room_type"], "King")
        self.assertEqual(result[1]["room_type"], "Queen")

if __name__ == "__main__":
    unittest.main()
