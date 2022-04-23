import sys, pygame
pygame.init()
pygame.mixer.init()

class MyPlatformaClass(pygame.sprite.Sprite):
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
            self.speed[0] = -3*koeff
        if keystate[pygame.K_RIGHT] and keystate[pygame.K_LEFT] == False:
            self.speed[0] = 3*koeff
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
class MyKubikClass(pygame.sprite.Sprite):
    def __init__(self, image_filey, locationy, speedy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_filey)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = locationy
        self.speedy = speedy
        
    def move(self):
        self.rect = self.rect.move(self.speedy)

        if self.rect.left < 0 or self.rect.right > width:
            self.speedy[0] = -self.speedy[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speedy[1] = -self.speedy[1]
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

pygame.mixer.music.load("music\Gta 4 - OST Remix.mp3")
pygame.mixer.music.set_volume(0.30)
#pygame.mixer.music.play(-1)

koeff = 1
score = 0
record = 0
score_font = pygame.font.Font(None, 36)
score_surf = score_font.render(str(score), 1, (0, 0, 0))
score_pos = [10, 10]

score_surf_record = score_font.render(str(record), 1, (0, 0, 0))
score_pos_record = [400, 10]

img_filey = "image\kubik.jpg"
img_file = "image\platforma.jpg"
balls = []
speed = [0, 0]
speedy = [2, 2] 
location = [270, 430]
locationy = [270, 0]
platforma = MyPlatformaClass(img_file, location, speed)
kubik = MyKubikClass(img_filey, locationy, speedy)
balls.append(platforma)
balls.append(kubik)

myachi = pygame.sprite.Group()
myachi.add(platforma)

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

    if record <= score:
        record = record + 0.02
    ochki_record = "Record: " + str(int(record))
    score_surf_record = score_font.render(ochki_record, 1, (0, 0, 0))
    screen.blit(score_surf_record, score_pos_record)

    score = score + 0.02
    ochki = "Score: " + str(int(score))
    score_surf = score_font.render(ochki, 1, (0, 0, 0))
    screen.blit(score_surf, score_pos)

    
    speedy[0] = speedy[0]*1.0004
    speedy[1] = speedy[1]*1.0004

    koeff = koeff*1.0004
    
    for ball in balls:
        platforma.move()
        kubik.move()
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()    
    if pygame.sprite.spritecollide(kubik, myachi, False):
        errormusic = pygame.mixer.music
        errormusic.load("music\error.mp3")
        errormusic.set_volume(0.30)
        errormusic.play(1)
        
        if score == record:
            final_text0 = "New record: " + str(int(record))
            ft0_font = pygame.font.Font(None, 70)
            ft0_surf = ft0_font.render(final_text0, 1, (0, 0, 0))
            screen.blit(ft0_surf, [screen.get_width()/2 - ft0_surf.get_width()/2, 100])
        final_text1 = "Game Over"
        final_text2 = "Score: " + str(int(score))
        ft1_font = pygame.font.Font(None, 70)
        ft1_surf = ft1_font.render(final_text1, 1, (0, 0, 0))
        ft2_font = pygame.font.Font(None, 50)
        ft2_surf = ft2_font.render(final_text2, 1, (0, 0, 0))
        screen.blit(ft1_surf, [screen.get_width()/2 - ft1_surf.get_width()/2, 200])
        screen.blit(ft2_surf, [screen.get_width()/2 - ft2_surf.get_width()/2, 300])
        speedy[0] = -speedy[0]
        speedy[1] = -speedy[1]
        pygame.display.flip()
        clock.tick(1)
        score = 0
        pygame.mixer.music.load("music\Gta 4 - OST Remix.mp3")
        pygame.mixer.music.set_volume(0.30)
        pygame.mixer.music.play(-1)
    clock.tick(50)
pygame.quit()
