import pygame


### DEFAULT SETTINGS
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("JAE GAME")

clock = pygame.time.Clock()

###USER SETTINGS(BACKGROUND<CHARACTER)




running = True      
while running:
    dt = clock.tick(30)     
    ### EVENT(KEYBOARD,MOUSE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    ### GAME CHARACTOR LOCATION


    ### COLLISION


    ###DRAW IN SCREEN

    pygame.display.update()  #게임화면 다시 그리기! 이거없으면 실행 안됨

pygame.QUIT