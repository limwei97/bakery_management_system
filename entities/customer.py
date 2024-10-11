import os
def Customer():
    #provide full path to the folder name datastore
    DATA_FILEPATH =  os.path.join(os.getcwd(),"datastore")

    CUSTOMER_ACCOUNT_MANAGEMENT = 1

    while True:
        print("==Customer System==")
        print("1.Customer Account Management\n2.Product Browsing\n3.Cart Management\n4.Order Tracking\n5.Product Review")
    
        userAction = input("Please select action: ")

        #validation: if user provide empty value
        if userAction =='':
            continue
        userAction = int(userAction)
        #validation: if user does not select within 1-5
        if userAction < 1 or userAction > 5:
            continue
        elif userAction == CUSTOMER_ACCOUNT_MANAGEMENT:
            CustomerAccountManagement(DATA_FILEPATH)
        input()

def CustomerAccountManagement(data_filepath):
    """
    This function is to create, manage, login and update personal information
    """
    print("This is customer account management")
    #CreateAccount(data_filepath)
    LoginAccount(data_filepath)
    

def ProductBrowsing():
    """
    This function is for customers to explore a variety of bakery items available for purchase"""
    pass

def CartManagement():
    """
    This function is for customers to add, remove, or modify items in their shopping cart
    """
    pass

def OrderTracking():
    """
    This function is to monitor the status of placed orders
    """
    pass

def ProductReview():
    """
    This function is for customers to share feedback and suggestions about purchased products.
    """
    pass

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
    
    firstName = input("Please enter first name: ")
    lastName = input("Please enter last name: ")
    userName = input("Please enter username: ")
    dateOfBirth = input("Please enter date of birth: ")
    password = input("Please enter password: ")

    print(user_dict)

    # with open(os.path.join(data_filepath,"userAccount.txt"), "w") as file:
    #     newData = ""
    #     print(file)

if __name__ == "__main__":
    Customer()