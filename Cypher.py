while True:
    while True:
        list = []
        secondList = []
        thirdList = []
        fourthList = []
        a = input("Type here:")
        test = input("Is "+ a +" correct? y or n:")
        if (test =='Y' or test =='y' or test =='yes' or test =='Yes'):
            break
        else:
            if (test =='N' or test =='n' or test =='no' or test =='No'): 
                print ("Try again")
            else:
                print ("Unknown cypher, try again") 
    while True:
        p = input("Cypher amount, positive to Encrypt, negitive to Dycrypt:")
        if (p =='1' or p =='2' or p =='3' or p =='4' or p =='5' or p =='6' or p =='7' or p =='8' or p =='9' or p =='10' or p =='11' or p =='12' or p =='13' or p =='14' or p =='15' or p =='16' or p =='17' or p =='18' or p =='19' or p =='20' or p =='21' or p =='22' or p =='23' or p =='24' or p =='25' or p =='26' or p =='-1' or p =='-2' or p =='-3' or p =='-4' or p =='-5' or p =='-6' or p =='-7' or p =='-8' or p =='-9' or p =='-10' or p =='-11' or p =='-12' or p =='-13' or p =='-14' or p =='-15' or p =='-16' or p =='-17' or p =='-18' or p =='-19' or p =='-10' or p =='-21' or p =='-22' or p =='-23' or p =='-24' or p =='-25' or p =='-26'):
            print ("Number accepted")
            testp = input("Is "+ p +" correct? y or n:")
            if (testp =='Y' or testp =='y' or testp =='yes' or testp =='Yes'):
                if int(p) <= -1:
                    print ("Dycrypt mode")
                    p = int(p) + 26
                    break
                else:
                    if int(p) >= 0:
                        print ("Encrypt Mode")
                        break
            else:
                if (testp =='N' or testp =='n' or testp =='no' or testp =='No'): 
                    print ("Try again")
                else:
                    print ("Unknown cypher amount, try again") 
        else:
            print ("Number error, Make sure number is between -26 and 26")
    for char in a:
        list.append(char)
    for e in list:
            if e == " ":
                secondList.append(e)
            else:
                l = ord(e) - 96
                secondList.append(l)
    for f in secondList:
        print (f)
    for g in secondList:
        if g == " ":
            thirdList.append(g)
        else:
            h = int(g) + int(p)
            print (h)
            thirdList.append(h)
    for y in thirdList:
        if y == " ":
            print (" ")
            fourthList.append(" ")
        else:
            if y >= 27:
                    y = y - 26
            if y == int(1):
                print ("a")
                fourthList.append("a")
            if y == int(2):
                print ("b")
                fourthList.append("b")
            if y == int(3):
                print ("c")
                fourthList.append("c")
            if y == int(4):
                print ("d")
                fourthList.append("d")
            if y == int(5):
                print ("e")
                fourthList.append("e")
            if y == int(6):
                print ("f")
                fourthList.append("f")
            if y == int(7):
                print ("g")
                fourthList.append("g")
            if y == int(8):
                print ("h")
                fourthList.append("h")
            if y == int(9):
                print ("i")
                fourthList.append("i")
            if y == int(10):
                print ("j")
                fourthList.append("j")
            if y == int(11):
                print ("k")
                fourthList.append("k")
            if y == int(12):
                print ("l")
                fourthList.append("l")
            if y == int(13):
                print ("m")
                fourthList.append("m")
            if y == int(14):
                print ("n")
                fourthList.append("n")
            if y == int(15):
                print ("o")
                fourthList.append("o")
            if y == int(16):
                print ("p")
                fourthList.append("p")
            if y == int(17):
                print ("q")
                fourthList.append("q")
            if y == int(18):
                print ("r")
                fourthList.append("r")
            if y == int(19):
                print ("s")
                fourthList.append("s")
            if y == int(20):
                print ("t")
                fourthList.append("t")
            if y == int(21):
                print ("u")
                fourthList.append("u")
            if y == int(22):
                print ("v")
                fourthList.append("v")
            if y == int(23):
                print ("w")
                fourthList.append("w")
            if y == int(24):
                print ("x")
                fourthList.append("x")
            if y == int(25):
                print ("y")
                fourthList.append("y")
            if y == int(26):
                print ("z")
                fourthList.append("z")
            if y == int(-61):
                print (" ")
                fourthList.append("_")
    listToStr = ''.join([str(elem) for elem in fourthList])
    print(listToStr) 