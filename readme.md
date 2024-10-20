# Operatorsin Python
1- Arithmetic
Operators:
1- '+'
2- '-' 
3- '*'
4- '/' (For float datatype)

list attribute in python allows us to store data in a single variable 

Command To build a docker image: 
docker build -f Dockerfile -t my-first-image .

Practice Code for text manipulation:
#print(text1 + text2) 
casefolded_text = text1.capitalize()
#print(casefolded_text)
centered_text1 = text1.center(10, '*')
#print(centered_text1)
centered_text2 = text2.center(10,"*")
#print(centered_text2)
count_a= text1.count("l")
#print(count_a)
endoded_text = text2.encode("utf-8")
#print(endoded_text) 

Lecture#5:
name = input('Enter your name:')
#age = int(input('Enter your age:'))
#String functions:
#result_not_equal: bool = 5!=5
#print(result_not_equal)

#print('My name is %s and my age is %d' %(name, age))
#print(id(name))

Practice Code:
weather : str = "Rainy"

if weather == "sunny":
    print("It's a beautiful day! Go for a walk.")
else:
    print("Read the book, you can't go out in this weather") 

Practice Code:
first_number : int = 30
second_num : int = 20 

score : int = 30

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
