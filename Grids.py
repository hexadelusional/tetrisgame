def grid():
    answers = ["Circle","Triangle","Diamond"]
    format = int(input("What type of board do you want to play on ?"))
    file = open((format+".txt"), "r")

    
    
    
    
    
    

#Diamond grid
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

#creation of the D txt doc
D = open("diamondgrid.txt","w")

def grid_diamond():
    length = 12
    for i in range(length):
        D.write("0  " * (length - i) + "1  " * (2 * i + 1) + "0  " * (length - i) + "\n")
    for i in range(length - 2, -1, -1):
        D.write("0  " * (length - i) + "1  " * (2 * i + 1) + "0  " * (length - i) + "\n")
    D.close()
grid_diamond()

#reading the lines of the D txt
D = open("diamondgrid.txt","r")
line = D.readline()
print(line)
for elt in line:
    if elt=="1":
        print("a",end=" ")
    if elt=="0":
        print("b", end=" ")
line = D.readline()
'''  
D = open("diamondgrid.txt","r")
lines = D.readlines()
D.close()
for line in lines:
    for elt in line:
        if elt == "0":
            print(" ", end=" ")
        if elt == "1":
            print(chr(2), end=" ")
    print("\n")
'''

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







#Circle





