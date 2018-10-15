# File_Name: mainmenu.py
# Author: Christopher Strnad
# Purpose: Create a program menu for the user


def display_customers():
    print("           A1 Party Suppliers Order Entry System")
    print("                   List of Customers")
    print("---------------------------------------------------------------------")
    print("Name                 Address                        City, State, Zip")
    print("---------------------------------------------------------------------")
    return;


def add_customer():
    print("         A1 Party Suppliers Order Entry System")

    str_cust_name = str(input("Enter Customer Name: "))  # Request the Customers name.
    str_address = str(input('Enter Address:'))  # Request the address of the customer.
    str_address_two = str(input('Enter City, State, zip: '))  # Request city, state, and zip from Customer.

    # Repeat information back to User.
    print('\n')
    print('Customer Name:', str_cust_name)
    print('Address: ', str_address)
    print('City, State, zip: ', str_address_two)

    print('\n')
    affirmation_check = str(
        input('Enter "Y" to add customer: '))  # Request the user to confirm the data entered is correct.

    if str(affirmation_check) == 'y' or 'Y' or 'yes' or 'Yes':
        print('Added to registry.')
    return;


def delete_customers():
    print('Not implemented yet.')
    return;


#Create command line memo.
print('A1 Party Suppliers Order Entry System')
print('\n')  # Print empty line
print('1.     Display all customers')
print('2.     Add a new customer')
print('3.     Delete Customer')
print('4.     EXIT')
print('\n')  # Print empty line

int_menu_usr_input = int(input('Enter selection. Must be a number 1-4 : '))   #Request input from user.

while not int_menu_usr_input < 5 or not int_menu_usr_input > 0:   #Validate that inputs are within menu range.
    print('Error!', int_menu_usr_input, 'is not a valid input.')
    int_menu_usr_input = int(input('Enter selection. Must be a number 1-4 : '))

print("You've entered", int_menu_usr_input)

if (int_menu_usr_input == 1):
    display_customers()

if (int_menu_usr_input == 2):
    add_customer()

if (int_menu_usr_input == 3):
    delete_customers()

''' 
1. Create the Main Menu Screen - mainmenu.py
Create a program called mainmenu.py to display the following screen. User input is highlighted in yellow:


              A1 Party Suppliers Order Entry System


                1.        Display all Customers
                2.        Add a new customer
                3.        Delete Customer
                4.        EXIT


Enter selection. Must be a number 1-4 : 4
'''  # Prompt
