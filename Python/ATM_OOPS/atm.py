class ATM:
    
    # first cal constructor
    # for encapsulation we used __ before variable /methods 
    # for data hiding we used to private the data variable and public the method 
    #in python noone is completely private
    # for that we use getter setter function present

    def __init__(self):
        self.__pin = ""
        self.__balanace = 0

        self.__menu()
    
    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("Your Atm pin updated successfully")
        else:
            print("TypeError! type not supported")
    
    # create menu methods
    def __menu(self):
        user_input = input(
            """
            Hello, How would you like to proceed?
            1. Press 1 for create pin.
            2. Press 2 for diposit money.
            3. Press 3 for withdraw money.
            4. Press 4 for checek balance.
            5. Press 5 for exit.
            """
        )
        if user_input == "1":
            self.create_pin()
            # self.__menu()
        elif user_input == "2":
            self.deposit_money()
            # self.__menu()
        elif user_input == "3":
            self.withdraw_money()
            # self.__menu()
        elif user_input == "4":
            self.check_balance()
            # self.__menu()
        else:
            print("Exit")
        
    def create_pin(self):
        self.__pin = input("for creation, Enter your pin: ")
        print("ATM pin created successfully")
    
    def check_auth(self):
        pin = input("Enter your pin: ")
        if self.__pin == pin:
            return True
        else:
            return False

    def deposit_money(self):
        if self.check_auth():
            amount = int(input("Enter deposit amount: "))
            self.__balanace += amount
            print(f"{amount} created successfully")
        else:
            print("Invalid pin!")
    
    def withdraw_money(self):
        if self.check_auth():
            amount = int(input("Enter amount to be withdrawn: "))
            if self.__balanace >= amount:
                self.__balanace -= amount
                print(f"{amount} debited from your bank")
            else:
                print("Insufficient balanace")
        else:
            print("Invalid balanace")
        

    def check_balance(self):
        if self.check_auth():
            print(f"Your current balnace is {self.__balanace} Rs.")
        