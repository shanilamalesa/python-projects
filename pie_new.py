import random

low = int(input("Enter the low number:\n"))
high = int (input("Enter the ghiest number:\n"))
random_number = random.randint(low,high)

attempts = 0
while True:
    guess = int(input("Guess the number: \n"))
    attempts +=1
    if guess < random_number:
        print("The guess is too low!")
    elif guess > random_number:
        print("The guess is too high!")
    else:
        print(f"Congrats!🎊 you have succedecd with {attempts} tries")
        break