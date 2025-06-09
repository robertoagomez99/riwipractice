inventory = {}
#Valid that the product name is not duplicated in the inventory database
def valid_name(index):
    while True:
        name = input(f"Enter the product name {index}: ").strip().capitalize()
        if not name:
            print("The name cannot be empty")
        elif name in inventory:
            print(f"The product {name} is already in the database")
        else:
            return name
#I do this validation because to change the name of the program a different input is requested.
def valid_change_name(index):
    name = input(f"Enter the new product name {index} of: ").strip().capitalize()
    if not name:
        print("The name cannot be empty")
    elif name in inventory:
        print(f"The product {name} is already in the database")
    else:
        return name
#I validate the price so that the number is not negative and it is float since there may be prices that are not integers.
def valid_price(message):
    while True:
        try:
            value = float(input(message))
            if value >0:
                return value
            print(f"The value {value} cannot be correct. Try a positive number.")
        except ValueError:
            print("You entered the wrong number. Please try again.")

#I validate the amount so that the number is not negative and it is a float since there may be amounts that are not integers.
def valid_quantity(message):
    while True:
        try:
            value = float(input(message))
            if value>0:
                return value
            print(f"The value {value} cannot be. Try a positive number.")
        except ValueError:
            print("You entered the wrong number. Please try again.")
#Since the program asks for 5 to be entered initially, I make a range from 5 to 10 so that a permanent loop is not created and the program is not so large.
def enter_initial_value():
    while True:
        try:
            n = int(input("Enter the quantity of product you want to enter, 5 to 10 products are allowed: "))
            if 5<=n<=10:
                for i in range(n):
                    name = valid_name(i+1)
                    price = valid_price(f"Enter the price of {name}: ")
                    quantity = valid_quantity(f"Enter the amount of {name}: ")
                    inventory[name] = (price,quantity)
                    print(f"The product {name} was added")
                break
            else:
                print("The quantity should be between 5 to 10.")
        except ValueError:
            print("You entered the number incorrectly. Please try again.")
#I create a function to add a product in which you cannot add a product name that already exists in the database.
def add_product():
    name = input("Enter the product name (existen product): ").strip().capitalize() #you have to put an exists product data
    if not name or name in inventory:
        name = valid_name(len(inventory)+1)
        price = valid_price(f"Enter the price of {name}:" )
        quantity = valid_quantity(f"Enter the quantity of {name}: ")
        inventory[name] = (price,quantity)
        print(f"{name} was added successfully")
#The user can also search for a specific product by asking for the name of the product they want to search for, then enter its price and quantity.
def view_product():
    name = input("Enter the product name: ").strip().capitalize()
    product = inventory.get(name)
    if product:
        price,quantity = product
        print(f"Product:{name}\nPrice:${price}\nQuantity:{quantity}")
#The user can change or update the quantity of the product by entering the name of the product.
def update_quantity():
    name = input("Enter the product name:").strip().capitalize()
    if name in inventory:
        new_quantity = valid_quantity(f"Enter the quantity of {name}:")
        price = inventory[name][0]
        inventory[name] = (price,new_quantity)
        print(f"The quantity of {name} was updated to {new_quantity}")

#The user can update or change the price of the product, just write the product you want to change the price of.
def update_price():
    name = input("Enter the product name:").strip().capitalize()
    if name in inventory:
        new_price = valid_price(f"Enter the price for {name}:")
        quantity = inventory[name][1]
        inventory[name] = (new_price, quantity)
        print(f"The price of {name} was updated to {new_price}")

#The program gives you the possibility to delete the product, first it asks you the name of the product, 
# then if you want to delete the product and gives you 2 options Yes/No, if you click Yes it deletes the product 
# from the database and if not it returns you to the interactive menu   
def delete_product():
    name = input("Enter the product name: ").strip().capitalize()
    if name in inventory:
        print(f"{name} was found.")
        asked = input(f"Do you want to delete {name} 'Si' / 'No': ").strip().capitalize()
        if asked=="Si":
            if inventory.pop(name,None):
                print(f"Product {name} removed")
            elif asked=="No":
                return
        else:
            print("Ingrese un caracterer valido como 'Si' / 'No'")
    else:
        print(f"Product {name} not found")
#To calculate the total cost of each product we multiply price * quantity and use a lambda function, to make it a little more realistic we add IVA
    
def calculate_total_value():
    if not inventory:
        print("There is no product")
        return
    print(f"{'INVENTORY INVOICE':^58}")
    print(f"{'Product':<20}{'Price':^12}{'Quantity':^12}{'Total':^12}")
    
    total_sum = 0
    calculate = lambda p,q:p*q
    for name, (price,quantity) in inventory.items():
        total = calculate(price,quantity)
        total_sum +=total
        print(f"{name:<20}${price:^10.2f}{str(quantity):^12}${total:^10.2f}")
#We created a mini table so that you can see the product name, price, quantity, total cost and it is also shown as a subtotal because it shows later 
# that it has to be multiplied by 19% IVA
    iva = total_sum * 0.19
    total_with_iva = total_sum + iva
    print(" " * 44 + f"Subtotal:       ${total_sum:.2f}")
    print(" " * 44 + f"IVA (19%):      ${iva:.2f}")
    print(" " * 44 + f"Grand total:    ${total_with_iva:.2f}")
