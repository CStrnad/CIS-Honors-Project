# File_Name: addCustomer.py
# Author: Christopher Strnad
# Purpose: Create a program that
#          allows the user to add
#          a customer to their system.

print("         A1 Party Suppliers Order Entry System")

str_cust_name = str(input("Enter Customer Name: "))   #Request the Customers name.
str_address = str(input('Enter Address:'))   #Request the address of the customer.
str_address_two = str(input('Enter City, State, zip: '))   #Request city, state, and zip from Customer.

# Repeat information back to User.
print('\n')
print('Customer Name:', str_cust_name)
print('Address: ', str_address)
print('City, State, zip: ', str_address_two)

print('\n')
affirmation_check = str(input('Enter "Y" to add customer: '))   #Request the user to confirm the data entered is correct.

if str(affirmation_check) == 'y' or 'Y' or 'yes' or 'Yes':
    print('Added to registry.')

