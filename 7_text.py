import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("JAE GAME")

clock = pygame.time.Clock()


background = pygame.image.load("D:\\pygame_basic\\background.png")
character =  pygame.image.load("D:\\pygame_basic\\character.png")
character_size = character.get_rect().size #character size?
character_width = character_size[0] #character wid
character_height = character_size[1] #character height
character_x_pos = screen_width / 2 - (character_width/2)  #character x location
character_y_pos = screen_height - character_height  #character y location

to_x = 0
to_y = 0
character_speed = 0.6



enemy =  pygame.image.load("D:\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size #character size?
enemy_width = enemy_size[0] #character wid
enemy_height = enemy_size[1] #character height
enemy_x_pos = screen_width / 2 - (enemy_width/2)  #character x location
enemy_y_pos = screen_height /2 - enemy_height/2  #character y location

game_font = pygame.font.Font(None, 40)

total_time = 10
start_ticks = pygame.time.get_ticks()  #시작 tick 받아옴


running = True      #게임진행중?
while running:
    dt = clock.tick(60)     #초당 프레임

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:    #key 눌러졌는 지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP :         #키 뗐을때!
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x=0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0


    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0 : 
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width : 
        character_x_pos = screen_width - character_width

    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height - character_height


    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("Crashed!!")
        running = False


    screen.blit(background, (0,0)) #background
    screen.blit(character, (character_x_pos, character_y_pos)) #character 
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    elapsed_time = (pygame.time.get_ticks()-start_ticks)/1000   #경과시간을 1000으로 나누어서 sec 단위 표시
    timer = game_font.render(str(int(total_time - elapsed_time)),True, (255,255,255)) #시간정보(출력할 정보), True, Color
    screen.blit(timer,(10,10))
    if total_time - elapsed_time <=0:
        print("Time out")
        running = False

    pygame.display.update()  #게임화면 다시 그리기! 이거없으면 실행 안됨
pygame.time.delay(2000) #2sec wait


pygame.QUIT