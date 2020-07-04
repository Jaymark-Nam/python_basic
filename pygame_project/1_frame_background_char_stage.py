import os
import pygame


### DEFAULT SETTINGS
pygame.init()

screen_width = 640      
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("JAE's GAME")

clock = pygame.time.Clock()

###USER SETTINGS(BACKGROUND<CHARACTER)


#current_path = os.path.dirname(__file__)
#image_path = os.path.join(current_path,"image")

background =  pygame.image.load("D:\\pygame_project\\image\\background.png")

stage =  pygame.image.load("D:\\pygame_project\\image\\stage.png")
stage_size = stage.get_rect().size
stage_height = stage_size[1]


character =  pygame.image.load("D:\\pygame_project\\image\\char.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height - stage_height



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
    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height - stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))


    pygame.display.update()  #게임화면 다시 그리기! 이거없으면 실행 안됨

pygame.QUIT