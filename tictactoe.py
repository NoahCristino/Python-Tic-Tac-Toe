'''
Tic Tac Toe
By Noah Cristino
'''
import os
board = [["-", "-", "-"],
         ["-", "-", "-"], 
		 ["-", "-", "-"]]
#print(board[1][1])
def printboard():
	os.system('cls')
	row1 = ""
	row2 = ""
	row3 = ""
	for sym1 in board[0]:
		row1 = row1 + sym1
	for sym2 in board[1]:
		row2 = row2 + sym2
	for sym3 in board[2]:
		row3 = row3 + sym3
	print("1" + row1)
	print("2" + row2)
	print("3" + row3)
	print(" 123")
plrone = input("X's or O's Player one? ")
plrtwo = ""
if plrone == "X":
	plrtwo = "O"
else:
	plrtwo = "X"
win = False
turn = "Player One"
while win == False:
	if board[0][0] == board[1][0] == board[2][0] == "X":
		if plrone == "X":
			printboard()
			print("Player One wins!")
			break
		else:
			printboard()
			print("Player Two wins!")
			break
	if board[0][1] == board[1][1] == board[2][1] == "X":
		if plrone == "X":
			printboard()
			print("Player One wins!")
			break
		else:
			printboard()
			print("Player Two wins!")
			break
	if board[0][2] == board[1][2] == board[2][2] == "X":
		if plrone == "X":
			printboard()
			print("Player One wins!")
			break
		else:
			printboard()
			print("Player Two wins!")
			break
	if board[0][0] == board[0][1] == board[0][2] == "X":
		if plrone == "X":
			printboard()
			print("Player One wins!")
			break
		else:
			printboard()
			print("Player Two wins!")
			break
	if board[1][0] == board[1][1] == board[1][2] == "X":
		if plrone == "X":
			printboard()
			print("Player One wins!")
			break
		else:
			printboard()
			print("Player Two wins!")
			break
	if board[2][0] == board[2][1] == board[2][2] == "X":
		if plrone == "X":
			printboard()
			print("Player One wins!")
			break
		else:
			printboard()
			print("Player Two wins!")
			break
	if board[0][0] == board[1][1] == board[2][2] == "X":
		if plrone == "X":
			printboard()
			print("Player One wins!")
			break
		else:
			printboard()
			print("Player Two wins!")
			break
	if board[0][2] == board[1][1] == board[2][0] == "X":
		if plrone == "X":
			printboard()
			print("Player One wins!")
			break
		else:
			printboard()
			print("Player Two wins!")
			break
	if board[0][0] == board[1][0] == board[2][0] == "O":
		if plrone == "O":
			printboard()
			print("Player One wins!")
			break
		else:
			printboard()
			print("Player Two wins!")
			break
	if board[0][1] == board[1][1] == board[2][1] == "O":
		if plrone == "O":
			printboard()
			print("Player One wins!")
			break
		else:
			printboard()
			print("Player Two wins!")
			break
	if board[0][2] == board[1][2] == board[2][2] == "O":
		if plrone == "O":
			printboard()
			print("Player One wins!")
			break
		else:
			printboard()
			print("Player Two wins!")
			break
	if board[0][0] == board[0][1] == board[0][2] == "O":
		if plrone == "O":
			printboard()
			print("Player One wins!")
			break
		else:
			printboard()
			print("Player Two wins!")
			break
	if board[1][0] == board[1][1] == board[1][2] == "O":
		if plrone == "O":
			printboard()
			print("Player One wins!")
			break
		else:
			printboard()
			print("Player Two wins!")
			break
	if board[2][0] == board[2][1] == board[2][2] == "O":
		if plrone == "O":
			printboard()
			print("Player One wins!")
			break
		else:
			printboard()
			print("Player Two wins!")
			break
	if board[0][0] == board[1][1] == board[2][2] == "O":
		if plrone == "O":
			printboard()
			print("Player One wins!")
			break
		else:
			printboard()
			print("Player Two wins!")
			break
	if board[0][2] == board[1][1] == board[2][0] == "O":
		if plrone == "O":
			printboard()
			print("Player One wins!")
			break
		else:
			printboard()
			print("Player Two wins!")
			break
	printboard()
	print("It is " + turn + "'s turn!")
	ypos = int(input("Y: ")) - 1
	xpos = int(input("X: ")) - 1
	if turn == "Player One":
		if board[ypos][xpos] == "-":
			board[ypos][xpos] = plrone
			turn = "Player Two"
		else:
			print("Space Taken!")
	else:
		if board[ypos][xpos] == "-":
			board[ypos][xpos] = plrtwo
			turn = "Player One"
		else:
			print("Space Taken!")
