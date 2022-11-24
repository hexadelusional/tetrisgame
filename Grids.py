
################################################################ GRIDS ################################################################


################# DIAMOND GRID ################

# creation + filling up the Diamond txt according to the size chosen by the user
def grid_diamond(size):
    if size == "L":
        with open("diamond.txt", "w") as D:
            length = 25
            space = 11
            j = 25
            for i in range(length):
                j = j - 1
                if i <= 12:
                    D.write("0  " * (space - i + 1) + "1  " * (length - (space - i + 1) * 2) + "0  " * (
                                space - i + 1) + "\n")
                if i > 12:
                    D.write("0  " * (space - j + 1) + "1  " * (length - (space - j + 1) * 2) + "0  " * (
                                space - j + 1) + "\n")
    if size == "M":
        with open("diamond.txt", "w") as D:
            length = 23
            space = 10
            j = 23
            for i in range(length):
                j = j - 1
                if i <= 11:
                    D.write("0  " * (space - i + 1) + "1  " * (length - (space - i + 1) * 2) + "0  " * (space - i + 1) + "\n")
                if i > 11:
                    D.write("0  " * (space - j + 1) + "1  " * (length - (space - j + 1) * 2) + "0  " * (space - j + 1) + "\n")
    if size == "S":
        with open("diamond.txt", "w") as D:
            length = 21
            space = 9
            j = 21
            for i in range(length):
                j = j - 1
                if i <= 10:
                    D.write("0  " * (space - i + 1) + "1  " * (length - (space - i + 1) * 2) + "0  " * (space - i + 1) + "\n")
                if i > 10:
                    D.write("0  " * (space - j + 1) + "1  " * (length - (space - j + 1) * 2) + "0  " * (space - j + 1) + "\n")



################ TRIANGLE GRID ################

# creation + filling up the Triangle txt doc according to the size chosen by the user

def grid_triangle(size):
    with open("triangle.txt", "w") as T:
        if size == "L":
            length = 25
            space = 11
            for i in range(length):
                if i <= 12:
                    T.write("0  " * (space - i + 1) + "1  " * (length - (space - i + 1) * 2) + "0  " * (space - i + 1) + "\n")
        if size == "M":
            length = 23
            space = 10
            for i in range(length):
                if i <= 11:
                    T.write("0  " * (space - i + 1) + "1  " * (length - (space - i + 1) * 2) + "0  " * (space - i + 1) + "\n")
        if size == "S":
            length = 21
            space = 9
            for i in range(length):
                if i <= 10:
                    T.write("0  " * (space - i + 1) + "1  " * (length - (space - i + 1) * 2) + "0  " * (space - i + 1) + "\n")


################# CIRCLE GRID ################
# creation + filling up the Circle txt doc according to the size chosen by the user
def grid_circle(size):
    if size == "L":
        with open("circle.txt", "w") as C:
            length = 25
            space = 5
            for i in range(1, length + 1):
                if i <= 5:
                    C.write("0  " * (space - i + 1) + "1  " * (length - (space - i + 1) * 2) + "0  " * (
                                space - i + 1) + "\n")
                elif i >= 21:
                    C.write("0  " * (i - (length - space)) + "1  " * (length - (i - (length - space)) * 2) + "0  " * (
                                i - (length - space)) + "\n")
                else:
                    C.write("1  " * (length) + "\n")
    if size == "M":
        with open("circle.txt", "w") as C:
            length = 23
            space = 5
            for i in range(1, length + 1):
                if i <= 5:
                    C.write("0  " * (space - i + 1) + "1  " * (length - (space - i + 1) * 2) + "0  " * (
                            space - i + 1) + "\n")
                elif i >= 19:
                    C.write("0  " * (i - (length - space)) + "1  " * (length - (i - (length - space)) * 2) + "0  " * (
                            i - (length - space)) + "\n")
                else:
                    C.write("1  " * (length) + "\n")
    if size == "S":
        with open("circle.txt", "w") as C:
            length = 21
            space = 5
            for i in range(1, length + 1):
                if i <= 5:
                    C.write("0  " * (space - i + 1) + "1  " * (length - (space - i + 1) * 2) + "0  " * (
                            space - i + 1) + "\n")
                elif i >= 17:
                    C.write("0  " * (i - (length - space)) + "1  " * (length - (i - (length - space)) * 2) + "0  " * (
                            i - (length - space)) + "\n")
                else:
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


# creating a matrix to store the grid in
M = []
# function print_grid(grid) which displays the status of the grid in ascii symbols
def print_grid(grid):
    with open(grid + ".txt", "r") as G:
        # creating two strings minu and maju: the coordinates the user will enter to place the blocks
        minu = " abcdefghijklmnopqrstuvwxy"
        maju = "ABCDEFGHIJKLMNOPQRSTUVWXY"
        # going through each element of each line of the file and appending it to a big matrix M: our grid
        for line in G:
            l = []
            line = line.strip()
            columns = line.split()
            for elt in columns:
                l.append(elt)
            M.append(l)
        # writing the lowercase coordinates on the top of the grid & the ascii symbols
        for i in range(len(columns)+1):
            print(" " + minu[i] + " ", end="")
        print("\n " + chr(9556) + "  " + (chr(9552)+"  ") * (len(columns))+chr(9559))
        # replacing every 0 of our list with a blank ascii code symbol and every 1 with a little cube
        for i in range(len(M)):
            print(maju[i] + chr(9553), end="  ")
            for j in range(len(M[i])):
                if M[i][j] == "0":
                    print(chr(10240), end="  ")
                elif M[i][j] == '1':
                    print(chr(9642), end="  ")
            print(chr(9553),"\n".strip())
    print(" " + chr(9562) + "  " + (chr(9552) + "  ") * (len(columns)) + chr(9565))

