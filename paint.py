 #Paint
import pygame
from pygame import *
import time
import platform
import os
import sys
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
pygame.init()
menuOn=True
screenSize=(800,640)
#music
pygame.mixer.music.load('mariopaint.mp3')
pygame.mixer.music.play(999,0.0)
#====
clock = pygame.time.Clock()
screen=pygame.display.set_mode((screenSize))
pygame.display.set_caption("Justin's Awesome Paint")
eraserPic = pygame.image.load("icons/eraser.png")
brushPic = pygame.image.load("icons/brush.png")
pencilPic=pygame.image.load("icons/pencil.png")
savePic=pygame.image.load("icons/save.png")
paintingPic=pygame.image.load("icons/paint.jpg")
savePic=pygame.image.load("icons/save.png")
fillPic=pygame.image.load("icons/fill.png")
linePic=pygame.image.load("icons/line.png")
loadPic=pygame.image.load("icons/load.png")
textValue=""
headingFont=pygame.font.SysFont("Arial Black",20)
myfont = pygame.font.SysFont("Times New Roman", 25)
startFont = pygame.font.SysFont("Calibri", 40)
head=headingFont.render("Please type in your name",True,(0,0,0))
errorText=headingFont.render("That name is not in the list!",True,(200,0,0))
fileNameText=headingFont.render("Type in the file name *with extension",True,(0,0,0))
lengthText=headingFont.render("Maximum 12 characters!",True,(0,0,0))
newGameText=headingFont.render("New Game",True,(0,200,0))
loadText=startFont.render("Load",True,(0,200,0))
saveText=startFont.render("Save",True,(0,200,0))
text=myfont.render(textValue, True, (0,0,0))
pygame.transform.scale(paintingPic,(8000,6400))
namesRead=open("names.txt","r")
namesAdd=open("names.txt","a")
namesList=namesRead.read().splitlines()
print namesList
namesString="".join(namesList)
namesRead.close()
names=myfont.render(namesString,True,(0,0,0))
button=0
toolType="brush"
clock=pygame.time.Clock()
toolColor=((0,0,0))
loopExit=True
canvas=screen.subsurface((50,0) + (750,580))
menu=screen.subsurface((0,0)+(800,640))
def brush(screen, color, start, end, radius):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for index in range(distance):
        x = int( start[0]+float(index)/distance*dx)
        y = int( start[1]+float(index)/distance*dy)
        pygame.draw.circle(screen, color, (x, y), radius)
def eraser(screen, color,start,end,height,width):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int( start[0]+float(i)/distance*dx)
        y = int( start[1]+float(i)/distance*dy)
        pygame.draw.rect(screen, color, (x,y,height,width))
colorList=[(110,590,20,20),(140,590,20,20),(170,590,20,20),(200,590,20,20),(230,590,20,20),(260,590,20,20),(290,590,20,20),(320,590,20,20),(350,590,20,20)]
toolList=[(5,5,32,32),(5,50,32,32),(5,100,32,32),(5,150,32,32),(5,360,32,32)]
#select variables
selEraser=Rect(toolList[0])
selBrush=Rect(toolList[1])
selFill=Rect(toolList[3])
selWhite=Rect (colorList[0])
selBlack=Rect (colorList[1])
selRed=Rect(colorList[2])
selGreen=Rect(colorList[3])
selBlue=Rect(colorList[4])
selYellow=Rect(colorList[5])
selOrange=Rect(colorList[6])
selBrown=Rect(colorList[7])
selPurple=Rect(colorList[8])
selPencil=Rect(toolList[2])
selSave=Rect(5,540,32,32)
selStart=Rect(200,300,190,50)
selExit=Rect(200,500,60,100)
selLoad=Rect(200,400,150,100)
selXL=Rect(5,210,32,32)
selL=Rect(5,255,32,32)
selM=Rect(5,290,32,32)
selS=Rect(5,320,32,32)
selCanvas=Rect(50,0,750,580)
selLoadMenu=Rect(40,290,100,50)
selNewGame=Rect(40,290,200,50)
selLine=Rect(toolList[4])
selLoadIMG=Rect(5,500,32,32)
toolSize=5
radius=toolSize
menuOn=True
loadMenuOn=False
newGameMenu=False
loadImg=False
turn=1
font = pygame.font.SysFont("Calibri", 40)
while menuOn==True:
    clock.tick(1000)
    menu.blit(paintingPic,(0,0))
    title=font.render("Justin's Paint",1,(0,0,0))
    start=font.render("Start New Game",1,(0,0,0))
    load=font.render("Load Game",1,(0,0,0))
    exitText=font.render("Exit",1,(0,0,0))
    menuLines=font.render("---------------------------------",1,(0,0,0))
    menu.blit(title,(300,100))
    menu.blit(start,(200,300))
    menu.blit(load,(200,400))
    menu.blit(exitText,(200,500))
    for event in pygame.event.get():
        position=pygame.mouse.get_pos()
        mx=position[0] 
        my=position[1]
        butt=pygame.mouse.get_pressed() 
        rel=pygame.mouse.get_rel()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            keepGoing = False
        elif event.type==MOUSEBUTTONDOWN:
            button=1
        elif event.type==MOUSEBUTTONUP:
            button=0
        if button==1:
            if selStart.collidepoint(pygame.mouse.get_pos()):
                menuOn=False
                canvas.fill((255,255,255))
                newGameMenu=True
            elif selExit.collidepoint(pygame.mouse.get_pos()):
                 sys.exit()
                 pygame.quit()
            elif selLoad.collidepoint(pygame.mouse.get_pos()):
                screen.fill((255,255,255))
                menuOn=False
                loadMenuOn=True
        pygame.display.flip()
if loadMenuOn==True:
    while loadMenuOn==True:
        menu.blit(paintingPic,(0,0))
        screen.blit(head,(10,60))
        pygame.draw.rect(screen,(0,0,0),(10,100,445,40),3)
        pygame.draw.rect(screen,(0,0,0),(40,290,100,50))
        screen.blit(text, (18,105))
        screen.blit(names,(500,50))
        screen.blit(lengthText,(10,150))
        screen.blit(loadText,(50,300))
        clock.tick(60)
        for event in pygame.event.get():
            position=pygame.mouse.get_pos()
            mx=position[0] 
            my=position[1]
            rel=pygame.mouse.get_rel()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                keepGoing = False
            elif event.type==MOUSEBUTTONDOWN:
                button=1
            elif event.type==MOUSEBUTTONUP:
                button=0          
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE and len(textValue) > 0:
                    textValue = textValue[:-1] 
                elif event.unicode and len(textValue) < 12:
                    textValue = textValue + event.unicode 
                text = myfont.render(textValue, True, (0,0,0))
                screen.blit(head,(10,60))
                pygame.draw.rect(screen, (0,0,0), (10, 100, 445, 40),3)
                pygame.draw.rect(screen,(0,0,0),(40,290,100,50))
                screen.blit(text, (18, 105))
                screen.blit(names,(500,50))
                screen.blit(lengthText,(10,150))
                screen.blit(loadText,(50,300))
            if button==0:
                if selLoadMenu.collidepoint(position):
                    pygame.draw.rect(screen, (20,20,20), (40,290,100,50))
            if button==1:
                if selLoadMenu.collidepoint(position):
                    if textValue in namesList:
                        loadMenuOn=False
                        canvas.fill((255,255,255))
                    elif textValue not in namesList:
                        screen.blit(errorText,(300,350))
                        time.sleep(1)
        pygame.display.update()
        pygame.display.flip()
if newGameMenu==True:
    while newGameMenu==True:
        menu.blit(paintingPic,(0,0))
        screen.blit(head,(10,60))
        pygame.draw.rect(screen,(0,0,0),(10,100,445,40),3)
        pygame.draw.rect(screen,(0,0,0),(40,290,200,50))
        screen.blit(text, (18,105))
        screen.blit(newGameText,(50,300))
        screen.blit(lengthText,(10,150))
        clock.tick(60)
        for event in pygame.event.get():
            position=pygame.mouse.get_pos()
            mx=position[0] 
            my=position[1]
            rel=pygame.mouse.get_rel()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                keepGoing = False
            elif event.type==MOUSEBUTTONDOWN:
                button=1
            elif event.type==MOUSEBUTTONUP:
                button=0          
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE and len(textValue) > 0:
                    textValue = textValue[:-1] 
                elif event.unicode and len(textValue) < 12:
                    textValue = textValue + event.unicode 
                text = myfont.render(textValue, True, (0,0,0))
                screen.blit(head,(10,60))
                pygame.draw.rect(screen, (0,0,0), (10, 100, 445, 40),3)
                pygame.draw.rect(screen,(0,0,0),(40,290,200,50))
                screen.blit(text, (18, 105))
                screen.blit(lengthText,(10,150))
                screen.blit(newGameText,(50,300))
            if button==0:
                if selLoadMenu.collidepoint(position):
                    pygame.draw.rect(screen, (20,20,20), (40,290,200,50))
            if button==1:
                if selLoadMenu.collidepoint(position):
                    if len(textValue) > 0 and len(textValue) < 12:
                        textValue+="\n"
                        namesAdd.write(textValue)
                        newGameMenu=False
                        canvas.fill((255,255,255))
        pygame.display.update()
        pygame.display.flip()
while loopExit==True:
    clock.tick(100)
    pygame.draw.rect(screen, (50,100,50), (0,0,50,1000),0)
    pygame.draw.rect(screen, (50,100,50), (0,580,1000,1000),0)
    #selected color
    pygame.draw.rect(screen, toolColor, (50,590,20,20))
    #white
    pygame.draw.rect(screen,(255,255,255),colorList[0])
    #black
    pygame.draw.rect(screen,(0,0,0),colorList[1])
    #red
    pygame.draw.rect(screen,(255,0,0),colorList[2])
    #green
    pygame.draw.rect(screen,(0,255,0),colorList[3])
    #blue
    pygame.draw.rect(screen,(0,0,255),colorList[4])
    #yellow
    pygame.draw.rect(screen,(255,255,0),colorList[5])
    #orange
    pygame.draw.rect(screen,(255,165,0),colorList[6])
    #brown
    pygame.draw.rect(screen,(139,69,19),colorList[7])
    #purple
    pygame.draw.rect(screen,(160,32,240),colorList[8])
    for event in pygame.event.get():
        position=pygame.mouse.get_pos()
        mx=position[0] 
        my=position[1]
        rel=pygame.mouse.get_rel()
        butt=pygame.mouse.get_pressed() 
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            keepGoing = False
        elif event.type==MOUSEBUTTONDOWN:
            button=1
        elif event.type==MOUSEBUTTONUP:
            button=0
        if button==1:
            if selBrush.collidepoint(pygame.mouse.get_pos()) and button==1 :
                toolType="brush"
            if selEraser.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolType="eraser"
            if selPencil.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolType="pencil"
            if selSave.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolType="save"
            if selLoadIMG.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolType="load"
            if selFill.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolType="fill"
            if selLine.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolType="line"
            if selXL.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolSize=15
            if selL.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolSize=10
            if selM.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolSize=5
            if selS.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolSize=2
            if selWhite.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolColor=(255,255,255)
            if selBlack.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolColor=(0,0,0)
            if selRed.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolColor=(255,0,0)
            if selGreen.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolColor=(0,255,0)
            if selBlue.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolColor=(0,0,255)
            if selYellow.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolColor=(255,255,0)
            if selOrange.collidepoint(pygame.mouse.get_pos())and button==1:
                toolColor=(255,160,0)
            if selBrown.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolColor=(139,69,19)
            if selPurple.collidepoint(pygame.mouse.get_pos()) and button==1:
                toolColor=(160,32,240)
            if toolType=="brush":
                brush(canvas,toolColor,(position[0]-50,position[1]), (position[0]-50-rel[0], position[1]-rel[1]),toolSize)
            elif toolType=="eraser":
                eraser(canvas,((255,255,255)),(position[0]-50,position[1]),(position[0]-50-rel[0], position[1]-rel[1]),toolSize+7,toolSize+7)
            elif toolType=="pencil":
                pygame.draw.line(canvas,(toolColor),(position[0]-50,position[1]), (position[0]-50-rel[0], position[1]-rel[1]),1)
            elif toolType=="save":
                img=pygame.image.save(canvas,("screenshot.png"))
                toolType="brush"
            elif toolType=="load":
                textValue=""
                loadImg=True
                if loadImg==True:
                    while loadImg==True:
                        menu.blit(paintingPic,(0,0))
                        screen.blit(fileNameText,(10,60))
                        pygame.draw.rect(screen,(0,0,0),(10,100,445,40),3)
                        pygame.draw.rect(screen,(0,0,0),(40,290,100,50))
                        screen.blit(text, (18,105))
                        screen.blit(loadText,(50,300))
                        clock.tick(60)
                        for event in pygame.event.get():
                            position=pygame.mouse.get_pos()
                            mx=position[0] 
                            my=position[1]
                            rel=pygame.mouse.get_rel()
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                                keepGoing = False
                            elif event.type==MOUSEBUTTONDOWN:
                                button=1
                            elif event.type==MOUSEBUTTONUP:
                                button=0          
                            elif event.type == KEYDOWN:
                                if event.key == K_BACKSPACE and len(textValue) > 0:
                                    textValue = textValue[:-1] 
                                elif event.unicode and len(textValue) < 30:
                                    textValue = textValue + event.unicode 
                                text = myfont.render(textValue, True, (0,0,0))
                                screen.blit(fileNameText,(10,60))
                                pygame.draw.rect(screen, (0,0,0), (10, 100, 445, 40),3)
                                pygame.draw.rect(screen,(0,0,0),(40,290,100,50))
                                screen.blit(text, (18, 105))
                                screen.blit(loadText,(50,300))
                            if button==0:
                                if selLoadMenu.collidepoint(position):
                                    pygame.draw.rect(screen, (20,20,20), (40,290,100,50))
                            if button==1:
                                if selLoadMenu.collidepoint(position):
                                    try:
                                        canvas.fill((255,255,255))
                                        img=pygame.image.load(textValue)
                                        toolType="brush"
                                        canvas.blit(img,(0,0))
                                        loadImg=False
                                    except IOError:
                                        pass
                        pygame.display.update()
                        pygame.display.flip()
            elif toolType=="fill":
                if selCanvas.collidepoint(pygame.mouse.get_pos()):
                    canvas.fill(toolColor)
            elif toolType=="line":
                if butt[0]==1 and turn ==1:
                    linePos1=pygame.mouse.get_pos()
                    pygame.display.update()
                    turn = 2
                if butt[2]==1 and turn == 2:
                    linePos2=pygame.mouse.get_pos()	    
                    pygame.display.update()
                    pygame.draw.line(canvas,toolColor,(linePos1[0]-50,linePos1[1]),(linePos2[0]-50,linePos2[1]),toolSize)
                    turn=1
    if toolType=="brush":
        pygame.draw.rect(screen,(200,200,200),(3,50,36,36), 2)
    elif toolType == "eraser":
        pygame.draw.rect(screen,(200,200,200),(3,5,36,36), 2)
    elif toolType=="pencil":
        pygame.draw.rect(screen,(200,200,200),(3,100,36,36), 2)
    elif toolType=="save":
        pygame.draw.rect(screen,(200,200,200),(3,540,36,36), 2)
    elif toolType=="load":
        pygame.draw.rect(screen,(200,200,200),(3,500,36,36), 2)
    elif toolType=="fill":
        pygame.draw.rect(screen,(200,200,200),(3,150,36,36), 2)
    elif toolType=="line":
        pygame.draw.rect(screen,(200,200,200),(3,360,36,36), 2)
    if toolSize==15:
        pygame.draw.rect(screen,(200,200,200),(3,202,36,36), 2)
    elif toolSize==10:
        pygame.draw.rect(screen,(200,200,200),(3,247,36,36), 2)
    elif toolSize==5:
        pygame.draw.rect(screen,(200,200,200),(3,282,36,36), 2)
    elif toolSize==2:
        pygame.draw.rect(screen,(200,200,200),(3,312,36,36), 2)
    if event.type==KEYDOWN:
        if event.key==K_r:
            canvas.fill((255,255,255))
        elif event.key==K_ESCAPE:
            menuOn=True
            while menuOn==True:
                clock.tick(1000)
                menu.blit(paintingPic,(0,0))
                title=font.render("Justin's Paint",1,(0,0,0))
                start=font.render("Start New Game",1,(0,0,0))
                load=font.render("Load Game",1,(0,0,0))
                exitText=font.render("Exit",1,(0,0,0))
                menuLines=font.render("---------------------------------",1,(0,0,0))
                menu.blit(title,(300,100))
                menu.blit(start,(200,300))
                menu.blit(load,(200,400))
                menu.blit(exitText,(200,500))
                for event in pygame.event.get():
                    position=pygame.mouse.get_pos()
                    mx=position[0] 
                    my=position[1]
                    butt=pygame.mouse.get_pressed() 
                    rel=pygame.mouse.get_rel()
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                        keepGoing = False
                    elif event.type==MOUSEBUTTONDOWN:
                        button=1
                    elif event.type==MOUSEBUTTONUP:
                        button=0
                    if button==1:
                        if selStart.collidepoint(pygame.mouse.get_pos()):
                            menuOn=False
                            canvas.fill((255,255,255))
                            newGameMenu=True
                        elif selExit.collidepoint(pygame.mouse.get_pos()):
                             sys.exit()
                             pygame.quit()
                        elif selLoad.collidepoint(pygame.mouse.get_pos()):
                            screen.fill((255,255,255))
                            menuOn=False
                            loadMenuOn=True
                    pygame.display.flip()
        if loadMenuOn==True:
            while loadMenuOn==True:
                menu.blit(paintingPic,(0,0))
                screen.blit(head,(10,60))
                pygame.draw.rect(screen,(0,0,0),(10,100,445,40),3)
                pygame.draw.rect(screen,(0,0,0),(40,290,100,50))
                screen.blit(text, (18,105))
                screen.blit(names,(500,50))
                screen.blit(lengthText,(10,150))
                screen.blit(loadText,(50,300))
                clock.tick(60)
                for event in pygame.event.get():
                    position=pygame.mouse.get_pos()
                    mx=position[0] 
                    my=position[1]
                    rel=pygame.mouse.get_rel()
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                        keepGoing = False
                    elif event.type==MOUSEBUTTONDOWN:
                        button=1
                    elif event.type==MOUSEBUTTONUP:
                        button=0          
                    elif event.type == KEYDOWN:
                        if event.key == K_BACKSPACE and len(textValue) > 0:
                            textValue = textValue[:-1] 
                        elif event.unicode and len(textValue) < 12:
                            textValue = textValue + event.unicode 
                        text = myfont.render(textValue, True, (0,0,0))
                        screen.blit(head,(10,60))
                        pygame.draw.rect(screen, (0,0,0), (10, 100, 445, 40),3)
                        pygame.draw.rect(screen,(0,0,0),(40,290,100,50))
                        screen.blit(text, (18, 105))
                        screen.blit(names,(500,50))
                        screen.blit(lengthText,(10,150))
                        screen.blit(loadText,(50,300))
                    if button==0:
                        if selLoadMenu.collidepoint(position):
                            pygame.draw.rect(screen, (20,20,20), (40,290,100,50))
                    if button==1:
                        if selLoadMenu.collidepoint(position):
                            if textValue in namesList:
                                loadMenuOn=False
                                canvas.fill((255,255,255))
                            elif textValue not in namesList:
                                screen.blit(errorText,(300,350))
                                time.sleep(1)
                pygame.display.update()
                pygame.display.flip()
        if newGameMenu==True:
            while newGameMenu==True:
                menu.blit(paintingPic,(0,0))
                screen.blit(head,(10,60))
                pygame.draw.rect(screen,(0,0,0),(10,100,445,40),3)
                pygame.draw.rect(screen,(0,0,0),(40,290,200,50))
                screen.blit(text, (18,105))
                screen.blit(newGameText,(50,300))
                screen.blit(lengthText,(10,150))
                clock.tick(60)
                for event in pygame.event.get():
                    position=pygame.mouse.get_pos()
                    mx=position[0] 
                    my=position[1]
                    rel=pygame.mouse.get_rel()
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                        keepGoing = False
                    elif event.type==MOUSEBUTTONDOWN:
                        button=1
                    elif event.type==MOUSEBUTTONUP:
                        button=0          
                    elif event.type == KEYDOWN:
                        if event.key == K_BACKSPACE and len(textValue) > 0:
                            textValue = textValue[:-1] 
                        elif event.unicode and len(textValue) < 12:
                            textValue = textValue + event.unicode 
                        text = myfont.render(textValue, True, (0,0,0))
                        screen.blit(head,(10,60))
                        pygame.draw.rect(screen, (0,0,0), (10, 100, 445, 40),3)
                        pygame.draw.rect(screen,(0,0,0),(40,290,200,50))
                        screen.blit(text, (18, 105))
                        screen.blit(lengthText,(10,150))
                        screen.blit(newGameText,(50,300))
                    if button==0:
                        if selLoadMenu.collidepoint(position):
                            pygame.draw.rect(screen, (20,20,20), (40,290,200,50))
                    if button==1:
                        if selLoadMenu.collidepoint(position):
                            if len(textValue) > 0 and len(textValue) < 12:
                                textValue+="\n"
                                namesAdd.write(textValue)
                                newGameMenu=False
                                canvas.fill((255,255,255))
                pygame.display.update()
                pygame.display.flip()
    screen.blit(eraserPic, (5,5))
    screen.blit(brushPic, (5,50))
    screen.blit(pencilPic,(5,100))
    screen.blit(savePic,(5,540))
    screen.blit(fillPic,(5,150))
    screen.blit(linePic,(5,360))
    screen.blit(loadPic,(5,500))
    pygame.draw.circle(screen,(toolColor),(22,220),15)
    pygame.draw.circle(screen,(toolColor),(22,265),10)
    pygame.draw.circle(screen,(toolColor),(22,300),5)
    pygame.draw.circle(screen,(toolColor),(22,330),2)
    pygame.display.flip()
    pygame.display.update()
pygame.quit()
