

# DIAMOND GRID

# creation + filling up the Diamond txt doc
D = open("diamondgrid.txt", "w")

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
T = open("trianglegrid.txt","w")

def grid_triangle():
    length = 12
    for i in range(length):
        T.write("0  " * (length - i)+ "1  " * (2 * i + 1)+"0  " * (length - i)+"\n")
    T.close()
grid_triangle()




# CIRCLE GRID






#function read_grid that returns a valid grid read from the contents of the file specified by path.

def read_grid():
    format = input("What board do you want to play on ? [Circle] [Triangle] [Diamond] ")
    while format != "diamond" and format != "triangle" and format != "circle":
        format = input("Error, this board does not exist. You must write the name in lowercase letters of one of the boards proposed: [Circle] [Triangle] [Diamond] ")
    if format == "diamond":
        with open("diamondgrid.txt") as d:
            for line in d:
                print(line.strip())
    if format == "triangle":
        with open("trianglegrid.txt") as t:
            for line in t:
                print(line.strip())



read_grid()
