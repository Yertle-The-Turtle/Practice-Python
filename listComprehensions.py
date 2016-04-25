#ListComprehensions
#Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
#Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] #list a
aEven = [even for even in a if even % 2 ==0 ] #go through list a if elements in list a is even then add to list aEven
print (aEven) #show user your new list ;)
