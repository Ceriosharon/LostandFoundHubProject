from helpers import (
    add_lost_item,
    add_found_item,
    view_items,
    view_item_details,
    claim_item,
    delete_item,
    update_item,
    search_items,
    initialize_db
)

def main():
    print("Welcome to the Lost and Found Hub CLI!")
    print("What would you like to do?")
    print("""
    1. Add Lost Item
    2. Add Found Item
    3. View All Items
    4. View Item Details
    5. Claim Item
    6. Update Item
    7. Delete Item
    8. Search Items
    9. Exit
    """)

    while True:
        try:
            choice = int(input("Enter your choice (1-9): "))
            if choice == 1:
                add_lost_item()
            elif choice == 2:
                add_found_item()
            elif choice == 3:
                view_items()
            elif choice == 4:
                view_item_details()
            elif choice == 5:
                claim_item()
            elif choice == 6:
                update_item()
            elif choice == 7:
                delete_item()
            elif choice == 8:
                search_items()
            elif choice == 9:
                print("Thank you for using the Lost and Found Hub CLI. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 9.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    initialize_db()  # Ensure the database and table are created
    main()
