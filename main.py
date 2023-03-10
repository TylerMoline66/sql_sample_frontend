import functions
import os


options = ['View all customers', 'Search customers', 'Add new customer','Remove a customer', 'Quit']

while True:
    # os.system('clear')

    print("\nCustomer Database\n---------------------------\n")
    for i, val in enumerate(options, start=1):
      print(f"{i}. {val}")
    print('\n---------------------------\n')
    
    user_input = input('What would you like to do? ')
    print()

    if user_input == '1':
       functions.view_customers()
    elif user_input == '2':
      print(functions.search_by_name())
    elif user_input == '3':
       functions.add_a_customer()
    elif user_input == '4':
       functions.remove_a_customer()
    else:
      break
      