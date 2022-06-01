import pygame

FPS = 60
WIDTH = 500
HIGHT = 600

WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init() #遊戲初始化
screen = pygame.display.set_mode((WIDTH,HIGHT)) #創建視窗
pygame.display.set_caption("main") #命名視窗
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(GREEN)  
        self.rect = self.image.get_rect()  #框起來
        
        #self.rect.x = 200 #設定位置
        #self.rect.y = 200
        #top、right、center.......
        self.rect.center = (WIDTH/2,HIGHT/2)
       
    def update(self):
        self.rect.x += 2 #往右動
        if self.rect.left > HIGHT:
            self.rect.right = 0
all_sprites = pygame.sprite.Group()  #創建群組  
player = Player()    
all_sprites.add(player)

running = True

while running:
    clock.tick(FPS) #一秒鐘之內執行次數 FPS
    
    #取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #更新遊戲
    all_sprites.update() #執行update
            
    #畫面顯示
    screen.fill(WHITE)  #視窗填滿
    
    all_sprites.draw(screen)
    pygame.display.update() #更新   

pygame.quit()
            
        