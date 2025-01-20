class VendingMachine:
    def __init__(self):
        # Step 1: Initialize the vending machine with a dictionary of products
        self.products = {
            "1": {"name": "Hot Chocolate", "category": "Hot Drinks", "price": 7.00, "stock": 10},
            "2": {"name": "Coffee", "category": "Hot Drinks", "price": 3.00, "stock": 10},
            "3": {"name": "Mountain Dew", "category": "Cold Drinks", "price": 2.50, "stock": 10},
            "4": {"name": "Lays", "category": "Snacks", "price": 1.00, "stock": 15},
            "5": {"name": "Kinder Joy", "category": "Snacks", "price": 1.50, "stock": 12},
            "6": {"name": "Beef Jerky", "category": "Snacks", "price": 5.50, "stock": 20},
            "7": {"name": "Milko", "category": "Cold Drinks", "price": 1.50, "stock": 10},
            "8": {"name": "Redbull", "category": "Cold Drinks", "price": 5.00, "stock": 10}
        }

    def display_menu(self):
        # Step 2: Display the menu of products with details such as category, code, price, and stock
        menu = "\nWelcome to Abdul's Vending Machine!\n"
        menu += "Category | Code | Product       | Price ($) | Stock\n"
        menu += "---------------------------------------------------\n"
        for code, details in self.products.items():
            menu += f"{details['category']:10} | {code:4} | {details['name']:12} | {details['price']:>6.2f}   | {details['stock']}\n"
        return menu

    def select_product(self, code):
        # Step 3: Validate the product code and return the corresponding product or None if invalid
        return self.products.get(code, None)

    def process_transaction(self, product, money_inserted):
        # Step 4: Handle the transaction: check stock, validate payment, calculate change, and update stock
        if product["stock"] == 0:
            return "Out of stock", money_inserted, False

        if money_inserted < product["price"]:
            return "Insufficient balance", money_inserted, False

        change = round(money_inserted - product["price"], 2)
        product["stock"] -= 1
        return f"Dispensing {product['name']}. Change: ${change:.2f}\nThank you for your purchase!", change, True

    def run(self):
        # Step 5: Run the vending machine loop to allow users to select products and process payments
        while True:
            print(self.display_menu())

            code = input("Enter product code or 'q' to quit: ").strip()
            if code.lower() == 'q':
                print("Goodbye!")
                break

            product = self.select_product(code)
            if not product:
                print("Invalid product code. Please try again.")
                continue

            print(f"You selected: {product['name']} (${product['price']:.2f})")

            while True:
                try:
                    money_inserted = float(input("Enter amount of money: "))
                    if money_inserted <= 0:
                        print("Please enter a valid amount.")
                        continue

                    message, change, success = self.process_transaction(product, money_inserted)
                    print(message)
                    if success:
                        continue_shopping = input("Would you like to buy anything else? Enter 'yes' to continue or 'no' to quit: ").strip().lower()
                        if continue_shopping != 'yes':
                            print("Thank you for using Abdul's Vending Machine! SEE YOU AGAIN:) BYEE!")
                            return
                        else:
                            break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    # Step 7: Instantiate and run the vending machine
    machine = VendingMachine()
    machine.run()

 