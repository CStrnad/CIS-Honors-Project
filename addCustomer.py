# File_Name: addCustomer.py
# Author: Christopher Strnad
# Purpose: Create a program that
#          allows the user to add
#          a customer to their system.

print("         A1 Party Suppliers Order Entry System")

str_cust_name = str(input("Enter Customer Name: "))
print('Customer Name:', str_cust_name)
str_address = str(input('Enter Address:'))
print('Address: ', str_address)
str_address_two = str(input('Enter City, State, zip: '))
print('City, State, zip: ', str_address_two)
affirmation_check = str(input('Click "Y" to add customer: '))

if str(affirmation_check) == 'y' or 'Y' or 'yes' or 'Yes':
    print('Added to registry.')

