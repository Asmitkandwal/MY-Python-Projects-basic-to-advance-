import random

def guess(number):
    random_number = random.randint(1,number)
    wrong = 0
    while True:
        try:
            guessed_number = int(input("enter the number to guess"))
        except ValueError:
            print("enter the right value")
            continue

        if guessed_number < random_number:
            print("low")
            wrong += 1
        elif guessed_number > random_number:
            print("high")
            wrong +=1
        else:
            print(f" congrats you have guess the right number {random_number} with {wrong} wrong erros")





number = int(input(" enter the number you wanted to guess up to 1 to x.."))
guess(number)