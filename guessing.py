#greet player
#get player name
#choose random number between 1 and 100
#while True:
#    get guess
#   if guess is incorrect:
#        give hint
#   else:
#       congratulate player
print "Hi! Welcome to our guessing game!"
print "Please, tell us your name (real names only)"
name = raw_input()
number = 42
print "Guess a number between 1 and a 100"
number = 0
while True:
    guess = int(raw_input())
    number += 1
    if guess < 100 and guess > 1:
            if guess < 42:
                print "Try Again %s! Your guess is too low" % name
            elif guess > 42:
                print "Try Again %s! Your guess is too high" % name
            else:
                print "HELLYA! YOU GOT IT IN %s TRIES!!!" % number
                break 
    else: 
        print "Please enter a valid number"



