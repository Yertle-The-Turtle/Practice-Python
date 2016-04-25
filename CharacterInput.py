#CharacterInput
#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
#import the datetime module
import datetime
#Return the current local date and time
currTimeDate = datetime.datetime.now()
#Return current year
currYear= currTimeDate.year
#get user to enter name
name = str(input("Please enter your name:\n" ))
#get user to enter age
age = int(input("Please enter your age:\n"))
#calculate the year that user will be 100
yearHund = int(((100-age)+currYear))
#display year user will turn 100
#print ("Hello", name, "you will turn 100 in the year", yearHund)
print ("Hello %s, you will turn 100 in the year %i " %(name, yearHund))
