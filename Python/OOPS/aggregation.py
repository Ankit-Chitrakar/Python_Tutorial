# this represent has a relationship 
#  here we implement two classes (Customer, Address) --> Customer has Address

class Customer:
    # constructor 
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
    
    # used for print
    def __str__(self):
        return "Hello, my name is {}, I am {} years old. Gender is {} and I am living in {}".format(self.name, self.age, self.gender, self.address)
    
    # use Aggregation
    def edit_profile(self, name, age, gender, new_city, new_state, new_pin):
        self.name = name
        self.age = age
        self.gender = gender
        self.address.change_address(new_city, new_state, new_pin)

class Address:
    def __init__(self, city, state, pin):
        self.city = city
        self.state = state 
        self.pin = pin
    
    def __str__(self):
        return "{}, {}, {}".format(self.city, self.state, self.pin)
    
    # edit_profile use this method to edit address
    def change_address(self, new_city, new_state, new_pin):
        self.city = new_city
        self.state = new_state
        self.pin = new_pin


cust1_add = Address("Kolkata", "West Bengal", "700149")
cust1 = Customer("Ankit Chitrakar", 21, "Male", cust1_add)   
print(cust1)

cust1.edit_profile("Tiasa Ash", 22, "Female", "Boubazar","West Bengal", "700012")
print(cust1)