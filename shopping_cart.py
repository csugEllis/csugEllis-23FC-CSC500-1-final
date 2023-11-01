class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        
    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="October 31, 2023"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        removed = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                removed = True
                break
        if not removed:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                if item.item_quantity > 0:
                    cart_item.item_quantity = item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum([item.item_quantity for item in self.cart_items])

    def get_cost_of_cart(self):
        return sum([item.item_price * item.item_quantity for item in self.cart_items])

    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    choice = ''
    while choice != 'q':
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option:\n")

        # Output shopping cart
        if choice == 'o':
            cart.print_total()
        # Output items' descriptions
        elif choice == 'i':
            cart.print_descriptions()
        # Add item to cart
        elif choice == 'a':
            print("\nADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(item)
        # Remove item from cart
        elif choice == 'r':
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)
        # Change item quantity
        elif choice == 'c':
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            # Create a new ItemToPurchase object with the updated quantity
            item = ItemToPurchase(item_name, item_quantity=quantity)
            cart.modify_item(item)
        # Invalid option handling
        elif choice != 'q':
            print("Invalid option, please try again.")

if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print("\nCustomer name:", customer_name)
    print("Today's date:", current_date)

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)
