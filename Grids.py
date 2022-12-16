# GRIDS


# DIAMOND GRID

# creation + filling up the diamond.txt according to the size chosen by the user
def grid_diamond(size):
    with open("D.txt", "w") as D:
        if size == "L":
            length = 25
            space = 11
            j = 25
            for i in range(length):
                j = j - 1
                if i <= 12:
                    D.write("0  " * (space - i + 1) + "1  " * (length - (space - i + 1) * 2) + "0  " *
                            (space - i + 1) + "\n")
                if i > 12:
                    D.write("0  " * (space - j + 1) + "1  " * (length - (space - j + 1) * 2) + "0  " *
                            (space - j + 1) + "\n")

        if size == "M":
            length = 23
            space = 10
            j = 23
            for i in range(length):
                j = j - 1
                if i <= 11:
                    D.write("0  " * (space - i + 1) + "1  " * (length - (space - i + 1) * 2) + "0  " *
                            (space - i + 1) + "\n")
                if i > 11:
                    D.write("0  " * (space - j + 1) + "1  " * (length - (space - j + 1) * 2) + "0  " *
                            (space - j + 1) + "\n")

        if size == "S":
            length = 21
            space = 9
            j = 21
            for i in range(length):
                j = j - 1
                if i <= 10:
                    D.write("0  " * (space - i + 1) + "1  " * (length - (space - i + 1) * 2) + "0  " *
                            (space - i + 1) + "\n")
                if i > 10:
                    D.write("0  " * (space - j + 1) + "1  " * (length - (space - j + 1) * 2) + "0  " *
                            (space - j + 1) + "\n")


# TRIANGLE GRID

# creation + filling up the triangle.txt doc according to the size chosen by the user
def grid_triangle(size):
    with open("T.txt", "w") as T:

        if size == "L":
            length = 25
            space = 11
            for i in range(length):
                if i <= 12:
                    T.write("0  " * (space - i + 1) + "1  " * (length - (space - i + 1) * 2) + "0  " *
                            (space - i + 1) + "\n")

        if size == "M":
            length = 23
            space = 10
            for i in range(length):
                if i <= 11:
                    T.write("0  " * (space - i + 1) + "1  " * (length - (space - i + 1) * 2) + "0  " *
                            (space - i + 1) + "\n")

        if size == "S":
            length = 21
            space = 9
            for i in range(length):
                if i <= 10:
                    T.write("0  " * (space - i + 1) + "1  " * (length - (space - i + 1) * 2) + "0  " *
                            (space - i + 1) + "\n")


# CIRCLE GRID

# creation + filling up the circle.txt doc according to the size chosen by the user
def grid_circle(size):
    with open("C.txt", "w") as C:
        if size == "L":
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
                    C.write("1  " * length + "\n")

        if size == "M":
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
                    C.write("1  " * length + "\n")

        if size == "S":
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
                    C.write("1  " * length + "\n")


# function read_grid that returns a valid grid read from the contents of the file specified by path
def read_grid(path):
    with open(path + ".txt", "r") as file:
        # opening the path (in reading mode) corresponding to the grid chosen by the user (which is current_grid)
        matrix = []
        # going through each element of each line of the file and appending it to a big matrix : our grid
        for line in file:
            sub_list = []
            line = line.strip()
            columns = line.split()
            for elt in columns:
                sub_list.append(elt)
            matrix.append(sub_list)
        return matrix


# function save_grid(path, grid) that save a grid in a file specified by path
def save_grid(path, grid):
    """
    :param path: name of the grid chosen by the user
    :param grid: the matrix M of the grid
    :return: none
    """
    with open(path + ".txt", "w") as G:  # opening the file current_grid and updating the changing matrix into the file
        for i in range(len(grid)):
            string = ""
            for j in range(len(grid[i])):
                string += grid[i][j] + "  "
            string += "\n"
            G.write(string)


# function print_grid(grid) which displays the status of the grid in ascii symbols
def print_grid(grid):
    # creating two strings minu and maju : the coordinates the user will enter to place the blocks
    minu = "abcdefghijklmnopqrstuvwxy"
    maju = "ABCDEFGHIJKLMNOPQRSTUVWXY"

    # writing the lowercase coordinates on the top of the grid & the ascii symbols
    line = ""
    print(format(line, '>37s'), end=" ")  # adjusting aesthetic line (with 37 spaces before the first element)
    for i in range(len(grid[0])):
        line += " " + minu[i] + " "
    print(line)  # displaying the line of letters corresponding to the columns of the grid
    line = ""
    print(format(line, '>36s'), end="")  # adjusting aesthetics line (with 36 spaces before the first ascii character)
    print("╔" + "  " + ("═" + "  ") * (len(grid[0])) + "╗")  # top frame display
    for i in range(len(grid)):
        line = maju[i] + "║"  # displaying the line of letters corresponding to the row + frame display
        print(format(line, '>37s'), end="  ")
        for j in range(len(grid[i])):
            if grid[i][j] == "0":
                print(chr(10240), end="  ")  # replacing every 0 of the list with a blank ascii code symbol
            elif grid[i][j] == '1':
                print(chr(9643), end="  ")  # replacing every 1 of the list with a little cube
            elif grid[i][j] == '2':
                print(chr(9632), end="  ")  # replacing every 2 of the list with a big cube
        print(chr(9553) + maju[i]+"\n".strip())  # frame display + line of letters corresponding to the row
    line = ""
    print(format(line, '>36s'), end="")  # adjusting aesthetics line (with 36 spaces before the first ascii character)
    print("╚" + "  " + ("═" + "  ") * (len(grid[0])) + "╝")  # bottom frame display
    line = ""
    print(format(line, '>37s'), end=" ")  # adjusting aesthetic line (with 37 spaces before the first element)
    for i in range(len(grid[0])):
        line += " " + minu[i] + " "
    print(line + "\n")  # displaying the line of letters corresponding to the columns of the grid



    # function row_state that verifies if line i in grid is full
def row_state(grid, i):
    """
    :param grid: the matrix M of the grid
    :param i: the coordinates y of the row state to be checked
    :return: a boolean that states if the row i is full or not
    """
    row_is_full = True  # assuming the row is full
    for x in grid[i]:
        if x == '1':  # if an element in the row is not a 2, here a 1, the row is not full
            row_is_full = False
    return row_is_full


# function col_state that verifies if column j in grid is full
def col_state(grid, j):
    """
    :param grid: the matrix M of the grid
    :param j: the coordinates x of the column state to be checked
    :return: a boolean that states if the column j is full or not
    """
    col_is_full = True  # assuming the column is full
    for row in range(len(grid)):
        if grid[row][j] == '1':  # if an element in the column is not a 2, here a 1, the column is not full
            col_is_full = False
    return col_is_full


# function row_clear(grid, i) that cancels the row i in the grid and shifts all lines from the top to the bottom
def row_clear(grid, i):
    """
    :param grid: the matrix M of the grid
    :param i: the coordinates y of the row to be cleared
    :return: the new matrix with i cleared
    """
    # replacing the full line of 2s by 1s (which means: a full line of blocks by empty spaces)
    for two in range(len(grid[i])):
        while grid[i][two] == '2':
            grid[i][two] = '1'
    # doing the "shift" so that the 2s go beneath (which means: the blocks go to the line right underneath them)
    x = i
    while x != 0:
        index = 0
        while index < len(grid[i]):
            if grid[x-1][index] == '2':  # if the element above is a 2
                if x+1 != len(grid[i]):  # if the element below is not in the last line of the grid
                    if grid[x+1][index] == '0':  # the element of the line below becomes a 0
                        pass
                    else:
                        grid[x][index] = '2'  # the element on the current line becomes a 2
                        grid[x - 1][index] = '1'  # the element on the above line becomes a 1
            index += 1  # increasing index to go through every element of each line
        x -= 1  # decreasing x to go from the full line, up to the first line of the grid
    return grid


# function col_clear that cancels the column j in a grid
def col_clear(grid, j):
    """
    :param grid: the matrix M of the grid
    :param j: the coordinates x of the column to be cleared
    :return: the new matrix with j cleared
    """
    for row in range(len(grid)):
        while grid[row][j] == '2':
            grid[row][j] = '1'
    for i in range(len(grid)):
        print(grid[i], end=" \n")
    return grid


# function update_score() which updates the score each time a row or a column is cancelled
def update_score(grid, mode, line):
    """
    :param grid: the matrix M of the grid
    :param mode: a string, either 'row' or 'column'
    :param line: the coordinates x or y of the full line
    :return: s, the score
    """
    # make col_clear / row_clear return the line that was cancelled and saved in a variable line
    s = 0
    if mode == "row":
        for elt in grid[line]:
            if elt == '2':
                s += 1
    else:
        for row in grid:
            if row[line] == '2':
                s += 1
    return s


# LOADING FEATURE TO RESUME A SAVED GAME

# function backup_save which saves all data in a new file
def backup_save(path, grid, size, shape, score):
    """
    :param path: the name (given by the user) of the new file to be created to save the data of his game performance
    :param grid: the matrix of the game to be saved into the path specified above
    :param size: recuperating the size of the game grid for later re-use
    :param shape: recuperating the shape of the grid to be played on for later re-use
    :param score: recuperating the score of the game for later re-use
    :return: none
    """
    with open(path + ".txt", "w") as G:
        for i in range(len(grid)):
            string = ''
            for j in range(len(grid[i])):
                string += grid[i][j] + '  '
            string += "\n"
            G.write(string)
        G.write(str(size) + str(shape) + str(score))
        # writing the size and score of the grid on the last line of the matrix


# function reloading_all_data that recuperates all data (size, score, shape ) to start from where the user left off
def reloading_all_data(path):
    """
    :param path: the name of the file the user chose to reload
    :return: the grid size, the score of the game the user chose to reload, the new name of current file he will play in
    """
    with open(path + ".txt", "r+") as path:
        lines = path.readlines()
        for line in lines:  # going to the last line of the file
            pass
        length = ""
        score = ""
        current_grid = ""
        # recuperating the data (written on the last line of the file)
        for x in range(2):
            length += line[x]
        current_grid += line[2]
        for x in range(3, len(line)):
            score += line[x]
        with open(current_grid + ".txt", "w") as gg:
            # deleting the data to be able to use the grid to play
            for line in lines[:len(lines)-1]:
                gg.write(line)
    return int(length), int(score), current_grid
