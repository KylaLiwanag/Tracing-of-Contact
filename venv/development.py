print("programmed by: Kyla Camille A. Liwanag")
All_contact = []
num = 1
choice = 1
while choice !=3:
    print("\n\n--------------- Contact Tracing Book ---------------\n\n"
          "What would you like to do?\n\n"
          "1. Add a Contact \n"
          "2. Search the Address Book \n"
          "3. Exit \n")
choice = int(input("Choose an option: "))
if choice == 1:
    print("\n--------------- Add Contact ---------------\n")
    if len(All_contact)< 100 :
        First_name = input("Enter the full name : ")
        Age = input("Enter the age : ")
        Address = input("Enter Address : ")
        Number = input("Enter Contact Number : ")
        Contact = [First_name, Age, Address, Number]
        All_contact.append(Contact)
        print("\nSuccessfully added entry no. " + str(num) + " to the Address Book!")
        num += 1
    else:
        print("Address book contains 100 entries. We can't add any more entries.")


