from logic_game import StaticVariables as sv
import logic

def poziomo(table, rule):
    w = len(table)
    h = len(table[0])
    sum = 0
    for i in range(w):
        for j in range(h):
            if table[i][j] == sv.user:
                sum += 1
            else:
                sum = 0

            if sum == rule:
                print("Gracz nr " + str(sv.user) + " wygral!")

                return True
        sum = 0


def pionowo(table,rule):
    w = len(table)
    h = len(table[0])
    sum = 0
    for j in range(h):
        for i in range(w):
            if table[i][j] == sv.user:
                sum += 1
            else:
                sum = 0

            if sum == rule:
                print("Gracz nr " + str(sv.user) + " wygral!")
                return True
        sum = 0


def ukosSlash(table,rule):
    w = len(table)
    h = len(table[0])
    sum = 0
    for n in range(3, w):
        j = 0
        for i in range(n, -1, -1):
            if table[i][j] == logic.User.user:
                sum += 1
            else:
                sum = 0
            j += 1

            if sum == rule:
                print("Gracz nr " + str(logic.User.user) + " wygral!")
                return True
    sum = 0

    for n in range(1, 4):
        i = w - 1
        for j in range(n, h):
            if table[i][j] == logic.User.user:
                sum += 1
            else:
                sum = 0
            i -= 1
            if sum == rule:
                print("Gracz nr " + str(logic.User.user) + " wygral!")
                return True
    return False


def ukosBackslash(table,rule):
    w = len(table)
    h = len(table[0])
    sum = 0
    for n in range(3):
        j = 0
        for i in range(n, w):
            if table[i][j] == logic.User.user:
                sum += 1
            else:
                sum = 0
            j += 1

            if sum == rule:
                print("Gracz nr " + str(logic.User.user) + " wygral!")
                logic.reset(table)
                return True
    sum = 0

    for n in range(1, 4):
        i = 0
        for j in range(n, h):
            if table[i][j] == logic.User.user:
                sum += 1
            else:
                sum = 0
            i += 1
            if sum == rule:
                print("Gracz nr " + str(logic.User.user) + " wygral!")
                logic.reset(table)
                return True
    return False