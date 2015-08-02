# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# helper function to start and restart the game
def new_game(mode):
    global secret_number
    global guess_time
    global status
    # initialize global variables used in your code here
    status=mode
    if(mode==1):
        secret_number = random.randrange(0, 100)
        print "New game. Range is from 0 to 100."
        
        guess_time=7
        print "Number of remaining guesses is "+str(guess_time)

    else:
        secret_number = random.randrange(0, 1000)
        print "New game. Range is from 0 to 1000."
        
        guess_time=10
        print "Number of remaining guesses is "+str(guess_time)
    print("\n")
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    new_game(1)
    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game  
    new_game(2)

    
def input_guess(guess):
    # main game logic goes here	
    global guess_time
    global status
    

    print "Guess was "+guess
    guess_number=int(guess)
    
    
    guess_time-=1
    print "Number of remaining guesses is "+str(guess_time)

    if secret_number<guess_number:
        print "Lower!"
    elif secret_number>guess_number:
        print "Higher!"
    else:
        print "Correct!"
        
        if(status==1):
            range100()
        else:
            range1000()
    print("\n")
    if(guess_time==0):
        print("You lose!!")
        if(status==1):
            range100()
        else:
            range1000()
    
    
# create frame
f = simplegui.create_frame("Calculator",300,300)

# register event handlers for control elements and start frame
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess!", input_guess, 200)


# call new_game 
new_game(1)


# always remember to check your completed program against the grading rubric
