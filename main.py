All_Contact = []
num = 1
print("="*20, "Contact Tracing Book","="*20)
choice = 1
while choice != 3:
    print("\n\n--------------- Contact Tracing Book ---------------\n\n"
          "What would you like to do?\n\n"
          "1. Add a Contact \n"
          "2. Search the Address Book \n"
          "3. Exit \n")
    choice = int(input("Choose an option: "))
    if choice == 1:
      print("\n--------------- Add Contact ---------------\n")
      if len(All_Contact)< 100 :
          First_name = input("Enter the full name : ")
          Age = input("Enter the age : ")
          Address = input("Enter Address : ")
          Number = input("Enter Contact Number : ")
          Contact = [ First_name , Age , Address , Number ]
          All_Contact.append(Contact)
          print("\nSuccessfully added entry no. " + str(num) + " to the Address Book!")
          num += 1
      else:
        print("Address book contains 100 entries. We can't add any more entries.")

    elif choice == 2:
        print("\n-------------- Search Contact Information ---------------\n")
        Option = (input("Enter the full name: "))
        Value = [All_Contact]
        count = 0
        for key in All_Contact:
            if Value in key:
                print(f"{key[0]}\t{key[1]}\t{key[2]}\t{key[3]}")
                count =1
        if count==0:
            print("The contact information does not exist.")

    elif choice == 3:
        exit()
        break
    else:
        print("That is not a valid option.")

    answer = input("Do you want to try again? yes/no: ")
    if answer == "yes":
        continue
    else:
        print("Thank you for using the program!")
        break


