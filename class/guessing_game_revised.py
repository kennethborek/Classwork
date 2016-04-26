import random

guesstaking=0
number=random.randint(1,10)
print(number)
print ("Please guess any number")
while guesstaking < 3:
    print("Take a guess")
    guess = input()
    guess = int(guess)
    guesstaking = guesstaking + 1

    if guess == number +1  or guess== number - 1:
        print("Guess is hot")
    if guess == number +2 or guess == number - 2:
        print("Guess is warm")
    elif guess > number +2 or guess < number -2:
        print("Guess is cold")
    if guess == number:
        break

if guess == number:
    #guesstaking=str(guesstaking)
    print ("Excellent you have it correct!!")
if guess!= number:
    #number=str(number)
    print ("Sorry wrong number, the actual number is" , number)