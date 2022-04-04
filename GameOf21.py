import random

pScore = 0
cScore  = 0
pList = []
cList = []
pSum = 0
cSum = 0
cardNumber = [1,2,3,4,5,6,7,8,9,10]
playStatus = 0
print("rules: the program will randomly distribute 2 cards for you. You can choose to have a third card or not. then, you will be compared with the computer's three cards, the winner is whomever has thesum of the cards cloer but less than 21")
while(playStatus == 0):
    print("game on, the player will recieve two cards and decide whether to have a third card.")
    pList.append(random.choice(cardNumber))
    pList.append(random.choice(cardNumber))
    cList.append(random.choice(cardNumber))
    cList.append(random.choice(cardNumber))
    cList.append(random.choice(cardNumber))
    print("Your cards are:",pList)
    pChoice = int(input("type 1 to have an extra card,0 to continue with 2 cards"))
    if(pChoice == 1):
        pList.append(random.choice(cardNumber))
        print("Your cards are:",pList)
        
    else:
        print("all set! your cards are:",pList)
        
    for pCard in pList:
        pSum += pCard
    for cCard in cList:
        cSum +=cCard
    
    if(pSum<=21 and cSum <=21):
        if pSum < cSum:
            print("the computer's cards are:",cList,"you've lost the round.")
            cScore += 1
        elif(pSum>cSum):
            print("the computer's cards are:",cList,"you've won this rouond.")
            pScore += 1
        else:
            print("the computer's cards are:",cList,"this round is a tie.")
    elif(pSum<=21 and cSum>21):
        print("the computer's cards are:",cList,"you've won this round.")
        pScore+=1
    elif(pSum>21 and cSum<=21):
        print("the computer's cards are:",cList,"you've lost the round.")
        cScore += 1
    else:
        print("the computer's cards are:",cList,"this round is a tie.")
    print("the computer's score is:",cScore,"your score is:",pScore)
    playStatus = 1
    nextRound = int(input("please enter 1 if you want to play another round, press 0 to end game"))
    if(nextRound == 1):
        pList = []
        cList = []
        pSum = 0
        cSum = 0
        playStatus = 0
    else:
        if(pScore > cScore):
            print("Alright, the winner is -- You! congradulations!")
        elif(cScore > pScore):
            print("Alright, the winner is -- computer! Good luck next time.")
        else:
            print("You guys have the same credit. this is a tie. Have fun!")
        pScore = 0
        cScore  = 0
        pList = []
        cList = []
        pSum = 0
        cSum = 0
        
        
