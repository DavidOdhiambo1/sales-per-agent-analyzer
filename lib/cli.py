from helpers import (
    exit_program,
    list_agents,
    find_agent_by_name,
    find_agent_by_id,
    create_new_agent,
    update_agent,
    delete_agent,
    list_sales,
    find_sale_by_id,
    create_new_sale,
    update_sale,
    delete_sale,
    total_agents_sales,
    total_sales_per_agent_report,
    best_sales_agent
    
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_agents()
        elif choice == "2":
            find_agent_by_name()
        elif choice == "3":
            find_agent_by_id()
        elif choice == "4":
            create_new_agent()
        elif choice == "5":
            update_agent()
        elif choice == "6":
            delete_agent()
        elif choice == "7":
            list_sales()
        elif choice == "8":
            find_sale_by_id()
        elif choice == "9":
            create_new_sale()
        elif choice == "10":
            update_sale()
        elif choice == "11":
            delete_sale()
        elif choice == "12":
            total_agents_sales()
        elif choice == "13":
            total_sales_per_agent_report()
        elif choice == "14":
            best_sales_agent()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all agents")
    print("2. Find agent by name")
    print("3. Find agent by id")
    print("4: Create new agent")
    print("5: Update agent's details")
    print("6: Delete agent")
    print("7. List all sales")
    print("8. Find sale by id")
    print("9. Create new sale")
    print("10: Update sale")
    print("11: Delete sale")
    print("12: Total sales for an agent")
    print("13: Total sales per agent report")
    print("14: Best sales agent")
    


if __name__ == "__main__":
    main()