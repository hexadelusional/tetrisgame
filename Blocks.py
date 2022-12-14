from random import *
from main import *

# BLOCKS

# COMMON BLOCKS

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

# CIRCLE BLOCKS

circle_list = [[] for i in range(12)]
circle_list[0] = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0]]
circle_list[1] = [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [0, 1, 1, 0, 0]]
circle_list[2] = [[0, 0, 0, 0, 0], [1, 0, 0, 1, 0], [1, 0, 0, 1, 0], [1, 0, 0, 1, 0], [1, 1, 1, 1, 0]]
circle_list[3] = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0]]
circle_list[4] = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 0, 0]]
circle_list[5] = [[0, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0]]
circle_list[6] = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0]]
circle_list[7] = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0]]
circle_list[8] = [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
circle_list[9] = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1]]
circle_list[10] = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]
circle_list[11] = [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 1, 0], [1, 1, 1, 1, 0]]

# DIAMOND BLOCKS

diamond_list = [[] for i in range(14)]
diamond_list[0] = [[0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0]]
diamond_list[1] = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 0]]
diamond_list[2] = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0]]
diamond_list[3] = [[0, 0, 0, 0, 0], [1, 0, 0, 1, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [1, 0, 0, 1, 0]]
diamond_list[4] = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]]
diamond_list[5] = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0]]
diamond_list[6] = [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0]]
diamond_list[7] = [[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [1, 1, 0, 0, 0]]
diamond_list[8] = [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
diamond_list[9] = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 0]]
diamond_list[10] = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]
diamond_list[11] = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 0]]
diamond_list[12] = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0]]
diamond_list[13] = [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0]]

# TRIANGLE BLOCKS

triangle_list = [[] for i in range(11)]
triangle_list[0] = [[1, 0, 0], [1, 1, 1], [0, 0, 1]]
triangle_list[1] = [[1, 1, 0], [0, 1, 0], [0, 1, 1]]
triangle_list[2] = [[0, 0, 1], [1, 1, 1], [1, 0, 0]]
triangle_list[3] = [[0, 1, 1], [0, 1, 0], [1, 1, 0]]
triangle_list[4] = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
triangle_list[5] = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
triangle_list[6] = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
triangle_list[7] = [[0, 0, 0], [1, 1, 1], [1, 1, 1]]
triangle_list[8] = [[0, 0, 0], [1, 0, 0], [1, 0, 0]]
triangle_list[9] = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
triangle_list[10] = [[0, 0, 0], [0, 0, 0], [1, 1, 0]]


# function print_blocs which displays the list of all the blocks associated with it
def print_blocks(list_blocks):
    """
    :param list_blocks: list of matrices
    :return: None
    :role: printing the blocks in list_blocks
    """
    # blocks : list of all the blocks to print
    # cpt : index of the last block we're currently printing
    blocks = list_blocks
    cpt = 0
    print("\n".strip())
    while blocks:
        # if there are less than 8 blocks in blocks :
        # => row_blocks takes all elements in blocks, and we empty blocks to get out of while loop
        # => length = number of remaining elements in blocks
        if len(blocks) < 8:
            row_blocks = blocks
            blocks = []
            nb = len(row_blocks)
        # if there are at least 8 blocks in blocks :
        # => row_blocks takes the first 8 elements from blocks
        # => we remove those 8 blocks from blocks
        # => length = 8
        else:
            row_blocks = blocks[0:8]
            blocks = blocks[8:]
            nb = 8
        # we add the given length to cpt to know at which index we are in terms of list_blocks
        cpt += nb
        # then we print the names "block n" from (cpt - length) to cpt
        for block in range(cpt - nb, cpt):
            print('| {:^10} |'.format("Block " + str(block)), end="")
        print("\n".strip())
        # max_ rows : number of rows of the biggest block
        max_rows = max(len(row_blocks[0]), len(row_blocks[-1]))
        # we go through row_blocks, row by row (row1 of all blocks, then row2 of all blocks ...)
        # for each block in row_blocks :
        # => if row exists in the block then we print | characters |
        # => if row doesn't exist then we print empty spaces between the | |
        for row in range(max_rows):
            for block in range(len(row_blocks)):
                if row < len(row_blocks[block]):
                    substring = ""
                    for elt in row_blocks[block][row]:
                        if elt == 0:
                            substring += chr(10240) + " "
                        else:
                            substring += chr(9632) + " "
                    print('| {:^10} |'.format(substring), end="")
                else:
                    print('| {:^10} |'.format(" "), end="")
            print("\n".strip())
        print('_' * 112)


# function select_blocks that displays the blocks proposed to the user according to the policy and type of tray chosen
def select_blocks(list_blocks, policy):
    """
    :param: list_blocks : given list of matrices (blocks)
    :param: policy: character that is either '1' or '2'
    :return: the matrix of the selected block
    """
    # we copy in blocks the elements in list_blocks
    blocks = list_blocks
    # if policy is '1' :
    # => we print all elements of blocks for the user
    # => we ask the user for the index of the matrix (chosen_index) in list_blocks that they want to place
    # => we repeat the previous task as long as chosen_index doesn't exist
    # => we return the matrix of the selected block
    if policy == '1':
        print_blocks(blocks)
        chosen_index = input(chr(8658) + " Enter the next block to place on the grid: \n")
        while not (not (not (1 <= len(chosen_index) <= 2)) and not (
                not ('0' <= chosen_index[0] <= '9' and '0' <= chosen_index[-1] <= '9')) and (
                           0 <= int(chosen_index) <= (len(blocks) - 1))):
            chosen_index = input(chr(8658) +
                " Enter the next block to place on the grid (you have to enter the number of next block) : \n")
        return blocks[int(chosen_index)]
    # => we randomly choose 3 elements in blocks (put in the_random_three) and print them for the user
    # => we ask the user for the index of the matrix (chosen_index) in the_random_three that they want to place
    # => we repeat the previous task as long as chosen_index doesn't exist
    # => we return the matrix of the selected block
    else:
        the_random_three = sample(blocks, 3)
        print_blocks(the_random_three)
        chosen_index = input(chr(8658) + " Enter the next block to place on the grid: \n")
        while not (0 <= int(chosen_index) <= 2):
            chosen_index = input(chr(8658) + 
                                 " Enter the next block to place on the grid (you have to enter the number of next block) : \n")
        return the_random_three[int(chosen_index)]


# function coordinates that transforms the letter coordinates given by the user to integers
def coordinates(grid, size):
    """
    :param grid: matrix of lists of characters ('0', '1' or '2')
    :param size: length of the grid (number of elements in each row)
    :return:
            row : integer, index of the row of the position
            col : integer, index of the column of the position
    """
    # asking for the y coordinates
    # we ask the user for col (a letter of the alphabet in lowercase)
    # we repeat the previous task as long as col doesn't exist
    col = str(input(chr(8658) + " Enter the y coordinates of the column: "))
    while col < chr(97) or col > (chr(97 + size - 1)) or len(col) != 1:
        col = str(input(chr(8658) +
            " This column doesn't exist ! You must enter the letter (in lowercase) of the column you want: "))

    # particular case for the triangle => y-axis = half of x-axis
    if grid == "T":
        size = (size + 1) // 2

    # asking for the x coordinates
    # we ask the user for row (a letter of the alphabet in uppercase)
    # we repeat the previous task as long as row doesn't exist
    row = str(input(chr(8658) + " Enter the x coordinates of the row: "))
    while row < chr(65) or row > (chr(65 + size - 1)) or len(row) != 1:
        row = str(input(chr(8658) +
            " This row does not exist ! You must enter the letter (in uppercase) of the row you want: "))

    # transforming the coordinates from letters to numbers
    return (ord(row) - 65), (ord(col) - 97)

# function valid_position which checks whether a block can be placed such that the lower left square of it is its center
def valid_position(grid, block, i, j):
    """
    :param grid : matrix of lists of characters ('0', '1' or '2')
    :param block : matrix of lists of integers (0 or 1)
    :param i : integer of the index of the row
    :param j: integer of the index of the column
    :return: boolean, True if the block can be placed, else False
    """
    # copying i in grid_row
    grid_row = i
    # we go through the rows of the block, from bottom to top
    for block_row in range(len(block) - 1, -1, -1):
        # => if there is a 1 in the row, but we already exceeded the rows of grid at the top then return False
        if (1 in block[block_row]) and (grid_row < 0):
            return False
        # => else :
        # ==> copying j in grid_col
        # ==> for each row, we go through the columns from left to right
        # ==> if block at index [block_row][block_col] is 1, but the block exceeds grid at the right then return False
        # ==> if block at [block_row][block_col] is 1, but grid at [grid_row][grid_col] is '0' or '2' then return False
        # ==> then we move to the next column in the grid
        grid_col = j
        for block_col in range(len(block)):
            if block[block_row][block_col] == 1:
                if grid_col >= len(grid[grid_row]):
                    return False
                elif (grid[grid_row][grid_col] == '0') or (grid[grid_row][grid_col] == '2'):
                    return False
            grid_col += 1
    # ==> after reaching the last column, we move to row above
        grid_row -= 1
    # After checking all the columns of all rows, then we return True
    return True


# function emplace_block that positions the block chosen by the user on the grid if and only if it's position is valid
def emplace_block(grid, block, i, j):
    """
    :param grid : matrix of lists of characters ('0', '1' or '2')
    :param block : matrix of lists of integers (0 or 1)
    :param i : integer = index of the row of the position
    :param j: integer = index of the column of the position
    :return: temp_grid : modified matrix of lists of characters ('0', '1' or '2')
    """
    # copying grid in temp_grid
    temp_grid = grid
    # block_row : index of the last row in the block
    block_row = len(block) - 1
    # we go through the grid from index i to (i-len(block)) || going up
    # => block_col : index of the first column in the sublist block_row of block
    for grid_row in range(i, i - len(block), -1):
        block_col = 0
        # => we go through the grid's sublist from j to (j+len(block)) || left to right
        # => if block at index [block_row][block_col] is 1, we change the temp_grid at index [grid_row][grid_col] to '2'
        # => then we move to the next column of the block
        # => after reaching the last column we move to the row of the block above
        for grid_col in range(j, j + (len(block))):
            if block[block_row][block_col] == 1:
                temp_grid[grid_row][grid_col] = '2'
            block_col += 1
        block_row -= 1
    return temp_grid
