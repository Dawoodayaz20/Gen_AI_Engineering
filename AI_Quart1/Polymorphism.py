# Polymorphism
# Poly means "many" and morphism means "forms".

class Human():
    def eat (self):
        print("Human Eats")
        
class Animal():
    def eat (self):
        print("Animal eats")

Human_obj = Human()
Animal_obj = Animal()


def eat_funct(obj):
    obj.eat()

eat_funct(Human_obj)
eat_funct(Animal_obj)
