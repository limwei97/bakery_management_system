from entities.customer import Customer

def main():
    MANAGER = 1
    CUSTOMER = 2
    CASHIER = 3
    BAKER = 4
    while True:
        print("==Bakery Management System==")
        print("1.Manager\n2.Customer\n3.Cashier\n4.Baker")
        #validation
        userAction = int(input("Please select action: "))
        if userAction == CUSTOMER:
            Customer()
        input()

        #control to break from while loop

if __name__ == "__main__":
    main()