import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    guesses = 9
    while feedback != 'c' and guesses > 0:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        print(f'Guesses remaining: {guesses}')
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            continue
        else:
            print("Enter a valid input".upper())
            continue
        guesses -= 1
    if feedback == 'c':
        print(f'Yay, the computer guessed your number, {guess}, correctly!!')
    else:
        print('Oh no, the comuter ran out of guesses')
computer_guess(100)