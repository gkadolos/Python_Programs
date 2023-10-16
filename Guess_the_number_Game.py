x=16
lifes=3
attempts=1
print("You have " + str(lifes)+" attempts to find the secret number!")
guess=int(input("Guess the number!:"))
if guess > x:
    print("It's less than " + str(guess))
    lifes-=1
elif guess < x:
    print("It's greater than " + str(guess))
    lifes-=1
while lifes>0 and guess!=x:
        attempts += 1
        if lifes==1:
            print("You have " + str(lifes) + " more attempt to find it!")
        else:
            print("You have " + str(lifes) + " more attempts to find it!")
        guess=int(input("Try Again!:"))
        if guess==x:
                break
        if guess>x:
            print("It's less than " +  str(guess))
        elif guess<x:
            print("It's greater than "+ str(guess))
        lifes -= 1

if lifes>0:
    if attempts==1:
        print("Congratulations! You found it!")
        print("It took you " + str(attempts) + " try!")
    else:
        print("Congratulations! You found it!")
        print("It took you " + str(attempts)+ " tries!")
else:
    print("You lost!")
