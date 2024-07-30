import random

randomNum = random.randint(1, 10)
#print(randomNum)

while True:
    guess=(input('Guess the number (1-10) or Quit (press Q):'))
    if(guess=="Q"):
        print('game over')
        break
    guess=int(guess)    
    if guess==randomNum:
        print('you are correct')
        break
    else:
        if guess>randomNum:
            print('too large') 
        elif(guess<randomNum):
            print('too small') 
       

    
