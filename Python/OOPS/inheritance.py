# following is a relationship

class User:
    def registration(self):
        print("Registration")
    
    def login(self):
        print("Login")

# Syntax of inheritance this is subclass of User
class Student(User):
    def enroll(self):
        print("Enroll")
    def review(self):
        print("Review")

st1 = Student()
st1.registration()
st1.login()
st1.enroll()
st1.review()

