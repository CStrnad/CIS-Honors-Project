# File_Name: mainmenu.py
# Author: Christopher Strnad
# Purpose: Create a program menu for the user


def display_customers(customerFileName):
    lst_customers = []
    print("           A1 Party Suppliers Order Entry System")
    print("                   List of Customers")
    print("---------------------------------------------------------------------")
    print("Name                 Address                        City, State, Zip")
    print("---------------------------------------------------------------------")
    user_file = open(customerFileName)  # Opens user_answers.txt

    one_line = user_file.readline()  # Reads initial line of text file.

    while (one_line != ""):  # Loop to read file line by line and strip \n to append to array.
        one_line_nl = one_line.strip("\n")
        lst_customers.append(one_line_nl)
        one_line = user_file.readline()

    print(lst_customers[0], "\t\t", lst_customers[1], "\t\t", lst_customers[2])

    for i in range(3, 10, 3):   #TODO finish setting range
        print(lst_customers[i], "\t", lst_customers[i+1], "\t\t", lst_customers[i+2])
        i += 3

    user_file.close()
    return;


def add_customer(customerFileName):
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


def delete_customers(customerFileName):
    print('Not implemented yet.')
    return;


def main_menu_get():
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

    if (int_menu_usr_input == 1):   #If user inputs 1, goto display_customers
        display_customers()

    if (int_menu_usr_input == 2):   #If user inputs 2, goto add_Customer
        add_customer()

    if (int_menu_usr_input == 3):   #If user inputs 3, goto delete_customers
        delete_customers()

def main():
    customerFileName = str("customers.txt")
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

    if (int_menu_usr_input == 1):   #If user inputs 1, goto display_customers
        display_customers(customerFileName)

    if (int_menu_usr_input == 2):   #If user inputs 2, goto add_Customer
        add_customer(customerFileName)

    if (int_menu_usr_input == 3):   #If user inputs 3, goto delete_customers
        delete_customers(customerFileName)

    return customerFileName;


main()