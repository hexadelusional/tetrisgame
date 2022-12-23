# MAIN   -  Tetris Puzzle  -  Adele Chamoux and Iriantsoa Rasoloarivalona

# The role of this file is to interrogate the user and call all the functions present in the other files

from Grid import *
from Blocks import *

if __name__ == "__main__":

    # welcoming the user
    print('\n╒{:═^150}╕\n'.format(" WELCOME "))
    print('{:^150}\n'.format(" Wanna play Tetris ?"))

    # start of the game
    ready = input('{:^150}'.format(" Press [ENTER] to start playing ;)"))
    print("\n")
    # asking the user if he wants to resume a saved game or if he wants to start a brand-new game
    print('\n{:^150}\n'.format(" ⇒ Press 'R' to resume a previously saved game ! "))
    print('{:^150}\n'.format(" OR "))
    option = input('{:^150}'.format("⇒ Press 'N' to start a new game ! "))
    while option != "R" and option != "r" and option != "N" and option != "n":
        option = input('\n{: ^150}'.format("⇒ Error, press letter 'R' to resume OR press letter 'N' for a new game : "))

    if option == "R" or option == "r":  # if the user chose to resume a previous game
        new_name = input("\n⇒ Give the name of the file you want to load : ")  # ask the name of the file to open
        file_exists = False  # assuming the file doesn't exist
        while not file_exists:  # while the name of the file given by the user doesn't exist
            try:  # test if the file can be open
                f = open(new_name + ".txt")
                file_exists = True  # if it can, the file exists
            # if the opening of the file returns an error (here FileNotFoundError), keep asking for a correct file name
            except IOError:
                new_name = input(
                    "⇒ Error, this file doesn't exist. Give the name of the file you want to load, the one of the "
                    "previous grid you played on (without the.txt) : ")
        length, score, current_grid = reloading_all_data(new_name)

    else:
        print('\n╞{:═^150}╡\n'.format(" BEWARE... THE GAME HAS STARTED ! "))
        # asking what board shape the user wants
        current_grid = input("⇒ What board shape do you want to play on ? "
                             " Enter 'C' for [Circle], 'T' for [Triangle], or 'D' [Diamond] : \n")
        while current_grid != "D" and current_grid != "T" and current_grid != "C":
            current_grid = input(
                "⇒ Error, this board shape does not exist. Write the uppercase letter of the board shape"
                " you want 'C' for [Circle], 'T' for [Triangle], 'D' for [Diamond] : \n")

        # asking what board shape the user wants,
        current_size = input("⇒  What board size do you want to play on ? Enter 'S' for [Small], 'M' for [Medium], "
                             "or 'L' for [Large] : \n")
        while current_size != "S" and current_size != "M" and current_size != "L":
            current_size = input("⇒ Error, this board size does not exist. Write the uppercase letter of "
                                 "the board size you want 'S' for [Small], 'M' for [Medium], 'L' for [Large] : \n")

        if current_grid == "C":
            grid_circle(current_size)
        elif current_grid == "D":
            grid_diamond(current_size)
        else:
            grid_triangle(current_size)

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

    if current_grid == 'C':
        current_blocks = common_blocks + circle_list
    elif current_grid == 'D':
        current_blocks = common_blocks + diamond_list
    else:
        current_blocks = common_blocks + triangle_list

    # asking which policy the user wants
    question = input("⇒ Choose : [Policy 1] (playing with all the blocks) or [Policy 2] "
                     "(playing with 3 random blocks) : \n")
    while question != "1" and question != "2":
        question = input("⇒ Error, this policy does not exist. You must enter 1 for [Policy 1] or 2 for "
                         "[Policy 2] : \n")

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
        print('\n{:^113}'.format(" THE AVAILABLE BLOCKS ARE: "))
        chosen_block = select_blocks(current_blocks, question)

        # saving the matrix of the grid in the file of the grid
        save_grid(current_grid, M)

        # reading and displaying the current grid
        M = read_grid(current_grid)
        print_grid(M)
        print('{: ^140}\n'.format(" SCORE = " + str(score)))

        # printing the block the user just chose
        print_blocks([chosen_block])

        # asking if the user wants to rotate the block
        rotation = input("⇒ Do you want to rotate the block before placing it ? 'Y' or 'N'\n")
        while rotation != "Y" and rotation != "N":
            rotation = input("⇒ Do you want to rotate the block before placing it ? Enter 'Y' or 'N'\n")

        while rotation == 'Y':
            direction = input("⇒ 'L' [left] or 'R' [right] ? : ")
            while direction != 'L' and direction != 'R':
                direction = input("⇒ 'L' [left] or 'R' [right] ? : ")
            if direction == 'L' \
                    :
                chosen_block = rotate(chosen_block, False)
            else:
                chosen_block = rotate(chosen_block, True)
            print_blocks([chosen_block])
            rotation = input("⇒ Do you want to rotate the block again before placing it ? 'Y' or 'N'\n")
            while rotation != "Y" and rotation != "N":
                rotation = input("⇒ Do you want to rotate the block before placing it ? Enter 'Y' or 'N'\n")
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
        else:
            # placing the block chosen by the user onto the grid and displaying it
            M = emplace_block(M, chosen_block, x, y)
            print_grid(M)
            print('{: ^140}\n'.format(" SCORE = " + str(score)))
            # checking if the rows and columns are full
            while x >= 0:
                while row_state(M, x):
                    score += update_score(M, 'row', x)
                    M = row_clear(M, x)
                    print_grid(M)
                    print('{: ^140}\n'.format(" SCORE = " + str(score)))
                x -= 1

            while y < len(M):
                while col_state(M, y):
                    score += update_score(M, 'line', y)
                    M = col_clear(M, y)
                    print_grid(M)
                    print('{: ^140}\n'.format(" SCORE = " + str(score)))
                y += 1

            # asking the player if they want to pursue the game or quit
            answer = input("⇒  Do you wish to continue ? Y or N : \n")
            while answer != "Y" and answer != "N":
                answer = input("⇒  Do you wish to continue ? Please type 'Y' or 'N' : \n")

    # asking the user if he wants to save his game in a file
    wanna_save = input("⇒  Do you want to save your game to resume another time ? Y or N : \n")
    while wanna_save != "Y" and wanna_save != "N":
        wanna_save = input(" ⇒ Do you want to save your game to resume another time ? Please type 'Y' or 'N' : \n")

    if wanna_save == "Y":
        # saving the current grid in a file named by the user
        name = input("⇒  Give the name of the file you want to save your grid in : \n")
        while len(name) >= 10:
            name = input(
                "⇒  Give the name of the file you want to save your grid in, it cannot exceed 10 characters : \n")
        backup_save(name, M, length, current_grid, score)

    print('╞{:═^150}╡'.format(""))
    print('\n{:^150}'.format("Your total score was : " + str(score)))
    print('\n{:^150}'.format("See you soon ! ;)"))
    print('\n╘{:═^150}╛\n'.format(""))

    print('\n\n\n{:^150}'.format("╒═════════════════════════════════════════════╕"))
    print('{:^150}'.format("╎                   CREDITS                   ╎"))
    print('{:^150}'.format("╎                                             ╎"))
    print('{:^150}'.format("╎  Adèle Chamoux & Iriantsoa Rasoloarivalona  ╎"))
    print('{:^150}'.format("╎                                             ╎"))
    print('{:^150}'.format("╘═════════════════════════════════════════════╛"))
