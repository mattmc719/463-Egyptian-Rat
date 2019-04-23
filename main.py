import random
import collections
import time


##First Priority: Get the game interface and basics to work.

##TODO: Player runs out of cards but they can still slap in, even if they slap incorrectly.
##TODO: Player removes two card from their pile for incorrectly slapping to bottom of stack.
##TODO: Player correctly slaps and gets all the cards in the pile.
##TODO: Player is unable to play another face card, CPU/Player that played a face card before them gets the pile.
##TODO: Player plays face card; CPU is unable to produce a face card the the player receives the pile.
##TODO: Player tries to play cards when its not their turn.
##TODO: Game pauses (disables buttons) while CPU is taking turn
##TODO: CPU waits a random amount of time between 1 and 5 seconds before slapping. CPU checks if it is a valid slap condition
##      before slapping and only one randomly selected CPU will try to slap

def main:
    deck= ["ca", "sa", "ha", "da",
              "c1", "s1", "h1", "d1",
              "c2", "s2", "h2", "d2",
              "c3", "s3", "h3", "d3",
              "c4", "s4", "h4", "d4",
              "c5", "s5", "h5", "d5",
              "c6", "s6", "h6", "d6",
              "c7", "s7", "h7", "d7",
              "c8", "s8", "h8", "d8",
              "c9", "s9", "h9", "d9",
              "c10", "s10", "h10", "d10",
              "cj", "sj", "hj", "dj",
              "cq", "sq", "hq", "dq",
              "ck", "sk", "hk", "dk"]

    random.shuffle(deck)
    random.shuffle(deck)

    player=collections.deque()
    cpu1=collections.deque()
    cpu2=collections.deque()
    cpu3=collections.deque()
    stack=collections.deque()

def menu:


def play:

    second #records second card
    third #records third card

    stack.append(player.pop())
    if stack[0]==deck.endswith('j') ##jack, once
    if stack[0]==deck.endswith('q') ##queen, twice
    if stack[0]==deck.endswith('k') ##king, three times
    if stack[0]==deck.endswith('a') ##aces, four times
    #slap function goes here and check for these conditions.
    if stack[0].endswith()==second.endswith()

    ##sandwiches
    if stack[0].endswith()==third.endswith()


    #This apparently to confirm that these are empty
    if player and cpu1 and cpu2:
        print("CPU3 wins.")
        end()
    if player and cpu1 and cpu3:
        print("CPU2 wins.")
        end()
    if player and cpu2 and cpu3:
        print("CPU1 wins.")
        end()
    if cpu1 and cpu2 and cpu3:
        print("You win.")
        end()
def end:
        choice=input("Do you wanna play again?(y/n)")
        input=="y" or input=="Y":
            play()
        #no
        else:
            exit()
