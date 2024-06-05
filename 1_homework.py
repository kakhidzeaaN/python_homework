# 1st exercise
a = input("Tell me your name: ")
b = input("Tell me your surname: ")
c = int(input("Log your age here: "))
d = input("Enter your city here: ")
doc = f"""
Name: {a.capitalize()}
Surname: {b.capitalize()}
Age: {c}
City: {d.capitalize()}
"""
print(doc)


# 2nd exercise
a_fruit = input("Log the name of the first fruit: ")
b_fruit = input("Log the name of the second fruit: ")
c_fruit = input("Log the name of the third fruit: ")
print(a_fruit.capitalize()+"//"+b_fruit.capitalize()+"%%"+c_fruit.capitalize())


# 3rd exercise
text = input("Enter your text here: ")
print("Number of symbols:", len(text))


# 4th additional exercise
n = input("Tell me your name: ")
s = input("Tell me your surname: ")
print(n.capitalize(), s.capitalize())


# 5th additional exercise
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num = num1**num2
print(num)