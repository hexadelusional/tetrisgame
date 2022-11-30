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

    # initializing current_blocks: the blocks that the user is allowed to use according to the grid
    if current_grid == "diamond":
        current_blocks = common_blocks + diamond_list
    elif current_grid == "triangle":
        current_blocks = common_blocks + triangle_list
    else:
        current_blocks = common_blocks + diamond_list

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
    M=print_grid(current_grid)

    # printing the blocks that the user can use according to the grid he chose
    print_blocks((current_grid + ".txt"))

    # asking which policy the user wants
    question = input("policy 1 or policy 2 ? (enter 1 or 2) ")
    while question != "1" and question != "2":
        question = input("policy 1 or policy 2 ? (you have to enter either 1 for policy one, or 2 for policy 2)")
    print("THESE ARE THE AVAILABLE BLOCKS: ")


    if question == "1": # selection of blocks following policy 1 (to display at each turn of the game all the available blocks and the user selects one)
        print_blocks((current_grid + ".txt"))

    elif question == "2": # selection of blocks following policy 2 (to display only 3 randomly selected blocks)

        # choosing 3 random blocks that correspond  to the chosen grid using the 'index'
        the_random_three = random.sample(current_blocks, 3)

        # printing the 3 random blocks
        print("RANDOM BLOC PIC: ")
        for i in range(len(the_random_three)):
            for j in range(len(the_random_three[i])):
                for k in range(len(the_random_three[i][j])):
                    if the_random_three[i][j][k] == 0:
                        print(chr(10240), end="  ")
                    elif the_random_three[i][j][k] == 1:
                        print(chr(9632), end="  ")
                print("\n".strip())
            print("_")



    # checking if the coordinates entered are admissible according to the size of the grid
    if current_size == "L":
        length = 25
    elif current_size == "M":
        length = 23
    else:
        length = 21

    x = str(input("Enter the x coordinates: "))
    while x < chr(97) or x > (chr(97 + length - 1)) or len(x) != 1:
        x = str(input(
            "Enter the x coordinates (you must enter the letter (in lowercase) corresponding to the column you want): "))

    y = str(input("Enter the y coordinates: "))
    while (y < chr(65) or y > (chr(65 + length - 1)) or len(y) != 1):
        y = str(input(
            "Enter the y coordinates (you must enter the letter (in uppercase) corresponding to the row you want): "))
