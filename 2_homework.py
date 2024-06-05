# 1st exercise
print("რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს დღესაც?")
answer = input("1.შუმერთა\n2.სელჩუკთა\n3.რომის\n4.მონღოლთა\n")
if answer == "3" or answer == "რომის":
    print("სწორია!")
else:
    print("არა! სწორი პასუხია რომის!")


# 2nd exercise
print("მაღაზიაში არის ლეპტოპები, პერსონალური კომპიუტერები და მობილურები, რომელი გნებავთ?")
answer = input("1.ლეპტოპი\n2.პერსონალური კომპიუტერი\n3.მობილური\n")
print("რა არის მაქსიმალური თანხა, რომელსაც გადაიხდით? ")
cost = int(input("<300\n300-500\n500-1000\n>1000\n"))
while cost <= 300:
    print("სამწუხაროდ, ამ თანხაში შეთავაზება არ გვაქვს!")
    break
while 300 < cost < 500:
    if answer == "1" or answer == "ლეპტოპი":
        print("ამ ფასად შეძლებთ ლენოვოს ყიდვას!")
        break
    elif answer == "2" or answer == "პერსონალური კომპიუტერი":
        print("შეგვიძლია შემოგთავაზოთ პენტიუმ 5")
        break
    elif answer == "3" or answer == "მობილური":
        print("თქვენ მაგ ფასად შეიძენთ ჰუავეის მობილურს")
        break
while 500 <= cost <= 1000:
    if answer == "1" or answer == "ლეპტოპი":
        print("ამ ფასად შეძლებთ hp-ს ყიდვას!")
        break
    elif answer == "2" or answer == "პერსონალური კომპიუტერი":
        print("შეგვიძლია შემოგთავაზოთ პენტიუმ 10")
        break
    elif answer == "3" or answer == "მობილური":
        print("თქვენ მაგ ფასად შეიძენთ samsung-ის მობილურს")
        break
while cost > 1000:
    if answer == "1" or answer == "ლეპტოპი":
        print("ამ ფასად შეძლებთ macbook-ის ყიდვას!")
        break
    elif answer == "2" or answer == "პერსონალური კომპიუტერი":
        print("შეგვიძლია შემოგთავაზოთ პენტიუმ 15")
        break
    elif answer == "3" or answer == "მობილური":
        print("თქვენ მაგ ფასად შეიძენთ iphone-ის მობილურს")
        break

# 3rd exercise, Quest about Georgia's bright future
print("Welcome, dear player! Let's see what kind of future will you end up with!")
while True:
    answer = input("Are you the member of current Georgian authority? ")
    if answer.lower() == "yes":
        print("Welcome, the member of parliament")
        print("You've entered the reality where you see two doors, which one would you like to open? ")
        command = input("Your command: ")
        if command.lower() == "west":
            print("This door takes you to the European Union, but there is one thing "
                  "you need to do, would you like to pursue the game? ")
            option = input("Continue or not: ")
            if option.lower() == "continue" or option.lower() == "yes":
                print("Please sign off on russian law!")
                response = input("there are 3 case scenarios: 1. reject the law, 2. don't reject the law\n"
                                 "3. don't reject the law and regret about it in the future,\n"
                                 "choose the most suitable for you: ")
                if response.lower() == "1":
                    print("Welcome to the EU, prosperity and freedom of choice!")
                    break
                elif response.lower() == "2":
                    print("A big rock fell on your head, you entered Russian federation with big bump on your forehead\n"
                          "russian ambulance took you to the hospital, most probably you will end up dying there,\n"
                          "because of incompetence of medical stuff")
                    break
                elif response.lower() == "3":
                    print("You spend rest of your life in embarrassment and humiliation, looks like there is still hope for your soul!")
                    break
                else:
                    print("Your choice in not included in the suggestions! Try respond appropriately")
            else:
                print("It was obvious you were coward from the beginning!")
                break
        elif command.lower() == "north":
            print("Are you sure you want to go back to Soviet union?!\n"
            "Try again, Vanya or Slava to be!")
        else:
            print("If you couldn't choose WEST, then zdravstvui, vanya!")
            break
    elif answer.lower() == "no":
        print("Welcome citizen of Georgia! I am sure you have pro european course! We will win valiantly!")
        break
    else:
        print("Your response in undetermined! TRY AGAIN")


# 4th additional exercise
print("In order to choose the right profession for you\n"
      "I will ask you few questions")
print("Did you like Math? ")
answer = input("Agree or disagree here: ")
if answer.lower() == "yes":
    print("would you like to teach or to explore?")
    answer1 = input("")
    if answer1 == "1":
        print("you can choose several technical subjects and\n"
              "teach them either at university or at school")
    elif answer1 == "2":
        print("You can become a scientist!")
    else:
        print("Try to choose from options!")
elif answer.lower() == "no":
    print("Do you like history and related subjects?")
    answer1 = input("1.history, 2.geography,or maybe astronomy\n")
    if answer1.lower() == "history" or answer1.lower() == "1":
        print("You could explore the earth!")
    else:
        print("Knowledge in modern world and universe is not less exciting!")
elif answer.lower() == "something else" or answer.lower() == "other":
    print("Maybe you are into arts, and could become artist or art appraiser!\n"
          "Do you sing?")
    answer2 = input("agree or disagree here: ")
    if answer2.lower == "yes":
        print("The career of singer can make you famous nowadays!")
    else:
        print("If not singing, there are many other directions within art you could choose\n"
              "dancing maybe")
else:
    print("If you aren't interested in none of the above, maybe you would like to be a looser, your choice")
