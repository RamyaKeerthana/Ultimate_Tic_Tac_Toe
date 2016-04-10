import sys
import random
import getopt

# Well-known board positions
WINNING_TRIADS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
    (2, 5, 8), (0, 4, 8), (2, 4, 6))

PRINTING_TRIADS = [(0, 1, 2, 3, 4, 5, 6, 7, 8),(9, 10, 11, 12, 13, 14, 15, 16, 17),(18, 19, 20, 21, 22, 23, 24, 25, 26),( 27, 28, 29, 30, 31, 32, 33, 34, 35),
(36, 37, 38, 39, 40, 41, 42, 43, 44),(45, 46, 47, 48, 49, 50, 51, 52, 53),(54, 55, 56, 57, 58, 59, 60, 61, 62),(63, 64, 65, 66, 67, 68, 69, 70, 71),
(72, 73, 74, 75, 76, 77, 78, 79, 80)]

FLAG_BLOCKS=[1 for i in range(9)]
VALID_BLOCKS={0:(1,3),1:(0,2),2:(1,5),3:(0,6),4:(4,),5:(2,8),6:(3,7),7:(6,8),8:(5,7)}
BLOCKS_CELLS={0:(0,1,2,9,10,11,18,19,20),1:(3,4,5,12,13,14,21,22,23),2:(6,7,8,15,16,17,24,25,26),3:(27,28,29,36,37,38,45,46,47),4:(30,31,32,39,40,41,48,49,50),5:(33,34,35,42,43,44,51,52,53),6:(54,55,56,63,64,65,72,73,74),7:(57,58,59,66,67,68,75,76,77),8:(60,61,62,69,70,71,78,79,80)}
X_token = -1
Open_token = 0
O_token = 1
MARKERS = ['_', 'O', 'X']

board=[0 for i in range(81)]
	
def Player33():
	global board
	global FLAG_BLOCKS
	global BLOCKS_CELLS         
	loop= True
	while loop:
		inp = input("Your block no: ")
		move = int(inp)
		inp1 = input("Your cell position: ")
		cell=int(inp1)
		if FLAG_BLOCKS[move]==1:
			Valid_blocks(cell) 	
	     	if board[BLOCKS_CELLS[move][cell]]==0:
	                board[BLOCKS_CELLS[move][cell]]= 1
	                loop = False
	        
	        
		else:
			print "Invalid block"
			continue
	print_board(board)
	print
	Player2()
	return (BLOCKS_CELLS[move][cell]/9,BLOCKS_CELLS[move][cell]%9)
	

def Player2():
	global board
	global FLAG_BLOCKS
	global BLOCKS_CELLS
	for i in range(9):
		if FLAG_BLOCKS[i]==1:
			for j in range(9):
				if board[BLOCKS_CELLS[i][j]]==0:
					board[BLOCKS_CELLS[i][j]]=-1
					Valid_blocks(j)						
					break
			break
	print_board(board)
	print
	Player33()




def Valid_blocks(last_block):
	global board
	global FLAG_BLOCKS
	global BLOCKS_CELLS
	FLAG_BLOCKS=[0 for i in range(9)]
	for i in VALID_BLOCKS[last_block]:
		FLAG_BLOCKS[i]=1


def print_board(board):
    '''Print the board in human-readable format.
       Called with current board (array of 9 ints).
    '''
    for row in PRINTING_TRIADS:
        for hole in row:
            print MARKERS[board[hole]],
        print

def main():
	print_board(board)
	Player33()	



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print
        sys.exit(1)
