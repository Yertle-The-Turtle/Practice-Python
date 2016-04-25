#Make a Rock-Paper-Scissors game user vs computer
scoreComp = 0 #set variables to 0 
scoreUsr = 0
while True:
    try:
        import random #random module
        user = (int(input("Welcome to paper, scissors, rock game.\nEnter 1 for paper.\nEnter 2 for scissors\nEnter 3 for rock\n"))) - 1 #give user instructions
        comp = random.randrange(0, 3, 1) #get a random int
        option = ['Paper', 'Scissors', 'Rock'] #list with string options
        print ('You picked: %s\nComputer picks: %s'%(option[user], option[comp]))#tell user what the computer picked and what the user picked
        if comp == 0 and user == 2 or comp == 1 and user == 0 or comp == 2 and user == 1: #if computer has won
            scoreComp = scoreComp + 1 #increase score
            print('computer wins.\nScore:\nComputer: %i\nYou:%i'%(scoreComp, scoreUsr))#tell user who has one and the new score
        elif comp == user: #if user and computer pick same thing
            print('DRAW') 
        else:
            scoreUsr = scoreUsr + 1
            print('You win.\nScore:\nComputer: %i\nYou:%i'%(scoreComp, scoreUsr))
        inpUser = input("\nDo you wish to continue playing?\nPress y to play again or q to quit\n").lower()#ask user if they want to quit
        if 'q' in inpUser: break #quit
        
    except ValueError: #catch inccoret value type 
        print("That's not an option")
    except IndexError: #catch value that's too big
        print("ERROR\nPick a number between one and three")
        
        