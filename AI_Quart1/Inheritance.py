# Parent Class:
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

# Child Class:
class Admin(User):
    def __init__(self, username, email, accessLevel):
        #Super is our parent class which links the child class to the parent.
        #without super, we can not access the parent attributes in the child class.
        super().__init__(username, email)
        self.accessLevel = accessLevel
        print("Child constructor called")

user01 = Admin("Rehan", "abs@gmail.com", "full access")

class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, breed)
