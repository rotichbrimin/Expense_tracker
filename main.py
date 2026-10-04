import os
import sys

from storage import load_data, save_data
from expenses import add_expense, view_expenses, update_expense, delete, clear_storage
from search import search
from analytics import total, sort_menu, view_summary
            
expenses = load_data()
    
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n=== MAIN MENU ===")
    print("1. Add Expense:")
    print("2. View Expenses:")
    print("3. Update Expense:")
    print("4. Delete :")
    print("5. Search :")
    print("6. Total  :")
    print("7. View Summary: ")
    print("8. Clear  :")
    print("9. Sort   :")
    # print("9. Export to CSV: ")
    print("10. Exit   :")
    
    try:
        option=int(input("\nEnter an option (1-10): "))
    except ValueError:
        print("Enter a valid option!")
        return
        
    if option==1:
        while True:
            expenses.append(add_expense(expenses))
            save_data(expenses)
            while True:

                again=input("\nAdd another expense? yes/y no/n :").strip().lower()
                if again in ["yes", "y"]:  
                    break #move out of this inner loop so that the user can enter the new expense
                elif again in ["no", "n"]:
                    view_expenses(expenses)
                    return #Exist the main function
                else:
                    print("Enter yes/y no/n")
                 
    elif option ==2:
        view_expenses(expenses)
    elif option ==3:
        view_expenses(expenses)
        update_expense(expenses)
        save_data(expenses)
    elif option ==4:
        view_expenses(expenses)
        delete(expenses)
        save_data(expenses)
    elif option ==5:
        search(expenses)
    elif option ==6:
        view_expenses(expenses)
        total(expenses)
    elif option == 7:
        view_summary(expenses)
    elif option ==8:
        clear_storage(expenses)
    elif option ==9:
        sort_menu(expenses)
    # elif option == 9:
    #     export_to_csv(expenses)
    elif option ==10:
        print("Exiting Expense Tracker! ")
        sys.exit()
    else:
        print("Enter a valid option")
while True:        
    main() 
    input("\nPress Enter to continue: ")              