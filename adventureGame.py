import time
import sys
import random

# disable output buffering
class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)
sys.stdout = Unbuffered(sys.stdout)

def sleepPrint(message):
    time.sleep(2)
    print(message)

def rollDice():
    return random.randint(1,3)

def getFirstChoice ():
    firstChoice = input("Press 1 to regain your wits by resting in the cave.  Press 2 to venture off on the trail.")
    if firstChoice == "1":
        getCaveResults()
    elif firstChoice == "2":
        getTrailResults()
    else:
        getFirstChoice()

def getCaveResults ():
    roll = rollDice()
    if roll == 1:
        sleepPrint("With your left foot you step on a rattlesnake.  Your right, a scorpion.  You Died.")
    elif roll == 2:
        sleepPrint("Oh, there is the treasure.  That was easy!")
    elif roll == 3:
        sleepPrint("There is something warm and fuzzy in this cave.  A bear.  You Died")
    playAgain()

def getTrailResults ():
    roll = rollDice()
    if roll == 1:
        sleepPrint("You set on the trail, weary and tired.  A storm sets in.  You succumb to exposure.  You Died")
    elif roll == 2:
        sleepPrint("Your determination has paid off.  You climb to the top of the mountain and find the treasure!")
    elif roll == 3:
        sleepPrint("You set out only to find that you look like dinner to the wolves.  You Died")
    playAgain()


def playAgain ():
    restart = input("Press 1 to play again.  Press 2 to quit.")
    if restart == "1":
        playGame()
    elif restart == "2":
        sleepPrint("Bye Bye")
    else:
        playAgain()

def playGame ():
    sleepPrint("Welcome the your adventure to find the treasure!")
    sleepPrint("Your adventure begins in the dark foothills of the Onyx Mountain in the Black Forest.")
    sleepPrint("You wake up cold and confused.  You look around to see a cave and a trail heading up into the mountain.")
    getFirstChoice()

playGame()
