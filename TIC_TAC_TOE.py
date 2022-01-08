import pygame
import random
pygame.font.init()

#screen variables
WIDTH,HEIGHT=600,600
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TIC TAC TOE GAME USING PYGAME MODULE ! ")
FPS=60 

#color variables
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

#game variables
board=[' ' for x in range(9)]

#font variables
X_FONT=pygame.font.SysFont("Arial Black",100)
O_FONT=pygame.font.SysFont("Arial Black",100)
WINNER_FONT=pygame.font.SysFont("Arial Black",40)

def isWinner(bo , le):
	for i in range(3):
		if bo[3*i] == bo[3*i + 1] == bo[3*i + 2] == le:
			pygame.draw.line(WIN,GREEN,(0,i * WIDTH //3 + WIDTH//6 ),(WIDTH ,i * WIDTH //3 + WIDTH//6 ),20)
			return True
		if bo[i] == bo[i + 3] == bo[i + 6] == le :
			pygame.draw.line(WIN,GREEN,(i * HEIGHT //3 + HEIGHT//6  , 0),(i * HEIGHT //3 + HEIGHT//6  , HEIGHT),20)
			return True
	if bo[0]==bo[4]==bo[8]==le:
		pygame.draw.line(WIN , GREEN , (0 , 0) , (WIDTH , HEIGHT) , 20)
		return True
	if bo[2]==bo[4]==bo[6]==le:
		pygame.draw.line(WIN , GREEN , (WIDTH , 0) , (0 , HEIGHT) , 20)
		return True

def playerMove():
	global run,play,board
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
			break
		if event.type==pygame.MOUSEBUTTONDOWN:
			m_x,m_y=pygame.mouse.get_pos()
			gap=WIDTH//3
			for i in range(9):
				flag=0
				if (i%3)*gap+10<m_x<(i%3+1)*gap-10 and (i//3)*gap<m_y+10<(i//3+1)*gap-10:
					if board[i]==' ':
						board[i]='X'
						return True

def compMove():
	global play,board
	possibleMoves=[x for x,letter in enumerate(board) if letter ==' ']
	move=-1

	#algorithm for winning or blocking the player
	for let in ['O','X']:
		for i in possibleMoves:
			boardCopy=board[:]
			boardCopy[i]=let
			if isWinner(boardCopy,let):
				move=i 
				return move 
	#checking for corners
	cornersOpen=[]
	for i in possibleMoves:
		if i in [0,2,6,8]:
			cornersOpen.append(i)

	if len(cornersOpen)>0:
		move=random.choice(cornersOpen)
		return move 
	if 4 in possibleMoves:
		move=4
		return move

	#checking for edges	
	edgesOpen=[]
	for i in possibleMoves:
		if i in [1,3,5,7]:
			edgesOpen.append(i)
	if len(edgesOpen)>0:
		move=random.choice(edgesOpen)
		return move

	#there may be a possibility that computer is unable to take a chance due to which -1 will be returned 
	return move


def redraw_window():
	global board,winner
	WIN.fill(BLACK)
	gap=WIDTH//3
	x,y=0,0
	for i in range(3):
		x+=gap
		y+=gap
		pygame.draw.line(WIN,GREEN,(x,0),(x,WIDTH))
		pygame.draw.line(WIN,GREEN,(0,y),(HEIGHT,y))
	
	#displaying X and O in the middle of their required boxes
	for i in range(9):
		if board[i]=='X':
			text=X_FONT.render('X',1,BLUE)
			WIN.blit(text,((i%3)*gap + gap//2 - text.get_width()//2,(i//3)*gap + gap//2 - text.get_height()//2))
		if board[i]=='O':
			text=O_FONT.render('O',1,RED)
			WIN.blit(text,((i%3)*gap + gap//2 - text.get_width()//2,(i//3)*gap + gap//2 - text.get_height()//2))

	if isWinner(board,'X'):
		winner='X'
	elif isWinner(board,'O'):
		winner='O'
	if winner != -1 :
		pygame.display.update()
		pygame.time.delay(1000)
		WIN.fill(BLACK)
		text=WINNER_FONT.render(winner+" WON !",1,WHITE)
		WIN.blit(text,(WIDTH//2-text.get_width()//2,HEIGHT//2-text.get_height()))
		pygame.display.update()
		pygame.time.delay(1000)
		return False
	pygame.display.update()

	if board.count(' ') == 0:
		pygame.time.delay(200)
		WIN.fill(BLACK)
		text=WINNER_FONT.render("THE GAME IS A TIE !",1,WHITE)
		WIN.blit(text,(WIDTH//2-text.get_width()//2,HEIGHT//2-text.get_height()))
		pygame.display.update()
		pygame.time.delay(1000)
		return False

def reset():
	global board,winner
	winner=-1
	board.clear()
	board=[' ' for x in range(9)]

def main():
	global run,play,board , winner
	winner = -1
	run=True
	clock=pygame.time.Clock()
	while run:
		clock.tick(FPS)
		test=redraw_window()
		if test==False:
			break
		if playerMove() :
			if redraw_window()==None:
				move=compMove()
				if move != -1 :
					board[move]='O'
			else:
				break		
	if run:
		reset()
		main()
	else:
		pygame.quit()

if __name__ == '__main__':
	main()