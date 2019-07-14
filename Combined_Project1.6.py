import random
class Player:
    def __init__(self, name="User1", health= 100):
        self.name = name
        self.health = health

    def minusHealth(self):
        if self.health>=100:
            self.health-=100
    def display_player(self):
        return "Your health is: "+ str(self.health)

def challenge_dice():
    '''challenge 1 function'''
    print("You come to a passage in the maze that is blocked")
    print("by a very large raccoon. He has a top hat on and")
    print("is holding a large suitcase. He is smiling at you.")
    print("You have two options:")
    print("1) Attack the raccoon")
    print("2) Ask the raccoon politely to move to the side")
    print("--------------------------------------")
    user_input = input("Choose 1 or 2: ")
    # while loop (7 points)
    while user_input != "1" and user_input != "2":
        print("That is not a correct option silly. Try Again.")
        print("You have two options:")
        print("1) Attack the raccoon")
        print("2) Ask the raccoon politely to move to the side")
        print("--------------------------------------")
        user_input = input("Choose 1 or 2: ")
    if user_input == "1":
        print("You run at the large raccoon flailing your hands")
        print("As you get close, the raccoon slaps you with his suitcase")
        print("You get slammed into the wall of the maze and slump to the ground")
        print("GAME OVER")
        quit()
    elif user_input == "2":
        print("The raccoon laughs at you, and tells you the only")
        print("way he is moving is if you can beat him in dice!")
        print("He says his name is Grits n' Gravy and he is the champion")
        print("of the World Series of Dice!")
        print("If you win you get to continue through the maze")
        print("but if you lose, you will become Grits n' Gravy's slave forever!")
        print("You have two options:")
        print("1) Play dice with Grits n' Gravy")
        print("2) Attack Grits n' Gravy")
        print("--------------------------------------")
        user_input_2 = input("Choose 1 or 2: ")
        while user_input_2 != "1" and user_input_2 != "2":
            print("That is not a valid option silly. Try Again.")
            print("You have two options:")
            print("1) Play dice with Grits n' Gravy")
            print("2) Attack Grits n' Gravy")
            print("--------------------------------------")
            user_input_2 = input("Choose 1 or 2: ")
        if user_input_2 == "1":
            print("Grits n' Gravy shouts in excitement! and proceeds")
            print("to open his large suitcase which becomes a dice board!")
            print("Grits n' Gravy says: the rules are simple, we both roll")
            print("6 20-sided dye, the player with the largest 3 numbers added")
            print("up wins!")
            print("Grits n' Gravy hands you six dice and tells you to roll first")
            print("You roll them all at once and watch in nervousness as they roll")
            print("--------------------------------------")
            # List (10 points)
            dice_roll = []
            for x in range(6):
                # random number generator (10 points)
                roll = random.randint(1, 20)
                dice_roll.append(roll)
            print("Your dice rolls are:", dice_roll)
            print("Grits n' Gravy sneers, that was a good roll, but now its my turn!")
            dice_roll_grits = []
            for x in range(6):
                roll_g = random.randint(1, 20)
                # using built in list functionality (3 points)
                dice_roll_grits.append(roll_g)
            print("Grits n' Gravy's dice rolls are:", dice_roll_grits)
            print("Grits n' Gravy says: now its time to see who wins!")
            print("--------------------------------------")
            # sorting through the contents of a list (20 points)
            # nested loops (12 points)
            # for loop (7 points)
            for i in range(0, len(dice_roll)):
                for j in range(i, len(dice_roll)):
                    if dice_roll[j] > dice_roll[i]:
                        temp = dice_roll[i]
                        dice_roll[i] = dice_roll[j]
                        dice_roll[j] = temp
            for i in range(0, len(dice_roll_grits)):
                for j in range(i, len(dice_roll_grits)):
                    if dice_roll_grits[j] > dice_roll_grits[i]:
                        temp = dice_roll_grits[i]
                        dice_roll_grits[i] = dice_roll_grits[j]
                        dice_roll_grits[j] = temp
            dice_sum = dice_roll[0] + dice_roll[1] + dice_roll[2]
            dice_grits_sum = dice_roll_grits[0] + dice_roll_grits[1] + dice_roll_grits[2]
            if dice_sum >= dice_grits_sum:
                print("your three largest dice summed is:", dice_sum, "!")
                print("and that's greater than Grits n' Gravy's dice summed:", dice_grits_sum)
                print("Grits n' Gravy says: Ok ok, I don't know how you beat me")
                print("but I am a man of my word, you can continue through the maze")
                print("Grits n' Gravy moves to the side and you continue through the maze")
                print("-----------------------------------------------")
            else:
                print("Your three largest dice summed is:", dice_sum, "!")
                print("and that's less than Grits n' Gravy's dice summed:", dice_grits_sum)
                print("Oh no you lost! Grits n' Gravy laughs: you are now my slave forever!")
                print("-----------------------------------------------")
                print("GAME OVER")
                quit()
        else:
            print("You run at Grits n' Gravy flailing your hands")
            print("As you get close, Grits n' Gravy slaps you with his suitcase")
            print("You get slammed into the wall of the maze and slump to the ground")
            print("-----------------------------------------------")
            print("GAME OVER")
            quit()

def doggo_challenge():
    print("Congratulations! You have made the right turn!")
    print("You come to a passage in the maze that is blocked")
    print("by a German Shepherd with nunchucks. You notice she is upset")
    print("")
    print("Doggo: ...ugh I have to deal with you, stupid human")

    print("-----------------------------------------------")
    print("You have two options:")
    print("1) Attack Doggo")
    print("2) Pet Doggo")
    print("3) Talk with Doggo")
    print("4) Doggo's Stats")
    print("-----------------------------------------------")

    while True:
        try:
            userOption = eval(input("What do you do? (Choose 1, 2, 3, or 4): "))
            if userOption == 1:
                print("You run at Doggo flailing your hands")
                print("As you get close, Doggo uses her nunchucks and cracks open your skull")
                print("Your guts splatter on the walls of the maze")
                print("G A M E   O V E R")
                break
            elif userOption == 2:
                print("Oooh that feels nice. Yes get a little lower.")
                print("Doggo seems to be in a better mood")
                print("-----------------------------------------------")
            elif userOption == 3:
                print("Doggo: Hey you don't seem too bad kid. I'll let you pass without")
                print("hurting you if you can beat me in HangMan, otherwise I have some")
                print("hungry puppies to feed and they love little kids like you.")
                print('')
                print("1) Attack Doggo")
                print("2) Play HangMan")
                try:
                    userOption2 = eval(input("Do you want to play HangMan? "))
                    if userOption2 == 1:
                        print("You run at Doggo flailing your hands")
                        print("As you get close, Doggo uses her nunchucks and cracks open your skull")
                        print("Your guts splatter on the walls of the maze")
                        print("G A M E   O V E R")
                        break
                    else:
                        print("Doggo: YAY!!! My kids are tired of playing HangMan")
                        print("Try to guess the word I am thinking of. You have 10 guesses.")
                        print("If you guess a right letter, you stay on the guess number you're on")
                        hangMan()
                        break
                except:
                    print("Come on. Enter one or two.")
            else:
                print("Doggo has 25 Attack Points and 25 Defense Points.")
                print("She is a good girl.")
                print("-----------------------------------------------")
        except:
            print("Gosh you're being difficult. It's easy, ONE TWO OR THREE OR FOUR")
def hangMan():
    '''challenge 2 function 2'''
    # CODE USED: https://codereview.stackexchange.com/questions/95997/simple-game-of-hangman
    guess = input("guess a character:")
    words = ("hangman", "puppy", "meat", "doggo",
             "computer", "python", "program", "coding", "quesadilla")
    chosen_word = random.choice(words).lower()
    guessed_letters = []
    word_guessed = []
    for char in chosen_word:
        word_guessed.append("-")

    HANGMAN = (
        """
        -----
        |   |
        |
        |
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        |
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        |  -+-
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\
        |   |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\
        |   |
        |   |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\
        |   |
        |   |
        |  |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\
        |   |
        |   |
        |  |
        |  |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\
        |   |
        |   |
        |  | |
        |  |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\
        |   |
        |   |
        |  | |
        |  | |
        |
        --------
        """)

    print(HANGMAN[0])
    attempts = len(HANGMAN) - 1
    while (attempts != 0 and "-" in word_guessed):
        print(("\nYou have {} attempts remaining").format(attempts))
        joined_word = "".join(word_guessed)
        print(joined_word)
        try:
            player_guess = str(input("\nGuess a letter" + "\n> ")).lower()
        except:
            print("All I ask is that you enter a letter. Can you not do that?")
            continue
        else:
            if not player_guess.isalpha():
                print("We both know that's not a letter.")
                continue
            elif len(player_guess) > 1:
                print("Only enter one letter! Please!!!")
                continue
            elif player_guess in guessed_letters:
                print("You have already guessed that letter. Your memory is bad.")
                continue
            else:
                pass
        guessed_letters.append(player_guess)
        for letter in range(len(chosen_word)):
            if player_guess == chosen_word[letter]:
                word_guessed[letter] = player_guess
        if player_guess not in chosen_word:
            attempts -= 1
            print(HANGMAN[(len(HANGMAN) - 1) - attempts])
    if "-" not in word_guessed:
        print(("\nCongratulations! {} was the word").format(chosen_word))
        print("Doggo: Fine. You won fair and square. I will let you go.")
    else:
        print(("\nUnlucky! The word was {}.").format(chosen_word))
        print("Doggo: Now how do you preferred to be cooked? In stew or a filet?")
        print("G A M E  O V E R")
        quit()

def introToSnakeChallenge():
    '''challenge 3 function 1'''
    print("-----------------------------------------------")
    print("Congratulations! You have made the right turn!")
    print("After turning the corner, you find that you are faced with three different doors.\n"
          "A key is laid out in front of the doors,\n"
          "You notice that a folded paper note is attached to the key.\n"
          "You reach over to pick up the key and open the note.\n"
          "It reads as follows:\n")
    print("-----------------------------------------------")

    #changed wording of the riddle a little - Manju
    print("-----------------------------------------")
    print("EACH LOCK WILL ACT IN ACCORDANCE WITH THE KEY,\n"
          "THE WISEST CHOICE WILL LET YOU SEE\n"
          "THE TREASURE THAT LAYS BEYOND ONE DOOR,\n"
          "THAT WILL TRANSFORM YOU TO A KING WHO ONCE WAS DEBTOR.\n"
          "THERE IS ONE CHOICE THAT DOES NOT GUARANTEE DOOM\n"
          "BUT ONLY IF YOUR WITS SAVE YOU FROM YOUR TOMB.\n"
          "CHOOSE WRONG AND YOU’LL BE GONE\n"
          "WITH NOT A SOUL TO REMEMBER YOU BY THE NEXT MOON.\n")
    print("-----------------------------------------------")

    print("The key you hold is a master key that will open any of these doors.\n"
          "Out of the three doors, choose one to go through.\n"
          "Let's hope that luck is on your side!")

    # This is the part of code I fixed from my original code and it does the same
    # thing as the code that you guys wrote that is commented out. I'm just putting
    # this in here just in case, but we can use either! - Manju
    userDoorChoice = input("Enter a number between 1 and 3: ")
    while userDoorChoice:
        if userDoorChoice == '1':
            door1Snake()
            break
        elif userDoorChoice == '2':
            door2Success()
            break
        elif userDoorChoice == '3':
            door3Doom()
            break
        else:  # error handling
            print("Silly goose! Enter a valid input.")
            userDoorChoice = input("Enter a number between 1 and 3: ")
    '''
    userDoorChoice = int(eval(input("Enter a number between 1 and 3: ")))
    while userDoorChoice != 1 and userDoorChoice != 2 and userDoorChoice != 3:
        print('')
        print("Silly goose! Enter a valid input.")
        print("You have 3 options: 1, 2, or 3")
        userDoorChoice = int(eval(input("Enter a number between 1 and 3: ")))
    if userDoorChoice == 1:
        door1Snake()
    elif userDoorChoice == 2:
        door2Success()
    elif userDoorChoice == 3:
        door3Doom()'''
def extremeBotheredSnake():
    '''challenge 3 function 2'''
    print("-----------------------------------------------")
    #changed the options to right, left and duck - Manju
    print("The snake begins to hiss at you. Choose either (1)right, (2)left, or (3)jump to dodge the snake.\n"
          "You have three chances to dodge it. ")
    #changed this part of the code to account for errors in user input - Manju
    dictValidMoves = {1: 'right', 2: 'left', 3: 'duck'}
    i = 3
    while i in range(1, 4):
        userMove = input("Select option (1)right, (2)left, or (3)duck to dodge the snake. ")
        while userMove:
            if userMove == '1':
                break
            elif userMove == '2':
                break
            elif userMove == '3':
                break
            else:
                print("Silly goose! Enter a valid input.")
                userMove = input("Select option (1)right, (2)left, or (3)duck to dodge the snake. ")
        snakeMove = random.randint(1, 3)
        if snakeMove == 2:
            print("The snake moved to the right and attacked.")
        elif snakeMove == 3:
            print("The snake moved to the left and attacked.")
        elif snakeMove == 1:
            print("The snake jumped at you.")
        userMoveInt = int(userMove)
        print("You chose {}.".format(dictValidMoves[userMoveInt]))
        if userMoveInt == snakeMove:
            print("Congratulations! You dodged the snake. You get to continue through the maze.")
            return
        elif userMoveInt != snakeMove and userMoveInt in range(1, 4):
            print("The snake bit you! You have {0} chances left.".format(i))
        i -= 1
        if i == 0:
            print("GAME OVER.")
def slightlyBotheredSnake(dict):
    print("Unfortunately, the wrong notes you played caused the snake to open its eyes.\n"
          "You have one more try to play the correct sequence of notes.")
    userCharmNotes = input("A) C, D E#\n"
                           "B) C, D, E\n"
                           "C) C, D#, E\n"
                           "Choose the correct sequence of notes by entering 'A', 'B', or 'C': ").upper()
    # changed this code to account for errors in user input - Manju
    while userCharmNotes:
        if userCharmNotes == 'A':
            print("The snake closed its eyes and went back to sleep. You're safe...for now.")
            break
        elif userCharmNotes == 'B':
            print(dict['C, D, E'])
            return extremeBotheredSnake()
        elif userCharmNotes == 'C':
            print(dict['C, D#, E'])
            print("The snake attacked you and you died on the spot.\n"
                  "GAME OVER")
            break
        else:
            print("Silly goose! Enter a valid input.")
            userCharmNotes = eval(input("A) C, D E#\n"
                                        "B) C, D, E\n"
                                        "C) C, D#, E\n"
                                        "Choose the correct sequence of notes by entering 'A', 'B', or 'C': ").upper())
def door1Snake():
    print("-----------------------------------------------")
    print("You have chosen door 1.\n"
          "You use the master key to unlock the door and cautiously push the door open.\n"
          "Inside, you are surprised to see a giant anaconda, the largest snake in the Amazon,\n"
          "curled up and sleeping on the floor.\n"
          "The anaconda begins to stir upon hearing the creaking of the door opening.\n"
          "You spot a flute leaning against the wall next to the door and have the bright idea to\n"
          "charm the anaconda with the flute so that it relaxes and returns back to sleep.\n"
          "You pick up the flute and begin to play.\n")
    print("You remember the classic snake charming song,\n"
          "but you can't remember the notes exactly, so you have to resort to guessing.")
    print("-----------------------------------------------")

    charmNotesDict = {"C, D, E#": "Congratulations! The snake fell back asleep.",
                      "C, D, E": "The snake was bothered by the notes you played.",
                      "C, D#, E": "The snake awoke from your horrible playing."}
    userCharmNotes = input("A) C, D E#\n"
                           "B) C, D, E\n"
                           "C) C, D#, E\n"
                           "Choose the correct sequence of notes by entering 'A', 'B', or 'C': ").upper()
    # changed this part of the code to account for user input errors - Manju
    while userCharmNotes:
        if userCharmNotes == 'A':
            print(charmNotesDict["C, D, E#"])
            break
        elif userCharmNotes == 'B':
            print(charmNotesDict["C, D, E"])
            return slightlyBotheredSnake(charmNotesDict)
        elif userCharmNotes == 'C':
            print(charmNotesDict["C, D#, E"])
            return extremeBotheredSnake()
        else:
            print("Silly goose! Enter a valid input.")
            userCharmNotes = input("A) C, D E#\n"
                                   "B) C, D, E\n"
                                   "C) C, D#, E\n"
                                   "Choose the correct sequence of notes by entering 'A', 'B', or 'C': ").upper()
def door2Success():
    print("-----------------------------------------")
    print("Congratulations! You've made it without dying.\n"
          "There's no challenge here! You get to continue through the maze. ")
    print("-----------------------------------------")
def door3Doom():
    print("-----------------------------------------------")
    print("Wrong choice! You fall into a pit of quicksand. \n"
          "You try to grab onto a vine hanging from the maze wall,\n"
          "but it snaps as you attempt to pull yourself out.\n"
          "You scream but no one hears you as quicksand buries you alive.\n")
    print("-----------------------------------------------")
    print("G A M E   O V E R")

def displayGameRules():
    print("-----------------------------------------")
    print("Challenge!!  You must solve this riddle!")
    print("Goal: get all the items across the river safely. You have straw, chicken, and a wolf.  "
          "If you leave the chicken alone with the straw, it will eat the straw.")
    print("If you leave the chicken alone with the wolf, the wolf will eat the chicken.")
    print("You have a boat that only holds yourself and one of the items. If you do not want to cross the river with an item, "
          "select the no item option")
    print("-----------------------------------------")
def userInputRiddleAcross(startAnimals):
    while True: #while loop
        try:   #try/except block
            print("")
            print("You are at the start of the river")
            across = int(input("You are crossing the river, make a choice: "
                               "1. straw, 2. chicken, 3. wolf, or 4. no item  Enter 1, 2, 3, or 4."))
            strawCounter = 0
            chickenCounter = 0
            wolfCounter = 0
            for x in range(0, len(startAnimals)):
                if int(startAnimals[x]) == 1:
                    strawCounter += 1
                if int(startAnimals[x]) == 2:
                    chickenCounter += 1
                if int(startAnimals[x]) == 3:
                    wolfCounter += 1
            if across == 1 and strawCounter == 1 or across == 2 and chickenCounter == 1 or across == 3 and \
                    wolfCounter == 1 or across == 4:
                return across
            if across == 1 and strawCounter == 0:
                print("You do not have straw on this side of the river")
            if across == 2 and chickenCounter == 0:
                print("You do not have a chicken on this side of the river")
            if across == 3 and wolfCounter == 0:
                print("You do not have a wolf on this side of the river")
            if across != 1 or across != 2 or across != 3 or across != 4:
                print("That is not a possible choice")
        except:
            print("That is not an acceptable choice")
def userInputComingBack(acrossRiverAnimals):
    while True:
        try:
            print("---------------------------------")
            print("You have successfully made it across the river and now you are coming back to the start.")
            print("You have the option of bringing an item back or not bringing one back at all.")
            back = int(input("make a choice: 1. straw, 2. chicken, 3. wolf, or 4. no item.  Enter 1, 2, 3, or 4."))
            print("----------------------------------")
            strawCounter = 0
            chickenCounter = 0
            wolfCounter = 0
            for x in range(0, len(acrossRiverAnimals)):
                if int(acrossRiverAnimals[x]) == 1:
                    strawCounter += 1
                if int(acrossRiverAnimals[x]) == 2:
                    chickenCounter += 1
                if int(acrossRiverAnimals[x]) == 3:
                    wolfCounter += 1
            if back == 1 and strawCounter==1 or back == 2 and chickenCounter==1 or back == 3 and \
                    wolfCounter== 1or back == 4:
                return back
            if back==1 and strawCounter==0:
                print("You do not have straw on this side of the river")
            if back==2 and chickenCounter==0:
                print("You do not have a chicken on this side of the river")
            if back==3 and wolfCounter==0:
                print("You do not have a wolf on this side of the river")
            if back != 1 or back != 2 or back != 3 or back != 4:
                print("That is not a possible choice")
        except:
            print("That is not an acceptable choice")
def checkAcross(acrossRiverAnimals):
    if len(acrossRiverAnimals)== 2:
        holder1= acrossRiverAnimals[0]
        holder2= acrossRiverAnimals[1]
        if holder1== 1 and holder2== 2 or holder1== 2 and holder2== 1:
            print("-----------------------------------------")
            print("The chicken ate the straw")
            return "game over"
        if holder1== 2 and holder2==3 or holder1==3 and holder2==2:
            print("The wolf ate the chicken")
            return "game over"
    return "all good"
def addAndSubtract(startAnimals, acrossRiverAnimals):
    strawCounter= 0
    chickenCounter=0
    wolfCounter=0
    newStartAnimals=[]
    for x in range (0, len(startAnimals)):
        if int(startAnimals[x])== 1:
            newStartAnimals.append(1)
            strawCounter+=1
        if int(startAnimals[x])== 2:
            newStartAnimals.append(2)
            chickenCounter+=1
        if int(startAnimals[x])== 3:
            newStartAnimals.append(3)
            wolfCounter+=1
    for x in range (0, len(acrossRiverAnimals)):
        if acrossRiverAnimals[x]== 1 and strawCounter==1:
            newStartAnimals.remove(1)
        if acrossRiverAnimals[x]== 2 and chickenCounter==1:
            newStartAnimals.remove(2)
        if acrossRiverAnimals[x]== 3 and wolfCounter==1:
            newStartAnimals.remove(3)
    return newStartAnimals, acrossRiverAnimals
def Subtract(userInput, newStartAnimals, acrossRiverAnimals):
    user=userInput
    strawCounter = 0
    chickenCounter = 0
    wolfCounter = 0
    checkedAcrossRiverAnimals=[]
    checkedNewStartAnimals=[]
    if user== 1:
        strawCounter+=1
    if user==2:
        chickenCounter+=1
    if user==3:
        wolfCounter+=1
    for x in range (0,len(acrossRiverAnimals)):
        checkedAcrossRiverAnimals.append(acrossRiverAnimals[x])
    for x in range(0, len(newStartAnimals)):
        checkedNewStartAnimals.append(newStartAnimals[x])
    for x in range (0, len(acrossRiverAnimals)):
        if acrossRiverAnimals[x]== 1 and strawCounter==1:
            checkedNewStartAnimals.append(1)
            checkedAcrossRiverAnimals.remove(1)
        if acrossRiverAnimals[x]== 2 and chickenCounter==1:
            checkedNewStartAnimals.append(2)
            checkedAcrossRiverAnimals.remove(2)
        if acrossRiverAnimals[x]== 3 and wolfCounter==1:
            checkedNewStartAnimals.append(3)
            checkedAcrossRiverAnimals.remove(3)
    return checkedAcrossRiverAnimals, checkedNewStartAnimals
def checkBeginningRiver(newstartAnimals):
    if len(newstartAnimals)== 2:
        holder1= newstartAnimals[0]
        holder2= newstartAnimals[1]
        if holder1== 1 and holder2== 2 or holder1== 2 and holder2== 1:
            print("-----------------------------------------")
            print("The chicken ate the straw")
            return "game over"
        if holder1== 2 and holder2==3 or holder1==3 and holder2==2:
            print("-----------------------------------------")
            print("The wolf ate the chicken")
            return "game over"
    return "all good"
def userView(acrossRiverAnimals, newStartAnimals):
#Function Definition with Paramenters and Function Call
    print("Here is what you have transported to the far side of the river so far:")
    for x in range(0, len(acrossRiverAnimals)):
        if acrossRiverAnimals[x] == 1:
            print("straw")
        if acrossRiverAnimals[x] == 2:
            print("chicken")
        if acrossRiverAnimals[x] == 3:
            print("wolf")
    print("Here is what is still at the start of the river:")
    for x in range(0, len(newStartAnimals)):
        if newStartAnimals[x] == 1:
            print("straw")
        if newStartAnimals[x] == 2:
            print("chicken")
        if newStartAnimals[x] == 3:
            print("wolf")
def winTheRiddle(acrossRiverAnimals):
    strawCounter = 0
    chickenCounter = 0
    wolfCounter = 0
    for x in range (0, len(acrossRiverAnimals)):
        if acrossRiverAnimals[x]== 1:
            strawCounter+=1
        if acrossRiverAnimals[x]==2:
            chickenCounter+=1
        if acrossRiverAnimals[x]==3:
            wolfCounter+=1
    if wolfCounter==1 and strawCounter==1 and chickenCounter==1:
        return True
def fakemain(figureOutRiddle, startAnimals, startAnimals2, acrossRiverAnimals):
    while figureOutRiddle == False:
        across = userInputRiddleAcross(startAnimals2)
        acrossRiverAnimals.append(across)  #Using build-in List
        endofgame = winTheRiddle(acrossRiverAnimals)
        if endofgame == True:
            figureOutRiddle=True
            break
        newStartAnimals, fakeAcrossRiverAnimals = addAndSubtract(startAnimals, acrossRiverAnimals)
        startAnimals2.clear()
        for x in range(0, len(newStartAnimals)):  #for loop
            startAnimals2.append(newStartAnimals[x])
        death2 = checkBeginningRiver(newStartAnimals)
        if death2 == "game over":
            print("You lost, start game over")
            acrossRiverAnimals.clear()
            break
        if death2 == "all good":
            userView(acrossRiverAnimals, newStartAnimals)
            x = userInputComingBack(acrossRiverAnimals)
            checkedAcrossRiverAnimals, checkedNewStartAnimals = Subtract(x, newStartAnimals, acrossRiverAnimals)
            acrossRiverAnimals.clear()
            for x in range(0, len(checkedAcrossRiverAnimals)):
                acrossRiverAnimals.append(checkedAcrossRiverAnimals[x])
            deathOfAcross = checkAcross(checkedAcrossRiverAnimals)
            if deathOfAcross == "game over":
                print("You lost, start game over")
                acrossRiverAnimals.clear()
                break
    return (figureOutRiddle)
def playRiddle():
    #Function Definition and Function call
    startAnimals = [1, 2, 3]  #list
    startAnimals2 = [1, 2, 3]
    acrossRiverAnimals = []
    displayGameRules()
    figureOutRiddle = False
    decider = fakemain(figureOutRiddle, startAnimals, startAnimals2, acrossRiverAnimals)
    #function definition with parameters and function call
    if decider== True:
        figureOutRiddle=True
    if decider == False:
        acrossRiverAnimals.clear()
        startAnimals=[1,2,3]
        startAnimals2=[1,2,3]
        displayGameRules()
        decider = fakemain(figureOutRiddle, startAnimals, startAnimals2, acrossRiverAnimals)
        if decider == True:  #nested if statement
            figureOutRiddle = True
        if decider == False:
            acrossRiverAnimals.clear()
            startAnimals=[1,2,3]
            startAnimals2=[1,2,3]
            displayGameRules()
            decider = fakemain(figureOutRiddle, startAnimals, startAnimals2, acrossRiverAnimals)
            if decider == True:
                figureOutRiddle = True
    if figureOutRiddle == False:
        print("-----------------------------------------")
        print("You did not figure out the riddle fast enough")
        print('')
        print("Goodbye.")
        exit()
    if figureOutRiddle == True:
        print("-----------------------------------------")
        print("Congratulations! You figured out the riddle. You have escaped the maze!")
        print("WOOOOOO!!!")
        print("-----------------------------------------")

def main():
    print("-----------------------------------------------")
    print("Hello user!")
    User1Name= Player(input("Please enter your name: "))
    print("""You are a human and were playing outside, but you fell into a hole
    that led you into an underground maze. To get back to the real world, 
    you must find your way out.""")
    print("-----------------------------------------------")
    print("You have 2 options left or right")
    input1 = input("Choose L or R: ").upper()
    while input1 != "L" and input1 != "R":
        print('')
        print("That is not a valid choice")
        print("You have 2 options left or right")
        input1 = input("Choose L or R: ").upper()
    if input1 == "R":
        challenge1 = challenge_dice()
        print("-----------------------------------------------")
        print("You again come to a fork in the maze")
        print("You have 2 options: left or right")
        print("-----------------------------------------------")
        input2 = input("Choose L or R: ").upper()
        while input2 != "L" and input2 != "R":
            print('')
            print("That is not a valid choice")
            print("You have 2 options: left or right")
            input2 = input("Choose L or R: ").upper()
        if input2 == "L":
            challenge2 = doggo_challenge()
            print("-----------------------------------------------")
            print("You again come to a fork in the maze")
            print("You have 2 options: left or right")
            print("-----------------------------------------------")
            input3 = input("Choose L or R: ").upper()
            while input3 != "L" and input3 != "R":
                print('')
                print("That is not a valid choice")
                print("You have 2 options: left or right")
                input3 = input("Choose L or R: ").upper()
            if input3 == "L":
                challenge3 = introToSnakeChallenge()
                print("-----------------------------------------------")
                print("You are finished with the third challenge!")
                print("You have 2 options left or right")
                print("-----------------------------------------------")
                input4 = input("Choose L or R: ").upper()
                while input4 != "L" and input4 != "R":
                    print('')
                    print("that is not a valid choice")
                    print("You have 2 options left or right")
                    input4 = input("Choose L or R: ").upper()
                if input4 == "R":
                    challenge4 = playRiddle()
                    print("-----------------------------------------------")
                    print("You are finished with the fourth challenge")
                    print("you have just found the exit to the maze!")
                    print("-----------------------------------------------")
                elif input4 == "L":
                    print("you come to a dead end! oh no!")
                    User1Name.minusHealth()
                    print("A meteor hit you.  You lost all of your health")
                    print(User1Name.display_player())
                    quit()
            elif input3 == "R":
                print("You come to a dead end! oh no!")
                User1Name.minusHealth()
                print("A dinosaur ate you. You lost all of your health.")
                print(User1Name.display_player())
                quit()
        elif input2 == "R":
            print("You come to a dead end! oh no!")
            User1Name.minusHealth()
            print("You fell into an endless abyss. You lost all of your health")
            print(User1Name.display_player())
            quit()

    elif input1 == "L":
        print("You come to a dead end! oh no!")
        User1Name.minusHealth()
        print("You contracted a deadly disease. You lost all of your health")
        print(User1Name.display_player())
        quit()
    print("Congratulations! You have exited the maze and returned home.")

main()