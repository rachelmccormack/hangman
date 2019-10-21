import urllib.request
import random

class Hangman:
    def __init__(self):
        self.gameWon = False
        self.gameLost = False
        self.misses = 0
        self.guessedLetters = []

    def man(self):
        head  = "   o "
        neck = " - | - "
        legs = "  / \\ "
        if self.misses > 0:
            print( head )
        if self.misses == 2:
            print(neck[:2])
        elif self.misses ==  3:
            print(neck[:4])
        elif self.misses > 3:
            print(neck)
        if self.misses == 5:
            print (legs[:4])
        elif self.misses>5:
            print (legs)
        #Must be more elegant way of doing this- console always outputs None?

    def word(self, goal):
        self.wordList = list(goal)
        self.wordList = [i.replace(' ', '_') for i in self.wordList]
        self.guessing = ['_'] * len(goal)

    def display(self):
        print (self.guessing)
        print ("So far you have guessed: " )
        print(self.guessedLetters)
        print("\n")
        self.man()

    def checkGame(self):

        if self.guessing == self.wordList:
            self.gameWon = True
        if self.misses > 5:
            self.gameLost = True
        self.display()

    def check(self, letter):
        self.guessedLetters.append(letter)
        if letter in self.wordList and letter not in self.guessing:
            self.guessing
            for i, x in enumerate(self.wordList):
                if x == letter:
                    self.guessing[i] = self.wordList[i]
            self.checkGame()
        else:
            self.misses += 1
            self.checkGame()


game = Hangman()

with urllib.request.urlopen("http://www.desiquintans.com/downloads/nounlist/nounlist.txt") as url:
    txt = url.read()
    words = txt.splitlines()

goal = random.choice(words)
game.word((goal.decode("utf-8")))

while not game.gameLost and not game.gameWon:
    game.check(str(input("Hello, please guess a letter: ")))
if game.gameWon:
    print ("YOU WON")
else:
    print("YOU LOST")
print("The word was : " + goal.decode("utf-8"))
print ("GAME OVER")



