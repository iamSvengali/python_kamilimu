#MWANIKI NYAGA
#RockPaperScissors Game

import random 

def ropasc():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice_rock()
    elif computer_choice == 2:
        computer_choice_paper()
    else:
        computer_choice_scissors()

def computer_choice_rock():
    user_choice = raw_input("1 = Rock, 2 = Paper, 3 = Scissors:")
    if user_choice == "1":
        print "You Tie. You chose Rock. Player 2 chose Rock."
        try_again()
    if user_choice == "2":
        print "You Win! You chose Paper. Player 2 chose Rock."
        try_again()
    if user_choice == "3":
        print "You Lose. You chose Scissors. Player 2 chose Rock."
        try_again()
    else:
        print "Invalid Choice. Try Again..."
        computer_choice_rock()

def computer_choice_paper():
    user_choice = raw_input("1 = Rock, 2 = Paper, 3 = Scissors:")
    if user_choice == "1":
        print "You Lose. You chose Rock. Player 2 chose Paper."
        try_again()
    if user_choice == "2":
        print "You Tie. You chose Paper. Player 2 chose Paper."
        try_again()
    if user_choice == "3":
        print "You Win! You chose Scissors. Player 2 chose Paper."
        try_again()
    else:
        print "Invalid Choice. Try Again..."
        computer_choice_paper()

def computer_choice_scissors():
    user_choice = raw_input("1 = Rock, 2 = Paper, 3 = Scissors:")
    if user_choice == "1":
        print "You Win! You chose Rock. Player 2 chose Scissors."
        try_again()
    if user_choice == "2":
        print "You Lose. You chose Paper. Player 2 chose Scissors."
        try_again()
    if user_choice == "3":
        print "You Draw. You chose Scissors. Player 2 chose Scissors."
        try_again()
    else:
        print "Invalid Choice. Try Again..."
        computer_choice_scissors()

def try_again():
    choice = raw_input("Would you like another go? y/n")
    if choice == "y" or choice == "yes" or choice == "Y" or choice == "Yes":
        ropasc()
    elif choice == "n" or choice == "no" or choice == "N" or choice == "No":
        print "Thank You for playing!"
        quit()
    else:
        print "Invalid Choice. Try Again..."
        try_again()

ropasc()
       
