#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

string = list((input('Please enter a string:').lower()).replace(" ",""))#get a string from the user covert to lower case and remove spaces
if string == list(reversed(string)): #if the strings are the same
    print ("string is a palindrome")
else:
    print("string is not a palindrome")
