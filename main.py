from Grid import*
from Blocks import*

if __name__ == "__main__":
    # welcoming the user
    print('{:#^150}\n'.format(" WELCOME "))
    print('{: ^150}\n'.format(" Wanna play Tetris ?"))

    # start of the game
    ready = input('{: ^150}'.format(" Press [ENTER] to start playing ;) "))

    # asking what board shape the user wants
    current_grid = input("\n -> What board shape do you want to play on ? [Circle], [Triangle] or [Diamond] : " )
    while current_grid != "diamond" and current_grid != "triangle" and current_grid != "circle":
         current_grid = input("\n -> Error, this board shape does not exist. You must write the name (in lowercase letters) of one of the board shapes proposed; [Circle] [Triangle] [Diamond] : ")


    # asking what board shape the user wants,
    current_size = input("\n -> What board size do you want to play on ? [S], [M] or [L] : ")
    while current_size != "S" and current_size != "M" and current_size != "L":
         current_size = input("\n -> Error, this board size does not exist. You must write the uppercase letter of the board sizes proposed [S] for small, [M] for medium, [L] for large : ")

    grid_circle(current_size)
    grid_diamond(current_size)
    grid_triangle(current_size)

    # reading the grid chosen above according to its size 'current_size'
    M = read_grid(current_grid)

    # printing the current grid in the console
    print_grid(M)

    if current_grid == 'circle':
        current_blocks = common_blocks + circle_list
    elif current_grid == 'diamond':
        current_blocks = common_blocks + diamond_list
    else :
        current_blocks = common_blocks + triangle_list

    # asking which policy the user wants
    question = input("\n -> Which do you want ? [Policy 1] (you choose from all the blocks) or [Policy 2] (you choose from 3 random blocks) : ")
    while question != "1" and question != "2":
        question = input("\n -> Error, this policy does not exist. You must enter 1 for [Policy 1] or 2 for [Policy 2] : ")


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
    score = 0
    while answer == "Y":
        # showing the user the blocks he can use
        print("\n -> The available blocks are:")
        chosen_block = select_blocks(current_blocks, question)


        # saving the matrix of the grid in the file of the grid
        save_grid(current_grid, M)

        # reading and displaying the current grid
        M = read_grid(current_grid)
        print_grid(M)

        # printing the block the user just chosed
        print_blocks([chosen_block])

        # asking the coordinates of where the user wants to put the block
        x, y = coordinates(current_grid, length)

        # checking if the position entered by the user is valid
        # the user only gets to make 3 mistakes, after that he looses and the game stops
        mistake = 1
        while not valid_position(M, chosen_block, x, y) and mistake < 3:
            mistake += 1
            print("\n Oops, you made a mistake !")
            x, y = coordinates(current_grid, length)
        if mistake == 3:
            print("\n Oops, that was 3 mistakes... YOU LOSE !")
            answer = 'N'
        else :
            # placing the block chosen by the user onto the grid and displaying it
            M = emplace_block(M,chosen_block,x,y)
            print_grid(M)

            # checking if the rows and columns are full
            while x >= 0 :
                while row_state(M, x):
                    score += update_score(M,'row',x)
                    M = row_clear(M, x)
                    print_grid(M)
                x -= 1

            while y < len(M) :
                 while col_state(M, y):
                    score += update_score(M,'line',y)
                    M = col_clear(M, y)
                    print_grid(M)
                 y += 1

            # asking the player if they want to pursue the game or quit
            answer = input("\n Do you wish to continue ? Y or N : ")
            while answer != "Y" and answer != "N":
                answer = input("\n Do you wish to continue ? [Please type 'Y' or 'N'] : ")
    print("Your score is :", score)
