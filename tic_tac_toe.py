'''
	Tic Tac Toe
	EduMedM
'''
import sys
from os import system, name
from random import choice, randint
from time import sleep

def clear():

	if (name == 'nt'): #for Windows
		_ = system('cls')

	else:              #for Linux or Mac (name is 'posix')
		 _ = system('clear')

def displayBoard(board):

	print(f'''
	 
	  {board[6]} | {board[7]} | {board[8]}
	 ---+---+---
	  {board[3]} | {board[4]} | {board[5]} 
	 ---+---+---
	  {board[0]} | {board[1]} | {board[2]} 
	 
	''')

def spaceFree(board, move):
	return board[move] == ' '

def getPlayerMove(board, player_letter):

	while True:

		print(''' 
	 ---+---+---	
	  7 | 8 | 9
	 ---+---+---
	  4 | 5 | 6 
	 ---+---+---
	  1 | 2 | 3 
	 ---+---+---
			''')

		print("\tYou are '",player_letter,"'")
		move = input("\n\t---> ")

		if (move in "1 2 3 4 5 6 7 8 9".split()):
			move = int(move)-1
			if spaceFree(board,move):
				return move
			else:
				print("\n\n\tChoose another movement.",end='')
		else:
			print("\n\n\tChoose a correct option.",end='')
		sleep(1)
		clear()
		displayBoard(board)

def getPlayerLetter(turn):

	if turn == "player":
		while True:

			letter = input("\n\tChoose a letter (X or O): ").upper()
			if letter in 'XO':
				if letter == 'X':
					return ['X','O']
				else:
					return ['O','X']
			else:
				print("\n\n\tChoose a correct letter.",end='')
				sleep(1)
			clear()
	else: 
		return choice([['X','O'],['O','X']])

def whoBegin():

	while True:

		print("\n\tWho goes first?: ")
		print("\t1.- Random.")
		print("\t2.- Player.")
		print("\t3.- Cpu.")

		choose = input("\n\t---> ").lower()

		if (choose.startswith('r') or choose == '1'):
			return choice(["player","cpu"])
		elif(choose.startswith('p') or choose == '2'):
			return "player"
		elif(choose.startswith('c') or choose == '3'):
			return "cpu"
		else:
			print("\n\n\tChoose a correct option.",end='')
			sleep(1)
		clear()

def winner(b, l):

	#b: board | l: letter('X' or 'O')
	return((b[6] == l and b[7] == l and b[8] == l) or \
	   (b[3] == l and b[4] == l and b[5] == l) or \
	   (b[0] == l and b[1] == l and b[2] == l) or \
	   (b[6] == l and b[3] == l and b[0] == l) or \
	   (b[7] == l and b[4] == l and b[1] == l) or \
	   (b[8] == l and b[5] == l and b[2] == l) or \
	   (b[6] == l and b[4] == l and b[2] == l) or \
	   (b[8] == l and b[4] == l and b[0] == l))

def boardCopy(board):

	board_copy = []
	for i in board:
		board_copy.append(i)
	return board_copy

def getCPUMove(board, cpu_letter, player_letter):

	board_copy = []
	corners = [0,2,6,8]
	corners_free = []
	sides = [1,3,5,7]
	sides_free = []

	#Make winning move
	for i in range(len(board)):
		board_copy = boardCopy(board)
		if spaceFree(board,i):
			board_copy[i] = cpu_letter
			if winner(board_copy, cpu_letter):
				return i

	#Block player's winning move
	for i in range(len(board)):
		board_copy = boardCopy(board)
		if spaceFree(board,i):
			board_copy[i] = player_letter
			if winner(board_copy, player_letter):
				return i

	#Move on corner
	for i in corners:
		if spaceFree(board,i):
			corners_free.append(i)
	if len(corners_free) != 0:
		return choice(corners_free)

	#Move on center
	if spaceFree(board,4):
		return 4

	#Move on side
	for i in sides:
		if spaceFree(board,i):
			sides_free.append(i)
	if len(sides_free) != 0:
		return choice(sides_free)

def tie(board):
	return (' ' not in board)

def playAgain():
	print("\n\n\tDo you want to play again (yes/no)?")
	return input("\n\t---> ").lower().startswith('y')

while True:

	clear()
	board = [' ']*9
	cont = 0
	cpu_letter = player_letter = ''
	movelist = []
	turn = whoBegin()
	clear()
	player_letter, cpu_letter = getPlayerLetter(turn)

	while cont < 9:

		if turn == "player":

			move = getPlayerMove(board, player_letter)
			movelist.append(move)
			board[move] = player_letter

			if winner(board, player_letter):
				clear()
				print("\n\tYou won!")
				cont = 9
			elif tie(board):
				clear()
				print("\n\tIt's a tie!")
				cont = 9
			else:
				turn = "cpu"
				clear()

		elif turn == "cpu":

			move = getCPUMove(board, cpu_letter, player_letter)
			movelist.append(move)
			board[move] = cpu_letter

			if winner(board, cpu_letter):
				clear()
				print("\n\tThe Computer Won!")
				cont = 9
			elif tie(board):
				clear()
				print("\n\tIt's a tie!")
				cont = 9
			else:
				turn = "player"
				clear()

		displayBoard(board)
		cont += 1

	if not(playAgain()):
		clear()
		exit()