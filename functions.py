import database

# View all customers function
def view_customers():
    rows = database.find_all()
    
    print()
    print(f"{'Customer ID':<13}{'Name':<30}{'City':<30}{'State':<10}{'Phone number'}")
    print(f"{'-----------':<13}{'----':<30}{'----':<30}{'-----':<10}{'------------'}")

    for val in rows:
        print(f"{val[0]:<13}{val[1]:<30}{val[2]:<30}{val[3]:<10}{val[4]}")
        print(f"{'-----------':<13}{'----':<30}{'----':<30}{'-----':<10}{'------------'}")


      

# Search for customer by name
def search_by_name():
    user_input = input('Search by name: ')
    result = database.find_one(user_input)

    print()
    for i in result:
         the_result = (f"ID: {i[0]}\n----------\nName: {i[1]}\n----------\nStreet Address: {i[2]}\n---------\nCity: {i[3]}\n----------\nState: {i[4]}\n----------\nPostal Code: {i[5]}\n----------\nPhone: {i[6]}\n----------\nEmail: {i[7]}")

    return the_result



# Update customers
def update_customer():
    user_id_input = input("Please enter the Customer ID for the customer you would like to update:")
    if user_id_input.isalpha():
        print("Please enter a valid number")
        return         
    if user_id_input != None:
        id_data = list(cursor.execute("SELECT * FROM Customers WHERE customer_id = ?",(user_id_input,)).fetchone())
        values = [{id_data[0]},{id_data[1]},{id_data[2]},{id_data[3]},{id_data[4]},{id_data[5]},{id_data[6]},{id_data[7]}]
        
        print(f'\n1:  NAME:           {id_data[1]}\n2:  STREET ADDRESS: {id_data[2]}\n3:  CITY:           {id_data[3]}\n4:  STATE:          {id_data[4]}\n5:  POSTAL CODE:    {id_data[5]}\n6:  PHONE:          {id_data[6]}\n7:  EMAIL:          {id_data[7]}\n')
        field_to_update = input('\nPlease enter the number of the field you would like to update:\n>>>')
        if field_to_update.isalpha():
            print("Please enter a valid number:")
            return
        elif field_to_update =='1':
            id_data[1] = input("New name:")
        elif field_to_update =='2':
            id_data[2] = input("New address:")
        elif field_to_update =='3':
            id_data[3] = input("New city:")
        elif field_to_update =='4':
            id_data[4] = input("New state:")
        elif field_to_update == '5':
            id_data[5] = input("New postal code:")
        elif field_to_update == '6':
            id_data[6] = input("New phone:")
        elif field_to_update == '7':
            id_data[7] = input("New email:")
        else:
            return(id_data)
    
        updated_values = id_data[1:]
        updated_values.append(id_data[0])
      
    query = f'UPDATE Customers SET name = ?, street_address = ?, city = ?, state=?, postal_code = ?, phone = ?, email=?  WHERE customer_id = ?'

    cursor.execute(query,updated_values)
    connection.commit()
    print(f"Customer ID: {user_id_input} has been updated.")


# To add a customer
def add_a_customer():
    while True:
        result = database.add()
        if result == True or result == None:
            return 'Action Complete'


# to remove a customer
def remove_a_customer():
    rows = database.find_all()

    for val in rows:
        print(f"{val[0]:<13}{val[1]:<30}")
        print(f"{'-----------':<13}{'----':<30}")

    removed_customer = int(input('What customer would you like to remove?(SELECT BY ID): '))
    
    saved = database.find_one_from_id(removed_customer)
    print(saved)

    remove = input(f'Are you sure you would like to remove {saved} from the data base? THIS IS PERMANENT(Y or N): ').lower()

    if remove == 'y':
       return database.delete(removed_customer)

