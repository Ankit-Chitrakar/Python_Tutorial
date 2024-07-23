class Fraction:

    # Constructor
    def __init__(self, num, den):
        self.num = num
        self.den = den

    # magic method to print
    def __str__(self):
        return "{}/{}".format(self.num, self.den)
    
    # magic method to add
    def __add__(self, other):
        temp_num = self.num *  other.den + other.num * self.den
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num, temp_den)

    # magic method to subtract
    def __sub__(self, other):
        temp_num = self.num *  other.den - other.num * self.den
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num, temp_den)
    
    # magic method to multiply
    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num, temp_den)
    
    # magic method to division
    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num

        return "{}/{}".format(temp_num, temp_den)
 