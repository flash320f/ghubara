game_running = True

while game_running:
    level = "1"

    if level == "1":
        print("Welcome to \"Ghubara\" traveler. Your wisdom has chosen your fate to save the cosmic princess!")
        print("There will be five challenges you have to complete for you to save the Cosmic Princess")
        print("You want a spaceship to embark on your majestic travels, answer the question and you shall receive it")
        q_1 = str(input("The biggest planet in our solar system is: "))
        q_1 = q_1.lower()
        if q_1 == "jupiter":
            print("Congrats, you are given the spaceship!")
            level = "2"
        else:
            print("Wrong answer! (Hint: It starts with a \"J\")")
    print()
    if level == "2":
        print("Moving to second level, you encounter some challenges in your space journey!")
        print("An asteroid comes your way at a velocity of 5m/s and its distance from ship is 15 meters, What is the reaction time before which the asteroid hits if you don't do something?")
        time = float(input("Time for reaction: "))
        while level == "2":
            if time == 3:
                print("U a smart guy! Move to next level")
                level = "3"
            else:
                print("Try Again!!!")
                time = float(input("Time for reaction: "))
    print()
    if level == "3":
        print("Things are getting srios!!")
        print("The big bad space guy traps you in a puzzle and the only way out is to read his mind!")
        print("Guess the number inside their mind to move to level four!")

        number = 27
        guess = int(input("Guess the number 1-50: "))
        while guess != number:
            if guess == number:
                print("Wooww! you are so smartt!")
                print("Moving to level 4")
            elif guess < number:
                print("U r close but a bit low")
                #guess = int(input("Try again!: "))
            else:
                print("U r close but a bit high")
                #guess = int(input("Try again!: "))
            guess = int(input("Try again!: "))
        level = "4"
    print()
    if level == "4":
        print("Now at level 4")
        print("Lets get personal! hehe ;)")
        print("To pass this level you need to guess the topic of my interest")
        print("a. Space","\nb. Ocean", "\nc. Country songs\n")
        user_mind = input("Enter a or b or c: ")
        while user_mind != "a":
            if user_mind == "a":
                print("U know me well ;))")
                level = "5"
            elif user_mind == "b":
                print("Umm its cool but not on my top interest!")
                user_mind = input("Enter a or b or c: ")
            elif user_mind == "c":
                print("srsly! what made u think that option!")
                user_mind = input("Enter a or b or c: ")
            else:
                print("Invalid entry")
                user_mind = input("Enter a or b or c: ")
            #user_mind = input("Enter a or b or c: ")
        level = "5"
    print()
    if level == "5":
        print("This level sinks u to a dungeon, navigate your way through!")
        print("U see two paths, one is leading to red lit mountains and the other to forest")
        print("Find the portal, there maybe other paths")
        path = "dungeon"
        cosmic_gold = 0
        while path == "dungeon":
            chose_path = input("Enter 1 for mountain and 2 for forest: ")
            #cosmic_gold = 0
            if chose_path == "1":
                print("U enter mountains but a ghost follows u")
                print("U see a sword")
                pick = input("1 to pick sword and 2 to do nothing: ")
                if pick == "1":
                    print("The ghost gets scared and attacks u, ultimately kling u")
                    path = "dungeon"
                    cosmic_gold = 0
                elif pick == "2":
                    print("ignrng smth that doesn't bother is best choice!")
                    print("The ghost leaves u with four sacks of cosmic gold")
                    cosmic_gold = 4
                    print("An old board leads u back to dungeon start!")
                    print("MAybe the forest has the portal!")
                    path = "dungeon"
            #cosmic_gold = cosmic_gold
            if chose_path == "2":
                print("A fairy asks u for ur name while u navigate the forest")
                answer = input("1 for ignore and 2 for answer: ")
                if answer == "1":
                    print("Gd job, never trust fairies!")
                    print("You see the fairy turn into a portal")
                    print("u jump into portal")
                    if cosmic_gold == 4:
                        print("Nice! ur gold was used as fuel to transport u")
                        level = "passed"
                        if level=="passed":
                            print("congrats!"*3, "\nU saved the princess by simply reaching her")
                            game_running = False
                            path = "passed"
                    elif cosmic_gold != 4:
                        print("Wait! u need cosmic gold as fuel for travelling through portals")
                        print("Ancient rumors have it that red lit mountains have'em")
                        path = "dungeon"
                elif answer == "2":
                    print("Strngr Dangr Strng Dngr")
                    print("The fairy devours ur soul - turns out it was a bad fairy")
                    path = "dungeon"
        print("Goodbye")