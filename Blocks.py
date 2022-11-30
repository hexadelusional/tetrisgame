from main import*
################################################################ BLOCKS ################################################################


################ COMMON BLOCKS ################

common_blocks = [[] for i in range(20)]
common_blocks[0] = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0]]
common_blocks[1] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
common_blocks[2] = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 0]]
common_blocks[3] = [[0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]
common_blocks[4] = [[0, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
common_blocks[5] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [1, 1, 1, 0]]
common_blocks[6] = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0]]
common_blocks[7] = [[0, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]]
common_blocks[8] = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
common_blocks[9] = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0]]
common_blocks[10] = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]]
common_blocks[11] = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
common_blocks[12] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [1, 1, 1, 0]]
common_blocks[13] = [[0, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0]]
common_blocks[14] = [[0, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]]
common_blocks[15] = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0]]
common_blocks[16] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [1, 1, 0, 0]]
common_blocks[17] = [[0, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
common_blocks[18] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
common_blocks[19] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]

################ CIRCLE BLOCKS ################

circle_list = [[] for i in range(12)]
circle_list[0] = [[0,0,0,0,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0]]
circle_list[1] = [[0,0,0,0,0],[0,1,1,0,0],[1,1,1,1,0],[1,1,1,1,0],[0,1,1,0,0]]
circle_list[2] = [[0,0,0,0,0],[1,0,0,1,0],[1,0,0,1,0],[1,0,0,1,0],[1,1,1,1,0]]
circle_list[3] = [[0,0,0,0,0],[1,1,1,1,0],[0,0,0,1,0],[0,0,0,1,0],[0,0,0,1,0]]
circle_list[4] = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,0],[1,1,1,0,0]]
circle_list[5] = [[0,0,0,0,0],[1,1,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[1,1,1,0,0]]
circle_list[6] = [[0,0,0,0,0],[1,1,0,0,0],[1,1,0,0,0],[1,1,0,0,0],[1,1,0,0,0]]
circle_list[7] = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,0],[1,1,1,1,0]]
circle_list[8] = [[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]]
circle_list[9] = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1],[1,0,0,0,1]]
circle_list[10] = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1]]
circle_list[11] = [[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,1,0],[1,1,1,1,0]]

################ DIAMOND BLOCKS ################

diamond_list = [[] for i in range(14)]
diamond_list[0] = [[0,0,0,0,0],[0,0,1,1,0],[0,1,1,0,0],[1,1,0,0,0],[1,0,0,0,0]]
diamond_list[1] = [[0,0,0,0,0],[1,1,0,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,0,1,0]]
diamond_list[2] = [[0,0,0,0,0],[1,1,1,1,0],[0,1,1,0,0],[0,1,1,0,0],[0,1,1,0,0]]
diamond_list[3] = [[0,0,0,0,0],[1,0,0,1,0],[0,1,1,0,0],[0,1,1,0,0],[1,0,0,1,0]]
diamond_list[4] = [[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]]
diamond_list[5] = [[0,0,0,0,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0]]
diamond_list[6] = [[0,0,0,0,0],[1,0,0,0,0],[1,1,0,0,0],[0,1,1,0,0],[0,0,1,1,0]]
diamond_list[7] = [[0,0,0,0,0],[0,0,0,1,0],[0,0,1,1,0],[0,1,1,0,0],[1,1,0,0,0]]
diamond_list[8] = [[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]]
diamond_list[9] = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,1,1,0],[0,0,0,1,0]]
diamond_list[10] = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1]]
diamond_list[11] = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,0],[0,0,0,1,0]]
diamond_list[12] = [[0,0,0,0,0],[1,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0]]
diamond_list[13] = [[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,1,0,0,0]]

################ TRIANGLE BLOCKS ################

triangle_list = [[] for i in range(11)]
triangle_list[0] = [[1,0,0],[1,1,1],[0,0,1]]
triangle_list[1] = [[1,1,0],[0,1,0],[0,1,1]]
triangle_list[2] = [[0,0,1],[1,1,1],[1,0,0]]
triangle_list[3] = [[0,1,1],[0,1,0],[1,1,0]]
triangle_list[4] = [[0,0,1],[0,1,0],[1,0,0]]
triangle_list[5] = [[1,0,0],[0,1,0],[0,0,1]]
triangle_list[6] = [[1,0,0],[1,0,0],[1,0,0]]
triangle_list[7] = [[0,0,0],[1,1,1],[1,1,1]]
triangle_list[8] = [[0,0,0],[1,0,0],[1,0,0]]
triangle_list[9] = [[0,1,0],[1,1,1],[0,1,0]]
triangle_list[10] = [[0,0,0],[0,0,0],[1,1,0]]

blocks_list = [diamond_list, triangle_list, circle_list]



# function print_blocs(grid) which takes as parameters the shape of the chosen tray, and which displays the list of all the blocks associated with it

def print_blocks(blocks):
    print("ALL BLOCKS :\n")
    if len(blocks) % 5 == 0 :
        length = len(blocks)
    else :
        length = len(blocks) - (len(blocks) % 5 + 1)
    for block in range(0,length,5):
        #Printing the line with name of blocks
        for n in range(block, block+5) :
            print('| {:^10} |'.format("Block "+ str(n)),end= "")
        print("\n".strip())
        max_rows = max(len(blocks[0]), len(blocks[-1]))
        for row in range(max_rows):
            for block_i in range(block,block+5):
                if row < len(blocks[block_i]) :
                    substring = ""
                    for elt in blocks[block_i][row]:
                        if elt == 0 :
                            substring += chr(10240) + " "
                        else :
                            substring += chr(9632) + " "
                    print('| {:^10} |'.format(substring),end="")
                else :
                    print('| {:^10} |'.format(" "),end="")
            print("\n".strip())
        print('_' * 70)
    if length != len(blocks) :
        for block in range(length+1, len(blocks)):
            print('| {:^10} |'.format("Block " + str(block)), end="")
        print("\n".strip())
        for row in range(len(blocks[-1])):
            for block in range(length + 1, len(blocks)):
                substring = ""
                for elt in blocks[block][row]:
                    if elt == 0 :
                        substring += chr(10240) + " "
                    else :
                        substring += chr(9632) + " "
                print('| {:^10} |'.format(substring),end="")
            print("\n".strip())
        print('_' * 70)



def select_blocks():
    for i in range(len(current_blocks)):
        chosen_block = int(input("Enter the next block to place on the grid: "))
        while chosen_block < 0 or chosen_block > len(current_blocks):
            chosen_block = int(input("Enter the next block to place on the grid (you have to enter the number next to the block you want) : "))
    return current_blocks[chosen_block]



"""
Matrix = []
def valid_position(grid, row, col):
    x = 0
    z = 0
    maju = "ABCDEFGHIJKLMNOPQRSTUVWXY"
    minu = "abcdefghijklmnopqrstuvwxy"
    for i in range(25):
        if row == maju[i]:
            x = i
        if col == minu[i]:
            y = i

    # filling a matrix with the elements of the grid file
    with open(grid + ".txt", "r") as G:
        for line in G:
            l = []
            line = line.strip()
            columns = line.split()
            for elt in columns:
                l.append(elt)
            Matrix.append(l)

    # going through the matrix to check if the block is positionable
    possible = True
    while possible == True:
        for i in range(len(select_blocks())-1):
            for j in range(len(select_blocks()[i])):
                if Matrix[x][y]==0:
                    if select_blocks()[-1][0] == 1:
                        print("Error, you made a mistake ! ")
                        possible = False
                    if select_blocks()[]
                if Matrix[x][y]==1:
                    if select_blocks()[-1][0] == 1:
                    if select_blocks()[i][0] == 1 and Matrix[x][y-1]
            if select_blocks()[i][0] ==

print(valid_position(current_grid, "A", "b"))


"""
