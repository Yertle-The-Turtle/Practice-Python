#play video evey two hours

import webbrowser #imprt webbrowser module
import time #import time module
count = 0
breaks = int(input("please enter amount of breaks you wish to take within the next 12 hours:\n"))#get number from user
sleepTime = 12/breaks #caculate time sleep time needed
print ("this programe started on", time.ctime()) #tell user when programe started
while count < breaks: #do this when number of breaks taken is less than the number of breaks needed
    time.sleep(sleepTime*60*60) #sleep for amount of time
    webbrowser.open("https://www.youtube.com/watch?v=FhykvrPZwA4") #you fucking druggo
    count = count + 1 #add to counter
    print("You have taken %i break(s)"%(count)) #let user know how many breaks they have taken
