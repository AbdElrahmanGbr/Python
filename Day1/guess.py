import random
from xmlrpc.client import boolean

print("Welcome to Guess The Number Game")

file1 = open('file.txt', 'r')
lines= file1.readline()
newlines= lines.split(",")
file1.close()

gamesPlayed= int(newlines[0]) | 0 
print("you have played ",gamesPlayed," games")

wins = int(newlines[1]) | 0
print("you have won ",wins," games")

losses = int(newlines[2]) | 0
print("you have lost ",losses," games")

playAgain = "yes"

while playAgain =="yes" or playAgain =="Y" or playAgain =="y":
    chances=10
    randomNumber = random.randint(1,100)
    gamesPlayed+=1
    allTries =[]
   
    while(chances > 0):
        guessedNumber = (input("please enter a number between 1 & 100 "))
        if (guessedNumber.isnumeric() == False):
            print("please enter a number")
            continue
        guessedNumber = int(guessedNumber)
        if(guessedNumber > 100 or guessedNumber <= 0 ):
            print("Your number is out of range")
            print("you have ",chances," turns left")
            continue
        # checking if the number is already in the list
        elif(guessedNumber in allTries ):
            print("Your have entered this number before")
            print("you have ",chances," turns left")
            continue
        elif(guessedNumber == randomNumber):
            print("You win ") 
            win =True
            wins+=1 
            randomNumber = random.randint(1,100)
            gamesPlayed+=1
            allTries =[]
            chances-=1
            print("you have ",chances," turns left")  
        elif(guessedNumber > randomNumber):
            print("your number is bigger than the required number")
            chances-=1
            print("you have ",chances," turns left")
            allTries.append(guessedNumber)
            continue    
        elif(guessedNumber < randomNumber):
            print("your number is smaller than the required number")
            chances-=1
            print("you have ",chances," turns left")
            allTries.append(guessedNumber)
            continue  


    print("you finished your tries")
    losses+=1
    playAgain =(input("Do you want to play again? yes or no? "))
 
print("Thanks for playing")
file1 = open('file.txt', 'w')
L = [str(gamesPlayed),",",str(wins),",",str(losses)]
file1.writelines(L)
file1.close()







    

     

