import sqlite3
connection = sqlite3.connect('dp_customers.db')
cursor = connection.cursor()

def find_one(value):
  parsed_value = f"%{value}%"
  query = 'SELECT * From customers WHERE name LIKE ?'
  results =  cursor.execute(query, (parsed_value,)).fetchall()
  return results 

def find_one_from_id(value):
  query = 'SELECT name From customers WHERE customer_id = ?'
  results =  cursor.execute(query, (value,)).fetchall()
  return results 

def find_all():
  query = 'SELECT customer_id, name, city, state, phone FROM customers ORDER BY name'
  rows = cursor.execute(query).fetchall()
  return rows



def add():
  add_name = input('What is the new customers name: ')
  add_street_address = input('What is the new customers street address: ')
  add_city = input('What is the new customers city: ')
  add_state = input('What is the new customers state: ')
  add_zip = input('What is the new customers zip code: ')
  add_phone = input('What is the new customers phone number: ')
  add_email = input('What is the new customers email: ')

  values = (add_name, add_street_address, add_city, add_state, add_zip, add_phone, add_email)

  query = 'INSERT into CUSTOMERS (name, street_address, city, state, postal_code, phone, email) values (?, ?, ?, ?, ?, ?, ?)'
  cursor.execute(query, values)
  final = input(f'are you sure you want to add {values} to your database?(Y or N): ').lower()

  if final == 'y':
    connection.commit()
    return True
  else:
    another_input = input('would you like to quit this process? (Y or N)').lower()
    if another_input == 'y':
      return None
    else:
      print("sucks to suck, start over")
      return False




def update(input1, input2):
  user_input = input('what fields would you like to update: ')
  update_values = input('what are those values respectivly: ')
  query = 'UPDATE Customers SET name = ?, city = ? WHERE name = ?'

  cursor.execute(query, (input1,), (input2,))
  connection.commit()
  return


def delete(value):
  query = 'DELETE FROM customers WHERE customer_id = ?'

  cursor.execute(query, (value,))
  final_check = input('ARE YOU SURE!?!?!(Y or N): ').lower()

  if final_check == 'y':
    connection.commit()
  
