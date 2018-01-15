import os


class Game:
    def __init__(self):
        pass
    def ktoWygral(self):
        pass

class User:
    user = 1  # number of user
    wygrana=0
    wariant=0

class EasyGame(Game):
    def __init__(self):
        pass
    def ktoWygral(self, table):
        if(poziomo(table) or pionowo(table)):
            return True
        return False

class NotEasyGame(Game):
    def __init__(self):
        pass
    def ktoWygral(self, table):
        if (poziomo(table,4) or pionowo(table,4) or ukosBackslash(table,4) or ukosSlash(table,4)):
            return True
        return False

class Five_In_Row(Game):
    def __init__(self):
        pass
    def ktoWygral(self, table):
        if (poziomo(table, 5) or pionowo(table, 5) or ukosBackslash(table, 5) or ukosSlash(table, 5)):
            return True
        return False



def full(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j]==0:
                return False
    return True

def poziomo(table, rule):
    w = len(table)
    h = len(table[0])
    sum = 0
    for i in range(w):
        for j in range(h):
            if table[i][j] == User.user:
                sum += 1
            else:
                sum = 0

            if sum == rule:
                print("Gracz nr " + str(User.user) + " wygral!")

                return True
        sum = 0


def pionowo(table,rule):
    w = len(table)
    h = len(table[0])
    sum = 0
    for j in range(h):
        for i in range(w):
            if table[i][j] == User.user:
                sum += 1
            else:
                sum = 0

            if sum == rule:
                print("Gracz nr " + str(User.user) + " wygral!")
                return True
        sum = 0


def ukosSlash(table,rule):
    w = len(table)
    h = len(table[0])
    sum = 0
    for n in range(3, w):
        j = 0
        for i in range(n, -1, -1):
            if table[i][j] == User.user:
                sum += 1
            else:
                sum = 0
            j += 1

            if sum == rule:
                print("Gracz nr " + str(User.user) + " wygral!")
                return True
    sum = 0

    for n in range(1, 4):
        i = w - 1
        for j in range(n, h):
            if table[i][j] == User.user:
                sum += 1
            else:
                sum = 0
            i -= 1
            if sum == rule:
                print("Gracz nr " + str(User.user) + " wygral!")
                return True
    return False


def ukosBackslash(table,rule):
    w = len(table)
    h = len(table[0])
    sum = 0
    for n in range(3):
        j = 0
        for i in range(n, w):
            if table[i][j] == User.user:
                sum += 1
            else:
                sum = 0
            j += 1

            if sum == rule:
                print("Gracz nr " + str(User.user) + " wygral!")
                reset(table)
                return True
    sum = 0

    for n in range(1, 4):
        i = 0
        for j in range(n, h):
            if table[i][j] == User.user:
                sum += 1
            else:
                sum = 0
            i += 1
            if sum == rule:
                print("Gracz nr " + str(User.user) + " wygral!")
                reset(table)
                return True
    return False


def reset(table):
    h, w = 7, 6
    #table = [[0 for x in range(h)] for y in range(w)]
    for i in range(w):
        for j in range(h):
            table[i][j]=0

# diplay a board- temporary for tests
def display(table):
    h = len(table[0])
    w = len(table)

    for i in range(w):
        for j in range(h):
            print(str(table[i][j]) + "   ", end="")
        print('\n')
    print('\n')


def move(column, table):
    if(User.wygrana==1):
        reset(table)
        User.wygrana=0

    w = len(table)
    h = len(table[0])

    if table[0][column] != 0:
        print("Kolumna zapelniona!")
        return

    for i in range(w - 1, -1, -1):
        if table[i][column] == 0:
            table[i][column] = int(User.user)
            break
        else:
            pass

    war=NotEasyGame()

    if war.ktoWygral(table):
        User.wygrana = 1
        return
    elif(not war.ktoWygral(table) and full(table)):
        print('Remis!')
        reset(table)



    '''if (poziomo(table) or pionowo(table) or ukosSlash(table) or ukosBackslash(table)):
        User.wygrana=1
        return
    elif not(poziomo(table) or pionowo(table) or ukosSlash(table) or ukosBackslash(table)) and full(table):
        print('Remis!')
        reset(table)
        '''


    User.user = (not User.user-1)+1


''' main'''
h, w = 7, 6
board = [[0 for x in range(h)] for y in range(w)]
'''
while(True):
    h, w = 7, 6
    board = [[0 for x in range(h)] for y in range(w)]

    print("1. Normal")
    print("2. Easy")
    print("3. 5 w rzędzie")
    rule = int(input('Jaki wariant wybierasz?'))
    if (rule>0 and rule<=3):
        User.wariant=rule
        break
'''

display(board)

while (True):
    print("Runda gracza nr "+str(User.user))
    x = int(input('Which column?'))
    if(x==9):
        reset(board)
    elif(x>=0 and x<8):
        move(x, board)
        display(board)
