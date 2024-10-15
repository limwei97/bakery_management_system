# 1. Systems Administration: Manage user accounts and credentials
def manage_users(self, action, user=None):
    if action == "add":
        print(f"User {user} added successfully!")
    elif action == "update":
        print(f"User {user} updated successfully!")
    elif action == "remove":
        print(f"User {user} removed successfully!")
    else:
        print("Invalid action for user management.")

# 2. Order Management: Add, View, and Update orders
def add_order(self, order_id, product, quantity, status="In progress"):
    order = {
        "order_id": order_id,
        "product": product,
        "quantity": quantity,
        "status": status
    }
    self.orders.append(order)
    print(f"Order {order_id} added: {product} (x{quantity})")

def view_orders():
    if not orders:
        print("No orders available.")
    else:
        for order in orders:
            print(f"Order ID: {order['order_id']}, Product: {order['product']}, Quantity: {order['quantity']}, Status: {order['status']}")

def update_order_status(order_id, new_status):
    for order in orders:
        if order["order_id"] == order_id:
            order["status"] = new_status
            print(f"Order {order_id} status updated to {new_status}")
            return
    print(f"Order {order_id} not found.")

# 3. Financial Management: Track income, expenses, and profitability
def update_finances(income=50, expenses=100):
    income += product_income
    expenses += product_expenses
    print(f"Updated Financials - Income: {income}, Expenses: {expenses}")

def calculate_profit():
    profit = product_income - product_expenses
    print(f"Total profit: {profit}")

# 4. Inventory Control: Add, update, and remove items from inventory
def add_to_inventory(item_name, quantity, price):
    inventory[item_name] = {"quantity": quantity, "price": price}
    print(f"{item_name} added to inventory with quantity {quantity} at ${price:.2f} each.")

def update_inventory(item_name, quantity=None, price=None):
    if item_name in inventory:
        if quantity is not None:
            inventory[item_name]["quantity"] = quantity
        if price is not None:
            inventory[item_name]["price"] = price
        print(f"{item_name} updated: Quantity - {quantity}, Price - ${price:.2f}")
    else:
        print(f"{item_name} not found in inventory.")

def view_inventory():
    if not inventory:
        print("No items in inventory.")
    else:
        for item, details in inventory.items():
            print(f"Item: {item}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}")

def remove_from_inventory(item_name):
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from inventory.")
    else:
        print(f"{item_name} not found in inventory.")

# 5. Customer Feedback: Add and review feedback
def add_feedback(feedback):
    customer_feedback.append(feedback)
    print("Feedback added successfully.")

def view_feedback():
    if not customer_feedback:
        print("No customer feedback available.")
    else:
        print("Customer Feedback:")
        for feedback in self.customer_feedback:
            print(f"- {feedback}")

def Manager():
    while True:
        print("\n1. Manage Users")
        print("2. Manage Orders")
        print("3. Manage Finances")
        print("4. Manage Inventory")
        print("5. View Customer Feedback")
        print("6. Exit Manager Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            action = input("Would you like to add, update, or remove a user? ")
            user = input("Enter username: ")
            manage_users(action, user)

        elif choice == "2":
            view_orders()

        elif choice == "3":
            update_finances(income=100, expenses=50)  # Example usage
            calculate_profit()

        elif choice == "4":
            view_inventory()

        elif choice == "5":
            view_feedback()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")