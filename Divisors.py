###Divisors
###Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
###(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)	
while True:
    try:
        result = [] #empty list
        inputNum = int(input('Number:')) #get number from the user
        result = [ num for num in range(1,inputNum + 1) if inputNum % num == 0]#go through possible divisors add to list if they are a divisor
        print ('Divisor(s) of %i are:'%(inputNum), result) #tell user the divisors of the input number
    except ValueError:
        print("That's not a number.") #give error