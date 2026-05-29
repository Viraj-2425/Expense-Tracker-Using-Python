expenses_list=[] # list in form dictionary

print("Welcome to expense Tracker")

while True:
    print("--Menu--")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice=int(input("Please Enter Your Choice : "))

    #Add Expense

    if(choice == 1):
        date=input("Date ? : ")
        category=input("Type of Expenses : ")
        description=input("Details : ")
        Amount=float(input("Enter the Amount : "))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "Amount":Amount
        }


        expenses_list.append(expense)
        print("Successfully Done")
# view expense
    elif(choice==2):
        if( len(expenses_list)==0):
            print("No Expenses Added")
        else:
            print("this is your Expenses")
            count=1
            for eachexpense in expenses_list:
                print(f"Expense 1 {count} -> {eachexpense["date"]},{eachexpense["category"]},{eachexpense["description"]},{eachexpense["Amount"]}")

    
# total expense
    elif (choice ==3):
        total=0
        for eachexpense in expenses_list:
            total=total + eachexpense["Amount"]

        print("\n Total Expense:",total)

# exit
    elif(choice==4):
        print("Thanks for Using Our System")
        break
    else:
        print("choice no. is wrong")