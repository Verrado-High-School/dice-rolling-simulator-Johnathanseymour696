# By Johnathan Seymour
#P1 2/10/19
#Dice Rolling Simulator
#This allows the computer to randomly select a number
import random
print("Dice Simulator")

#______________________________________________________________________________________
roll =input("How many times would you like to spin a six sided dice ")
cChoices =["1","2","3","4","6",]
countDown = (roll)
computerChoice = random.choice(cChoices)
while (countDown >= 0):
	print(("#")+ countDown +("Roll")+computerChoice)
	countDown= -1
    if countDown == 0:
    	print("Thats it")
    	break



	


