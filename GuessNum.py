import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    i = 8
    while guess != random_number and i > 0:
        print(f'You have {i} guesses left')
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        i -= 1
    if guess == random_number:
        print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')
    else:
        print(f'You lose. The correct option was {random_number}.')
guess(20)