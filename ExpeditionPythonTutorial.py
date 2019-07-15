#expedition_PythonTutorial.py
import pygame
#, time
size = (640,400)
white = (255,255,255)
black = (0,0,0)
x = 300
y = 100
fallx = 200
fally = -170
walkx = 233
walky = 268
walkcavex = 0
walkendx = 0
clocky = 0
clocky2 = 0
handx = 275
handy = 225


dir = '-'
handdir = '-'
enddir = '-'
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Expedition of Survival: Python Tutorial")
skydiver = pygame.image.load("skydiver.png")
sky = pygame.image.load("sky.png")
copter = pygame.image.load("copter.png")
cavein = pygame.image.load("cavein.png")
cavecode = pygame.image.load("caveofcode.png")
cave = pygame.image.load("cave.png")
fallguy = pygame.image.load("fallguy.png")
walkguy = pygame.image.load("walkguy.png")
walkguy2 = pygame.image.load("walkguy2.png")
spider = pygame.image.load("spider.png")
spider2 = pygame.image.load("spider2.png")
instructorsmall = pygame.image.load("instructorsmall.png")
instructorbig = pygame.image.load("instructorbig.png")
monitor = pygame.image.load("monitor.png")
hand = pygame.image.load("hand.png")
trophy = pygame.image.load("trophy.png")
collectme = pygame.image.load("collectme.png")
speechbubblebig = pygame.image.load("speechbubblebig.png")
speechbubblesmall = pygame.image.load("speechbubblesmall.png")
python1 = pygame.image.load("python1.png")
python2 = pygame.image.load("python2.png")
python3 = pygame.image.load("python3.png")
python4 = pygame.image.load("python4.png")
python5 = pygame.image.load("python5.png")
python6 = pygame.image.load("python6.png")
python7 = pygame.image.load("python7.png")
caveorange = pygame.image.load("caveorange.png")
clock = pygame.image.load("clock.png")
hello = pygame.image.load("hello.png")#-------------------#1
hereyouwill = pygame.image.load("hereyouwill.png")#-------#2
makeyourown = pygame.image.load("makeyourown.png")#-------#3
tostart = pygame.image.load("tostart.png")#---------------#4
youcando = pygame.image.load("youcando.png")#-------------#5
mustalways = pygame.image.load("mustalways.png")#---------#6
getit = pygame.image.load("getit.png")#-------------------#7
letsstartby = pygame.image.load("letsstartby.png")#-------#8
theprogram = pygame.image.load("theprogram.png")#---------#9
canyouguess = pygame.image.load("canyouguess.png")#------#10
correct = pygame.image.load("correct.png")#--------------#11
congrats = pygame.image.load("congrats.png")#------------#12
incorrect = pygame.image.load("incorrect.png")#----------#13
answer1 = pygame.image.load("answer1.png")
answer2 = pygame.image.load("answer2.png")
answer3 = pygame.image.load("answer3.png")
answer4 = pygame.image.load("answer4.png")
walk = walkguy
game = 0

while (True):
	screen.fill(black)
	screen.blit(sky,(0,0))
	screen.blit(fallguy,(x,y))
	y = y + 1
	screen.blit(copter,(200,50))
	pygame.display.flip()
	event=pygame.event.poll()
	if (y>400):
		break
		
while (True):
	screen.fill(black)
	screen.blit(cavein,(0,0))
	screen.blit(cavecode,(475,25))
	screen.blit(skydiver,(fallx,fally))
	fally = fally + 0.7
	pygame.display.flip()
	event=pygame.event.poll()
		
	if (fally>123):
		break
		
while (True):	
	screen.blit(cavein,(0,0))
	screen.blit(cavecode,(475,25))
	screen.blit(walkguy,(walkx,walky))
	pygame.display.flip()
	event = pygame.event.poll() 
	if (event.type == pygame.KEYDOWN):
		if (event.key == pygame.K_RIGHT):
			dir = 'r'
	if (event.type == pygame.KEYUP):
		dir = '-'
	if (event.type == pygame.QUIT):
			break
	if (dir == 'r'):
		walkx = walkx + 3#1
		
	if (walkx>=472):
		break
		
while (True):
	screen.blit(cave,(0,0))
	screen.blit(walk,(walkcavex,233))
	screen.blit(spider,(105,250))
	screen.blit(spider2,(350,13))
	pygame.display.flip()
	event = pygame.event.poll()
	
	if (event.type == pygame.KEYDOWN):
		if (event.key == pygame.K_LEFT):
			dir = 'l'
		if (event.key == pygame.K_RIGHT):
			dir = 'r'
	if (event.type == pygame.KEYUP):
		dir = '-'

	if (event.type == pygame.QUIT):
			break

	if (dir == 'l'):
		walk = walkguy2
		walkcavex = walkcavex - 3#1
	if (dir == 'r'):
		walk = walkguy
		walkcavex = walkcavex + 3#1
		
		
	if (walkcavex>=600):
		break
#Hello		
while (True):
	screen.blit(clock,(400,clocky))
	screen.blit(caveorange,(0,0))
	screen.blit(instructorbig,(-20,200))
	screen.blit(speechbubblebig,(150,30))
	screen.blit(hello,(200,75))
	clocky = clocky + 1
	pygame.display.flip()
	event = pygame.event.poll()
	
	if (clocky>150):
		clocky = 0
		break
		
#Here you will learn		
while (True):
	screen.blit(clock,(400,clocky))
	screen.blit(caveorange,(0,0))
	screen.blit(instructorbig,(-20,200))
	screen.blit(speechbubblebig,(150,30))
	screen.blit(hereyouwill,(125,70))
	clocky = clocky + 1
	pygame.display.flip()
	event = pygame.event.poll()
	
	if (clocky>250):
		clocky = 0
		break
		
#make a program		
while (True):
	screen.blit(clock,(400,clocky))
	screen.blit(caveorange,(0,0))
	screen.blit(instructorbig,(-20,200))
	screen.blit(speechbubblebig,(150,30))
	screen.blit(makeyourown,(165,67))
	clocky = clocky + 1
	pygame.display.flip()
	event = pygame.event.poll()
	
	if (clocky>300):
		clocky = 0
		break
		
#to start		
while (True):
	screen.blit(clock,(400,clocky))
	screen.blit(caveorange,(0,0))
	screen.blit(monitor,(16,15))
	screen.blit(python1,(74,38))
	screen.blit(instructorsmall,(-0,280))
	screen.blit(speechbubblesmall,(133,290))
	screen.blit(tostart,(133,290))
	clocky = clocky + 1
	pygame.display.flip()
	event = pygame.event.poll()
	
	if (clocky>200):
		clocky = 0
		break
		
#you can do this by		
while (True):
	screen.blit(clock,(400,clocky))
	screen.blit(caveorange,(0,0))
	screen.blit(monitor,(16,15))
	screen.blit(python2,(74,38))#100,40
	screen.blit(instructorsmall,(-0,280))
	screen.blit(speechbubblesmall,(133,290))
	screen.blit(youcando,(133,290))
	clocky = clocky + 1
	pygame.display.flip()
	event = pygame.event.poll()
	
	if (clocky>200):
		clocky = 0
		break
		
#must ALWAYS		
while (True):
	screen.blit(clock,(400,clocky))
	screen.blit(caveorange,(0,0))
	screen.blit(monitor,(16,15))
	screen.blit(python3,(74,38))
	screen.blit(instructorsmall,(-0,280))
	screen.blit(speechbubblesmall,(133,290))
	screen.blit(mustalways,(133,290))
	clocky = clocky + 1
	pygame.display.flip()
	event = pygame.event.poll()
	
	if (clocky>200):
		clocky = 0
		break
		
#Now let's get the user input		
while (True):
	screen.blit(clock,(400,clocky))
	screen.blit(caveorange,(0,0))
	screen.blit(monitor,(16,15))
	screen.blit(python3,(74,38))
	screen.blit(instructorsmall,(-0,280))
	screen.blit(speechbubblesmall,(133,290))
	screen.blit(getit,(133,290))
	clocky = clocky + 1
	pygame.display.flip()
	event = pygame.event.poll()
	
	if (clocky>200):
		clocky = 0
		break
		
#start by making a variable		
while (True):
	screen.blit(clock,(400,clocky))
	screen.blit(caveorange,(0,0))
	screen.blit(monitor,(16,15))
	screen.blit(python4,(74,38))
	screen.blit(instructorsmall,(-0,280))
	screen.blit(speechbubblesmall,(133,290))
	screen.blit(letsstartby,(133,285))
	clocky = clocky + 1
	pygame.display.flip()
	event = pygame.event.poll()
	
	if (clocky>275):
		clocky = 0
		break
		
#program will now ask ask for input		
while (True):
	screen.blit(clock,(400,clocky))
	screen.blit(caveorange,(0,0))
	screen.blit(monitor,(16,15))
	screen.blit(python5,(74,38))
	screen.blit(instructorsmall,(-0,280))
	screen.blit(speechbubblesmall,(133,290))
	screen.blit(theprogram,(133,290))
	clocky = clocky + 1
	pygame.display.flip()
	event = pygame.event.poll()
	
	if (clocky>200):
		clocky = 0
		break
		
#can you guess		
while (True):
	screen.blit(clock,(400,clocky2))
	screen.blit(caveorange,(0,0))
	screen.blit(monitor,(16,15))
	screen.blit(python6,(74,38))
	screen.blit(instructorsmall,(-0,280))
	screen.blit(speechbubblesmall,(133,290))
	screen.blit(canyouguess,(133,290))
	screen.blit(answer1,(0,5))
	screen.blit(answer2,(155,5))
	screen.blit(answer3,(313,5))
	screen.blit(answer4,(473,3))
	screen.blit(hand,(handx,handy))
	pygame.display.flip()
	event = pygame.event.poll()
	
	if (event.type == pygame.KEYDOWN):
		if (event.key == pygame.K_LEFT):
			handdir = 'l'
		if (event.key == pygame.K_RIGHT):
			handdir = 'r'
		if (event.key == pygame.K_UP):
			handdir = 'up'
		if (event.key == pygame.K_DOWN):
			handdir = 'd'
	if (event.type == pygame.KEYUP):
		handdir = '-'

	if (event.type == pygame.QUIT):
			break

	if (handdir == 'l'):
		handx = handx - 3#1
	if (handdir == 'r'):
		handx = handx + 3#1
	if (handdir == 'up'):
		handy = handy - 3#1
	if (handdir == 'd'):
		handy = handy + 3#1
	
	while (handx>150 and handy<50):
		screen.blit(speechbubblesmall,(133,290))
		screen.blit(incorrect,(133,290))
		clocky2 = clocky2 + 0.5
		pygame.display.flip()
		event = pygame.event.poll() 
		if (clocky2>400):
			handx = 275
			handy = 225
			clocky2 = 0
			break	
		
	if (handx<150 and handy<50):
		clocky = 0
		break
		
#correct		
while (True):
	screen.blit(clock,(400,clocky))
	screen.blit(caveorange,(0,0))
	screen.blit(monitor,(16,15))
	screen.blit(python7,(74,38))
	screen.blit(instructorsmall,(-0,280))
	screen.blit(speechbubblesmall,(133,290))
	screen.blit(correct,(133,290))
	clocky = clocky + 1
	pygame.display.flip()
	event = pygame.event.poll()
	
	if (clocky>225):
		clocky = 0
		break
		
#congrats		
while (True):
	screen.blit(clock,(400,clocky))
	screen.blit(caveorange,(0,0))
	screen.blit(instructorbig,(-20,200))
	screen.blit(speechbubblebig,(150,30))
	screen.blit(congrats,(150,55))
	clocky = clocky + 1
	pygame.display.flip()
	event = pygame.event.poll()
	
	if (clocky>250):
		clocky = 0
		walk = walkguy2
		walkendx = 580
		break
		
#trophy
while (True):
	screen.blit(caveorange,(0,0))
	screen.blit(instructorbig,(-20,200))
	screen.blit(trophy,(200,175))
	screen.blit(collectme,(250,150))
	screen.blit(walk,(walkendx,245))
	pygame.display.flip()
	event = pygame.event.poll()
	if (event.type == pygame.KEYDOWN):
		if (event.key == pygame.K_LEFT):
			enddir = 'l'
		if (event.key == pygame.K_RIGHT):
			enddir = 'r'
	if (event.type == pygame.KEYUP):
		enddir = '-'

	if (event.type == pygame.QUIT):
			break

	if (enddir == 'l'):
		walk = walkguy2
		walkendx = walkendx - 3#1
	if (enddir == 'r'):
		walk = walkguy
		walkendx = walkendx + 3#1
		
	if (walkendx<=270):
		print ("GOOD JOB!")
		break


		
	event=pygame.event.poll()
	if (event.type == pygame.QUIT):
		break
