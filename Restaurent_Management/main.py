from food_item import FoodItem
from menu import Menu
from Users import Customer, Admin, Employee
from restaurent import Restaurent
from order import Order

vuter_bari_restaurent = Restaurent("Vuter Bari Restaurement")
def customer_menu():
    name = input("Enter Your Name : ")
    phone = input("Enter Your Phone : ")
    email = input("Enter Your Email : ")
    address = input("Enter Your Address : ")
    customer = Customer(name=name, phone=phone, email=email, address=address)
    
    while True:
        print(f"Welcome {customer.name}!!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")
        
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            customer.view_menu(vuter_bari_restaurent)
        elif choice == 2:
            item_name = input("Enter item name : ")
            item_quantity = int(input("Enter item quantity : "))
            customer.add_to_cart(vuter_bari_restaurent, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Input")


def admin_menu():
    name = input("Enter Your Name : ")
    phone = input("Enter Your Phone : ")
    email = input("Enter Your Email : ")
    address = input("Enter Your Address : ")
    admin = Admin(name=name,  phone=phone,email=email, address=address)
    
    while True:
        print(f"Welcome {admin.name}!!")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Item")
        print("6. Exit")
        
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            item_name = input("Enter Item Name : ")
            item_price = int(input("Enter Item Price : "))
            item_quantity = int(input("Enter Item Quantity : "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(vuter_bari_restaurent, item)
            
        elif choice == 2:
            name = input("Enter employee name : ")
            phone = input("Enter employee phone : ")
            email = input("Enter employee email : ")
            designation = input("Enter employee designation : ")
            age = input("Enter employee age : ")
            salary = input("Enter employee salary : ")
            address = input("Enter employee address : ")
            employee = Employee(name, email, phone, address,
                               age, designation, salary)
            admin.add_employee(vuter_bari_restaurent, employee)
        elif choice == 3:
            admin.view_employee(vuter_bari_restaurent)
        elif choice == 4:
            admin.view_menu(vuter_bari_restaurent)
        elif choice == 5:
            item_name = input("Enter item name : ")
            admin.remove_item(vuter_bari_restaurent, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid Input")

while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input!!")