# Classes:

# attributes/variables
# methdos/functions 

class person:
    def __init__(self, name, hobby):
        # self makes a link with the object with the class variables
        self.cname = name 
        self.hobby = hobby
    
    def display_info(self):
        print(f"My name is {self.cname} and {self.hobby}")


# Creating an object:
new_person = person("Rehan", "He never studies")

new_person.display_info()


# Practice Coding:
class Person2:
    def __init__(self, name, habbit):
        self.name = name
        self.habbit = habbit

    def interest(self):
        print(f"My name is {self.name} and my habbit is {self.habbit}")

another_person = Person2("Usman", "I never practice coding at home")
another_person.interest()

