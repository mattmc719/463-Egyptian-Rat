import random
import collections
import time
from threading import Timer
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

def play():
    player = collections.deque()
    cpu1 = collections.deque()
    cpu2 = collections.deque()
    cpu3 = collections.deque()
    stack = collections.deque()

    deck = ["ca", "sa", "ha", "da",
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

    for i in deck[0:12]:  # deal cards
        player.append(i)
    for i in deck[13:25]:  # deal cards
        cpu1.append(i)
    for i in deck[26:38]:  # deal cards
        cpu2.append(i)
    for i in deck[39:51]:  # deal cards
        cpu3.append(i)
    game = 0
    turn = 0
    while game == 0:
        print("\n",len(player),"\n",len(cpu1),"\n",len(cpu2),"\n",len(cpu3))
        if turn % 4 == 0:
            if player:
                print("Player plays: ",player[0])
                stack.append(player.popleft())
            else:
                turn += 1
        if turn % 4 == 1:
            if cpu1:
                print("CPU1 plays: ", cpu1[0])
                stack.append(cpu1.popleft())
            else:
                turn += 1
        if turn % 4 == 2:
            if cpu2:
                print("CPU2 plays: ", cpu2[0])
                stack.append(cpu2.popleft())
            else:
                turn += 1
        if turn % 4 == 3:
            if cpu3:
                print("CPU3 plays: ", cpu3[0])
                stack.append(cpu3.popleft())
            else:
                turn += 1

        turn=slap(player, cpu1, cpu2, cpu3, stack, turn)
        if len(stack)==0:
            print("New stack.")
        elif stack[-1][1]=='j' or stack[-1][1]=='q' or stack[-1][1]=='k' or stack[-1][1]=='a':
            turn = face(player, cpu1, cpu2, cpu3, stack, turn)
        if len(stack) !=0:
            turn += 1

        print("Priority: ", turn%4)
        # facetime
        if not player and not cpu1 and not cpu2:
            print("CPU3 wins.")
            end()
        if not player and not cpu1 and not cpu3:
            print("CPU2 wins.")
            end()
        if not player and not cpu2 and not cpu3:
            print("CPU1 wins.")
            end()
        if not cpu1 and not cpu2 and not cpu3:
            print("You win.")
            end()

def face(player, cpu1, cpu2, cpu3, stack, original):
    turn = original+1

    if stack[-1][1]=='j':
        print("A jack has been played, set one: ")
        x = 1
    if stack[-1][1]=='q':
        print("A queen has been played, set two: ")
        x = 2
    if stack[-1][1]=='k':
        print("A king has been played, set three: ")
        x = 3
    if stack[-1][1]=='a':
        print("An ace has been played, set four: ")
        x = 4

    if turn % 4 == 0:
        while x > 0:
            if player:
                print("Player places: ", player[0])
                stack.append(player.popleft())
                original=slap(player, cpu1, cpu2, cpu3, stack, original)
                if len(stack) == 0:
                    return original
                x-=1
                if stack[-1][1]=='j' or stack[-1][1]=='q' or stack[-1][1]=='k' or stack[-1][1]=='a':
                    original=turn
                    original=face(player, cpu1, cpu2, cpu3, stack, original)
                    return original
            else:
                turn += 1
                continue

    if turn % 4 == 1:
        while x > 0:
            if cpu1:
                print("CPU1 places: ", cpu1[0])
                stack.append(cpu1.popleft())
                original=slap(player, cpu1, cpu2, cpu3, stack, original)
                if len(stack)==0:
                    return original
                x-=1
                if stack[-1][1]=='j' or stack[-1][1]=='q' or stack[-1][1]=='k' or stack[-1][1]=='a':
                    original = turn
                    original = face(player, cpu1, cpu2, cpu3, stack, original)
                    return original
            else:
                turn += 1
                continue

    if turn % 4 == 2:
        while x > 0:
            if cpu2:
                print("CPU2 places: ", cpu2[0])
                stack.append(cpu2.popleft())
                original=slap(player, cpu1, cpu2, cpu3, stack,original)
                if len(stack)==0:
                    return original
                x-=1
                if stack[-1][1]=='j' or stack[-1][1]=='q' or stack[-1][1]=='k' or stack[-1][1]=='a':
                    original = turn
                    original = face(player, cpu1, cpu2, cpu3, stack, original)
                    return original
            else:
                turn += 1
                continue

    if turn % 4 == 3:
        while x >  0:
            if cpu3:
                print("CPU3 places: ", cpu3[0])
                stack.append(cpu3.popleft())
                original=slap(player, cpu1, cpu2, cpu3, stack, original)
                if len(stack)==0:
                    return original
                x -= 1
                if stack[-1][1]=='j' or stack[-1][1]=='q' or stack[-1][1]=='k' or stack[-1][1]=='a':
                    original = turn
                    original = face(player, cpu1, cpu2, cpu3, stack, original)
                    return original
            else:
                turn += 1
                continue

    if not stack[-1][1]=='j' or stack[-1][1]=='q' or stack[-1][1]=='k' or stack[-1][1]=='a':
        # append everything to one who put down face card.
        if original % 4 == 0:
            print("You won the stack.", stack)
            while stack:
                player.append(stack.popleft())

        if original % 4 == 1:
            print("CPU1 won the stack.", stack)
            while stack:
                cpu1.append(stack.popleft())
        if original % 4 == 2:
            print("CPU2 won the stack.", stack)
            while stack:
                cpu2.append(stack.popleft())

        if original % 4 == 3:
            print("CPU3 won the stack.", stack)
            while stack:
                cpu3.append(stack.popleft())
        print(original%4)
        return original
        time.sleep(2)


def slap(player, cpu1, cpu2, cpu3, stack, turn):
    if not stack:
        return
    if len(stack) > 1 :
        t = Timer(3.0, print, ["Continue."])
    elif len(stack) > 2:
        if stack[-1][1] == stack[-2][1] or stack[-1][1] == stack[-3][1]:
            t = Timer(3.0, print, ["Too slow."])
    else:
        t = Timer(3.0, print, ["Continue."])

    t.start()
    print("Stack: ", stack)
    slapper = input("Will you slap?")
    if slapper == 'y' and t:
        if len(stack) == 1:
            print("Dipshit. There is only one card.... well not anymore.\n You lost cards: ")
            if player:
                print(player[-1])
                stack.appendleft(player.pop())
            if player:
                print(player[-1])
                stack.appendleft(player.pop())
            if not player:
                print("Stop losing cards!")
        elif len(stack) == 2:
            if stack[-1][1] == stack[-2][1]:
                print("You got the stack.")
                while stack:
                    player.append(stack.popleft())
                    while turn % 4 != 0:
                        turn += 1
                print(turn % 4)
                return turn
            else:
                print("Dipshit. You lost cards: ")
                if player:
                    print(player[-1])
                    stack.appendleft(player.pop())
                if player:
                    print(player[-1])
                    stack.appendleft(player.pop())
                if not player:
                    print("Stop losing cards!")
        elif len(stack) >= 2:
            if stack[-1][1] == stack[-2][1] or stack[-1][1]==stack[-3][1]:
                print("You got the stack.")
                while stack:
                    player.append(stack.popleft())
                    while turn % 4 != 0:
                        turn += 1
                print(turn % 4)
                return turn
            else:
                print("Dipshit. You lost cards: ")
                if player:
                    print(player[-1])
                    stack.appendleft(player.pop())
                if player:
                    print(player[-1])
                    stack.appendleft(player.pop())
                if not player:
                    print("Stop losing cards!")

    elif slapper == 'n':
            print("You passed.")

    t.cancel()

    # after input
    if len(stack)>2:
        if stack[-1][1] == stack[-2][1] or stack[-1][1] == stack[-3][1]:
             steal = randint(1, 3)
             if steal == 1:
                print("CPU1 slapped the stack.", stack)
                while stack:
                    cpu1.append(stack.popleft())
                    while turn % 4 != 1:
                        turn += 1
             if steal == 2:
                print("CPU2 slapped the stack.", stack)
                while stack:
                    cpu2.append(stack.popleft())
                    while turn % 4 != 2:
                        turn += 1
             if steal == 3:
                print("CPU3 slapped the stack.", stack)
                while stack:
                    cpu3.append(stack.popleft())
                    while turn % 4 != 3:
                        turn += 1
    print(turn % 4)
    return turn

def end():
    choice = input("Do you wanna play again?(y/n)")
    if choice == "y" or choice == "Y":
        play()
    # no
    else:
        exit()

play()
