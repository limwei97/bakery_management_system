import operator

# Bakery products and prices
products = ["Baguette", "Sourdough", "Ciabatta", "Focaccia", "Rye Bread",
            "Brioche", "Multigrain Bread", "Pita Bread", "Challah", "Whole Wheat Bread"]

prices = [2.0, 4.0, 3.0, 5.0, 6.0, 8.0, 6.0, 4.0, 7.0, 5.0]
# discount 10% of the total prices

# Number of products
num_products = len(products)

# Array to track total sales for each product
total_sold = [0] * num_products

# Variable to track total revenue
total_revenue = 0.0


# Function to display main menu
def display_main_menu():
    print("\n-------------------MENU-------------------")
    print("1. Make a Sale")
    print("2. Generate Sales Report")
    print("3. Show Total Revenue")
    print("4. Exit")
    print("------------------------------------------")
    return int(input("Choose an option: "))


# Function to display products with aligned columns
def display_products():
    print("\n\n-----------------Items for Sale-----------------")
    for i in range(num_products):
        print(f"{i + 1}. {products[i]:<25} RM{prices[i]:>5.2f}")
    print("-------------------------------------------------")


# Function to handle transactions and show the receipt pattern
def complete_transaction():

    global total_revenue
    selected_products = [0] * num_products
    total = 0
    discount_rate = 0.10  # 10% discount

    while True:
        product_num = int(input("\nEnter product number (or 0 to EXIT): "))

        if product_num == 0:
            break

        elif 1 <= product_num <= num_products:
            quantity = int(input("Enter quantity: "))
            selected_products[product_num - 1] += quantity
            total += prices[product_num - 1] * quantity

        else:
            print("Invalid product number.")

    # Apply 10% discount to the total
    discount = total * discount_rate
    total_after_discount = total - discount

    # Update total sold quantities and total revenue
    for i in range(num_products):
        total_sold[i] += selected_products[i]
    total_revenue += total_after_discount

    # Display the receipt
    print("\n\n-------------------RECEIPT-------------------")
    print(f"{'Product':<25}{'Quantity':<10}{'Subtotal':<10}")
    print("---------------------------------------------")

    for i in range(num_products):

        if selected_products[i] > 0:
            print(f"{products[i]:<25}{selected_products[i]:<10}RM{selected_products[i] * prices[i]:>7.2f}")

    print(f"\nTotal amount before discount: RM{total:.2f}")
    print(f"Discount (10%):              -RM{discount:.2f}")
    print(f"Total amount after discount:  RM{total_after_discount:.2f}")
    print("---------------------------------------------")
    print("Thank you for your purchase!\n\n")

    return total_after_discount


# Function to generate a report on sales performance and product popularity
def generate_report():
    print("\n\n-------------------SALES REPORT-------------------")
    print(f"{'Product':<25}{'Units Sold':<10}")
    print("--------------------------------------------------")

    # Create a list of tuples pairing product names with total sold units
    sales_report = [(products[i], total_sold[i]) for i in range(num_products)]

    # Sort sales report in descending order by units sold
    sales_report.sort(key=operator.itemgetter(1), reverse=True)

    for product, units_sold in sales_report:
        print(f"{product:<25}{units_sold:<10}")

    # Find and display the most popular product
    most_popular_product = sales_report[0]
    print(f"\nMost Popular Product: {most_popular_product[0]} with {most_popular_product[1]} units sold.")
    print("--------------------------------------------------\n\n")


# Function to show total revenue
def show_total_revenue():
    print("\n-------------------TOTAL REVENUE-------------------")
    print(f"Total Revenue Collected: RM{total_revenue:.2f}")
    print("--------------------------------------------------\n")


# Main Program Loop

def Cashier():
    while True:
        choice = display_main_menu()

        if choice == 1:
            display_products()
            complete_transaction()

        elif choice == 2:
            generate_report()

        elif choice == 3:
            show_total_revenue()

        elif choice == 4:
            confirm_exit = input("Are you sure you want to exit? (y/n): ").lower()

            if confirm_exit == 'y':
                print("Exiting...\n")
                break
        else:
            print("There is an error, please try again.")