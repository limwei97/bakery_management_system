import os
import constant

def Customer():
    #provide full path to the folder name datastore
    DATA_FILEPATH =  os.path.join(os.getcwd(),"datastore")

    while True:
        print("--- Customer System ---")
        print("1.Customer Account Management\n2.Product Browsing\n3.Cart Management\n4.Order Tracking\n5.Product Review")
    
        userAction = input("\nPlease select action: ")

        #validation: if user provide empty value
        if userAction =='':
            continue
        userAction = int(userAction)
        #validation: if user does not select within 1-5
        print()
        if userAction < 1 or userAction > 5:
            continue
        elif userAction == constant.CUSTOMER_ACCOUNT_MANAGEMENT:
            CustomerAccountManagement(DATA_FILEPATH)
        elif userAction == constant.PRODUCT_BROWSING:
            ProductBrowsing(DATA_FILEPATH)
        elif userAction == constant.CART_MANAGEMENT:
            CartManagement(DATA_FILEPATH)
        elif userAction == constant.ORDER_TRACKING:
            OrderTracking(DATA_FILEPATH)
        elif userAction == constant.PRODUCT_REVIEW:
            ProductReview(DATA_FILEPATH)
        input()

def CustomerAccountManagement(data_filepath):
    """
    This function is to create, manage, login and update personal information
    """
    print("This is customer account management")
    #CreateAccount(data_filepath)
    LoginAccount(data_filepath)
    print("\n1. Create Profile")
    print("2. Login")
    print("3. Update Profile")
    choice = input("Choose an option: ")
    if choice == "1":
        CreateAccount(data_filepath)
    elif choice == "2":
        LoginAccount(data_filepath)
    elif choice == "3":
        UpdatePersonalInformation(data_filepath, ObtainAllUsers(data_filepath))

def ProductBrowsing(data_filepath):
    """
    This function is for customers to explore a variety of bakery items available for purchase
    """
    with open(os.path.join(data_filepath, "product.txt"), "r") as file:
        data = file.readlines()
        for line in data:
            print(line[:-1])

def CartManagement():
    """
    This function is for customers to add, remove, or modify items in their shopping cart
    """
    pass

def OrderTracking(data_filepath):
    """
    This function is to monitor the status of placed orders
    """
    temp = []
    with open(os.path.join(data_filepath, "order.txt"), "r") as file:
        data = file.readlines()
        for line in data:
            print(line[:-1])
            temp.append(line[:-1].split(","))
        print(temp)
    return temp

def ProductReview(data_filepath):
    """
    This function is for customers to share feedback and suggestions about purchased products.
    """
    new = []
    listProduct = OrderTracking(data_filepath)
    userAction = input("\nPlease select product to review: ")
    for product in listProduct:
        if userAction == product[0]:
            review = input("Please enter review for products: ")
            product[-1] = review
        new.append(', '.join(product)+"\n")

    with open(os.path.join(data_filepath, "order.txt"), "w") as file:
        file.writelines(new)

def CreateAccount(data_filepath):
    """This function is to create user account"""
    
    firstName = input("Please enter first name: ")
    lastName = input("Please enter last name: ")
    userName = input("Please enter username: ")
    dateOfBirth = input("Please enter date of birth: ")
    password = input("Please enter password: ")

    with open(os.path.join(data_filepath,"userAccount.txt"), "a") as file:
        file.write(firstName + ":" + lastName + ":" + userName + ":" + dateOfBirth + ":" + password + "\n")

def LoginAccount(data_filepath):
    """This function is to login account"""
    userName = input("Please enter username to login: ")
    password = input("Please enter password to login: ")
    user_dict = {}

    with open(os.path.join(data_filepath,"userAccount.txt"), "r") as file:
        data = file.readlines()
        for line in data:
            word = line.split(":")
            if userName == word[2] and password == word[4][:-1]:
                print(word)
                user_dict[word[2]] = word
                UpdatePersonalInformation(data_filepath, user_dict)
                return
    
    print("User does not exist")
    CreateAccount(data_filepath)

def ObtainAllUsers(data_filepath):
    user_dict = {}
    with open(os.path.join(data_filepath,"userAccount.txt"), "r") as file:
        data = file.readlines()
        for line in data:
            word = line.split(":")
            user_dict[word[2]] = word
    return user_dict

def UpdatePersonalInformation(data_filepath, user_dict):

    userName = input("Please enter username to pick profile to update: ")
    firstName = input("Please enter first name: ")
    lastName = input("Please enter last name: ")
    dateOfBirth = input("Please enter date of birth: ")
    password = input("Please enter password: ")

    print(user_dict)
    if username in user_dict:
        user_dict[userName] = [firstName, lastName, userName, dateOfBirth, password]
    for value in user_dict.values():
        temp.append(value)

    with open(os.path.join(data_filepath,"userAccount.txt"), "w") as file:
        file.writelines(temp)

if __name__ == "__main__":
    Customer()