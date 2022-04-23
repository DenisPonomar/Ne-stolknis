import sys, pygame
pygame.init()
class MyBallClass(pygame.sprite.Sprite): #������ ����� ���������
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] and keystate[pygame.K_RIGHT] == False:
            self.speed[0] = -3*koeff #���� ������ �� ������� �����, �� ��������� ������ �����
        if keystate[pygame.K_RIGHT] and keystate[pygame.K_LEFT] == False:
            self.speed[0] = 3*koeff #���� ������ �� ������� ������, �� ��������� ������ ������

        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0] #���� ��������� ��������� �� ������, �� ��� ���������
class MyRaketaClass(pygame.sprite.Sprite): #������ ����� ������ 
    def __init__(self, image_filey, locationy, speedy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_filey)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = locationy
        self.speedy = speedy
        
    def move(self):
        self.rect = self.rect.move(self.speedy)

        if self.rect.left < 0 or self.rect.right > width:
            self.speedy[0] = -self.speedy[0] #���� ��������� ��������� �� ������, �� �� ���������
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speedy[1] = -self.speedy[1] #���� ��������� ��������� � �������� ��� �����, �� �� ���������
size = width, height = 640, 480 #������������ ������ ����
screen = pygame.display.set_mode(size)

koeff = 1 #������ ����������, ������� ����� ������������� �� ����� ���� 

score = 0 #������ ����, ������� ����� ������������� �� ����� ����
score_font = pygame.font.Font(None, 36)
score_surf = score_font.render(str(score), 1, (0, 0, 0))
score_pos = [10, 10] #������ ���������� ��� ����������� �����

img_filey = "image\kubik.jpg" #������ ���������� � ������ ����� ������
img_file = "image\platforma.jpg" #������ ���������� � ������ ����� ���������
balls = [] #������ ������, � ������� ����� ������� ��������� � �����
speed = [0, 0] #������ ������ �� ��������� ���������
speedy = [1, 1] #������ ������ �� ��������� ������
location = [270, 430] #������ ������ � ������������ ���������
locationy = [270, 0] #������ ������ � ������������ ������
ball = MyBallClass(img_file, location, speed) #������ ���������
raketa = MyRaketaClass(img_filey, locationy, speedy) #������ ����� 
balls.append(ball) #�������� ��������� � ������
balls.append(raketa) #�������� ����� � ������

myachi = pygame.sprite.Group() #������ ������ ��������
myachi.add(ball) #�������� ��������� � ������

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill([255, 255, 255])
    keystate = pygame.key.get_pressed()

    if score == 0:
        speedy[0] = speedy[0]/koeff
        speedy[1] = speedy[1]/koeff
        koeff = 1

    score = score + 0.02
    ochki = "Score: " + str(int(score))
    score_surf = score_font.render(ochki, 1, (0, 0, 0))

    screen.blit(score_surf, score_pos)
    
    speedy[0] = speedy[0]*1.0002
    speedy[1] = speedy[1]*1.0002

    koeff = koeff*1.0002
    
    for ball in balls:
        ball.move()
        raketa.move()
        screen.blit(ball.image, ball.rect)
      
    pygame.display.flip()    
    if pygame.sprite.spritecollide(raketa, myachi, False):
        final_text1 = "Game Over"
        final_text2 = "Score: " + str(int(score))
        ft1_font = pygame.font.Font(None, 70)
        ft1_surf = ft1_font.render(final_text1, 1, (0, 0, 0))
        ft2_font = pygame.font.Font(None, 50)
        ft2_surf = ft2_font.render(final_text2, 1, (0, 0, 0))
        screen.blit(ft1_surf, [screen.get_width()/2 - ft1_surf.get_width()/2, 100])
        screen.blit(ft2_surf, [screen.get_width()/2 - ft2_surf.get_width()/2, 200])
        speedy[0] = -speedy[0]
        speedy[1] = -speedy[1]
        pygame.display.flip()
        clock.tick(1)
        score = 0
    clock.tick(50)
pygame.quit()
