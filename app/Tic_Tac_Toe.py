import sys

print("Welcome to Tic Tac Tow game !!")

def display_board(board):
	print(board['7'] + '|' + board['8'] + '|' + board['9'])
	print('-+-+-')
	print(board['4'] + '|' + board['5'] + '|' + board['6'])
	print('-+-+-')
	print(board['1'] + '|' + board['2'] + '|' + board['3'])

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
display_board(theBoard)

liNames = ['X', 'O']
name = input("Do you want to be X or O? ")
print("Nice to meet you " + name + "!")
name = name.upper()
assert name in liNames, 'It Can be only X or O.'

liProcess = ['YES', 'NO']
toProcess = input("Are you ready to Play Yes or No? ")
print(toProcess)
toProcess = toProcess.upper()
assert toProcess in liProcess, 'Please answer Yes or No.'

if toProcess == 'YES':
	print("Let's Play now")

	nums = []
	for i in range(10):
		num1 = input("player1: which numebr you like: ")
		if num1 not in nums:
			nums.append(num1)
		else:
			sys.exit()


		num2 = input("player2: your turn: ")
		if num1 not in nums:
			nums.append(num2)
		print(nums)

	# board_keys = []

	# for key in theBoard:
	#     board_keys.append(key)

else:
	print("Ok then I'll stop.")
	sys.exit()

