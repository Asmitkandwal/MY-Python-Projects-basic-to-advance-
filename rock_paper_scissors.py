import random

def play():
    while True:
        choice = input("if you wanted to play press enter else press q for exit ")
        if choice == 'q':
            quit()
        else:
            player = input("choose  rock , scissor ,  paper ")

            computer = random.choice(['rock','scissor','paper'])
            print("computer choosed " + computer)
            if player == computer :
                print("its a tie")

            elif who_won(player,computer):
                 print(f" {player} > {computer} ")
                 print("you won!!")
            else:
                print(f" {player} < {computer} ")
                print("you lose")



def who_won(p,c):
    if (p == 'rock' and c == 'scissor') or (p=='scissor' and c == 'paper') or (p == 'paper' and c == 'rock'):
        return True
    else:
        return False

play()
