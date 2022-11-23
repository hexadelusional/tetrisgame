
if __name__ == "__main__":
    print("######################################### WELCOME ######################################### \n")
    # start of the game
    ready = input("-> Press [ENTER] to start playing ! ")
    while ready == " ":
        ready = input("-> Press [enter] to start playing ! ")
    from Blocks import *


    # asks which policy is to be used
    question = input("policy 1 or policy 2 ? (enter 1 or 2) ")
    while question != "1" and question != "2":
        question = input("policy 1 or policy 2 ? (you have to enter either 1 or 2) ")
    print("THESE ARE THE AVAILABLE BLOCKS: ")
    if question == "1":
        # selection of blocks following policy 1 : display at each turn of the game all the available blocks and the user selects one
        print_blocks((current_grid + ".txt"))

    elif question == "2":
        # selection of blocs following policy 2 : display only 3 randomly selected blocks
        if current_grid == "diamond":
            indice = 0
        elif current_grid == "triangle":
            indice = 1
        elif current_grid == "circle":
            indice = 2
        the_random_three = random.sample(blocks_list[indice] + common_blocks, 3)
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


