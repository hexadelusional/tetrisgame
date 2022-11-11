
#with tkinter


################################################################ GRIDS ################################################################


################# DIAMOND GRID ################

# creation + filling up the Diamond txt doc
D = open("diamond.txt", "w")


def grid_diamond():
    length = 12
    for i in range(length):
        D.write("0  " * (length - i) + "1  " * (2 * i + 1) + "0  " * (length - i) + "\n")
    for i in range(length - 2, -1, -1):
        D.write("0  " * (length - i) + "1  " * (2 * i + 1) + "0  " * (length - i) + "\n")
    D.close()


grid_diamond()

################ TRIANGLE GRID ################

# creation + filling up the Triangle txt doc

T = open("triangle.txt", "w")


def grid_triangle():
    length = 12
    for i in range(length):
        T.write("0  " * (length - i) + "1  " * (2 * i + 1) + "0  " * (length - i) + "\n")
    T.close()


grid_triangle()

################# CIRCLE GRID ################
# creation + filling up the Circle txt doc


# interaction with the user
current_grid = input("What board do you want to play on ? [Circle] [Triangle] [Diamond] ")
while current_grid != "diamond" and current_grid != "triangle" and current_grid != "circle":
    current_grid = input("Error, this board does not exist. You must write the name (in lowercase letters) of one of the boards proposed: [Circle] [Triangle] [Diamond] ")


# function read_grid that returns a valid grid read from the contents of the file specified by path
def read_grid(path):
    p = open(path + ".txt", "r")


read_grid(current_grid)


# function save_grid(path, grid)that save a grid in a file specified by path
def save_grid(path, grid):
    with open(grid + ".txt", "r") as G, open(path, "w") as P:
        lines = G.readlines()
        G.close()
        for line in lines:
            P.write(line)
        P.close()


save_grid("game_grid.txt", current_grid)

# building the grid the user will see
print(
    "   " + " a " + " b " + " c " + " d " + " e " + " f " + " g " + " h " + " i " + " j " + " k " + " l " + " m " + " n " + " o " + " p " + " q " + " r " + " s " + " t " + " u " + " v " + " w " + " x " + " y ")
print(" " + chr(9556) + chr(9552) * 77 + chr(9559))


# function print_grid(grid) which displays the status of the grid in ascii symbols
def print_grid(grid):
    with open(grid + ".txt", "r") as p:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        i = 0
        for line in p:
            line = line.strip()
            columns = line.split()
            print(alphabet[i] + chr(9553), end="  ")
            i += 1
            for elt in columns:
                if elt == "0":
                    print(chr(10240), end="  ")
                elif elt == '1':
                    print(chr(9642), end="  ")
            print(chr(9553), "\n".strip())


print_grid(current_grid)

print(" " + chr(9562) + chr(9552) * 77 + chr(9565))



################################################################ BLOCKS ################################################################

import random

#Creation of all the blocks
#Espace de width à droite
#Espace de length en haut

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
    print("COMMON BLOCS:")
    for i in range(len(common_blocks)):
        for j in range(len(common_blocks[i])):
            for k in range(len(common_blocks[i][j])):
                if common_blocks[i][j][k] == 0:
                    print(chr(10240), end="  ")
                elif common_blocks[i][j][k] == 1:
                    print(chr(9632), end="  ")
            print("\n".strip())
        print("_")

    if grid == "diamond.txt":
        A = 0
        print("DIAMOND BLOCS:")
        for i in range(len(blocks_list[A])):
            for j in range(len(blocks_list[A][0])):
                for k in range(len(blocks_list[A][0][j])):
                    if blocks_list[0][i][j][k] == 0:
                        print(chr(10240), end="  ")
                    elif blocks_list[0][i][j][k] == 1:
                        print(chr(9632), end="  ")
                print("\n".strip())
            print("_")
        return A
    elif grid == "triangle.txt":
        A = 1
        print("TRIANGLE BLOCS:")
        for i in range(len(blocks_list[A])):
            for j in range(len(blocks_list[A][0])):
                for k in range(len(blocks_list[A][0][j])):
                    if blocks_list[A][i][j][k] == 0:
                        print(chr(10240), end="  ")
                    elif blocks_list[1][i][j][k] == 1:
                        print(chr(9632), end="  ")
                print("\n".strip())
            print("_")
        return A

    elif grid == "circle.txt":
        A = 2
        print("CIRCLE BLOCS:")
        for i in range(len(blocks_list[A])):
            for j in range(len(blocks_list[A][0])):
                for k in range(len(blocks_list[A][0][j])):
                    if blocks_list[2][i][j][k] == 0:
                        print(chr(10240), end="  ")
                    elif blocks_list[2][i][j][k] == 1:
                        print(chr(9632), end="  ")
                print("\n".strip())
            print("_")
        return A


current_blocks = print_blocks(current_grid + ".txt")


def select_block():
    question = input("policy 1 or policy 2 ? (enter 1 or 2)")
    if question == "1":
        # selection of blocs following policy 1 : display at each turn of the game all the available blocks and the user selects one
        print(blocks_list[current_blocks])


    elif question == "2":
        # selection of blocs following policy 2 : display only 3 randomly selected blocks
        the_random_three = random.sample(blocks_list[current_blocks], 3)
        print("RANDOM BLOC PIC: ")
        for i in range(len(the_random_three)):
            for j in range(len(the_random_three[i])):
                for k in range(len(the_random_three[i][j])):
                    if the_random_three[i][j][k] == 0:
                        print(chr(10240), end="  ")
                    elif the_random_three[i][j][k] == 1:
                        print(chr(9632), end="  ")
                print("\n".strip())
            print("_")



select_block()
