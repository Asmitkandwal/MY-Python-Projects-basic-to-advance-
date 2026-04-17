import random

def computer_guess(range):
    low = 0
    high = range
    feedback = ''
    while feedback != 'c':
        # if low != high:
        guess_number = random.randint(low,high)
        '''else:
            guess_number = low'''

        print(f"the guess number is {guess_number}")
        feedback = input("enter the feedback 'l' for low , 'h' for high , 'c' for correct")

        if feedback == 'l':
                print("number is low")
                low = guess_number + 1
        elif feedback == 'h':
                print("number is high")
                high = guess_number - 1

    print(f"finally you got it the number is {guess_number}")








while True:
        try:
            number = int(input("enter the range 1 to x.."))
            if number>0:
                break
            else:
                print("the number here ")
        except ValueError:
            print("enter again value here ")

computer_guess(number)