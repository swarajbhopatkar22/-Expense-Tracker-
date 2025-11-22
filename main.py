# Expense Tracker Application

expenses = [] #list of expenses in form of dictionary
print("Welcome to the Expense Tracker Application!")

while True:
    print("\nMenu:")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
#Add Expense    
    if (choice == '1'):
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category (e.g., Food, Travel, Books): ")
        amount = input("Enter amount: ")
        description = input("Enter description: ")
        
        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }
        
        expenses.append(expense)
        print("Expense added successfully!")
        
    elif (choice == '2'):
        if len(expenses) <= 0:
            print("No expenses recorded yet.")
        else:
            print("\n Recorded Expenses:")
            for exp in expenses:
                print(f"Date: {exp['date']}, Category: {exp['category']}, Amount: {exp['amount']}, Description: {exp['description']}")
                
    elif (choice == '3'):
        total = 0
        for item in expenses:        # item is a dict
            total += int(item['amount'])
        print(f"Total Expenses: {total}")

    elif (choice == '4'):
    
        print("Exiting the application. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")