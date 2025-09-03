import os
import csv

FILE_NAME = "rental_car.csv"

def add_details(aadhar_no, name, city,phone_no,age,gender,nationality,date,from_place,to_place,pick_up,car):
    if os.path.exists(FILE_NAME):#Checks if the file already exists
        with open(FILE_NAME, "r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == aadhar_no:
                    print("\nRecord already added, add a new aadhar_no number.")
                    return
    with open(FILE_NAME, "a", newline='') as file:
        writer = csv.writer(file)#This writes one complete row (as a list) to the CSV file.
        writer.writerow([aadhar_no, name, city,phone_no,age,gender,nationality,date,from_place,to_place,pick_up,car])
    print("\nThe record is successfully added.....\n ")

def display_details():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
-    max_name_length = 0
    # First pass to find the max length of the name
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) == 11:
                max_name_length = max(max_name_length, len(row[1]))
    
    # Second pass to display the students
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
          
                print(f"aadhar_no:{row[0]}\nname:{row[1]}\ncity:{row[2]}\nphone_no:{row[3]} \nage:{row[4]} \ngender:{row[5]} \nnationality:{row[6]}\ndate:{row[7]} \nfrom_place:{row[8]}\nto_place:{row[9]}\npick_up:{row[10]}\ncar:{row[11]}\n")
                print("*"*35)
def display_name_and_date():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    max_name_length = 0
    # First pass to find the max length of the name
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) == 11:
                max_name_length = max(max_name_length, len(row[1]))
    

    
    # Second pass to display the students
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            #if len(row) == 3:
                #aadhar_no,name, date = row
                # Print name column with dynamic spaces based on longest name
                print(f"aadhar_no:{row[0]}\nname:{row[1]} \ndate:{row[7]} \n")
                print("*"*35)
def delete_details(aadhar_no):
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    rows = []
    found = False  # Flag to check if the record is found
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Check if the record exists and filter out the student
    with open(FILE_NAME, "w", newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == aadhar_no:
                found = True  # Mark as found if record is deleted
            else:
                writer.writerow(row)
    
    if found:
        print("\nRecord deleted.")
    else:
        print("Record not found.")

def update_details(aadhar_no):
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    
    rows = []
    updated = False  # Flag to check if record is updated
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Check if the record exists before asking for new details
    for row in rows:
        if row[0] == aadhar_no:
            updated = True
            break  # Exit the loop as record is found
    
    if not updated:
        print("Record not found.")
        return  # Exit the function early if the record is not found

    # If record is found, ask for new details
    new_name = input("Enter New Name: ")
    new_city = input("Enter the New City you belong to: ")
    new_phone_no = input("Enter New phone no: ")
    new_age = input("Enter New age: ")
    new_gender = input("Enter New gender: ")
    new_nationality = input("Enter New nationality: ")
    new_date = input("Enter the New date you want car: ")
    new_from_place = input("Enter the new  place from you want to start your journey: ")
    new_to_place = input("Enter the new  place to which you want to end your journey: ")
    new_pick_up = input("Enter the new car pick up time: ")
    new_car = input("Enter new car you would like to have your journey with: ")

    # Update the record
    with open(FILE_NAME, "w", newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == aadhar_no:
                writer.writerow([aadhar_no, new_name, new_city,new_phone_no, new_age,new_gender, new_nationality,new_date,new_from_place, new_to_place,new_pick_up, new_car])
            else:
                writer.writerow(row)
    print("\n Record updated successfully.")

def search_by_aadhar_no(aadhar_no):
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == aadhar_no:
                print(f"aadhar_no:{row[0]}\nname:{row[1]}\ncity:{row[2]}\nphone_no:{row[3]} \nage:{row[4]} \ngender:{row[5]} \nnationality:{row[6]}\ndate:{row[7]} \nfrom_place:{row[8]}\nto_place:{row[9]}\npick_up:{row[10]}\ncar:{row[11]}\n")
                print("*" * 35)
                
                return
    print("costumer record not found.")
def search_by_name(name):
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == name:
                print(f"aadhar_no:{row[0]}\nname:{row[1]}\ncity:{row[2]}\nphone_no:{row[3]} \nage:{row[4]} \ngender:{row[5]} \nnationality:{row[6]}\ndate:{row[7]} \nfrom_place:{row[8]}\nto_place:{row[9]}\npick_up:{row[10]}\ncar:{row[11]}\n")
                print("*" * 35)
                
                return
    print("costumer record not found.")
def clear_all_records():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    with open(FILE_NAME, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["aadhar_no", "Name", "City", "phone_no", "age", "gender", "nationality", "date", "from_place", "to_place", "pick_up", "car"])  # Write only the header
    print("All records have been cleared.")


def initialize_file():
    # Check if file exists, if not, create it with header
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["aadhar_no", "Name", "City","phone_no", "age", "gender", "nationality", "date" , "from_place","to_place","pick_up"  ,"car"])  # Writing the header

# Initialize file with header if it doesn't exist
initialize_file()

while True:
    print("1. Add details ")
    print("2. Display details")
    print("3. Delete details")
    print("4. Update details")
    print("5. Search by aadhar no")
    print("6. Search by name")
    print("7. Display name and date")
    print("8. Clear all records")
    print("9. Exit")
    print("*"*35)
    choice = input("Enter your choice: ")
    if choice == "1":
        aadhar_no = input("Enter aadhar no: ")
        name = input("Enter Name: ")
        city = input("Enter the City you belong to: ")
        phone_no = input("Enter contact no: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        nationality = input("Enter nationality: ")
        date = input("Enter the date you want car: ")
        from_place = input("Enter the place from you want to start your journey: ")
        to_place = input("Enter the place to which you want to end your journey: ")
        pick_up = input("Enter the car pick up time: ")
        car = input("Enter car you would like to have your journey with: ")
        add_details(aadhar_no,name,city,phone_no,age,gender,nationality,date,from_place,to_place,pick_up,car)
    elif choice == "2":
        display_details()
    elif choice == "3":
        aadhar_no = input("Enter aadhar_no to delete: ")
        delete_details(aadhar_no)
    elif choice == "4":
        aadhar_no = input("Enter aadhar_no to update: ")       
        update_details(aadhar_no)
    elif choice == "5":
        aadhar_no = input("Enter aadhar_no to search: ")
        search_by_aadhar_no(aadhar_no)
    elif choice == "6":
        name = input("Enter name to search: ")
        search_by_name(name)
    elif choice=='7':
        display_name_and_date()
    elif choice == "8":
        clear_all_records()  # Clear all records when option 8 is selected
    
    elif choice == "9":
        break
    else:
        print("Invalid choice, please try again.")
