import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("JAE GAME")

background = pygame.image.load("D:\\pygame_basic\\background.png")

character =  pygame.image.load("D:\\pygame_basic\\character.png")
character_size = character.get_rect().size #character size?
character_width = character_size[0] #character wid
character_height = character_size[1] #character height
character_x_pos = screen_width / 2 - (character_width/2)  #character x location
character_y_pos = screen_height - character_height  #character y location


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(background, (0,0)) #background
    screen.blit(character, (character_x_pos, character_y_pos)) #character 

    pygame.display.update()  #게임화면 다시 그리기! 이거없으면 실행 안됨

pygame.QUIT