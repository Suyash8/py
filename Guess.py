#from random import randrange
import random

secret_word = {
    0: "",
    1: "giraffe",
    2: "elephant", 
    3: "dog", 
    4: "cat", 
    5: "lion", 
    6: "tiger", 
    7: "camel",
    8: "zebra",
    9: "monkey",
    10: "goat"
    #Add more inputs in the same format
    #Remember to increase the index every word
}
print(secret_word)
num = random.randint(1, 10) #The "10" should be replaced by the largest index in the secret_word
guess = 0
guess_word = secret_word[num]
i = 5 #Number of tries, change if wanted

while guess_word != secret_word[guess]:
    if i < 1:
        break
    print(f"{i} guesses left.")
    guess = int(input("Enter guess: "))
    i -= 1
if guess_word == secret_word[guess]:
    print(f"The secret word is \"{num}: {guess_word}\".\nYou win!")
else:
    print(f"The secret word is \"{num}: {guess_word}\".\nYou lose.")

