import database

# ----------View all customers function----------
def view_customers():
    rows = database.find_all()
    
    print()
    print(f"{'Customer ID':<13}{'Name':<30}{'City':<30}{'State':<10}{'Phone number'}")
    print(f"{'-----------':<13}{'----':<30}{'----':<30}{'-----':<10}{'------------'}")

    for val in rows:
        print(f"{val[0]:<13}{val[1]:<30}{val[2]:<30}{val[3]:<10}{val[4]}")
        print(f"{'-----------':<13}{'----':<30}{'----':<30}{'-----':<10}{'------------'}")

# ----------Search for customer by name----------
def search_by_name():
    user_input = input('Search by name: ')
    result = database.find_one(user_input)

    print()
    for i in result:
         the_result = (f"ID: {i[0]}\n----------\nName: {i[1]}\n----------\nStreet Address: {i[2]}\n---------\nCity: {i[3]}\n----------\nState: {i[4]}\n----------\nPostal Code: {i[5]}\n----------\nPhone: {i[6]}\n----------\nEmail: {i[7]}")

    return the_result

# ----------Update customers----------
def update_customer():

    view_customers()

    print()
    user_id_input = int(input("Please enter the Customer ID for the customer you would like to update:"))

    id_data = database.find_one_from_id(user_id_input)
    values = [id_data[0][0],id_data[0][1],id_data[0][2],id_data[0][3],id_data[0][4],id_data[0][5],id_data[0][6],id_data[0][7]]
    
    for i, value in enumerate(values):
        print(f'Field {i}: {value}')

    while True:
        print()
        value_to_update = int(input('What field number would you like to update? please just choose a number: '))
        print()

        print(f"\n{values[value_to_update]}\n")

        updated_value = input('What would you like to update the value to be? ')

        print(f"\nthe field of {values[value_to_update]} will be changed to {updated_value}\n")
        final_choice = input('are you sure you want to update the values above?(Y or N): ').lower()

        if final_choice == 'y':
            values[value_to_update] = updated_value
            database.update(values)
            return

# ----------To add a customer----------
def add_a_customer():
    while True:
        add_name = input('What is the new customers name: ')
        add_street_address = input('What is the new customers street address: ')
        add_city = input('What is the new customers city: ')
        add_state = input('What is the new customers state: ')
        add_zip = input('What is the new customers zip code: ')
        add_phone = input('What is the new customers phone number: ')
        add_email = input('What is the new customers email: ')

        new_customer = [add_name, add_street_address, add_city, add_state, add_zip, add_phone, add_email]

        add_new_user = input(f'{new_customer}\nAre you sure you would like to add this customer?(Y or N or [Q]uit): ').lower()
                
        if add_new_user == 'y':
            database.add(new_customer)
            return 'Action Complete'
        elif add_new_user == 'q':
            break
        else:
            print('Ok try again')

# ----------to remove a customer----------
def remove_a_customer():
    rows = database.find_all()

    for val in rows:
        print(f"{val[0]:<13}{val[1]:<30}")
        print(f"{'-----------':<13}{'----':<30}")

    removed_customer = int(input('What customer would you like to remove?(SELECT BY ID): '))
    
    saved = database.find_one_from_id(removed_customer)
    print(f"\n{saved}\n")

    remove = input(f'Are you sure you would like to remove "{saved[0][1]}" from the data base? THIS IS PERMANENT(Y or N): ').lower()

    if remove == 'y':
       return database.delete(removed_customer)