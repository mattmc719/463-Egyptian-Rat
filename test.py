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
display_height = 500
display_width = 800
win = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Egyptian Rat Screw')
cardBack = pygame.image.load('card.png')
cardFront = pygame.image.load('card front.png')

def textObject(text,font):
        textSurface = font.render(text,True,(255,255,255))
        return textSurface, textSurface.get_rect()

def welcomeDisplay():
    titleFont = pygame.font.Font('freesansbold.ttf',30)
    instructFont = pygame.font.Font('freesansbold.ttf',20)
    titleSurf, titleText = textObject("Egyptian Rat Screw",titleFont)
    instructSurf, instructText = textObject("How To Play",instructFont)

    titleText.center = ((display_width/2), (display_height/2 - 200))
    win.blit(titleSurf,titleText)

    win.blit(cardBack,(350,display_height / 2 - 100))

    instructText.center = ((display_width/2), (display_height/2 + 150))
    win.blit(instructSurf,instructText)

    pygame.display.update()


def main():
    welcomeDisplay()
    
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.draw.rect(win,(255,0,0), (200,150,100,140))
        mouse = pygame.mouse.get_pos()
        print(mouse)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            run = False
        pygame.display.update()

    '''

        mouse = pygame.mouse.get_pos()

        x = 220
        y = 320
        height = 110
        width =  80
        if  x + height > mouse[0] > x and width + y > mouse[1] > y:
            pygame.draw.rect(win,(128,128,0), (x,y,width,height))
        else:
            pygame.draw.rect(win,(0,128,0), (x,y,width,height))

        if keys[pygame.K_UP]:
            print("UP")
    '''

def game():
    win.fill((255,255,255))
    print("GAME LOOP")
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.draw.rect(win,(255,0,0), (200,150,100,140))
        mouse = pygame.mouse.get_pos()
        print(mouse)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            run = False
        pygame.display.update()


#function calls
main()
game()
over()
pygame.quit()
quit()
