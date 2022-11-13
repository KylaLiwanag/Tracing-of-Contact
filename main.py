print("*********** Kyla Camille Liwanag ************")
print("="*20, "Contact Tracing Book","="*20)

All_Contact = {}

num = 1

choice = 1
while choice != 3:
    print("\n\n--------------- Contact Tracing Book ---------------\n\n"
          "What would you like to do?\n\n"
          "1. Add a Contact \n"
          "2. Search a Contact \n"
          "3. Exit \n")
    choice = int(input("Choose an option: "))
    if choice == 1:
      print("\n--------------- Add Contact ---------------\n")
      if len(All_Contact)< 100 :
          Full_name = input("Enter the full name : ")
          Age = input("Enter the age : ")
          Address = input("Enter the Address : ")
          Number = input("Enter the Contact Number : ")
          All_Contact[Full_name] = {"Age: ": Age, "Address: ": Address, "Contact number: ": Number}
          print("\nSuccessfully added entry no. " + str(num) + " to the Contact Tracing Book!")
          num += 1
      else:
        print("Contact tracing book can only contain 100 entries. We can't add any more entries.")

    elif choice == 2:
        print("\n-------------- Search Contact Information ---------------\n")
        Option = (input("Enter the full name you want to tract: "))
        for key, value in All_Contact[Option].items():
            if Option in All_Contact:
                print(key,value)


    elif choice == 3:
        print("Thank you for using this program!")
        exit()
        break
    else:
        print("That is not a valid option.")

    Answer = input("Do you want to try again? yes/no: ")
    if Answer == "yes":
        continue
    else:
        print("Thank you for using the program!")
        break



