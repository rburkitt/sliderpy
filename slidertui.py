#! /usr/bin/env python3

import random, sys
import os

BLANK = '  '

def main():
  clear_screen()
	input('Press Enter to begin...')
	
	gameBoard = getNewPuzzle()
	
	while True:
		displayBoard(gameBoard)
		playerMove = askForPlayerMove(gameBoard)
		makeMove(gameBoard, playerMove)
		
		if gameBoard == getNewBoard():
			print('You won!')
			sys.exit()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def getNewBoard():
	return [['1 ', '5 ', '9 ', '13'], ['2 ', '6 ', '10', '14'], ['3 ', '7 ', '11', '15'], ['4 ', '8 ', '12', BLANK]]
	
def displayBoard(board):
	labels = [board[0][0], board[1][0], board[2][0], board[3][0],
						board[0][1], board[1][1], board[2][1], board[3][1],
						board[0][2], board[1][2], board[2][2], board[3][2],
						board[0][3], board[1][3], board[2][3], board[3][3]]
	boardToDraw = """
	+------+------+------+------+
	|      |      |      |      |
	|  {}  |  {}  |  {}  |  {}  |
	|      |      |      |      |
	+------+------+------+------+
	|      |      |      |      |
	|  {}  |  {}  |  {}  |  {}  |
	|      |      |      |      |
	+------+------+------+------+
	|      |      |      |      |
	|  {}  |  {}  |  {}  |  {}  |
	|      |      |      |      |
	+------+------+------+------+
	|      |      |      |      |
	|  {}  |  {}  |  {}  |  {}  |
	|      |      |      |      |
	+------+------+------+------+
	""".format(*labels)
	print(boardToDraw)
			
def findBlankSpace(board):
	for x in range(4):
		for y in range(4):
			if board[x][y] == '  ':
				return (x, y)
				
def askForPlayerMove(board):
	blankx, blanky = findBlankSpace(board)
	
	w = 'W' if blanky != 3 else '  '
	a = 'A' if blankx != 3 else '  '
	s = 'S' if blanky != 0 else '  '
	d = 'D' if blankx != 0 else '  '
	
	while True:
		print('                          ({})'.format(w))
		print('Enter WASD (or QUIT): ({}) ({}) ({})'.format(a, s, d))
		
		reponse = input('> ').upper()
		if reponse == 'QUIT':
			sys.exit()
		if reponse in (w + a + s + d).replace('  ', ''):
			return reponse
			
def makeMove(board, move):
	bx, by = findBlankSpace(board)
	
	if move == 'W':
		board[bx][by], board[bx][by+1] = board[bx][by+1], board[bx][by]
	elif move == 'A':
		board[bx][by], board[bx+1][by] = board[bx+1][by], board[bx][by]
	elif move == 'S':
		board[bx][by], board[bx][by-1] = board[bx][by-1], board[bx][by]
	elif move == 'D':
		board[bx][by], board[bx-1][by] = board[bx-1][by], board[bx][by]
		
def makeRandomMove(board):
	blankx, blanky = findBlankSpace(board)
	validMoves = []
	if blanky != 3:
		validMoves.append('W')
	if blankx != 3:
		validMoves.append('A')
	if blanky != 0:
		validMoves.append('S')
	if blankx != 0:
		validMoves.append('D')
	
	makeMove(board, random.choice(validMoves))
	
def getNewPuzzle(moves=200):
	board = getNewBoard()
	
	for i in range(moves):
		makeRandomMove(board)
	return board
	
if __name__ == '__main__':
	main()
