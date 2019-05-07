import pygame
import random
import hello
pygame.init()
#setup code
deck = ["ca", "sa", "ha", "da",
        "c1", "s1", 'h1','d1',
        "c2", "s2", "h2", "d2",
        "c3", "s3", 'h3','d3',
        "c4", "s4", "h4", "d4",
        "cq", "sq", "hq", "dq",
        "c5", "s5", 'h5','d5',
        "c6", "s6", "h6", "d6",
        "c7", "s7", 'h7','d7',
        "c8", "s8", "h8", "d8",
        "c9", "s9", 'h9','d9',
        "c10", "s10", "h10", "d10",
        "cj", "sj", 'hj','dj',
        "ck", "sk", 'hk','dk']

deckImg = ["PNG/AC.png","PNG/2C.png","PNG/3C.png","PNG/4C.png","PNG/5C.png","PNG/6C.png",
            "PNG/7C.png","PNG/8C.png","PNG/9C.png","PNG/10C.png","PNG/JC.png","PNG/QC.png",
            "PNG/KC.png",
            "PNG/AS.png","PNG/2S.png","PNG/3S.png","PNG/4S.png","PNG/5S.png","PNG/6S.png",
            "PNG/7S.png","PNG/8S.png","PNG/9S.png","PNG/10S.png","PNG/JS.png","PNG/QS.png",
            "PNG/KS.png"
            "PNG/AD.png","PNG/2D.png","PNG/3D.png","PNG/4D.png","PNG/5D.png","PNG/6D.png",
            "PNG/7D.png","PNG/8D.png","PNG/9D.png","PNG/10D.png","PNG/JD.png","PNG/QD.png",
            "PNG/KD.png",
            "PNG/AH.png","PNG/2H.png","PNG/3H.png","PNG/4H.png","PNG/5H.png","PNG/6H.png",
            "PNG/7H.png","PNG/8H.png","PNG/9H.png","PNG/10H.png","PNG/JH.png","PNG/QH.png",
            "PNG/KH.png"
            ]
random.shuffle(deck)
display_height = 600
display_width = 600
cardHeight = 100
cardWidth = 70
win = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Egyptian Rat Screw')

# shuffle and display top of deck. rotozoom used to resize png

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
# evokes a given function
def button(x,y,width,height,color,hoverColor, function):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height  > mouse[1] > y:
        pygame.draw.rect(win, hoverColor,(x,y,width,height))

        if click[0] == 1:
            function()
    else:
        pygame.draw.rect(win, color,(x,y,width,height))

# display home screen and start button
def welcomeDisplay():
    titleFont = pygame.font.Font('freesansbold.ttf',50)
    instructFont = pygame.font.Font('freesansbold.ttf',30)
    titleSurf, titleText = textObject("Egyptian Rat Screw",titleFont)
    instructSurf, instructText = textObject("How To Play",instructFont)

    titleText.center = ((display_width/2), (display_height/2 - 200))
    win.blit(titleSurf,titleText)


    instructText.center = ((display_width/2 - 15), (display_height/2 + 150))
    win.blit(instructSurf,instructText)

    pygame.display.update()

# create initial play area
def playArea():
    #player
    button(display_width / 2 - 50, display_height / 2 + 150, cardWidth,cardHeight,(0,0,255), (0,128,0), game)
    displayText(360,470,"Player",20)
    #cpu2
    button(display_width / 2 - 50, display_height / 2 - 250, cardWidth,cardHeight,(255,0,0), (0,128,0), game)
    displayText(360,60,"CPU 2",20)

    #middle pile
    button(display_width / 2 - 50, display_height / 2 - 50, cardWidth,cardHeight,(255,255,255), (0,128,0), end)

    #cpu1
    button(display_width / 2 - 250, display_height / 2 - 50, cardWidth,cardHeight,(0,255,0), (0,128,0), game)
    displayText(480 ,370,"CPU 3",20)

    #cpu3
    button(display_width / 2 + 150, display_height / 2 - 50, cardWidth,cardHeight,(128,128,128), (0,128,0), game)
    displayText(80,370,"CPU 4",20)

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
        #start
        button(display_width / 2 - 50, display_height / 2 - 75, cardWidth,cardHeight,(128,128,0), (0,128,0), game)


        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
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
            run = False
        pygame.display.update()

# if outcome decided, go to endgame
if():
    end()

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
end()

pygame.quit()
quit()
