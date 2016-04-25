###ListLessThan10
###Take a list and write a program that prints out all the elements of the list that are less than 5.
#the list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#get number from the user
numb = int(input("Choose a number: "))
#create a new list (empty)
newList = []
#loop though a and assingn each element of the list to the variable call element
for element in a:
	#if the current element selected is less than the number add it to the list
	if element < numb:
		newList.append(element)

#print the list
print (newList)

#one line
print([ element for element in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if element < numb])
#for loop example with a string 
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
	print (word)