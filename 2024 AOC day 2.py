with open("data.txt", "r") as file:
	data = file.read()
#this is for testing the logics
#data = """7 6 4 2 1
#1 2 7 8 9
#9 7 6 2 1
#1 3 2 4 5
#8 6 4 4 1
#1 3 6 7 9"""


#convert raw data into processable
data = [[int(numbers) for numbers in lines.split(" ")]for lines in data.split("\n")]

#number of safe
safe = 0


#The levels are either all increasing or all decreasing.
#Any two adjacent levels differ by at least one and at most three.
for lin in data:
	triggered = False
	isrule3 = False
	
	#this line to *2* is implementation for rule 3
	for i in range(len(lin)):
		line = lin.copy()
		line.pop(i)
		#*2*
		
		#rule1
		temp = list(line)#copy
		temp.sort()#sort
		#compare the sorted copy of the data
		#on the non sorted and flipped sorted
		#cus figure it out why lmao
		if not (temp in (line, line[::-1])):
			continue
		
		#rule 2
		isrule2 = True
		
		prev_num = None
		for num in line:
			if prev_num != None:
				#checking for duplicate 
				if prev_num == num:
					isrule2 = False
				
				#if the change is too much
				if abs(prev_num-num) > 3:
					isrule2 = False
			
			prev_num = num
			
		#stfu I like this was of debugging
		#if lin == data[4]:
			#print(line,i,isrule2)

		#from here the logic of rule 3
		if (not triggered) and isrule2:
			isrule3 = True
			
		
	
	print(lin, isrule3)
	#upto here
	safe+= 1 if isrule3 else 0



#print safe
print(".   ",safe)
			
#idk...
302


