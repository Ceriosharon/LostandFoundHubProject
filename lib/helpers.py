import sqlite3

DB_NAME = "app_database.db"

# Initialize the database
def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Create the `items` table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL,
            item_name TEXT NOT NULL,
            item_color TEXT NOT NULL,
            description TEXT NOT NULL,
            phone TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Add a lost item
def add_lost_item():
    user_name = input("Enter your name: ")
    item_name = input("Enter the name of the lost item: ")
    item_color = input("Enter the color of the lost item: ")
    description = input("Enter a description of the lost item: ")
    phone = input("Enter your phone number: ")
    status = "lost"

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (user_name, item_name, item_color, description, phone, status) VALUES (?, ?, ?, ?, ?, ?)",
        (user_name, item_name, item_color, description, phone, status)
    )
    conn.commit()
    print(f"Lost item '{item_name}' added successfully!")
    conn.close()


# Add a found item
def add_found_item():
    user_name = input("Enter your name: ")
    item_name = input("Enter the name of the found item: ")
    item_color = input("Enter the color of the found item: ")
    description = input("Enter a description of the found item: ")
    phone = input("Enter your phone number: ")
    status = "found"

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (user_name, item_name, item_color, description, phone, status) VALUES (?, ?, ?, ?, ?, ?)",
        (user_name, item_name, item_color, description, phone, status)
    )
    conn.commit()
    print(f"Found item '{item_name}' added successfully!")
    conn.close()


# Claim an item
def claim_item():
    item_id = input("Enter the ID of the item to claim: ")
    user_name = input("Enter your name: ")
    phone = input("Enter your phone number for verification: ")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Check if the item exists and is available for claiming
    cursor.execute("SELECT * FROM items WHERE id = ? AND status = 'found'", (item_id,))
    item = cursor.fetchone()

    if item:
        item_name = item[2]
        item_color = item[3]
        description = item[4]
        owner_phone = item[5]

        # Ask the user for the description and color to match
        claim_description = input(f"Please provide a description of the {item_name}: ")
        claim_color = input(f"Please provide the color of the {item_name}: ")

        # Compare all relevant fields for verification
        if phone == owner_phone and claim_description.strip().lower() == description.strip().lower() and claim_color.strip().lower() == item_color.strip().lower():
            cursor.execute(
                "UPDATE items SET status = 'claimed', user_name = ? WHERE id = ?",
                (user_name, item_id)
            )
            conn.commit()
            print(f"Item '{item_name}' claimed successfully!")
        else:
            print("Details do not match. Unable to claim the item.")
    else:
        print("Item not found or is not available for claiming.")
    
    conn.close()


# View all items
def view_items():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()

    if rows:
        print("\nAll Items:")
        for row in rows:
            print(
                f"ID: {row[0]}, User: {row[1]}, Item Name: {row[2]}, Color: {row[3]}, Status: {row[6]}, "
                f"Description: {row[4]}, Phone: {row[5]}"
            )
    else:
        print("No items found.")
    conn.close()


# View details of a specific item
def view_item_details():
    item_id = input("Enter the ID of the item to view: ")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    row = cursor.fetchone()

    if row:
        print(
            f"\nItem Details:\nID: {row[0]}, User: {row[1]}, Item Name: {row[2]}, Color: {row[3]}, "
            f"Status: {row[6]}, Description: {row[4]}, Phone: {row[5]}"
        )
    else:
        print("Item not found.")
    conn.close()


# Update an item
def update_item():
    item_id = input("Enter the ID of the item to update: ")
    new_description = input("Enter additional details (e.g., color or other description): ")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE items SET description = description || ' ' || ? WHERE id = ?",
        (new_description, item_id)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print("Item updated successfully with additional details!")
    else:
        print("Item not found.")
    conn.close()


# Delete an item
def delete_item():
    item_id = input("Enter the ID of the item to delete: ")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Item deleted successfully!")
    else:
        print("Item not found.")
    conn.close()


# Search for items by name
def search_items():
    search_term = input("Enter a search term: ")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE item_name LIKE ?", (f"%{search_term}%",))
    rows = cursor.fetchall()

    if rows:
        print("\nSearch Results:")
        for row in rows:
            print(
                f"ID: {row[0]}, User: {row[1]}, Item Name: {row[2]}, Color: {row[3]}, Status: {row[6]}, "
                f"Description: {row[4]}, Phone: {row[5]}"
            )
    else:
        print("No matching items found.")
    conn.close()
