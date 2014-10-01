import random
print "Hi! Welcome to our guessing game!"
print "Please, tell us your name (real names only)"
number = random.randrange(1, 101)
name = raw_input()
print "Guess a number between 1 and a 100"
tries = 0
while True:
    guess = raw_input()
    tries += 1
    if not (ord(guess[0]) > 64 and ord(guess[0]) < 123):
        guess = int(guess)    
        if guess < 100 and guess > 1:
            if guess < number:
                print "Try Again %s! Your guess is too low" % name
            elif guess > number:
                print "Try Again %s! Your guess is too high" % name
            else:
                if tries <= 5:
                    print "HELLYA! YOU GOT IT IN %s TRIES!!!" % tries
                else:
                    print "You took a while.....to guess %s tries..." % tries
                print "Would you like to play again?"
                answer = raw_input()
                if answer == "yes":
                    print "Guess a number between 1 and a 100"
                    tries = 0 
                    number = random.randrange(1, 101)
                    continue
                if answer == "no":
                    break 
        else: 
            print "Please enter a valid number you retard"
    else:
        print "Enter a valid number!"


