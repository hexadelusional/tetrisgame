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

def print_blocks(current_blocks):
    #block = list of all the blocks to print
    #cpt = index of the last block to print CURRENTLY
    blocks = current_blocks
    cpt = 0
    print("Available blocks :\n")
    while blocks != []:
        #length = number of blocks to print in this round
        length = 0
        #if there are less than 5 blocks in blocks :
            #row_blocks becomes blocks and we empty blocks to get out of while loop
            #so length = number of remaining blocks in blocks
        if len(blocks) < 5 :
            row_blocks = blocks
            blocks = []
            length = len(row_blocks)
        #if there are at least 5 blocks in blocks :
            #row_blocks just take the first 5 blocks in blocks
            #and we remove those 5 blocks from blocks
            #length = 5
        else :
            row_blocks = blocks[0:5]
            blocks = blocks[5:]
            length = 5
        #we add this length to cpt to know at which total index we are
        cpt += length
        #then we print the names "block n" from cpt - length to cpt
        for block in range(cpt - length, cpt):
            print('| {:^10} |'.format("Block "+ str(block)),end= "")
        print("\n".strip())
        #max_ rows = number rows of the biggest block (because size_common < size_circle for ex)
        max_rows = max(len(row_blocks[0]),len(row_blocks[-1]))
        #we need the row of all the blocks, row by row (row1 of all the blocks then row2 ...)
        #if row exists in the block then we print | ... |
        #if row doesn't exist we print void between the | |
        for row in range(max_rows) :
            for block in range(len(row_blocks)):
                if row < len(row_blocks[block]) :
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
        print('_' * 70)


#Depending in the policy => print the blocks affiliated and
def select_blocks(current_blocks, question):
    if question == 1 :
        print_blocks(current_blocks)
        chosen_block = int(input("Enter the next block to place on the grid: "))
        while not 0 <= chosen_block < len(current_blocks):
            chosen_block = int(input(
                "Enter the next block to place on the grid (you have to enter the number next to the block you want) : "))
        return current_blocks[chosen_block]
    else :
        the_random_three = sample(current_blocks, 3)
        print_blocks(the_random_three)
        chosen_block = int(input("Enter the next block to place on the grid: "))
        while not 0 <= chosen_block <= 2 :
            chosen_block = int(input("Enter the next block to place on the grid (you have to enter the number next to the block you want) : "))
        return the_random_three[chosen_block]


##### Ask for coordinates :
def coordinates(grid, length) :
    # asking for the x coordinates
    x = str(input("Enter the x coordinate: "))
    while x < chr(97) or x > (chr(97 + length - 1)) or len(x) != 1:
        x = str(input(
            "This column does not exist ! You must enter the letter (in lowercase) corresponding to the column you want: "))

    # particular case for the triangle => y-axis = half of x-axis
    if grid == "triangle":
        length = (length + 1) // 2

    # asking for the y coordinates
    y = str(input("Enter the y coordinate: "))
    while y < chr(65) or y > (chr(65 + length - 1)) or len(y) != 1:
        y = str(input(
            "This row does not exist ! You must enter the letter (in uppercase) corresponding to the row you want: "))
    return (ord(x) - 97), (ord(y) - 65))

##### Validating a block :
def valid_position(grid,block,i,j):
    # Check until which block row to check valid position:
    block_row = (len(block)-1)
    row = 0
    while (1 not in block[row]) and row < len(block):
        row += 1
        block_row -= 1
    # Declare all the necessary variables
    size_block = len(block)
    grid_row = (ord(i)-97)
    res = True
    # Starting verification
    while res and block_row >= 0 :
        if block_row >= 1 and grid_row == 0 :
            return not res
        else :
            block_col, grid_col = 0, (ord(j)-65)
            while res and block_col < size_block :
                if block_col < size_block - 1 and grid_col == len(grid[grid_row]) :
                    res = False
                elif (grid[grid_row][grid_col] == 0 and block[block_row][block_col] == 1 ) or (grid[grid_row][grid_col] == 2 and block[block_row][block_col] == 1) :
                    res = False
                else :
                    block_col += 1
                    grid_col += 1
        block_row -= 1
        grid_row -= 1
    return res
