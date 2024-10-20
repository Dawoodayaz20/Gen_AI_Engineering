"""
students : list[str] = ["Rehan", "Ali", "Ahmad", "Mazhar"]
print(students[0]) 
# Append a new student
students.append("Usman") 
print(students)
# Pop the last student
students.pop()
print(students)
# Remove a specific student by name
students.remove("Rehan")
#Slicing with Indexes: 
Msg = str("LongLivePakistan!")
part1 = Msg[0:4]
part2 = Msg[4:8]
part3 = Msg[8:16]
print(Msg)
print(part1)
print(part2)
print(part3)


classroom : list = [
    ["Rehan", [85, 90, 88]],
    ["Mazhar", [50, 80, 70]],
    ["Usman", [92, 72, 81]],
    ["Zia", [80, 70, 75]]
]

print(classroom[1][1])


Boys = ["Alice", "Bob", "Charlie", "David", "Eve"]  # and so on, up to 50 names

for friend in Boys:
    print(f"Hi {friend}, you’re invited to my birthday party!")

Close_friends = ["Hamza", "Faizan", "Ali", "Hammad"]
Friends = ["Sahil", "Wahab", "Sami", "Ahmed"]

for Close_friend in Close_friends:
    print(f'Hey! {Close_friend}, You are invited in the party, I will be happy to see you')
    

names = ["Alice", "Bob", "Charlie"]
ages = [23, 54, 45, 56]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")


condition = ""
while condition != "exit!":
    user_in = input("Enter command:")
    if user_in != "exit!":
        print(user_in)
    elif user_in == "exit!":
        print("Exiting the program")

for table_nmbr in range(2, 11):
    for inner_table in range(1, 10):
        if table_nmbr==5 and inner_table == 5:
            continue
        print(f"{table_nmbr} x {inner_table} = {table_nmbr * inner_table}")
    print("")


#list comprehensions: 
sqr : list = [x**2 for x in range (1, 11)]
print(sqr) 
Msg = str("LongLivePakistan!")
part1 = Msg[0:4]
part2 = Msg[4:8]
part3 = Msg[8:16]
print(part1)
"""

#Class:08
student_scores = {"Alice": 85,"Bob": 92, "Charlie": 78}
for score in student_scores:
    print(f"key is {score} and corresponding value is {student_scores[score]}")
print(student_scores["Alice"]) #Output 85 


names = {True: {1:"Rehan"}, False: ["Rehan","Usman"], False: "Mazhar"}
print(names[False])

del student_scores["Alice"]
print(student_scores)



