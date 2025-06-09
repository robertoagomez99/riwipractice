This is a store inventory file where the program starts by asking you for the quantity of products you want to buy, ranging from 5 to 10 products in the inventory system. 
The program will ask for a product, the price of that product, and then the quantity. The program is able to detect if there are duplicate product names.
When that happens, the program does not allow the duplicate name to be registered and requests that it be changed.
The program presents the following options where each option has its function done in the utils
You have to select one of the numbers shown below or else it will return you until the available numbers come out.
1. Add product
To add the product, it is taken into account that the product to be entered is not in the database to avoid duplication
where the user is asked for their name to verify if they are in the database
2. View product
To view the product you just have to write the name of the product you want to consult.
3. Update quantity
To update the quantity you only need the name of the product you want to update.
4. Update price
To update the price, you only need to enter the name of the product and enter the new price.
5. Delete the product
To delete the product you just have to write the name of the product and confirm if you want to delete the product or not so that you have the option
6. Calculate the total value
Here is an example of what it looks like with option 7
For the calculation, the following operation is performed for each product "price*quantity". I use the lambda function to multiply each product, its price and quantity.
                    INVENTORY INVOICE                     
Product                Price      Quantity     Total    
x                   $   3.00       3.0     $   9.00   
Y                   $  20.00       5.0     $  100.00  
P                   $   2.00       7.0     $  14.00   
M                   $   3.00       6.0     $  18.00   
U                   $   3.00       5.0     $  15.00   
                                            Subtotal:       $156.00
                                            IVA (19%):      $29.64
                                            Grand total:    $185.64

7. Exit
