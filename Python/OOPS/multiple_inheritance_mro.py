# Multiple inheritance supported in python

class Phone:
    def __init__(self, price, brand, camera_px):
        self.price = price
        self.brand = brand
        self.camera_px = camera_px
    
    def buy(self):
        print(f"Phone Buy, {self.brand}")

class Product:
    def buy(self):
        print(f"Product Buy, {self.brand}")

class Smartphone(Phone, Product):  # ordering is importing who is firts their buy method will executed if their is a mismatch
    pass

m1 = Smartphone(20000, "Apple", 48)
m1.buy()

# This called MRO (Method Resolution Order)