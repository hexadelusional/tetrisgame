
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
# creation + filling up the Circle txt doc
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
    open(path + ".txt", "r")


# function save_grid(path, grid)that save a grid in a file specified by path
def save_grid(path, grid):
    with open(grid + ".txt", "r") as G, open(path, "w") as P:
        lines = G.readlines()
        G.close()
        for line in lines:
            P.write(line)
        P.close()


# function print_grid(grid) which displays the status of the grid in ascii symbols
def print_grid(grid):
    M = []
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
    return M

# function row_state that verifies if line i in grid is full
def row_state(grid, i):
    row_is_full = True
    for x in grid[i-1]:
        if x == '1':
            row_is_full = False
    return row_is_full

# function col_state that verifies if column j in grid is full
def col_state(grid, j):
    col_is_full = True
    for row in range(len(grid)):
        if grid[row][j-1] == '1':
            col_is_full = False
    return col_is_full

#function row_clear(grid, i) that cancels the row i in a grid grid by shifting all lines
#from the top of a unit down. Be careful because depending on the shape of the board, some boxes
#from the previous line may no longer be present in the board.
def row_clear(grid, i):
    line = i-1
    # replacing the full line of 2s by 1s
    for j in range(len(grid[line])):
        if grid[line][j] == '2':
            grid[line][j] = '1'
    # shift of the 1s and 2s
    for L in range(line, -1, -1):
        for elt in range(len(grid[L])):
            if grid[L-1][elt] == '2':
                grid[L][elt] = '2'
                grid[L-1][elt] = '1'
            elif grid[L-1][elt] != '0':
                grid[L][elt] = '1'
    # special case for the first line seen as it has nothing to shift from
    for elt in range(len(grid[0])):
        if grid[0][elt] == '2':
            grid[0][elt] = '1'
    return grid

##### keeping score
def update_score(grid,mode,line) :
    #make col_clear / row_clear return the line that was cancelled and saved in a variable line
    s = 0
    if mode == "row" :
        for elt in grid[line] :
            if elt == 1 or elt == 2 :
                s += 1
    else :
        for row in grid :
            if row[line] == 1 or row[line] == 2 :
                s += 1
    return s
