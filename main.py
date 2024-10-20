print("Hello Jarvis") 

students = ["Ali", "Usman", "Mazhar", "Rehan"]

students.append("Ahmed")
print(students)


def add(x, y):
    if x>10 and y > 10:
        print("Hello")
        return
    else:
        return x + y

print(add(12, 20))


def return_multi_value ():
  x = 4 
  y = 5
  return x, y

print(return_multi_value())