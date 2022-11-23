from Grids import*
import random

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

def print_blocks(grid):
    print("COMMON BLOCKS:")
    for i in range(len(common_blocks)):
        print("Block : " + str(i))
        for j in range(len(common_blocks[i])):
            for k in range(len(common_blocks[i][j])):
                if common_blocks[i][j][k] == 0:
                    print(chr(10240), end="  ")
                elif common_blocks[i][j][k] == 1:
                    print(chr(9632), end="  ")
            print("\n".strip())
        print("_")

    if grid == "diamond.txt":
        print("DIAMOND BLOCKS:")
        for i in range(len(blocks_list[0])):
            print("Block : " + str(len(common_blocks)+i))
            for j in range(len(blocks_list[0][0])):
                for k in range(len(blocks_list[0][0][j])):
                    if blocks_list[0][i][j][k] == 0:
                        print(chr(10240), end="  ")
                    elif blocks_list[0][i][j][k] == 1:
                        print(chr(9632), end="  ")
                print("\n".strip())
            print("_")

    elif grid == "triangle.txt":
        print("TRIANGLE BLOCKS:")
        for i in range(len(blocks_list[1])):
            print("Block : " + str(len(common_blocks) + i))
            for j in range(len(blocks_list[1][0])):
                for k in range(len(blocks_list[1][0][j])):
                    if blocks_list[1][i][j][k] == 0:
                        print(chr(10240), end="  ")
                    elif blocks_list[1][i][j][k] == 1:
                        print(chr(9632), end="  ")
                print("\n".strip())
            print("_")

    elif grid == "circle.txt":
        print("CIRCLE BLOCKS:")
        for i in range(len(blocks_list[2])):
            print("Block : " + str(len(common_blocks) + i))
            for j in range(len(blocks_list[2][0])):
                for k in range(len(blocks_list[2][0][j])):
                    if blocks_list[2][i][j][k] == 0:
                        print(chr(10240), end="  ")
                    elif blocks_list[2][i][j][k] == 1:
                        print(chr(9632), end="  ")
                print("\n".strip())
            print("_")
