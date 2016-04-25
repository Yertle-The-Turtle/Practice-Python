#list overlap
#write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
#Make sure your program works on two lists of different sizes.
#Randomly generate two lists to test this

import random #get random module
a = random.sample(range(120), 20) #create random list
b = random.sample(range(120), 20) #create random list
print ("list a:\n", a, "\nlist b:\n",b, "\nIntercection:") #print information about random lists
print ([num for num in range(min(a+b), max(a+b)+1) if num in a and num in b]) #if num is in list a and b print it in a list format
       
print (set(a).intersection(set(b))) #alternitve way