import pygame
import random
pygame.init()

# initialize window to win and set height and width
win = pygame.display.set_mode((500,500))


#loop that constantly checks for updates
run = True
while run:
    pygame.time.delay(100)
    
    #checks if window closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # draw rectangle (window, color, (x.pos, y.post, width, height) )
    pygame.draw.rect(win,(255,0,0), (250,50,100,50))

    
    #checks mouse x and y coordinates
    mouse = pygame.mouse.get_pos()

    #parameters of green box (player's deck). change these variables to change the box
    x = 220
    y = 320
    height = 110
    width =  80
    
    #calculation to check if mouse position is within the rectangle, highlight it 
    if  x + height > mouse[0] > x and width + y > mouse[1] > y:
        pygame.draw.rect(win,(128,128,0), (x,y,width,height))
    else:
        pygame.draw.rect(win,(0,128,0), (x,y,width,height))
    
    #needed to update window display
    pygame.display.update()

    #checks for key press and stores in array
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        print("Slap ")

    if keys[pygame.K_UP]:
        print("UP")

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
