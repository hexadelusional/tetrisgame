# DIAMOND GRID

# creation + filling up the Diamond txt doc
D = open("diamond.txt", "w")

def grid_diamond():
    length = 12
    for i in range(length):
        D.write("0  " * (length - i) + "1  " * (2 * i + 1) + "0  " * (length - i) + "\n")
    for i in range(length - 2, -1, -1):
        D.write("0  " * (length - i) + "1  " * (2 * i + 1) + "0  " * (length - i) + "\n")
    D.close()
grid_diamond()


#TRIANGLE GRID

#creation + filling up the triangle txt doc
T = open("triangle.txt","w")

def grid_triangle():
    length = 12
    for i in range(length):
        T.write("0  " * (length - i) + "1  " * (2 * i + 1) + "0  " * (length - i) + "\n")
    T.close()
grid_triangle()




# CIRCLE GRID
#creation + filling up the triangle txt doc




#transcription to ascii code of the 0's and 1's







#function read_grid that returns a valid grid read from the contents of the file specified by path
def read_grid(path):
    while path != "diamond" and path != "triangle" and path != "circle":
        path = input("Error, this board does not exist. You must write the name in lowercase letters of one of the boards proposed: [Circle] [Triangle] [Diamond] ")
    with open(path+".txt","r") as p:
        for line in p:
            print(line.strip())

read_grid(input("What board do you want to play on ? [Circle] [Triangle] [Diamond] "))

#function save_grid(path, grid)that save a grid in a file specified by path.
def save_grid(path, grid):
    with open(grid,"r") as G, open(path,"w") as P:
        lines = G.readlines()
        G.close()
        for line in lines:
            P.write(line)
        P.close()
save_grid( "game_grid.txt" , "triangle.txt")
