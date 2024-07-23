# Static variable is called class variable --> shared memory 

class Person:

    # static variable # make it private
    __userid = 0

    def __init__(self, name):
        self.name = name

        # userid ++
        Person.__userid += 1

    @staticmethod
    def get_userid():
        return Person.__userid
    
    @staticmethod
    def set_userid(update_id):
        if type(update_id) == int:
            Person.__userid = update_id
        else:
            print("TypeError! put a valid number.")
    
    def __str__(self):
        return "{}: {}".format(Person.__userid, self.name)
    
ankit = Person("Ankit Chitrakar")
print(ankit)
tiasa = Person("Tiasa Ash")
print(tiasa)
arpan = Person("Arpan Ghosh")
print(arpan)
sandy = Person("Soumen Mondal")
print(sandy)
sandy.set_userid(6)
print(Person.get_userid())
anirban = Person("Anirban Patra")
print(anirban)

    
