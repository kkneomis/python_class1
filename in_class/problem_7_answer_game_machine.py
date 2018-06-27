import random 

class GameMachine:

    def __init__(self, coins):

        self.coins = coins


    def play_game(self):

        while self.coins > 0:

            print "1: Guess the number"
            print "2: Rock, Paper, Scissors"
            choice  = int(raw_input("Choose a game"))

            if choice == 1:
                self.guessing_game()
            elif choice == 2:
                self.rpc()

            self.coins -=  1
            print "You have %s coins left" % self.coins
        else:
            print "You cannot play.  You have no more coins :("


    def guessing_game(self):
        """The guessing game"""
        print "playing the guessing game!"
        num = random.randint(1, 21)
        
        correct = False
        while not correct:
            guess = int(raw_input("Guess a number from 1-20"))
            print "You guessed %s" % guess
            if guess == num:
                print "That's correct!"
                correct = True
            else:
                print "Nope, that's not right!"



    def rpc(self):
        print "playing Rock, Paper, Scissors!"
        options = ["rock", "paper", "scissors"]
        system_choice = random.choice(options)
        print "Rock!"
        print "Paper!"
        print "Scissors!"
        user_choice = raw_input("SHOOT!").lower()
        
        losing_matrix = {
                   "rock": "paper",
                   "paper": "scissors",
                   "scissors": "rock"
                }

        if user_choice not in options:
            print "Oops, that is not a valid option"
        elif system_choice == user_choice:
            print "It's a tie!"
        elif losing_matrix.get(user_choice, None) == system_choice:
            print "You LOSE!! LLOOOOOOSSSEERRRRR!!!"
        else:
            print "You win, I guess... -_-"



m1 = GameMachine(2)
m1.play_game()

