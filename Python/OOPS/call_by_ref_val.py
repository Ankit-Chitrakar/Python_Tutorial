
import copy

class Customer:

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "My name is {}".format(self.name)
    
    def copy(self):
        return copy.copy(self)

def greet(customer):  # if we pass refence then customer == cust but if we pass only value then cust != customer
    customer.name = "Tiasa Chitrakar"  # if we pass ref then the cust object will also change but if va;ue then not cgange original obj
    print(customer.name)  # This will be Tiasa Chitrakar if ref else Arpan ghosh



print("-------------------------Call by Refernce------------------------------")

cust = Customer("Ankit Chitrakar")

print(cust.name) # Ankit Chitrakar
greet(cust) # Pass by Refernce of the object of cust
print(cust.name)  # This is also give Tiasa Chitrakar


# Call by value 
# Just give the value by copy method

print("-------------------------Call by Value------------------------------")

cust2 = Customer("Arpan Ghosh")
print(cust2)
greet(cust2.copy())
print(cust2.name)
