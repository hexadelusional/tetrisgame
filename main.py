#with tkinter

#Creation of all the blocks
#Espace de width à droite
#Espace de length en haut

#the blocks in common
common_blocks = [[] for i in range(21)]
common_blocks[1] = [[0,0,0,0],[0,0,0,0],[1,0,0,0],[1,1,0,0]]
common_blocks[2] = [[0,0,0,0],[0,0,0,0],[0,1,0,0],[1,1,0,0]]
common_blocks[3] = [[0,0,0,0],[0,0,0,0],[1,0,0,0],[1,1,1,0]]
common_blocks[4] = [[0,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,0,0]]
common_blocks[5] = [[0,0,0,0],[1,0,0,0],[1,1,0,0],[1,0,0,0]]
common_blocks[6] = [[0,0,0,0],[0,0,0,0],[0,1,0,0],[1,1,1,0]]
common_blocks[7] = [[0,0,0,0],[0,0,0,0],[1,1,0,0],[0,1,1,0]]
common_blocks[8] = [[0,0,0,0],[1,0,0,0],[1,1,0,0],[0,1,0,0]]
common_blocks[9] = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
common_blocks[10]= [[0,0,0,0],[0,0,0,0],[1,1,0,0],[1,1,0,0]]
common_blocks[11]= [[0,0,0,0],[0,0,0,0],[1,1,0,0],[0,1,0,0]]
common_blocks[12]= [[0,0,0,0],[0,0,0,0],[1,1,0,0],[1,0,0,0]]
common_blocks[13]= [[0,0,0,0],[0,0,0,0],[0,0,1,0],[1,1,1,0]]
common_blocks[14]= [[0,0,0,0],[1,0,0,0],[1,0,0,0],[1,1,0,0]]
common_blocks[15]= [[0,0,0,0],[0,1,0,0],[1,1,0,0],[0,1,0,0]]
common_blocks[16]= [[0,0,0,0],[0,0,0,0],[1,1,1,0],[0,1,0,0]]
common_blocks[17]= [[0,0,0,0],[0,0,0,0],[0,1,1,0],[1,1,0,0]]
common_blocks[18]= [[0,0,0,0],[0,1,0,0],[1,1,0,0],[1,0,0,0]]
common_blocks[19]= [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
common_blocks[20]= [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,1,1]]

#the circle blocks
circle_list = [[] for i in range(13)]
circle_list[1] = [[0,0,0,0,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0]]
circle_list[2] = [[0,0,0,0,0],[0,1,1,0,0],[1,1,1,1,0],[1,1,1,1,0],[0,1,1,0,0]]
circle_list[3] = [[0,0,0,0,0],[1,0,0,1,0],[1,0,0,1,0],[1,0,0,1,0],[1,1,1,1,0]]
circle_list[4] = [[0,0,0,0,0],[1,1,1,1,0],[0,0,0,1,0],[0,0,0,1,0],[0,0,0,1,0]]
circle_list[5] = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,0],[1,1,1,0,0]]
circle_list[6] = [[0,0,0,0,0],[1,1,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[1,1,1,0,0]]
circle_list[7] = [[0,0,0,0,0],[1,1,0,0,0],[1,1,0,0,0],[1,1,0,0,0],[1,1,0,0,0]]
circle_list[8] = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,0],[1,1,1,1,0]]
circle_list[9] = [[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]]
circle_list[10]= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1],[1,0,0,0,1]]
circle_list[11]= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1]]
circle_list[12]= [[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,1,0],[1,1,1,1,0]]

#the diamond blocks
diamond_list = [[] for i in range(15)]
diamond_list[1] = [[0,0,0,0,0],[0,0,1,1,0],[0,1,1,0,0],[1,1,0,0,0],[1,0,0,0,0]]
diamond_list[2] = [[0,0,0,0,0],[1,1,0,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,0,1,0]]
diamond_list[3] = [[0,0,0,0,0],[1,1,1,1,0],[0,1,1,0,0],[0,1,1,0,0],[0,1,1,0,0]]
diamond_list[4] = [[0,0,0,0,0],[1,0,0,1,0],[0,1,1,0,0],[0,1,1,0,0],[1,0,0,1,0]]
diamond_list[5] = [[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]]
diamond_list[6] = [[0,0,0,0,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0]]
diamond_list[7] = [[0,0,0,0,0],[1,0,0,0,0],[1,1,0,0,0],[0,1,1,0,0],[0,0,1,1,0]]
diamond_list[8] = [[0,0,0,0,0],[0,0,0,1,0],[0,0,1,1,0],[0,1,1,0,0],[1,1,0,0,0]]
diamond_list[9] = [[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]]
diamond_list[10]= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,1,1,0],[0,0,0,1,0]]
diamond_list[11]= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1]]
diamond_list[12]= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,0],[0,0,0,1,0]]
diamond_list[13]= [[0,0,0,0,0],[1,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0]]
diamond_list[14]= [[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,1,0,0,0]]

#the triangle blocks
triangle_list = [[] for i in range(12)]
triangle_list[1] = [[1,0,0],[1,1,1],[0,0,1]]
triangle_list[2] = [[1,1,0],[0,1,0],[0,1,1]]
triangle_list[3] = [[0,0,1],[1,1,1],[1,0,0]]
triangle_list[4] = [[0,1,1],[0,1,0],[1,1,0]]
triangle_list[5] = [[0,0,1],[0,1,0],[1,0,0]]
triangle_list[6] = [[1,0,0],[0,1,0],[0,0,1]]
triangle_list[7] = [[1,0,0],[1,0,0],[1,0,0]]
triangle_list[8] = [[0,0,0],[1,1,1],[1,1,1]]
triangle_list[9] = [[0,0,0],[1,0,0],[1,0,0]]
triangle_list[10]= [[0,1,0],[1,1,1],[0,1,0]]
triangle_list[11]= [[0,0,0],[0,0,0],[1,1,0]]

blocs_list = [diamond_list, circle_list, triangle_list]





# function read_grid(path) that returns a valid grid read from the contents of the file specified path


# function save_grid(path, grid) that saves a grid in a file specified by path
# function print_grid(grid) that displays the status of the grid

# function print_blocs(grid) which takes as parameters the shape of the choses tray and which diplays the list of all the blocks associated with it
# function select_block() which allows you to select the blocks to be proposed to the user according to one of the twho policies explained

# function valid_position(grid, block, i, j) which checks wheter the block block can be placed on the slot grid[i][j] in such a way that the lower left box of the block bloc is
# positioned on grid[i][j]
