from utils import *
print("------Welcome to the inventory system--------")

enter_initial_value()
flag = False
while not flag:
    print("\n-- Management manual")
    print("\n1. Add product")
    print("\n2. View product ")
    print("\n3. Update quantity")
    print("\n4. Update price")
    print("\n5. Delete the product")
    print("\n6. Calculate the total value")
    print("\n7. Exit")

    option = input("\nSelect an option: ")

    match option:
        case "1":
            add_product()
        case "2":
            view_product()
        case "3":
            update_quantity()
        case "4":
            update_price()
        case "5":
            delete_product()
        case "6":
            calculate_total_value()
        case "7":
            print("Thank you for using our services")
            flag = True
        case _:
            print("Invalid entry. Please try again.")
        