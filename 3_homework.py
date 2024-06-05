# 1st exercise
def triple_function():
    x = input("What's your favorite word? ")
    print(x*3)


triple_function()

# 2nd exercise
def my_weight():
    x = int(input("How much do you weigh in kg? "))
    print("your weight on moon will be: ", x/6, "kg")


my_weight()

# 3rd exercise
All_operations =["+", "-", "*", "/"]
def my_calculator():
    num1 = input("Enter first number here: ")
    operation = input("Enter your operation here: ")
    num2 = input("Enter second number here: ")
    if num1.isdigit() and num2.isdigit():
        if operation in All_operations:
            if operation == "+":
                return int(num1) + int(num2)
            elif operation == "-":
                return int(num1) - int(num2)
            elif operation == "*":
                return int(num1) * int(num2)
            elif operation == '/':
                if num2 == '0':
                    print("nolze gayofa ar sheidzleba")
                else:
                    return int(num1) / int(num2)
        else:
            print("Not valid operation")
    else:
        print("Please enter the number!")


print(my_calculator())
