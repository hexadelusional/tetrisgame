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
    with open(path + ".txt", "r") as G:
        M = []
        # going through each element of each line of the file and appending it to a big matrix M: our grid
        for line in G:
            l = []
            line = line.strip()
            columns = line.split()
            for elt in columns:
                l.append(elt)
            M.append(l)
        return M


# function save_grid(path, grid)that save a grid in a file specified by path
def save_grid(path, grid):
    with open(path + ".txt", "w") as G:
        for i in range(len(grid)):
            string = ''
            for j in range(len(grid[i])):
                string += grid[i][j] + ' '
            string += "\n"
            G.write(string)



# function print_grid(grid) which displays the status of the grid in ascii symbols
def print_grid(grid):
    # creating two strings minu and maju: the coordinates the user will enter to place the blocks
    print("\n")
    minu = "abcdefghijklmnopqrstuvwxy"
    maju = "ABCDEFGHIJKLMNOPQRSTUVWXY"
    # writing the lowercase coordinates on the top of the grid & the ascii symbols
    line = ""
    print(format(line, '>37s'), end=" ")
    for i in range(len(grid[0])):
        line += " " + minu[i] + " "
    print(line)
    line = ""
    print(format(line, '>36s'), end="")
    print((chr(9556) + "  " + (chr(9552)+"  ") * (len(grid[0]))+chr(9559)))
    # replacing every 0 of our list with a blank ascii code symbol and every 1 with a little cube
    for i in range(len(grid)):
        line = maju[i] + chr(9553)
        print(format(line, '>37s'), end="  ")
        for j in range(len(grid[i])):
            if grid[i][j] == "0":
                print(chr(10240), end="  ")
            elif grid[i][j] == '1':
                print(chr(9643), end="  ")
            elif grid[i][j] == '2':
                print(chr(9632), end="  ")
        print(chr(9553)+ maju[i]+"\n".strip())
    line = ""
    print(format(line, '>36s'), end="")
    print((chr(9562) + "  " + (chr(9552) + "  ") * (len(grid[0])) + chr(9565)))
    line = ""
    print(format(line, '>37s'), end=" ")
    for i in range(len(grid[0])):
        line += " " + minu[i] + " "
    print(line)
    return grid


# function row_state that verifies if line i in grid is full
def row_state(grid, i):
    row_is_full = True
    for x in grid[i]:
        if x == '1':
            row_is_full = False
    return row_is_full

# function col_state that verifies if column j in grid is full
def col_state(grid, j):
    col_is_full = True
    for row in range(len(grid)):
        if grid[row][j] == '1':
            col_is_full = False
    return col_is_full

#function row_clear(grid, i) that cancels the row i in a grid grid by shifting all lines from the top of a unit to the bottom

def row_clear(grid, i):

    # modifying only rows and columns aff
    # replacing the full line of 2s by 1s (a full line of blocks by empty spaces)
    for two in range(len(grid[i])):
        while grid[i][two] == '2':
            grid[i][two] = '1'
    # "shift" the 2s go down (the blocks go to the line right underneath them)
    x = i
    while x != 0:
        index = 0
        while index < len(grid[i]):
            if grid[x-1][index] == '2':
                grid[x][index] = '2'
                grid[x-1][index] = '1'
            index += 1
        x -= 1
    return grid

# function col_clear that cancels the column j in a grid
def col_clear(grid, j):
    for row in range(len(grid)):
        while grid[row][j] == '2':
            grid[row][j] = '1'
    for i in range(len(grid)):
        print(grid[i], end=" \n")
    return grid


##### keeping score
def update_score(grid,mode,line) :
    #make col_clear / row_clear return the line that was cancelled and saved in a variable line
    s = 0
    if mode == "row" :
        for elt in grid[line] :
            if elt == '1' or elt == '2' :
                s += 1
    else :
        for row in grid :
            if row[line] == '1' or row[line] == '2' :
                s += 1
    return s

