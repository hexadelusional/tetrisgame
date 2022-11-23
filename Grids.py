
################################################################ GRIDS ################################################################


################# DIAMOND GRID ################

# creation + filling up the Diamond txt doc

def grid_diamond():
    with open("diamond.txt", "w") as D :
        length = 12
        for i in range(length):
            D.write("0  " * (length - i) + "1  " * (2 * i + 1) + "0  " * (length - i) + "\n")
        for i in range(length - 2, -1, -1):
            D.write("0  " * (length - i) + "1  " * (2 * i + 1) + "0  " * (length - i) + "\n")

################ TRIANGLE GRID ################

# creation + filling up the Triangle txt doc

def grid_triangle():
    with open("triangle.txt", "w") as T :
        length = 12
        for i in range(length):
            T.write("0  " * (length - i) + "1  " * (2 * i + 1) + "0  " * (length - i) + "\n")
        

################# CIRCLE GRID ################
# creation + filling up the Circle txt doc

def grid_circle():
    with open("circle.txt","w") as C :
        length = 25
        space = 5
        for i in range(1,length+1):
            if i<=5 :
                C.write("0  "*(space-i+1) + "1  " *(length-(space-i+1)*2) + "0  " * (space - i+1) + "\n")
            elif i >= 21 :
                C.write("0  " * (i-(length-space)) + "1  " * (length -(i-(length-space))*2) + "0  " * (i-(length-space)) + "\n")
            else :
                C.write("1  " * (length) + "\n")


# function read_grid that returns a valid grid read from the contents of the file specified by path
def read_grid(path):
    p = open(path + ".txt", "r")


# function save_grid(path, grid)that save a grid in a file specified by path
def save_grid(path, grid):
    with open(grid + ".txt", "r") as G, open(path, "w") as P:
        lines = G.readlines()
        G.close()
        for line in lines:
            P.write(line)
        P.close()


# building the grid the user will see



# function print_grid(grid) which displays the status of the grid in ascii symbols
def print_grid(grid):
    print("   " + " a " + " b " + " c " + " d " + " e " + " f " + " g " + " h " + " i " + " j " + " k " + " l " + " m " + " n " + " o " + " p " + " q " + " r " + " s " + " t " + " u " + " v " + " w " + " x " + " y ")
    print(" " + chr(9556) + chr(9552) * 77 + chr(9559))
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
    print(" " + chr(9562) + chr(9552) * 77 + chr(9565))


