# -*- coding: utf-8 -*-
import sys, pygame, random
pygame.init()
pygame.mixer.init()
from PyQt4 import QtCore, QtGui, uic
form_class = uic.loadUiType("window.ui")[0]

class MyWindowClass(QtGui.QMainWindow, QtGui.QWidget, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        chislo_Vse_Game_Name = len(Vse_Game_Name[0])
        for i in range(chislo_Vse_Game_Name):
            button_Vse_Game_Name = QtGui.QPushButton(str(Vse_Game_Name[0][i]), self)
            button_Vse_Game_Name.setGeometry(100, (270+i*50), 100, 35)
            massiv_button_Vse_Game_Name.append(button_Vse_Game_Name)

            delete_Vse_Game_Name = QtGui.QPushButton(str(Vse_Game_Name[0][i]), self)
            delete_Vse_Game_Name.setGeometry(450, (270+i*50), 100, 35)
            delete_Vse_Game_Name.setStyleSheet("background: red")
            massiv_delete_Vse_Game_Name.append(delete_Vse_Game_Name)
        for i in range(len(Vse_Game_Name[0])):
            massiv_button_Vse_Game_Name[i].clicked.connect(self.button_clicked1)
            massiv_delete_Vse_Game_Name[i].clicked.connect(self.button_clicked2)
            massiv_delete_Vse_Game_Name[i].clicked.connect(massiv_button_Vse_Game_Name[i].deleteLater)
            massiv_delete_Vse_Game_Name[i].clicked.connect(massiv_delete_Vse_Game_Name[i].deleteLater)
        self.game.clicked.connect(self.button_clicked0)
        for i in range(chislo_Vse_Game_Name):
            label = QtGui.QLabel("score: " + str(Vse_Game_Name[1][i]), self)
            label.move(220, (270+i*50))
        
    def button_clicked0(self):
        global Game_Name
        if self.name.text() == "":
            Game_Name = "ANONIM"
        else:
            Game_Name = self.name.text()
        if Game_Name not in Vse_Game_Name[0]:
            Vse_Game_Name[0].append(str(Game_Name))
            Vse_Game_Name[1].append('0')
        f = open('Vse_Game_Name v 8.0+.txt', 'w')
        f.write(str(Vse_Game_Name) + '\n')
        f.close()
        myQExampleScrollArea.close()
        
    def button_clicked1(self):
        sender = self.sender()
        global Game_Name
        Game_Name = sender.text()
        myQExampleScrollArea.close()
        
    def button_clicked2(self):
        sender = self.sender()
        i = sender.text()
        index =  Vse_Game_Name[0].index(str(i))
        del Vse_Game_Name[1][index]
        Vse_Game_Name[0].remove(i)

        f = open('Vse_Game_Name v 8.0+.txt', 'w')
        f.write(str(Vse_Game_Name) + '\n')
        f.close()
        
class QExampleScrollArea (QtGui.QScrollArea, QtGui.QWidget ):
    def __init__ (self, parentQWidget = None):
        super(QtGui.QScrollArea, self).__init__(parentQWidget)
        QtGui.QWidget.setFixedSize(self, 645, 480)
        self.myAnnotator = MyWindowClass(self)
        self.setWidget(self.myAnnotator)

    def mousePressEvent (self, eventQMouseEvent):
        QtGui.QScrollArea.mousePressEvent(self, eventQMouseEvent)
        self.myAnnotator.mousePressEvent(eventQMouseEvent)

    def mouseReleaseEvent (self, eventQMouseEvent):
        QtGui.QScrollArea.mouseReleaseEvent(self, eventQMouseEvent)
        self.myAnnotator.mouseReleaseEvent(eventQMouseEvent)

    def mouseMoveEvent (self, eventQMouseEvent):
        QtGui.QScrollArea.mouseMoveEvent(self, eventQMouseEvent)
        self.myAnnotator.mouseMoveEvent(eventQMouseEvent)

    def wheelEvent (self, eventQWheelEvent):
        self.myAnnotator.wheelEvent(eventQWheelEvent)

massiv_delete_Vse_Game_Name = []
massiv_button_Vse_Game_Name = []

Vse_Game_Name = []
f = open('Vse_Game_Name v 8.0+.txt', 'r')
Vse_Game_Name = (eval(f.readlines()[0]))

app = QtGui.QApplication(sys.argv)
myQExampleScrollArea = QExampleScrollArea()
myQExampleScrollArea.show()

app.exec_()
    

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
        if paused == False:
            if keystate[pygame.K_LEFT] and keystate[pygame.K_RIGHT] == False:
                self.speed[0] = -koeff
            if keystate[pygame.K_RIGHT] and keystate[pygame.K_LEFT] == False:
                self.speed[0] = koeff
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
            self.speedy[0] = -self.speedy[0]*random.uniform(0.99, 1.01)
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speedy[1] = -self.speedy[1]*random.uniform(0.99, 1.01)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            global paused
            paused = True
        if keystate[pygame.K_DOWN]:
            paused = False
            
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

pygame.mixer.music.load("music\Gta 4 - OST Remix.mp3")
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play(-1)

koeff = 1
score = 0
if "Game_Name" in locals():
    index1 =  Vse_Game_Name[0].index(str(Game_Name))
    record = int(Vse_Game_Name[1][index1])
    score_font = pygame.font.Font(None, 36)
    score_surf = score_font.render(str(score), 1, (255, 255, 255))
    score_pos = [10, 10]

    score_surf_record = score_font.render(str(record), 1, (255, 255, 255))
    score_pos_record = [400, 10]
img_filey = "image\kubik.jpg"
img_file = "image\platforma.jpg"
balls = []
speed = [0, 0]
speedy = [1, 1] 
location = [270, 430]
locationy = [270, 0]
platforma = MyPlatformaClass(img_file, location, speed)
kubik = MyKubikClass(img_filey, locationy, speedy)
balls.append(platforma)
balls.append(kubik)

myachi = pygame.sprite.Group()
myachi.add(platforma)

stolk = 0

clock = pygame.time.Clock()
paused = False
running = True
if "Game_Name" not in locals():
        running = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill([0, 0, 0])

    if score == 0:
        speedy[0] = speedy[0]/koeff
        speedy[1] = speedy[1]/koeff
        koeff = 1

    if record <= score and paused == False:
        record = record + (0.01)
    ochki_record = "Record: "+ str(int(record))
    score_surf_record = score_font.render(ochki_record, 1, (223, 223, 223))
    screen.blit(score_surf_record, score_pos_record)
    
    if paused == False:
        score = score + (0.01)
    ochki = "Score: " + str(int(score))
    score_surf = score_font.render(ochki, 1, (223, 223, 223))
    screen.blit(score_surf, score_pos)

    if paused == True:
        if speedy[0] != 0 and speedy[1] != 0:
            global mem_speed
            mem_speed = [0, 0]
            mem_speed[0] = speed[0]
            mem_speed[1] = speed[1]
            global mem_speedy
            mem_speedy = [0, 0]
            mem_speedy[0] = speedy[0]
            mem_speedy[1] = speedy[1]
        speedy[0] = 0
        speedy[1] = 0
        speed[0] = 0
        speed[1] = 0

    if paused == False and speedy[0] == 0 and speedy[1] == 0:
        speedy[0] = mem_speedy[0]
        speedy[1] = mem_speedy[1]
        speed[0] = mem_speed[0]
        speed[1] = mem_speed[1]

    speedy[0] = speedy[0]*1.0001
    speedy[1] = speedy[1]*1.0001
    koeff = koeff*1.0001

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
            final_text0 = "New Record, " + str(Game_Name) + " : " + str(int(record))
            ft0_font = pygame.font.Font(None, 70)
            ft0_surf = ft0_font.render(final_text0, 1, (223, 223, 223))
            screen.blit(ft0_surf, [screen.get_width()/2 - ft0_surf.get_width()/2, 100])
        else:
            final_text0 = str(Game_Name)
            ft0_font = pygame.font.Font(None, 70)
            ft0_surf = ft0_font.render(final_text0, 1, (223, 223, 223))
            screen.blit(ft0_surf, [screen.get_width()/2 - ft0_surf.get_width()/2, 100])
        final_text1 = "Game Over"
        final_text2 = "Score: " + str(int(score))
        ft1_font = pygame.font.Font(None, 70)
        ft1_surf = ft1_font.render(final_text1, 1, (223, 223, 223))
        ft2_font = pygame.font.Font(None, 50)
        ft2_surf = ft2_font.render(final_text2, 1, (255, 255, 255))
        screen.blit(ft1_surf, [screen.get_width()/2 - ft1_surf.get_width()/2, 200])
        screen.blit(ft2_surf, [screen.get_width()/2 - ft2_surf.get_width()/2, 300])
        if stolk == 0:
            speedy[0] = -speedy[0]
            speedy[1] = -speedy[1]
        stolk = 1
        pygame.display.flip()
        clock.tick(1)
        score = 0
        pygame.mixer.music.load("music\Gta 4 - OST Remix.mp3")
        pygame.mixer.music.set_volume(0.30)
        pygame.mixer.music.play(-1)

        index_record =  Vse_Game_Name[0].index(str(Game_Name))
        Vse_Game_Name[1][index_record] = str(int(record))
        f = open('Vse_Game_Name v 8.0+.txt', 'w')
        f.write(str(Vse_Game_Name) + '\n')
        f.close()
    else:
        stolk = 0
    clock.tick(100)
pygame.quit()


