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


to_x = 0
to_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:    #key 눌러졌는 지 확인
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
        if event.type == pygame.KEYUP :         #키 뗐을때!
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x=0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0


    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0 : 
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width : 
        character_x_pos = screen_width - character_width

    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height - character_height

    screen.blit(background, (0,0)) #background
    screen.blit(character, (character_x_pos, character_y_pos)) #character 

    pygame.display.update()  #게임화면 다시 그리기! 이거없으면 실행 안됨

pygame.QUIT