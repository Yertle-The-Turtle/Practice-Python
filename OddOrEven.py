###OddOrEven
###Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
###If the number is a multiple of 4, print out a different message.
#get a number from the user
number = int(input("Please enter a number:\n"))
#check if number is divisable by 4
if (number % 4 == 0):
	#let user know the number is divisable by 4
	print ("%i is divisable by 4"%(number))
else:	
	#if divisable by two without a remainder
	if (number % 2 == 0):
		#tell user the number is even
		print ("%i is even"%(number))
	#else let them know it is odd
	else:
		print ("%i is odd"%(number))
	
###Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
###If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
#get two numbers from the user
num = int(input("please enter another number:\n"))
check = int(input("please enter another number:\n"))
#check if the unput numbers divide evenly
#let the user know if the do or dont
if (check % num == 0):
	print("%i divides evenly into %i" %(check,num))
else:
	print("%i does not divide evenly into %i" %(check,num))