def grid():
    answers = ["Circle","Triangle","Diamond"]
    format = int(input("What type of board do you want to play on ?"))
    file = open((format+".txt"), "r")




#Diamond grid

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

#Triangle grid

def grid_triangle():
    length = 12
    print("    a " +" b "+" c "+ " d "+" e "+" f "+" g "+ " h "+" i "+" j "+" k "+" l "+" m "+" n "+" o "+" p "+" q "+" r "+" s "+" t "+" u "+" v "+" w "+" x "+" y ")
    print(" ╔"+"═"*77+"╗")
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(length):
        print(alphabet[i]+"║  " + "0  " * (length - i)+ "1  " * (2 * i + 1)+"0  " * (length - i) + "║")
    print(" ╚" + "═" * 77 + "╝")
print(grid_triangle())


#Circle grid





