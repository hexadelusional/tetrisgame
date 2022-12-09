from Grid import*
from Blocks import*

if __name__ == "__main__":
    print("######################################### WELCOME ######################################### \n")
    # start of the game
    ready = input("-> Press [ENTER] to start playing ! ")
    while ready == " ":
        ready = input("-> Press [enter] to start playing ! ")

    # asking what board shape the user wants
    current_grid = input("What board shape do you want to play on ? [Circle] [Triangle] [Diamond] ")
    while current_grid != "diamond" and current_grid != "triangle" and current_grid != "circle":
         current_grid = input("Error, this board shape does not exist. You must write the name (in lowercase letters) of one of the board shapes proposed; [Circle] [Triangle] [Diamond]: ")


    # asking what board shape the user wants
    current_size = input("What board size do you want to play on ? [S] [M] [L] ")
    while current_size != "S" and current_size != "M" and current_size != "L":
         current_size = input("Error, this board size does not exist. You must write the uppercase letter of the board sizes proposed; [S] for small, [M] for medium, [L] for large: ")

    grid_circle(current_size)
    grid_diamond(current_size)
    grid_triangle(current_size)

    # reading the grid chosen above according to its size 'current_size'
    M = read_grid(current_grid)

    # saving the grid in a new file called 'game_grid.txt'
    save_grid("game_grid.txt", current_grid)

    # printing the current grid in the console
    print_grid(M)

    if current_grid == 'circle.txt' :
        current_blocks = common_blocks + circle_list
    elif current_grid == 'diamond.txt' :
        current_blocks = common_blocks + diamond_list
    else :
        current_blocks = common_blocks + triangle_list

    # asking which policy the user wants
    question = input("Policy 1 (choose from all blocks) or Policy 2 (choose from 3 random blocks) ?  ")
    while question != "1" and question != "2":
        question = input("Policy 1 or Policy 2 ? [1 for All | 2 for 3 random]")


    # size
    length = 0
    if current_size == "L":
        length = 25
    elif current_size == "M":
        length = 23
    else:
        length = 21



# Start of while loop (while the player wants to play // while rep == "Y")
        # We select block
        # Ask for coordinates
        # Verify the position => ask for coordinates again if False
        # print & save grid
        # print the current score
        # ask the user if he wants to continue playing (rep = input("Y" = yes, "N" = No)
    answer = "Y"
    while answer == "Y":
        #####Select the block
        print("AVAILABLE BLOCKS :\n")
        chosen_block = select_blocks(current_blocks, question)

        ##### Where to put the block

         #### Asking coordinates
        M = print_grid((current_grid))
        print_blocks([chosen_block])
        x, y = coordinates(current_grid, length)
        while not valid_position(M, chosen_block, x, y):
            print("Please insert correct coordinates !")
            # asking for the x coordinates
            x, y = coordinates(current_grid, length)
            
         ###Placing the block and printing its state
        emplace_block(current_grid,chosen_block,x,y)
        M = read_grid(current_grid)
        print(M)
        print_grid(M)

        # checking if the rows and columns are full
        if row_state(M, x):
            row_clear(M, x)
        elif col_state(M, y):
            col_clear(M, y)
        print_grid(current_grid)



        #asking the player if they want to pursue the game
        answer = input("DO YOU WISH TO CONTINUE ? Y or N : ")
        while answer != "Y" and answer != "N" :
            answer = input("DO YOU WISH TO CONTINUE ? [Please type 'Y' or 'N'] : ")

        print(row_state(M, 1))
        print(col_state(M, 1))

        print(M)
