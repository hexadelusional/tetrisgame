def grid():
    answers = ["Circle", "Triangle", "Diamond"]
    format = int(input("What type of board do you want to play on ?"))
    file = open((format + ".txt"), "r")


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
    # reading the lines of the D txt for retranscription in ascii code
    with open("diamondgrid.txt") as d:
        for line in d:
            print(line.strip())
grid_diamond()

""" 
def grid_diamond():
    length = 12
    print("    a " + " b " + " c " + " d " + " e " + " f " + " g " + " h " + " i " + " j " + " k " + " l " + " m " + " n " + " o " + " p " + " q " + " r " + " s " + " t " + " u " + " v " + " w " + " x " + " y ")
    print(" ╔" + "═" * 77 + "╗")
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(length):
        print(alphabet[i]+"║  " +"0  " * (length - i)+ "1  " * (2 * i + 1)+ "0  " * (length - i) + "║")
    for i in range(length - 2, -1, -1):
        print(alphabet[i]+"║  " +"0  " * (length - i)+ "1  " * (2 * i + 1)+ "0  " * (length - i) + "║")
    print(" ╚" + "═" * 77 + "╝")
print(grid_diamond())
"""

#TRIANGLE GRID

#creation + filling up the triangle txt doc
T = open("trianglegrid.txt","w")

def grid_triangle():
    length = 12
    for i in range(length):
        T.write("0  " * (length - i)+ "1  " * (2 * i + 1)+"0  " * (length - i)+"\n")
    T.close()
    # reading the lines of the T txt for retranscription in ascii code
    with open("trianglegrid.txt") as t:
        for line in t:
            print(line.strip())
grid_triangle()

""" 
def grid_triangle():
    length = 12
    print("    a " +" b "+" c "+ " d "+" e "+" f "+" g "+ " h "+" i "+" j "+" k "+" l "+" m "+" n "+" o "+" p "+" q "+" r "+" s "+" t "+" u "+" v "+" w "+" x "+" y ")
    print(" ╔"+"═"*77+"╗")
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(length):
        print(alphabet[i]+"║  " + "0  " * (length - i)+ "1  " * (2 * i + 1)+"0  " * (length - i) + "║")
    print(" ╚" + "═" * 77 + "╝")
print(grid_triangle())
"""




# CIRCLE GRID
