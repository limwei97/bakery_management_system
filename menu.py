from entities.customer import Customer
from entities.baker import Baker
from entities.cashier import Cashier
from entities.manager import Manager
import constant

def main():
    try:
        while True:
            print("--- Bakery Management System ---")
            print("1.Manager\n2.Customer\n3.Cashier\n4.Baker\n5.Exit")
            userAction = input("Please select action: ")
            if userAction =='':
                break
            userAction = int(userAction)
            if userAction == constant.CUSTOMER:
                Customer()
            elif userAction == constant.BAKER:
                Baker()
            elif userAction == constant.MANAGER:
                Manager()
            elif userAction == constant.CASHIER:
                Cashier()
            elif userAction == constant.EXIT:
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
            input()
    except:
        print("Please refer to any error raised above")


if __name__ == "__main__":
    main()