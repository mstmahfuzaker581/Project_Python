class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password)


class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.products = []

    def add_product(self, name, price, stock):
        product = {'name': name, 'price': price, 'stock': stock}
        self.products.append(product)
        print(f"Product {name} added successfully!")


class Store:
    def __init__(self):
        self.customers = []
        self.sellers = []
        self.available_products = [] 

    def sign_up(self, user_type):
        email = input("Enter Your Email: ")
        password = input("Enter Your Password: ")

        if user_type == 'customer':
            self.customers.append(Customer(email, password))
            print(f"Customer {email} signed up successfully!")

        elif user_type == 'seller':
            seller = Seller(email, password)
            self.sellers.append(seller)
            print(f"Seller {email} signed up successfully!")

    def login(self):
        email = input("Enter Your Email: ")
        password = input("Enter Your Password: ")
        user_type = int(input("Press 1 for Customer, Press 2 for Seller: "))

        if user_type == 1:
            for customer in self.customers:
                if customer.email == email and customer.password == password:
                    print("Customer logged in successfully!")
                    return 'customer', customer
            print("Invalid customer credentials.")

        elif user_type == 2:
            for seller in self.sellers:
                if seller.email == email and seller.password == password:
                    print("Seller logged in successfully!")
                    return 'seller', seller
            print("Invalid seller credentials.")
        return None, None

    def main_page(self):
        while True:
            print("\n--> Main Page:")
            print("Press 1 to sign up as Customer")
            print("Press 2 to sign up as Seller")
            print("Press 3 to Login")
            print("Press 4 to Exit")

            choice = input("--> ")

            if choice == '1':
                self.sign_up('customer')
            elif choice == '2':
                self.sign_up('seller')
            elif choice == '3':
                user_type, user = self.login()
                if user_type == 'seller':
                    self.seller_page(user)
                elif user_type == 'customer':
                    self.customer_page(user)
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

    def seller_page(self, seller):
        while True:
            print("\n--> Seller Page:")
            print("Press 1 to add products")
            print("Press 2 to go back to Main Page")

            choice = input("--> ")

            if choice == '1':
                product_name = input("Enter Product Name: ")
                product_price = float(input("Enter Product Price: "))
                product_stock = int(input("Enter Product Stock: "))
                seller.add_product(product_name, product_price, product_stock)
                self.available_products.append(seller.products[-1])  # Add to store's product list
               
            elif choice == '2':
                break
            else:
                print("Invalid choice. Please try again.")

    def customer_page(self, customer):
        while True:
            print("\n--> Customer Page:")
            print("Press 1 to view available products")
            print("Press 2 to buy a product")
            print("Press 3 to go back to Main Page")

            choice = input("--> ")

            if choice == '1':
                self.view_products()
            elif choice == '2':
                self.buy_product()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    def view_products(self):
        if not self.available_products:
            print("No products available.")
        else:
            print("\nAvailable Products:")
            for idx, product in enumerate(self.available_products):
                print(f"{idx + 1}. {product['name']}: Price: {product['price']}, Stock: {product['stock']}")

    def buy_product(self):
        self.view_products()
        if not self.available_products:
            return
        
        try:
            choice = int(input("Enter the number of the product you want to buy: "))- 1
            if 0 <= choice < len(self.available_products):
                product = self.available_products[choice]
                quantity = int(input(f"How many {product['name']} would you like to buy? "))
                if product['stock'] >= quantity:
                    product['stock'] -= quantity
                    print(f"You have successfully bought {quantity} {product['name']}(s).")
                else:
                    print(f"Sorry, only {product['stock']} {product['name']}(s) are available.")
            else:
                print("Invalid product selection.")
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")

store = Store()
store.main_page()
