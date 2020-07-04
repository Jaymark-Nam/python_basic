import random
import pygame


### DEFAULT SETTINGS
pygame.init()




screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("JAE GAME")

clock = pygame.time.Clock()

###USER SETTINGS(BACKGROUND<CHARACTER)
background = pygame.image.load("D:\\pygame_basic\\background.png")

character = pygame.image.load("D:\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height

to_x = 0
character_speed = 10

ddong = pygame.image.load("D:\\pygame_basic\\enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 10


running = True      
while running:
    dt = clock.tick(30)     
    ### EVENT(KEYBOARD,MOUSE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT :
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
                

    ### GAME CHARACTOR LOCATION
    character_x_pos += to_x

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed

    if ddong_y_pos > screen_height :
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width-ddong_width)

    ### COLLISION

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    
    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("Crashed!")
        running = False


    ###DRAW IN SCREEN
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(ddong,(ddong_x_pos, ddong_y_pos))
    
    pygame.display.update()  #게임화면 다시 그리기! 이거없으면 실행 안됨
    


pygame.QUIT