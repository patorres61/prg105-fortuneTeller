# Phyllis Torres
# Fortune Teller - Monty Python Style

# import the random library
import random

# define colors and bold text parameters
class color:
    def __init__(self):
        pass
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Create a list of words and initialize variables
response = ["Romani ite domum - Romans go home!", "Blessed are the cheesemakers.", "Language! And don't pick your nose!", "Manuel will show you to your rooms, if you're lucky!",
            "Alms for an ex-leper!", "What do you mean! An African swallow or a European swallow?", "Your mother was a hamster and your father smelt of elderberries!",
            "Always look on the bright side of life!", "Please! This is suppposed to be a happy occasion! Let's not bicker and argue over who killed who.", "A Duck.",
            "To seek the Holy Grail.", "Bring out your dead!", "You must cut down the mightiest tree in the forest with...a herring!", "Run Away!", "Blue, no YEELLLLLLLLLLLLOOOOOOOOWWWWWWWW!",
            "I warned you, but did you listen to me? Oh, no, you 'knew', didn't you? Oh, it's just a harmless little bunny, isn't it?",
            "If you do doubt your courage or your strength, come no further, for death awaits you all with nasty, big, pointy teeth... ", "Huh? I..I don't know that.",
            "It's just a flesh wound!", "Why don't you have another vat of wine, dear?", "You know, you came from nothing, your're going back to nothing. So, what have you lost? Nothing!",
            "He put Basil in the ratatouille!", "Or led by a bottle, more like!", "We are the knights who say...'Ni'!"]

# Random Choice
# Reference: https://docs.python.org/2/library/random.html
selection = random.choice(response)
answer = selection

# program title, describe the program and print instructions for the user
print color.BOLD + '                                        Fortune Telling...Monty Python Style\n\n' + color.END
print ('\n\nThis program is channeling the formidable, albeit ludicrous, spirit of Monty Python. Clear your mind and focus on your most burning desires.\n')
print ('Now, if you are truly courageous and ready to hear your fate, you may ask the spirit your question.\n'
       '\nRemember, only ask if you dare!')

# accept the user's question as input
question = raw_input('\nOk, you have been warned! What is your question? \n')

# print the randomized answer
print answer

keepGoing = raw_input("\nWould you like to ask another question? Enter the word 'yes' to continue or 'no' to stop. ")

# the variable, keepGoing, will keep track of whether or not the user wants to keep asking questions
# if the keepGoing value is no, the program will stop
# if the keepGoing value is yes, the program will allow the user to ask another question
while keepGoing == 'yes':
        nextQuestion = raw_input('\nWhat is your next question? \n')
        selection = random.choice(response)
        answer = selection
        print answer
        keepGoing = raw_input("\nIf you would like to ask another question, enter 'yes' to continue or 'no' to stop. ")

print ("\n\nThank you for asking your questions! And, remember...BEWARE the code of Python!!!")

