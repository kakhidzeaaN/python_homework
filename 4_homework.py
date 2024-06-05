# 1st exercise
# ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე
# ინფორმაცია საკუთარი სახელის, გვარის და ასაკის
# შესახებ. თითოეული მომხმარებლის ინფორმაცია
# შეინახე ინდივიდუალურ სიაში. შემდეგ კი სამივე სია
# დაამატე საერთო ცალრიელ სიას სახელად consumer_info.
# Input_ის მეშვეობით მომხმარებლის ინდექსის შეყვანის
# შემთხვევაში პროგრამამ უნდა დაბრუნოს არჩეულ
# მომხმარებელზე ინფორმაცია შემდეგნაირად:
# Name: Elene
# Lastname: Khardava
# Age: 21
# N_list = []
# S_list = []
# A_list = []
# for i in range(0, 3):
#     name = input("Enter your name: ")
#     N_list.append(name)
#     surname = input("Enter your surname: ")
#     S_list.append(surname)
#     age = input("Enter your age: ")
#     A_list.append(age)
#
# consumer_info = N_list + S_list + A_list
#
# x = int(input("enter the index here: "))
# if x in range(0, 3):
#     print(F"Name: {N_list[x]}\nSurname: {S_list[x]}\nAge: {A_list[x]}")
# else:
#     print("There is no element with this index here!")

# 2nd exercise
# შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული
# ცნობილი მსახიობების შესახებ ინფორმაცია.
# მომხმარებელს შემოჰყავს მსახიობის სახელი ან გვარი.
# თუ სიაში მოიძებნა მსახიობი, დაბეჭდe მის შესახებ
# არსებული ინფორმაცია რეზუმის სახით.

# star_info = ['Jack Nicholson', 'Morgan Freeman', 'Sophie Marceau', 'Brad Pitt']
# names = []
# surnames = []
# for i in range(0, len(star_info)):
#     names.append(star_info[i].split()[0])
#     surnames.append(star_info[i].split()[-1])
#     # print(names)
#     x = input("Enter star name or surname here: ").lower()
#     if x in names:
#         print(x)
#         # print(names.index(x))
#     else:
#         print("No!")
#
# print(names)
# nam = names
# print(nam)

# names = ['ann', 'bb', 'dd']
# x = input("enter name: ").lower()
# if x in names:
#     print(names.index(x))
# else:
#     print("no!")


    # print(F"Your desired actors name is {names[x]} and surname is {surnames[i]}")
# else:
#     print("Than person is not in the list!")
# print(names)
# print(surnames)


# 3rd exercise
# შექმენი ფუნქცია რომელიც მიიღებს სიას და
# დააბრუნებს ასევე სიას, თუმცა უნიკალური
# ელემენტებით (გამოიყენე set მონაცემთა ტიპი).
#
# def unique_list():
# ...
# return ...

# def unique_list():
    