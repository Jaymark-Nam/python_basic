
import pygame

pygame.init()  #초기화. pygame import 반드시

#화면 크기 설정
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("JAE GAME")

running = True #if game is continueing?
while running :
    for event in pygame.event.get():    #pygame 쓰기 위해 필수 코드
        if event.type ==pygame.QUIT:        #여러개 이벤트 중 QUIT이 발생할 때
            running = False


# pygame exit
pygame.quit()
