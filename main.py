import random
import collections
import time


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
    #use clocks
    second #records second card
    third #records third card
    if stack.append()==deck.endswith('j') ##jack condition

    if stack.append()==deck.endswith('q') ##jack condition ##queen condition

    if stack.append()==deck.endswith('k') ##jack condition ##king, three times

    if stack.append()==deck.endswith('a') ##jack condition ##aces, four times

    #slap function goes here and check for these conditions.
    if stack.append()==##pairs

    ##sandwiches
