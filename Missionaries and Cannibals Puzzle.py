Aim:
The aim of the program is to implement the Missionaries and Cannibals Puzzle, 
where the goal is to transport three missionaries and three cannibals from the left side of the river to the right side using a boat under specific constraints.
Algorithm:
1. Initialization:
Define the starting counts of missionaries (lM) and cannibals (lC) on the left side.
Initialize counters for the right side (rM, rC) and track the number of moves (k).
2. Game Loop:
Continuously prompt the user for inputs to transport missionaries and cannibals across the river until either the goal state is achieved or a rule is violated.
3. Left-to-Right Travel:
Prompt the user to specify how many missionaries (uM) and cannibals (uC) to move from the left side to the right side.
Validate the input:
The boat cannot be empty.
The total number of passengers cannot exceed two.
There must be sufficient missionaries and cannibals on the left side to make the trip.
Update the counts on both sides of the river and print the current state.
Check for rule violations (e.g., cannibals outnumbering missionaries).
Win Condition:
The game is won if all missionaries and cannibals are safely transported to the right side (rM + rC == 6).
6. Lose Condition:
The game is lost if, at any point, cannibals outnumber missionaries on either side of the river.
Code:
print("\n")
print("\tGame Start\nNow the task is to move all of them to right side of the river")
print("rules:\n1. The boat can carry at most two people\n2. If cannibals num greater than missionaries then the cannibals would eat the missionaries\n3. The boat cannot cross the river by itself with no people on board")
lM = 3
lC = 3		 
rM=0		 
rC=0		 
userM = 0	
userC = 0	 
k = 0
print("\nM M M C C C |	 --- | \n")
try:
	while(True):
		while(True):
			print("Left side -> right side river travel")
			uM = int(input("Enter number of Missionaries travel => "))	
			uC = int(input("Enter number of Cannibals travel => "))
			if((uM==0)and(uC==0)):
				print("Empty travel not possible")
				print("Re-enter : ")
			elif(((uM+uC) <= 2)and((lM-uM)>=0)and((lC-uC)>=0)):
				break
			else:
				print("Wrong input re-enter : ")
		lM = (lM-uM)
		lC = (lC-uC)
		rM += uM
		rC += uC
		print("\n")
		for i in range(0,lM):
			print("M ",end="")
		for i in range(0,lC):
			print("C ",end="")
		print("| --> | ",end="")
		for i in range(0,rM):
			print("M ",end="")
		for i in range(0,rC):
			print("C ",end="")
		print("\n")
		k +=1
		if(((lC==3)and (lM == 1))or((lC==3)and(lM==2))or((lC==2)and(lM==1))or((rC==3)and (rM == 1))or((rC==3)and(rM==2))or((rC==2)and(rM==1))):
			print("Cannibals eat missionaries:\nYou lost the game")
			break
		if((rM+rC) == 6):
			print("You won the game : \n\tCongrats")
			print("Total attempt")
			print(k)
			break
		while(True):
			print("Right side -> Left side river travel")
			userM = int(input("Enter number of Missionaries travel => "))
			userC = int(input("Enter number of Cannibals travel => "))
			if((userM==0)and(userC==0)):
					print("Empty travel not possible")
					print("Re-enter : ")
			elif(((userM+userC) <= 2)and((rM-userM)>=0)and((rC-userC)>=0)):
				break
			else:
				print("Wrong input re-enter : ")
		lM += userM
		lC += userC
		rM -= userM
		rC -= userC
		k +=1
		print("\n")
		for i in range(0,lM):
			print("M ",end="")
		for i in range(0,lC):
			print("C ",end="")
		print("| <-- | ",end="")
		for i in range(0,rM):
			print("M ",end="")
		for i in range(0,rC):
			print("C ",end="")
		print("\n")
		if(((lC==3)and (lM == 1))or((lC==3)and(lM==2))or((lC==2)and(lM==1))or((rC==3)and (rM == 1))or((rC==3)and(rM==2))or((rC==2)and(rM==1))):
			print("Cannibals eat missionaries:\nYou lost the game")
			break
except EOFError as e:
	print("\nInvalid input please retry !!")
