def tictactoe():
    lst1 = [" 0 ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 "]
    lst = ["   ", "   ", "   ", "   ", "   ", "  ", "   ", "   ", "  "]
    res1 = lst1[:3]
    res2 = lst1[3:6]
    res3 = lst1[6:9]
    for j, item in enumerate(res1):
        if j == 2:
            print(item)
        else:
            print(item, end = "|")
#print("")
    print("---+---+---")
    for a, item in enumerate(res2):
        if a == 2:
            print(item)
        else:
            print(item, end = "|")
#print("")
    print("---+---+---")
    for d, item in enumerate(res3):
        if d == 2:
            print(item)
        else:
            print(item, end = "|")
    print("")
    print("")
    lst2 = []
    for i in range(9):
        if i % 2 == 0:
            y = abs(int(input("player 1   ")))
            while y in lst2 or y >= 9:
                print("")
                print("pick another field")
                print("")
                y = abs(int(input("player 1   ")))
                continue
            lst[y] = " X "
            lst2.append(y)
        else:
            o = abs(int(input("player 2   ")))
            while o in lst2 or o >= 9:
                print("")
                print("pick another field")
                print("")
                o = abs(int(input("player 2   ")))
                continue
            lst[o] = " O "
            lst2.append(o)
        res1 = lst[:3]
        res2 = lst[3:6]
        res3 = lst[6:9]
        print("")
        for j, item in enumerate(res1):
            if j == 2:
                print(item)
            else:
                print(item, end = "|")
#print("")
        print("---+---+---")
        for a, item in enumerate(res2):
            if a == 2:
                print(item)
            else:
                print(item, end = "|")
#print("")
        print("---+---+---")
        for d, item in enumerate(res3):
            if d == 2:
                print(item)
            else:
                print(item, end = "|")
        print("")
        #print("")
        if (res1[0] == res1[1] == res1[2] == " X " or
            res2[0] == res2[1] == res2[2] == " X " or
            res3[0] == res3[1] == res3[2] == " X " or
            res1[0] == res2[0] == res3[0] == " X " or
            res1[1] == res2[1] == res3[1] == " X " or
            res1[2] == res2[2] == res3[2] == " X " or
            res1[0] == res2[1] == res3[2] == " X " or
            res1[2] == res2[1] == res3[0] == " X "):
            print("player1 is the winner")
            break
        elif (res1[0] == res1[1] == res1[2] == " O " or
            res2[0] == res2[1] == res2[2] == " O " or
            res1[0] == res2[0] == res3[0] == " O " or
            res1[1] == res2[1] == res3[1] == " O " or
            res1[2] == res2[2] == res3[2] == " O " or
            res3[0] == res3[1] == res3[2] == " O " or
            res1[0] == res2[1] == res3[2] == " O " or
            res1[2] == res2[1] == res3[0] == " O "):
            print("player2 is the winner")
            break
    else:
        print("The game is a draw.")
tictactoe()

