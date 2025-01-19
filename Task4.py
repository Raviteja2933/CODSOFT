#RockPaperScissorGame
import random
while True:
    print("="*50)
    print(" Enter Ur choice 1 for Rock, 2 for Paper, 3 for Scissor")
    print("1) Rock")
    print("2) Paper")
    print("3) Scissor")
    print("=" * 50)
    selection=int(input("Enter ur choice:"))
    if selection==1:
        Player_choose = "Rock"
    elif selection==2:
        Player_choose = "Paper"
    elif selection==3:
        Player_choose = "Scissor"
    else:
        print("Don't Enter other than: (1,2,3) numbers")
        print("please try again")

    print("Player Choose:",Player_choose)

    Throws=["Rock","Paper","Scissor"]
    computer_choice=random.choice(Throws)
    print("Computer selected:",computer_choice)

    if Player_choose==computer_choice:
        print("Tie Game!")
    elif (Player_choose=="Rock"):
        if (computer_choice=="Scissor"):
            print("you Won The Game.")
        elif (computer_choice=="Paper"):
            print("computer Won The Game.")
    elif (Player_choose=="Paper"):
        if (computer_choice=="Scissor"):
            print("Computer Won The Game.")
        elif (computer_choice=="Rock"):
            print("You Won The Game.")
    elif (Player_choose=="Scissor"):
        if (computer_choice=="Paper"):
            print("You Won The Game.")
        elif (computer_choice=="Rock"):
            print("Computer Won The Game.")

    print("="*50)
    print("1) Play Again")
    print("2) Quit the Game")
    selection=int(input("Enter Ur Choice:"))
    if selection==2:
        print("="*50)
        print("# # #Thq u for playing with us.# # #")
        print("=" * 50)
        break













