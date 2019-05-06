import random
import collections
import time
import threading
from random import randint


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

def menu():
    #menu stuff goes here

def shuffle(player,cpu1,cpu2,cpu3):
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
    
    for i in deck[0:12]: #deal cards
        player.append(i)
    for i in deck[13:25]: #deal cards
        cpu1.append(i)
    for i in deck[26:38]: #deal cards
        cpu2.append(i)
    for i in deck[39:51]: #deal cards
        cpu3.append(i)

def play():
    player = collections.deque()
    cpu1 = collections.deque()
    cpu2 = collections.deque()
    cpu3 = collections.deque()
    stack = collections.deque()
    shuffle(player,cpu1,cpu2,cpu3)
    game=0
    second #records second card
    third #records third card
    while game==0:
        turn=0
        second #records second card
        third #records third card

        if stack.count() > 1:
            second = stack()

        if stack.count() > 2:
            third = second

        if turn%4==0:
            if player:
                stack.append(player.popleft())
            else:
                turn+=1
        if turn%4==1:
            if cpu1:
                stack.append(cpu1.popleft())
            else:
                turn+=1
        if turn%4==2:
            if cpu2:
                stack.append(cpu2.popleft())
            else:
                turn+=1
        if turn%4==3:
            if cpu3:
                stack.append(cpu3.popleft())
            else:
                turn+=1

        slap(player,cpu1,cpu2,cpu3,stack,second,third,turn)

        #facetime
        if stack[0].endswith('j') or stack[0].endswith('q') or  stack[0].endswith('k') or stack[0].endswith('a'):
            face(stack[0],turn)

        if not player and cpu1 and cpu2:
            print("CPU3 wins.")
            end()
        if not player and cpu1 and cpu3:
            print("CPU2 wins.")
            end()
        if not player and cpu2 and cpu3:
            print("CPU1 wins.")
            end()
        if not cpu1 and cpu2 and cpu3:
            print("You win.")
            end()

def face(stack,turn):
    original=turn
    if stack[0].endswith('j'):
        x=1
    if stack[0].endswith('q'):
        x=2
    if stack[0].endswith('k'):
        x=3
    if stack[0].endswith('a'):
        x=4

    if turn%4==0:
        while x>0:
            if player:
                stack.append(player.popleft())
                slap(player,cpu1,cpu2,cpu3,stack,second,third,turn)
                x-=1
                if not stack:
                    return
                if stack[0].endswith('j') or stack[0].endswith('q') or stack[0].endswith('k') or stack[0].endswith('a'):
                    face(stack[0],turn+1)
            else:
                turn+=1

        if turn%4==1:
            if cpu1:
                stack.append(cpu1.popleft())
                slap(player,cpu1,cpu2,cpu3,stack,second,third,turn)
                x-=1
                if not stack:
                    return
                if stack[0].endswith('j') or stack[0].endswith('q') or stack[0].endswith('k') or stack[0].endswith('a'):
                    face(stack[0],turn+1)
            else:
                turn+=1

        if turn%4==2:
             if cpu2:
                stack.append(cpu2.popleft())
                slap(player,cpu1,cpu2,cpu3,stack,second,third,turn)
                x-=1
                if not stack:
                    return
                if stack[0].endswith('j') or stack[0].endswith('q') or stack[0].endswith('k') or stack[0].endswith('a'):
                    face(stack[0],turn+1)
             else:
                turn+=1

        if turn%4==3:
             if cpu3:
                stack.append(cpu3.popleft())
                slap(player,cpu1,cpu2,cpu3,stack,second,third,turn)
                x-=1
                if not stack:
                    return
                if stack[0].endswith('j') or stack[0].endswith('q') or stack[0].endswith('k') or stack[0].endswith('a'):
                    face(stack[0],turn+1)
             else:
                turn+=1

        if not stack[0].endswith('j') or stack[0].endswith('q') or stack[0].endswith('k') or stack[0].endswith('a'):
            #append everything to one who put down face card.
            if original%4==0:
                while stack:
                    player.append(stack.popleft())
                    time.sleep(2)

            if original%4==1:
                while stack:
                    cpu1.append(stack.popleft())
                    time.sleep(2)

            if original%4==2:
                while stack:
                    cpu2.append(stack.popleft())
                    time.sleep(2)

            if original%4==3:
                while stack:
                    cpu3.append(stack.popleft())
                    time.sleep(2)

def slap(player,cpu1,cpu2,cpu3,stack,second,third,turn):

        #slap function goes here and check for these conditions.
        #button for player here
        if stack[0].endswith()==second.endswith() or stack[0].endswith()==third.endswith():
            while stack:
                player.append(stack.popleft())
            while turn%4!=0:
                turn+=1
        #failure...
        else:
            stack.appendleft(player.pop())

        #after input
        if stack[0].endswith()==second.endswith() or stack[0].endswith()==third.endswith():
            chance=randint(0,9)
            if chance <4:
                steal=randint(1,3)
                if steal==1:
                    while stack:
                        cpu1.append(stack.popleft())
                        while turn%4!=1:
                            turn+=1
                if steal==2:
                    while stack:
                        cpu2.append(stack.popleft())
                        while turn%4!=2:
                            turn+=1
                if steal==3:
                    while stack:
                        cpu3.append(stack.popleft())
                        while turn%4!=3:
                            turn+=1


            
def end():
        choice=input("Do you wanna play again?(y/n)")
        if choice=="y" or choice=="Y":
            play()
        #no
        else:
            exit()

