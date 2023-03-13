import sqlite3
connection = sqlite3.connect('dp_customers.db')
cursor = connection.cursor()


# ------------------------------FIND ONE BY NAME QUERY------------------------------
def find_one(value):
  parsed_value = f"%{value}%"
  query = 'SELECT * From customers WHERE name LIKE ?'
  results =  cursor.execute(query, (parsed_value,)).fetchall()
  return results 

# ------------------------------FIND ONE BY ID QUERY------------------------------
def find_one_from_id(value):
  query = 'SELECT * From customers WHERE customer_id = ?'
  results =  cursor.execute(query, (value,)).fetchall()
  return results 

# ------------------------------SEARCH ALL CUSTOMERS QUERY------------------------------
def find_all():
  query = 'SELECT customer_id, name, city, state, phone FROM customers ORDER BY name'
  rows = cursor.execute(query).fetchall()
  return rows

# ------------------------------ADD NEW CUSTOMER QUERY------------------------------
def add(input):
  values = (input[0], input[1], input[2], input[3], input[4], input[5], input[6])

  query = 'INSERT into CUSTOMERS (name, street_address, city, state, postal_code, phone, email) values (?, ?, ?, ?, ?, ?, ?)'
  cursor.execute(query, values)
  connection.commit()

# ------------------------------UPDATE CUSTOMER QUERY------------------------------
def update(value):

  query = 'UPDATE Customers SET name = ?, street_address = ?, city = ?, state = ?, postal_code = ?, phone = ?, email = ? WHERE customer_id = ?'

  values = (value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[0])
  cursor.execute(query, values)

  user_input = input('Are you sure??(Y or N): ' )

  if user_input == 'y':  
    connection.commit()
    return

# ------------------------------REMOVE CUSTOMER QUERY------------------------------
def delete(value):
  query = 'DELETE FROM customers WHERE customer_id = ?'

  cursor.execute(query, (value,))
  final_check = input('ARE YOU SURE!?!?!(Y or N): ').lower()

  if final_check == 'y':
    connection.commit()