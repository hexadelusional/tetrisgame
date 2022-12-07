from Grid import*
from Blocks import*
import random

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
    read_grid(current_grid)

    # saving the grid in a new file called 'game_grid.txt'
    save_grid("game_grid.txt", current_grid)

    # printing the current grid in the console
    M = print_grid(current_grid)

    if current_grid == 'circle.txt' :
        current_blocks = common_blocks + circle_list
    elif current_grid == 'diamond.txt' :
        current_blocks = common_blocks + diamond_list
    else :
        current_blocks = common_blocks + triangle_list

    # printing the blocks that the user can use according to the grid he chose
    print_blocks(current_blocks)

    # asking which policy the user wants
    question = input("policy 1 or policy 2 ? (enter 1 or 2) ")
    while question != "1" and question != "2":
        question = input("policy 1 or policy 2 ? (you have to enter either 1 for policy one, or 2 for policy 2)")
    print_blocks(current_blocks)


    # size
    if current_size == "L":
        length = 25
    elif current_size == "M":
        length = 23
    else:
        length = 21

#Start of while loop (while the player wants to play // while rep == "Y")
        #We select block
        #Ask for coordinates
        #Verify the position => ask for coordinates again if False
        #print & save grid
        #print the current score
        #ask the user if he wants to continue playing (rep = input("Y" = yes, "N" = No)   
        
    answer = "Y"
    while answer == "Y":
        #####Select the block
        chosen_block = select_blocks(current_blocks, question)

        ##### Where to put the block
         #### Asking coordinates
        x, y = coordinates(current_grid, length)
        while not valid_position(current_grid, chosen_block, x, y):
            print("Please insert correct coordinates !")
            # asking for the x coordinates
            x, y = coordinates(current_grid, length)



        #asking the player if they want to pursue the game
        answer = input("DO YOU WISH TO CONTINUE ? Y or N")
        while answer != "Y" or answer != "N" :
            answer = input("DO YOU WISH TO CONTINUE ? Please type 'Y' or 'N'.")

        print(row_state(M, 1))
        print(col_state(M, 1))

        print(M)
