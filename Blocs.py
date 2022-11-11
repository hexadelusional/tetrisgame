import random

#Creation of all the blocks
#Espace de width à droite
#Espace de length en haut

################ COMMON BLOCS ################

common_blocs = [[] for i in range(20)]
common_blocs[0] = [[0,0,0,0],[0,0,0,0],[1,0,0,0],[1,1,0,0]]
common_blocs[1] = [[0,0,0,0],[0,0,0,0],[0,1,0,0],[1,1,0,0]]
common_blocs[2] = [[0,0,0,0],[0,0,0,0],[1,0,0,0],[1,1,1,0]]
common_blocs[3] = [[0,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,0,0]]
common_blocs[4] = [[0,0,0,0],[1,0,0,0],[1,1,0,0],[1,0,0,0]]
common_blocs[5] = [[0,0,0,0],[0,0,0,0],[0,1,0,0],[1,1,1,0]]
common_blocs[6] = [[0,0,0,0],[0,0,0,0],[1,1,0,0],[0,1,1,0]]
common_blocs[7] = [[0,0,0,0],[1,0,0,0],[1,1,0,0],[0,1,0,0]]
common_blocs[8] = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
common_blocs[9] = [[0,0,0,0],[0,0,0,0],[1,1,0,0],[1,1,0,0]]
common_blocs[10] = [[0,0,0,0],[0,0,0,0],[1,1,0,0],[0,1,0,0]]
common_blocs[11] = [[0,0,0,0],[0,0,0,0],[1,1,0,0],[1,0,0,0]]
common_blocs[12] = [[0,0,0,0],[0,0,0,0],[0,0,1,0],[1,1,1,0]]
common_blocs[13] = [[0,0,0,0],[1,0,0,0],[1,0,0,0],[1,1,0,0]]
common_blocs[14] = [[0,0,0,0],[0,1,0,0],[1,1,0,0],[0,1,0,0]]
common_blocs[15] = [[0,0,0,0],[0,0,0,0],[1,1,1,0],[0,1,0,0]]
common_blocs[16] = [[0,0,0,0],[0,0,0,0],[0,1,1,0],[1,1,0,0]]
common_blocs[17] = [[0,0,0,0],[0,1,0,0],[1,1,0,0],[1,0,0,0]]
common_blocs[18] = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
common_blocs[19] = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,1,1]]

################ CIRCLE BLOCS ################

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

################ DIAMOND BLOCS ################

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

################ TRIANGLE BLOCS ################

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

blocs_list = [diamond_list, triangle_list, circle_list]



# function print_blocs(grid) which takes as parameters the shape of the chosen tray, and which displays the list of all the blocks associated with it

def print_blocs(grid):

    if grid == "triangle.txt":
        for i in range(len(blocs_list[1])):
            for j in range(len(blocs_list[1][0])):
                for k in range(len(blocs_list[1][0][j])):
                    if blocs_list[1][i][j][k] == 0:
                        print(chr(10240), end="  ")
                    elif blocs_list[1][i][j][k] == 1:
                        print(chr(9632), end="  ")
                print("\n".strip())
            print("_")

    elif grid == "diamond.txt":
        for i in range(len(blocs_list[0])):
            for j in range(len(blocs_list[0][0])):
                for k in range(len(blocs_list[0][0][j])):
                    if blocs_list[0][i][j][k] == 0:
                        print(chr(10240), end="  ")
                    elif blocs_list[0][i][j][k] == 1:
                        print(chr(9632), end="  ")
                print("\n".strip())
            print("_")

    elif grid == "circle.txt":
        for i in range(len(blocs_list[2])):
            for j in range(len(blocs_list[2][0])):
                for k in range(len(blocs_list[2][0][j])):
                    if blocs_list[2][i][j][k] == 0:
                        print(chr(10240), end="  ")
                    elif blocs_list[2][i][j][k] == 1:
                        print(chr(9632), end="  ")
                print("\n".strip())
            print("_")
            
    print("COMMON BLOCS:")
    for i in range(len(common_blocs)):
        for j in range(len(common_blocs[i])):
            for k in range(len(common_blocs[i][j])):
                if common_blocs[i][j][k] == 0:
                    print(chr(10240), end="  ")
                elif common_blocs[i][j][k] == 1:
                    print(chr(9632), end="  ")
            print("\n".strip())
        print("_")


current_blocs = print_blocs("circle.txt")


def select_bloc():
    # selection of blocs following policy 1



    # selection of blocs following policy 2
    print(random.sample(blocs_list[1],3))


select_bloc()
