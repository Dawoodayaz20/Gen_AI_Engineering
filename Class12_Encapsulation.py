# Protected Attribute :
class MyClass():
  def __init__(self, name):
    self._name = name

obj = MyClass('Dawood')
print(obj._name)
#To access the protected attribute of a class, we have to write it with the underscore.

# Private Attribute:
# class MyClass():
#   def __init__(self, name):
#     self.__name = name # It is the private attribute

#   def get_acount_no(self):
#     return f"The Account number of {self.name} is {self.__account_no}"
# In this way, we cannot access this attribute bacause it is private.
# obj = MyClass('Dawood')
# print(obj.name)++++++ 