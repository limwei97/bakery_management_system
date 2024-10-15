import os

# Create a recipe
def create_recipe(recipes):
    name = input("Enter recipe name: ")
    if name in recipes:
        print("Recipe already exists.")
        return
    ingredients = input("Enter ingredients (comma separated): ").split(", ")
    recipes[name] = ingredients
    print(f"Recipe '{name}' created successfully.")

# Update a recipe
def update_recipe(recipes):
    name = input("Enter the recipe name to update: ")
    if name not in recipes:
        print("Recipe not found.")
        return
    new_ingredients = input("Enter new ingredients (comma separated): ").split(", ")
    recipes[name] = new_ingredients
    print(f"Recipe '{name}' updated successfully.")

# Delete a recipe
def delete_recipe(recipes):
    name = input("Enter the recipe name to delete: ")
    if name in recipes:
        del recipes[name]
        print(f"Recipe '{name}' deleted successfully.")
    else:
        print("Recipe not found.")

# Inventory Check
def check_inventory(data_filepath):
    inventory = {}
    with open(os.path.join(data_filepath,"inventory.txt"), "r") as file:
        data = file.readlines()
        for line in data:
            items = line.split(",")
            inventory[items[0]] = int(items[1])

    print("Checking inventory for ingredients.")
    required_ingredients = {}
    while True:
        ingredient = input("Enter ingredient (or 'done' to finish): ")
        if ingredient == 'done':
            break
        quantity = float(input(f"Enter quantity for {ingredient}: "))
        required_ingredients[ingredient] = quantity

    missing_items = {}
    for ingredient, quantity in required_ingredients.items():
        if ingredient not in inventory or inventory[ingredient] < quantity:
            missing_items[ingredient] = quantity - inventory.get(ingredient, 0)

    if not missing_items:
        print("All ingredients are available.")
    else:
        print(f"Missing or insufficient ingredients: {missing_items}")

# Production Record-keeping
def record_production(data_filepath):
    production_records = []
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity produced: "))
    batch_number = input("Enter batch number: ")
    expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
    record = {
        'product_name': product_name,
        'quantity': quantity,
        'batch_number': batch_number,
        'expiration_date': expiration_date
    }
    production_records.append(record)
    print(f"Production record for '{product_name}' added successfully.")
    with open(os.path.join(data_filepath,"recordProduction.txt"), "a") as file:
        file.write(str(production_records)+"\n")

# Equipment Management
def report_equipment_status(data_filepath):
    equipment_status = {}
    equipment_name = input("Enter equipment name: ")
    status = input(f"Enter status for {equipment_name} (e.g., Malfunction, Needs Maintenance): ")
    equipment_status[equipment_name] = status
    print(f"Equipment '{equipment_name}' status updated to '{status}'.")
    with open(os.path.join(data_filepath,"recordEquipmentStatus.txt"), "a") as file:
        file.write(str(equipment_status)+"\n")

#Baker main function
def Baker():
    DATA_FILEPATH = os.path.join(os.getcwd(), "datastore")
    recipes = {}
    while True:
        print("\n--- Baker System ---")
        print("1. Create Recipe")
        print("2. Update Recipe")
        print("3. Delete Recipe")
        print("4. Check Inventory")
        print("5. Record Production")
        print("6. Report Equipment Status")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            create_recipe(recipes)
        elif choice == '2':
            update_recipe(recipes)
        elif choice == '3':
            delete_recipe(recipes)
        elif choice == '4':
            check_inventory(DATA_FILEPATH)
        elif choice == '5':
            record_production(DATA_FILEPATH)
        elif choice == '6':
            report_equipment_status(DATA_FILEPATH)
        elif choice == '7':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")