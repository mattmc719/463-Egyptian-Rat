import pygame
import random
pygame.init()

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
random.shuffle(deck)

#setup code
display_height = 1000
display_width = 1000
cardHeight = 200
cardWidth = 140
win = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Egyptian Rat Screw')
#cardBack = pygame.image.load('card.png')
#cardFront = pygame.image.load('card front.png')

def textObject(text,font):
        textSurface = font.render(text,True,(255,255,255))
        return textSurface, textSurface.get_rect()

def displayText(x,y,text,size):

    font = pygame.font.Font('freesansbold.ttf',size)
    textSurf, textText = textObject(text,font)
    textText.center = (x,y)
    win.blit(textSurf,textText)

    pygame.display.update()


def welcomeDisplay():
    titleFont = pygame.font.Font('freesansbold.ttf',60)
    instructFont = pygame.font.Font('freesansbold.ttf',40)
    titleSurf, titleText = textObject("Egyptian Rat Screw",titleFont)
    instructSurf, instructText = textObject("How To Play",instructFont)

    titleText.center = ((display_width/2), (display_height/2 - 400))
    win.blit(titleSurf,titleText)


    instructText.center = ((display_width/2), (display_height/2 + 350))
    win.blit(instructSurf,instructText)

    pygame.display.update()

#def playArea():



# button function to create buttons with specified properties and a
# function when clicked within the bounds
def button(x,y,width,height,color,hoverColor, function):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height  > mouse[1] > y:
        pygame.draw.rect(win, hoverColor,(x,y,width,height))

        if click[0] == 1:
            function()
    else:
        pygame.draw.rect(win, color,(x,y,width,height))





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

        #player
        button(display_width / 2 - 50, display_height / 2 + 250, cardWidth,cardHeight,(0,0,255), (0,128,0), game)
        displayText(650,780,"Player",30)

        #cpu2
        button(display_width / 2 - 50, display_height / 2 - 400, cardWidth,cardHeight,(255,0,0), (0,128,0), game)
        displayText(650,120,"CPU 2",30)

        #middle pile
        button(display_width / 2 - 50, display_height / 2 - 70, cardWidth,cardHeight,(255,255,255), (0,128,0), game)

        #cpu1
        button(display_width / 2 - 400, display_height / 2 - 70, cardWidth,cardHeight,(0,255,0), (0,128,0), game)
        displayText(900,650,"CPU 3",30)

        #cpu3
        button(display_width / 2 + 300, display_height / 2 - 70, cardWidth,cardHeight,(128,128,128), (0,128,0), game)
        displayText(150,650,"CPU 4",30)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            run = False
        pygame.display.update()

# end game
def end():
    win.fill((0,0,0))

    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        button(350,150,100,150,(128,128,0), (0,128,0), main)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            run = False
        pygame.display.update()

#function calls
game()
pygame.quit()
quit()
