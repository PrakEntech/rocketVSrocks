import os
import keyboard
os.system('mode 40,20')
os.system('cls')
a="""
##### ##### ##### #   # ##### #####
#   # #   # #     #  #  #       #
##### #   # #     # #   #####   #
#  #  #   # #     #  #  #       #
#   # ##### ##### #   # #####   #

          #    # #####
          #    # #
          #    # #####
           #  #      #
            ##   #####

  ##### ##### ##### #   # #####
  #   # #   # #     #  #  #
  ##### #   # #     # #   #####
  #  #  #   # #     #  #      #
  #   # ##### ##### #   # #####
       PRESS P to Play
"""
print(a)
while True:
	if keyboard.is_pressed('p'):
		os.system('cls')
		break
import curses
from random import randint
os.system('mode 32,20')
os.system('cls')
curses.initscr()
win = curses.newwin(20,32,0,0) #y,x
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1) #-1
food  = [[1,30],[2,30],[3,30],[4,30],[5,30],[6,30],[7,30],[8,30],[9,30],[10,30],[11,30],[12,30],[13,30],[14,30],[15,30],[16,30],[17,30],[18,30]]
num=[None,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
esc=27
score=0
playerListCoord=[[9,1],[9,2],[9,3],[9,4],[9,5]]
chrq=""
c=1
key=curses.KEY_RIGHT
player = '>+-->'

while key != esc:
	event = win.getch()
	key = event if event != -1 else None
	temp = list(playerListCoord)
	
	if key == curses.KEY_DOWN:
		if playerListCoord[0][0]==18:pass
		else:
			for i in range(len(temp)):win.addch(temp[i][0],temp[i][1],' ')
			for i in range(len(playerListCoord)):playerListCoord[i][0]+=1
	elif key == curses.KEY_UP:
		if playerListCoord[0][0]==1:pass
		else:
			for i in range(len(temp)):win.addch(temp[i][0],temp[i][1],' ')
			for i in range(len(playerListCoord)):playerListCoord[i][0]-=1
	for i in range(len(playerListCoord)):win.addch(playerListCoord[i][0],playerListCoord[i][1],player[i])
	win.timeout(1)

	rand=[randint(1,17)]
	if food[0][1]==1:
		win.addch(food[0][0],food[0][1],' ')
		food[0]=[rand[0],30]
	temp=list(food[0])
	food[0][1]-=1
	try:win.addch(temp[0],temp[1],' ')
	except:pass
	win.addch(food[0][0],food[0][1],'•')

	for i in range(1,18):
		if (randint(1,15)==7 or num[i]==True):
			num[i]=True
			if food[i][1]==1:
				num[i]=False
				win.addch(food[i][0],food[i][1],' ')
				a=rand[0]
				while a in rand:a=randint(1,17)
				rand.append(a)
				food[i]=[rand[-1],30]
			temp=list(food[i])
			food[i][1]-=1
			try:win.addch(temp[0],temp[1],' ')
			except:pass
			win.addch(food[i][0],food[i][1],'•')
		if num[i]==False:win.addch(food[i][0],food[i][1],' ')
	for i in range(len(food)):
		if food[i] not in playerListCoord: score+=0.01
		if food[i] in playerListCoord:
			c=0
			break
	if c==0:
		break

	win.addstr(0,2,'Score '+str(int(score)) + ' ')

curses.endwin()
os.system('mode 40,20')
os.system('cls')
q="""
   ####### ###### #     # #######
   #       #    # # # # # #
   #   ### ###### #  #  # #######
   #     # #    # #     # #
   ####### #    # #     # #######
            SCORE - """+ str(int(score))+"""
   ####### #    # ####### #######
   #     # #    # #       #     #
   #     # #    # ####### #######
   #     #  #  #  #       #    #
   #######   ##   ####### #     #
"""
print(q)
input()
