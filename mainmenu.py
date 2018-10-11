# File_Name: mainmenu.py
# Author: Christopher Strnad
# Purpose: Create a program menu for the user

print('A1 Party Suppliers Order Entry System')
print('\n')  # Print empty line
print('1.     Display all customers')
print('2.     Add a new customer')
print('3.     Delete Customer')
print('4.     EXIT')
print('\n')  # Print empty line

int_menu_usr_input = int(input('Enter selection. Must be a number 1-4 : '))

while not int_menu_usr_input < 5 or not int_menu_usr_input > 0:
    print('Error!', int_menu_usr_input, 'is not a valid input.')
    int_menu_usr_input = int(input('Enter selection. Must be a number 1-4 : '))

print("You've entered", int_menu_usr_input)

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
