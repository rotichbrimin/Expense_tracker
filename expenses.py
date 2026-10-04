
from storage import save_data
from datetime import datetime

def clear_storage(expenses):
    expenses.clear()
    save_data(expenses)
    print("All saved data cleared")




def add_expense(expenses):
    # while True:
    if not expenses:
        expense_id = 1
    else:
        expense_id = max(exp['id'] for exp in expenses) + 1
        # try:
        #     expense_id =int(input("Enter Expense ID: "))
        #     exists = False
        #     for exp in expenses:
        #         if exp['id']==expense_id:
        #             exists=True
        #             break   
        #     if exists:
        #         print(f"ID {expense_id} exists. Try again!")
        #         continue
        #     else:
        #         break
        # except ValueError:
        #     print("Enter a valid ID")
     
    while True:           
        name = input("Enter expense name:").strip().title()
        if name:
            break
        print("Name cannot be empty!")
    while True:
        category = input("Enter category: ").strip().title()
        if category:
            break
        print("Category cannot be empty!")
    while True:
        try:
            amount = int(input(f"Enter amount for {name}:"))
            if amount >0:
                break
            print("Amount must be more than 0")
            continue
        except ValueError:
           print("Enter a valid amount")
           continue

     #Automatic date and time
    date = datetime.today().strftime('%Y-%m-%d')
    now = datetime.today()
    time_str = now.strftime('%I:%M %p')
    print(f"\nDate automatically recorded as :{date}") 
    print(f"Time recorded automatically as {time_str}")


    # while True:       
    #     date = input(f"Enter expence date (YYYY-MM-DD) for {name}:").strip()
    #     if not date:
    #         print("Date cannot be empty!")
    #         continue
    #     try:
    #         datetime.strptime(date, "%Y-%m-%d")
    #         break
    #     except ValueError:
    #         print("Invalid date. Use YYYY-MM-DD")
    #         continue
    
    return{
        "id":expense_id,
        "name":name,
        "category":category,
        "amount":amount,
        "date":date,
        "time": time_str
    }
    
    
    
def view_expenses(expenses):
    if not expenses:
        print("No expense made")
        return
    print("\n=== YOUR EXPENSES ===")
    print("-" * 89)
    print(f"{'ID':<5} | {'NAME':<15} | {'CATEGORY':<15} | {'AMOUNT(KSH)':<15} | {'DATE':<12} | {'TIME':<10}  | ")
    print("-" * 89)
    for exp in expenses:
        # print(f"ID: {exp['id']} | Name: {exp['name']} | Category: {exp['category']} | Amount: {exp['amount']} | Date: {exp['date']}")
        #.get ('time', 'N/A') prevent crashing on older entries that only had dates
        time_val = exp.get('time', 'N/A')
        print(f"{exp['id']:<5} | {exp['name']:<15} | {exp['category']:<15} | {exp['amount']:<15} | {exp['date']:<12} | {time_val:<10}  | ")
        # print("-" * 78)
    print("-" * 89)


def update_expense(expenses):
    if not expenses:
        print("No expense to update")
        return

    while True:
        search_update = input("\nEnter ID or name of expense to update: ").strip().lower()
        search = []
        found = False

        for exp in expenses:
            
            
            if search_update.isdigit() and int(search_update) == exp['id']:
                found = True
                search.append(exp)

            
            elif search_update == exp['name'].lower():
                found = True
                search.append(exp)

            if found:
                # print(f"\nID: {exp['id']} | Name: {exp['name']} | Category: {exp['category']} | Amount:{exp['amount']} | Date: {exp['date']}")
                view_expenses(search)
                print("\n1. Update Name")
                print("2. Update Amount")
                print("3. Update Date")
                print("4. Update Category")
                print("5. Back")
                
                while True:

                    try:
                        choice = int(input("Enter an Option: "))
                    except ValueError:
                        print("Enter a valid option")
                        continue
                    if choice in [1,2,3,4,5]:
                        break
                    else:
                        print("Invalid option!")

                if choice == 1:
                    new_name = input("Enter new name: ").strip().title()
                    exp['name'] = new_name
                    print(f"\nName updated to {new_name}")
                    save_data(expenses)
                    return

                elif choice == 2:
                    while True:
                        try:
                            new_amount = int(input("Enter new amount: "))
                            if new_amount > 0:
                                exp['amount'] = new_amount
                                print(f"\nAmount updated to {new_amount}")
                                save_data(expenses)
                                return
                            else:
                                print("Amount must be more than 0")
                        except ValueError:
                            print("Enter a valid number")

                elif choice == 3:
                    while True:     
                        new_date = input("Enter new date. Use format(YYYY-MM-DD): ").strip()
                        try:
                            datetime.strptime(new_date, "%Y-%m-%d")
                            exp['date'] = new_date
                            print(f"\nDate updated to {new_date}")
                            save_data(expenses)
                            return
                           
                        except ValueError:
                            print("Invalid date. Use YYYY-MM-DD")
                elif choice == 4:
                    new_category = input("Enter New Category: ").strip().title()
                    exp['category'] = new_category
                    print(f"New category updated to {new_category}")
                    save_data(expenses)
                    return
                
                elif choice == 5:
                    break

                else:
                    print("Invalid option")

        if not found:
            print("Expense not found")                   



def monthly_budget(expenses):
    if not expenses:
        print("No expense made! ")
        return
    current_month = datetime.today().strftime('%Y-%m')
    expense_list= [
        exp for exp in expenses
        if exp.get("date", "").startswith(current_month)
    ]
    if not expense_list:
        print(f"No expense made for this month {current_month}")
        return
    monthly_total = sum(exp['amount'] for exp in expense_list)
    print(f"\nMonthly Budget Report for this month KSH: {current_month}: ")
    print(f"Total Spent This Month KSH: {monthly_total}")

    try:
        limit = float(input("Enter your Monthly limit: "))
    except ValueError:
        print("Enter a valid digit! ")
        return
    print("-" * 40)
    if monthly_total > limit:
        excess = monthly_total - limit
        print(f"BUDGET EXCEEDED! You are over budget by KSH: {excess:.2f}!")
    elif monthly_total >= (limit * 0.8):
        print("WARNING! You have used 80% or more of your monthly budget!")
    else:
        remaining = limit - monthly_total
        print(f"You are within budget! Remaining KSH:{remaining:.2f}")
    print("-" * 40)
    

 
       
def delete(expenses):
    while True:
        print("")
        print("\n=== DELETE EXPENSE ===")
        print("1. Delete per ID or Name")
        print("2. Delete all.")
        print("3. Back")
        try:
            option = int(input("\nEnter an option (1,2,3): "))
        
            if option == 1:
                delete_expense(expenses)
            elif option ==2:
                delete_all_expenses(expenses)
            elif option ==3:
                return
            else:
                print("\nChoose either 1,2 or 3:")
         
        except ValueError:
            print("Invalid option! Try again")


         
def delete_expense(expenses):
    if not expenses:
        print("No expense to delete!")
        return
        
    while True:
        query= input("\nEnter expense ID or Name to delete: ").strip()
        for i, exp in enumerate(expenses):
            if query.isdigit():
                if int(query)==exp['id']:
                    confirm = input(f"Are you sure to delete ID: {exp['id']} - NAME: {exp['name']}? (yes/y), (no/n)! ").strip().lower()
                    if confirm in ["yes", "y"]:
                        del expenses[i]
                        save_data(expenses)
                        print(f"Expense: {exp['id']} - {exp['name']} deleted successfully! ")
                        return
                    elif confirm in ["no", "n"]:
                        print("Cancelled")
                        return
                         
            else:
                if query.lower() in exp['name'].lower():
                    confirm = input(f"Are you sure to delete ID: {exp['id']} - {exp['name']} ? (yes/y), (no/n)! ").strip().lower()
                    if confirm in ["yes", "y"]:
                        del expenses[i]
                        save_data(expenses)
                        print(f"Expense: {exp['id']} - {exp['name']} deleted successfully! ")
                        return
                    elif confirm in ["no", "n"]:
                        print("Cancelled")
                        return
                        
        else:
            print("Expense not found")
            retry = input("Try again? (yes/y) or (no/n)").strip().lower()
            if retry in ["yes", "y"]:
                continue
            elif retry in ["no", "n"]:
                return
            else:
                print("Enter yes/y no/n")




def delete_all_expenses(expenses):
    confirm = input("!!! WARNING: Are you sure you want to delete ALL expenses? (yes/no): ").strip().lower()
    if confirm in ["yes", "y"]:
        expenses.clear() 
        save_data(expenses)
        print("All data has been wiped successfully.")
    else:
        print("Deletion cancelled. Your data is safe.")
        
      