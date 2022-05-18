import pygame

FPS = 60
WHITE = (255,255,255)
WIDTH = 500
HIGHT = 600

pygame.init() #遊戲初始化
screen = pygame.display.set_mode((WIDTH,HIGHT)) #創建視窗
pygame.display.set_caption("main") #命名視窗
clock = pygame.time.Clock()


running = True

while running:
    clock.tick(FPS) #一秒鐘之內執行次數 FPS
    
    #取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #畫面顯示
    screen.fill(WHITE)  #視窗填滿
    pygame.display.update() #更新   
    
    
pygame.quit()
            
        