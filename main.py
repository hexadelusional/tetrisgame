from Grid import*
from Blocks import*

if __name__ == "__main__":

    # welcoming the user
    print('{:#^150}\n'.format(" WELCOME "))
    print('{: ^150}\n'.format(" Wanna play Tetris ?"))

    # start of the game
    ready = input('{: ^150}'.format(" -> Press [ENTER] to start a start playing ;)\n \n"))

    # asking the user if he wants to resume a saved game or if he wants to start a brand new game
    print('{: ^145}\n'.format(" -> Press [R] to resume a previously saved game !"))
    print('{: ^145}\n'.format(" OR "))
    option = input('{: ^145}\n'.format(" -> Press [N] to start a new game ! "))
    while option != "R" and option != "r" and option != "N"and option != "n":
         option = input("\n -> Error, press letter [R] to resume OR press letter [N] for a new game : ")

    if option == "R" or option == "r":  # if the user chose to resume a previous game
        path = input("\n Give the name of the file you want to load : ")  # ask the name of the file to open
        file_exists = False  # assuming the file doesn't exist
        while file_exists == False:  # while the name of the file given by the user doesn't exist
            try:  # test if the file can be open
                f = open(path + ".txt")
                file_exists = True  # if it can, the file exists
            except IOError:  # if the opening of the file returns an error (here FileNotFoundError), keep asking for a correct file name
                path = input("\n -> Error, this file doesn't exist. Give the name of the file you want to load, the one of the previous grid you played on (without the.txt) : ")
        length, score, current_grid = reloading_all_data(path)

    else:
        # asking what board shape the user wants
        current_grid = input("\n -> What board shape do you want to play on ? [Circle], [Triangle] or [Diamond] : ")
        while current_grid != "diamond" and current_grid != "triangle" and current_grid != "circle":
            current_grid = input(
                "\n -> Error, this board shape does not exist. You must write the name (in lowercase letters) of one of the board shapes proposed; [Circle] [Triangle] [Diamond] : ")

        # asking what board shape the user wants,
        current_size = input("\n -> What board size do you want to play on ? [S], [M] or [L] : ")
        while current_size != "S" and current_size != "M" and current_size != "L":
            current_size = input(
                "\n -> Error, this board size does not exist. You must write the uppercase letter of the board sizes proposed [S] for small, [M] for medium, [L] for large : ")


    if current_grid == "circle":
        grid_circle(current_size)
        current_blocks = common_blocks + circle_list
    elif current_grid == "diamond":
        grid_diamond(current_size)
        current_blocks = common_blocks + diamond_list
    else:
        grid_triangle(current_size)
        current_blocks = common_blocks + triangle_list

    # initializing the variable length
    length = 0
    if current_size == "L":
        length = 25
    elif current_size == "M":
        length = 23
    else:
        length = 21

    # initializing the score at 0
    score = 0

    # reading the grid chosen above according to its size 'current_size'
    M = read_grid(current_grid)

    # printing the current grid in the console
    print_grid(M)

    # asking which policy the user wants
    question = input("\n -> Which do you want ? [Policy 1] (you choose from all the blocks) or [Policy 2] (you choose from 3 random blocks) : ")
    while question != "1" and question != "2":
        question = input("\n -> Error, this policy does not exist. You must enter 1 for [Policy 1] or 2 for [Policy 2] : ")


# Start of while loop (while the player wants to play // while rep == "Y")
        # We select block
        # Ask for coordinates
        # Verify the position => ask for coordinates again if False
        # print & save grid
        # print the current score
        # ask the user if he wants to continue playing (rep = input("Y" = yes, "N" = No)
    answer = "Y"
    while answer == "Y":
        # showing the user the blocks he can use
        print("\n -> The available blocks are:")
        chosen_block = select_blocks(current_blocks, question)


        # saving the matrix of the grid in the file of the grid
        save_grid(current_grid, M)

        # reading and displaying the current grid
        M = read_grid(current_grid)
        print_grid(M)
        print('{: ^140}\n'.format(" SCORE = " + str(score)))

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
            answer = input("\n -> Do you wish to continue ? Y or N : ")
            while answer != "Y" and answer != "N":
                answer = input("\n -> Do you wish to continue ? Please type 'Y' or 'N' : ")

    # asking the user if he wants to save his game in a file, so that he can pick up from where he left off in the future
    wanna_save = input("\n -> Do you want to save your game to resume another time ? Y or N : ")
    while wanna_save != "Y" and wanna_save!= "N":
        wanna_save = input("\n -> Do you want to save your game to resume another time ? Please type 'Y' or 'N' : ")

    if wanna_save == "Y":
        # saving the current grid in a file named by the user
        name = input("\n -> Give the name of the file you want to save your grid in : ")
        while len(name) >= 10:
            name = input("\n -> Give the name of the file you want to save your grid in, the name cannot exceed 10 characters : ")
        backup_save(name, M, length, score)

    print("\n -> Your total score was : ", score)
