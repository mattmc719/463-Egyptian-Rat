import pygame
import random
import collections
pygame.init()
#setup code

deckImg = ["PNG/AC.png","PNG/2C.png","PNG/3C.png","PNG/4C.png","PNG/5C.png","PNG/6C.png",
"PNG/7C.png","PNG/8C.png","PNG/9C.png","PNG/10C.png","PNG/JC.png","PNG/QC.png",
"PNG/KC.png",
"PNG/AS.png","PNG/2S.png","PNG/3S.png","PNG/4S.png","PNG/5S.png","PNG/6S.png",
"PNG/7S.png","PNG/8S.png","PNG/9S.png","PNG/10S.png","PNG/JS.png","PNG/QS.png",
"PNG/KS.png",
"PNG/AD.png","PNG/2D.png","PNG/3D.png","PNG/4D.png","PNG/5D.png","PNG/6D.png",
"PNG/7D.png","PNG/8D.png","PNG/9D.png","PNG/10D.png","PNG/JD.png","PNG/QD.png",
"PNG/KD.png",
"PNG/AH.png","PNG/2H.png","PNG/3H.png","PNG/4H.png","PNG/5H.png","PNG/6H.png",
"PNG/7H.png","PNG/8H.png","PNG/9H.png","PNG/10H.png","PNG/JH.png","PNG/QH.png",
"PNG/KH.png"
]

display_height = 900
display_width = 800
cardHeight = 100
cardWidth = 70
win = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Egyptian Rat Screw')

# Deque setup
player = collections.deque()
cpu1 = collections.deque()
cpu2 = collections.deque()
cpu3 = collections.deque()
stack = collections.deque()
random.shuffle(deckImg)
for i in deckImg[0:12]:  # deal cards
   player.append(i)
for i in deckImg[13:25]:  # deal cards
   cpu1.append(i)
for i in deckImg[26:38]:  # deal cards
   cpu2.append(i)
for i in deckImg[39:51]:  # deal cards
   cpu3.append(i)


#function used to create text. args are desired text and fontsize
def textObject(text,font):
        textSurface = font.render(text,True,(255,255,255))
        return textSurface, textSurface.get_rect()

#function displays text at given coordinate.
def displayText(x,y,text,size):
    font = pygame.font.Font('freesansbold.ttf',size)
    textSurf, textText = textObject(text,font)
    textText.center = (x,y)
    win.blit(textSurf,textText)

    pygame.display.update()
# create button with passed in parameters. changes color on hover and onclick
# evokes a given function MIGHT NOT NEED BUTTONS ANYMORE SINCE
# WE'RE DOING KEYBOARD INPUTS
'''
def button(x,y,width,height,color,hoverColor, function):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height  > mouse[1] > y:
        pygame.draw.rect(win, hoverColor,(x,y,width,height))

        if click[0] == 1:
            function()
    else:
        pygame.draw.rect(win, color,(x,y,width,height))
'''
# display home screen and start button
def welcomeDisplay():
    titleFont = pygame.font.Font('freesansbold.ttf',50)
    instructFont = pygame.font.Font('freesansbold.ttf',30)
    titleSurf, titleText = textObject("Egyptian Rat Screw",titleFont)
    instructSurf, instructText = textObject("How To Play",instructFont)

    titleText.center = ((display_width/2), (display_height/2 - 350))
    win.blit(titleSurf,titleText)

    displayCard(display_width / 2 - 75, display_height /2 - 225 ,player[0])

    instructText.center = ((display_width/2), (display_height/2 + 150))
    win.blit(instructSurf,instructText)

    pygame.display.update()

# create initial play area
def playArea():
    #player
    displayCard(display_width / 2 - 75 , display_height/2 + 200,  player[0])
    displayText(530,670,"Player",35)
    displayText(530,705,"12",35)

    #cpu2
    displayCard(display_width / 2 - 75 , display_height/2 - 400,  cpu2[0])
    displayText(530,65,"CPU 2",35)
    displayText(530,100,"12",35)

    #middle pile
    # 4 possible scenarios: empty stack, stack has one card, two cards, or more than two cards
    # must display cards in correct order to prevent overlap
    if not stack:
        displayCard(display_width / 2 - 75 , display_height/2 - 100,  0)
        displayCard(display_width / 2 - 50 , display_height/2 - 100,  0)
        displayCard(display_width / 2 - 25 , display_height/2 - 100, 0)
    elif len(stack) == 1:
        displayCard(display_width / 2 - 25 , display_height/2 - 100,  stack[0])
    elif len(stack) == 2:
        displayCard(display_width / 2 - 75 , display_height/2 - 100, 0)
        displayCard(display_width / 2 - 50 , display_height/2 - 100,  stack[0])
        displayCard(display_width / 2 - 25 , display_height/2 - 100,  stack[1])
    else:
        displayCard(display_width / 2 - 75 , display_height/2 - 100, stack[len(stack) - 3])
        displayCard(display_width / 2 - 50 , display_height/2 - 100, stack[len(stack) - 2])
        displayCard(display_width / 2 - 25 , display_height/2 - 100, stack[len(stack)- 1])
    #cpu1
    displayCard(display_width / 2 + 200 , display_height/2 - 100,  cpu1[0])
    displayText(100,300,"CPU 1",35)
    displayText(100,335,"12",35)

    #cpu3
    displayCard(display_width / 2 - 350 , display_height/2 - 100,  cpu3[0])
    displayText(700,300,"CPU 3",35)
    displayText(700,335,"12",35)

# win/lose Screen
def endGame(outcome):
    titleFont = pygame.font.Font('freesansbold.ttf',50)
    instructFont = pygame.font.Font('freesansbold.ttf',30)
    if(outcome == 1):
        titleSurf, titleText = textObject("You Win!",titleFont)
    else:
        titleSurf, titleText = textObject("You Lose!",titleFont)

    instructSurf, instructText = textObject("Play Again?",instructFont)

    titleText.center = ((display_width/2), (display_height/2 - 200))
    win.blit(titleSurf,titleText)


    instructText.center = ((display_width/2 - 15), (display_height/2 + 150))
    win.blit(instructSurf,instructText)

    pygame.display.update()

# generates a random card to display
def genCard():
    random.shuffle(deckImg)
    cardBack = pygame.image.load(deckImg[0])
    cardBack = pygame.transform.rotozoom(cardBack, 0, .3)
    print(deckImg[0][4])
    win.blit(cardBack, (200,200))

def displayCard(x,y,card):
    if card == 0:
        cardBack = pygame.image.load("PNG/blue_back.png")
    else:
        cardBack = pygame.image.load(card)
    cardBack  = pygame.transform.rotozoom(cardBack ,0,.2)
    win.blit(cardBack,(x,y))

def addCard(activePlayer):
    print(activePlayer[0])
    stack.append(activePlayer.popleft())

# home screen
def main():
    win.fill((0,0,0))
    welcomeDisplay()

    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            run = False
        pygame.display.update()

# game screen
def game():
    win.fill((0,0,0))
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        playArea()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            addCard(player)
            print(stack)

        if keys[pygame.K_DOWN]:
            run = False
        pygame.display.update()


# end game
def end():
    win.fill((0,0,0))
    outcome = random.randint(0,1)
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        endGame(outcome)
        button(display_height / 2 - 50,display_width / 2 - 75,cardWidth,cardHeight,(128,128,0), (0,128,0), end)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            run = False
        pygame.display.update()

def test1():
    win.fill((0,0,0))
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        button(display_height / 2 - 50,display_width / 2 - 75,cardWidth,cardHeight,(128,128,0), (0,128,0), genCard)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            run = False
        pygame.display.update()


#function calls
main()
game()

pygame.quit()
quit()
