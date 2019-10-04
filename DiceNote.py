import random
roll = int(input("How many times do you want to roll the dice? "))
count = 0
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
while (count <= roll):
    count = count + 1
    cChoices = random.randint(1, 6)
    if cChoices == 1:
    	print("The dice rolled a 1.")
    	ones = ones + 1
    elif cChoices == 2:
    	print("The dice rolled a 2.")
    	twos = twos + 1
    elif cChoices == 3:
    	print("The dice rolled a 3.")
    	threes = threes + 1
    elif cChoices == 4:
    	print("The dice rolled a 4.")
    	fours = fours + 1
    elif cChoices == 5:
    	print("The dice rolled a 5.")
    	fives = fives + 1
    else:
    	print("The dice rolled a 6.")
    	sixes = sixes + 1
print("Results:")
print("1s: " + str(ones))
print("2s: " + str(twos))
print("3s: " + str(threes))
print("4s: " + str(fours))
print("5s: " + str(fives))
print("6s: " + str(sixes))