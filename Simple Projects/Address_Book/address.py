import sqlite3
import datetime

conn = sqlite3.connect("address_book.db")
cur = conn.cursor()

print("""
1: View Address Book
2: Create New Contact's Information
3: Edit Existing Contact's Information
4: Delete Contact
5: Quit
""")

user_choice = input("Please Select Your Choice (1-5): ")

if user_choice == '1':
  cur.execute("SELECT * FROM Address")
  address = cur.fetchall()
  for add in address:
    print(add)

elif user_choice == '2':
  first_name = input("Please Input Contact's First Name: ")
  last_name = input("Please Input Contact's Last Name: ")
  phone_number = input("Please Input Contact's Phone Number: ")
  email = input("Please Input Contact's Email: ")
  street = input("Please Input Contact's Street Address: ")
  city = input("Please Input Contact's City Address: ")
  state = input("Please Input Contact's State Address: ")
  zip_code = input("Please Input Contact's Zip Code: ")
  
  cur.execute("INSERT INTO Address(`First Name`, `Last Name`, `Phone Number`, `Email`, `Street`, `City`, `State`, `Zip Code`) VALUES (?, ? , ? , ? , ? , ? , ?, ?)", 
                (first_name, last_name, phone_number, email, street, city, state, zip_code))

  conn.commit()
  print("New Contact's Information Added")


elif user_choice == '3':
  first_name = input("Please Type in Contact's First Name: ")
  last_name = input("Please Type in Contact's Last Name: ")
  print("""
  1: First Name
  2: Last Name
  3: Phone Number
  4: Email
  5: Street
  6: City
  7: State
  8: Zip Code
  """)
  user_choice = input("Which Information Would You Like to Change (1-8): ")

  if user_choice == '1':
    new_first_name = input("Please Type in Contact's New First Name: ")
    print(f"Updating {first_name} {last_name} to {new_first_name}")
    conn.execute("UPDATE Address SET `First Name` = ? WHERE `First Name` = ? AND `Last Name` = ?", (new_first_name, first_name, last_name))
    conn.commit()
    print(f"{conn.total_changes} row(s) updated.")

  if user_choice == '2':
    new_last_name = input("Please Type in Contact's New Last Name: ")
    print(f"Updating {first_name} {last_name} to {new_last_name}")
    conn.execute("UPDATE Address SET `Last Name` = ? WHERE `First Name` = ? AND `Last Name` = ?", (new_last_name, first_name, last_name))
    conn.commit()
    print(f"{conn.total_changes} row(s) updated.")

  if user_choice == '3':
    new_phone_number = input("Please Type in Contact's Phone Number: ")
    print(f"Updating {first_name} {last_name}'s phone number to {new_phone_number}")
    conn.execute("UPDATE Address SET `Phone Number` = ? WHERE `First Name` = ? AND `Last Name` = ?", (new_phone_number, first_name, last_name))
    conn.commit()
    print(f"{conn.total_changes} row(s) updated.")

  if user_choice == '4':
    new_email = input("Please Type in Contact's Email Add: ")
    print(f"Updating {first_name} {last_name}'s email address to {new_email}")
    conn.execute("UPDATE Address SET `Email` = ? WHERE `First Name` = ? AND `Last Name` = ?", (new_email, first_name, last_name))
    conn.commit()
    print(f"{conn.total_changes} row(s) updated.")

  if user_choice == '5':
    new_street = input("Please Type in Contact's Street Address: ")
    print(f"Updating {first_name} {last_name} to {new_street}")
    conn.execute("UPDATE Address SET `Street` = ? WHERE `First Name` = ? AND `Last Name` = ?", (new_street, first_name, last_name))
    conn.commit()
    print(f"{conn.total_changes} row(s) updated.")

  if user_choice == '6':
    new_city = input("Please Type in Contact's City: ")
    print(f"Updating {first_name} {last_name}'s city to {new_city}")
    conn.execute("UPDATE Address SET `First Name` = ? WHERE `First Name` = ? AND `Last Name` = ?", (new_city, first_name, last_name))
    conn.commit()
    print(f"{conn.total_changes} row(s) updated.")

  if user_choice == '7':
    new_state = input("Please Type in Contact's State: ")
    print(f"Updating {first_name} {last_name}'s state to {new_state}")
    conn.execute("UPDATE Address SET `First Name` = ? WHERE `First Name` = ? AND `Last Name` = ?", (new_state, first_name, last_name))
    conn.commit()
    print(f"{conn.total_changes} row(s) updated.")

  if user_choice == '8':
    new_zip = input("Please Type in Contact's Zip Code: ")
    print(f"Updating {first_name} {last_name}'s email address to {new_zip}")
    conn.execute("UPDATE Address SET `First Name` = ? WHERE `First Name` = ? AND `Last Name` = ?", (new_zip, first_name, last_name))
    conn.commit()
    print(f"{conn.total_changes} row(s) updated.")

elif user_choice == '4':
  first_name = input("Please Type in Contact's First Name: ")
  last_name = input("Please Type in Contact's Last Name: ")
  cur.execute("DELETE FROM Address WHERE `First Name` = ? AND `Last Name` = ?", (first_name, last_name))
  conn.commit()
  print(f"{cur.rowcount} row(s) updated.")


elif user_choice  == '5':
  print("Thank you for choice MBsoft")
  print("Have a lovely rest of your day")

else:
  print("You did not select a correct choice.")
  print("Please try again later.")
  print("Thank you for choice MBsoft")
  print("Have a lovely rest of your day")
