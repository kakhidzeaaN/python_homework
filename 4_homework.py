# 1st exercise
# ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე
# ინფორმაცია საკუთარი სახელის, გვარის და ასაკის
# შესახებ. თითოეული მომხმარებლის ინფორმაცია
# შეინახე ინდივიდუალურ სიაში. შემდეგ კი სამივე სია
# დაამატე საერთო ცალრიელ სიას სახელად consumer_info.
# Input_ის მეშვეობით მომხმარებლის ინდექსის შეყვანის
# შემთხვევაში პროგრამამ უნდა დაბრუნოს არჩეულ
# მომხმარებელზე ინფორმაცია შემდეგნაირად:

N_list = []
S_list = []
A_list = []
for i in range(0, 3):
    name = input("Enter your name: ")
    N_list.append(name)
    surname = input("Enter your surname: ")
    S_list.append(surname)
    age = input("Enter your age: ")
    A_list.append(age)

consumer_info = N_list + S_list + A_list

x = int(input("enter the index here: "))
if x in range(0, 3):
    print(F"Name: {N_list[x]}\nSurname: {S_list[x]}\nAge: {A_list[x]}")
else:
    print("There is no element with this index here!")

# 2nd exercise
# შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული
# ცნობილი მსახიობების შესახებ ინფორმაცია.
# მომხმარებელს შემოჰყავს მსახიობის სახელი ან გვარი.
# თუ სიაში მოიძებნა მსახიობი, დაბეჭდe მის შესახებ
# არსებული ინფორმაცია რეზუმის სახით.

star_info = [
    {"name": "Jack",
     "surname": "Nicholson",
     "age": "78"},
    {"name": "Morgan",
     "surname": "Freeman",
     "age": "80"},
    {"name": "Sophie",
     "surname": "Marceau",
     "age": "75"}
    ]
name = input("Enter name: ")
surname = input("Enter surname: ")
i = 0
while i < len(star_info):
    if name == star_info[i]["name"].lower() or surname == star_info[i]["surname"].lower():
        print(star_info[i])
    i += 1

# კითხვა??
# print("That person is not in the list!")
# ეს როგორ დავპრინტო ერთხელ, როცა ინფუთი არაა სიაში


# 3rd exercise
# შექმენი ფუნქცია რომელიც მიიღებს სიას და
# დააბრუნებს ასევე სიას, თუმცა უნიკალური
# ელემენტებით (გამოიყენე set მონაცემთა ტიპი).
#
def unique_list(x):
    list_to_set = set(x)
    return list_to_set


mylist = [9, 7, 7, 6, 6, "a", "a", "Anna", "Name", "name", "name"]
print(list(unique_list(mylist)))


# 4th exercise
# შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის
# მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს
# tuple ტიპის მონაცემად და დააბრუნებს შედეგს.
# def set_to_tuple():
# ...
# return ...

def set_to_tuple(set1, set2):
    set3 = set1.union(set2)
    return tuple(set3)


set1 = {10, 15, 20}
set2 = {"green", "yellow"}
print(set_to_tuple(set1, set2))

# 5th exercise
# დაწერე პროგრამა, რომელიც შეამოწმებს გადაცემული
# ლექსიკონი არის თუ არა ცარიელი.


def empty_dict(x):
    if not x:
        return "Dictionary is empty"
    else:
        return "Dictionary contains items"


my_dict = {22, 67}
print(empty_dict(my_dict))

# 6th exercise
# დაწერე პროგრამა რომელიც სტრიქონისგან ქმნის
# ლექსიკონს.
# დათვალე სტრიქონში კონკრეტული სიმბოლოს
# ოდენობა.

def str_to_dict(x):
    my_dict = {}
    for i in x:
        if i in dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    return my_dict


print(str_to_dict("W3schools"))
