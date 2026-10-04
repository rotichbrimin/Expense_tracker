from datetime import datetime
from expenses import view_expenses

def search(expenses):
    while True:
        print("1. Search by ID or Name: ")
        print("2. Search by Date: ")
        print("3. Search by Category:")
        print("4. Back")
            
        try:
            option = int(input("Enter an option 1,2,3 or 4: "))
            
            if option == 1:
                search_expense(expenses)
            elif option ==2:
                search_by_date(expenses)
            elif option ==3:
                search_by_category(expenses)
            elif option ==4:
                return
            else:
                print("Choose either 1,2,3 or 4: ")
        except ValueError:
            print("Enter a valid option. Try again!")

def search_expense(expenses):
    if not expenses:
        print("No expense made") 
        return
    while True:
        search = input("Enter ID or name of expense to search:").lower().strip()
        results = []
        # found = False
        for exp in expenses:
            if search.isdigit():
                if int(search)==exp['id']:
                    results.append(exp)

                    # print(f"\nExpense: {exp['id']} | Name: {exp['name']} | Category: {exp['category']}| Amount: {exp['amount']} | Date: {exp['date']}")
                    # found =True
            else:
                if search in exp['name'].lower():
                    results.append(exp)
                    
                    # print("\n=== SEARCH RESULTS ===")  
                    # print(f"\nExpense: {exp['id']} | Name: {exp['name']} | Category: {exp['category']} | Amount: {exp['amount']} | Date: {exp['date']}")
                    # found = True
        if not results:
            print("Expense not found")  

        else:
            print("\n=== SEARCH RESULTS ===")
            view_expenses(results)     
        again = input("\nSearch again? (yes/y) or (no/n)? ").strip().lower()
        if again in ["yes", "y"]:
            continue       
        if again in ["no", "n"]:
            return     
        print("Enter yes or no")


def search_by_date(expenses):
    while True:
        target_date = input("Search expense per date. Use format (YYYY-MM-DD): ").strip()
        try:
            #fix input (eg, turns "2026-10-2" to "2026-10-02")
            user_date = datetime.strptime(target_date, "%Y-%m-%d")
            new_date = user_date.strftime("%Y-%m-%d")
            
            results = []
            # found = False
            for exp in expenses:
                if exp['date'] == new_date:
                    results.append(exp)
                    # print(f"ID: {exp['id']} | Name: {exp['name']} | Category: {exp['category']} | Amount: {exp['amount']} | Date: {exp['date']}")
                    # found = True
            if not results:
                print(f"Expense not found for date: {target_date}")
            else:
                print(f"=== SEARCH RESULTS === {target_date}")
                view_expenses(results)
            while True:
                again = input("\nSearch again? (Yes/y) or (No/n): ").strip().lower()
                if again in ["yes", "y"]:
                    break
                elif again in ["no", "n"]:
                    return
                else:
                    print("Enter (yes/y) or (no/n)! ")
        except ValueError:
            print("Enter a valid date! Try again")

def search_by_category(expenses):
    while True:
        search = input("Enter search category: ").lower().strip()
        results = []
        # found=False
    
        for exp in expenses:
            # if exp['category'].lower()== search:
            if search in exp['category'].lower():
                results.append(exp)
                # print("=== SEARCH BY CATEGORY ===")
                # print(f"ID: {exp['id']} | Name: {exp['name']} | Category: {exp['category']} | Amount: {exp['amount']} | Date: {exp['date']}")
            
                # found = True
            
        if not results:
            print("No expense in this category")

        else:
            view_expenses(results)    
        while True:    
            again = input("\nSearch again yes/y no/n: ").lower().strip()
            
            if again in ["yes", "y"]:
                break
            elif again in ["no", "n"]:
                return
            else:
                print("Type yes/y or no/n!")
            