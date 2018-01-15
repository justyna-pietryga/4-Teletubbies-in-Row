from abc import ABCMeta, abstractmethod


class StaticVariables:
    user = 1  # number of user
    wygrana = 0
    wariant = 0


def myGeneratorFromNtoZero(n):
    i = n
    while i >= 0:
        yield i
        i -= 1


class Game:
    def __init__(self, style):
        h, w = 7, 6
        self.board = [[0 for x in range(h)] for y in range(w)]
        self.war = style

    def move(self, column):

        w = len(self.board)
        h = len(self.board[0])

        row = 0
        winner = 0

        #for i in range(w - 1, -1, -1):
        for i in myGeneratorFromNtoZero(w-1):
            if self.board[i][column] == 0:
                self.board[i][column] = int(StaticVariables.user)
                row = i
                break
            else:
                pass

        if self.war.ktoWygrol(self.board):
            winner = StaticVariables.user

        elif (not self.war.ktoWygrol(self.board) and full(self.board)):
            winner = -1
            reset(self.board)

        return (row, winner)

    def getBoard(self):
        return self.board


class Rule(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def ktoWygrol(self, table):
        # raise NotImplementedError('subclasses must override ktoWygrol()!')
        pass


class EasyGame(Rule):
    def __init__(self):
        super().__init__()

    def ktoWygrol(self, table):
        if (poziomo(table, 4) or pionowo(table, 4)):
            return True
        return False


class NotEasyGame(Rule):
    def __init__(self):
        super().__init__()

    def ktoWygrol(self, table):
        if (poziomo(table, 4) or pionowo(table, 4) or ukosBackslash(table, 4) or ukosSlash(table, 4)):
            return True
        return False


class Five_In_Row(Rule):
    def __init__(self):
        super().__init__()

    def ktoWygrol(self, table):
        if (poziomo(table, 5) or pionowo(table, 5) or ukosBackslash(table, 5) or ukosSlash(table, 5)):
            return True
        return False


def reset(table):
    h, w = 7, 6
    # table = [[0 for x in range(h)] for y in range(w)]
    for i in range(w):
        for j in range(h):
            table[i][j] = 0


def full(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 0:
                return False
    return True


def poziomo(table, rule):
    w = len(table)
    h = len(table[0])
    sum = 0
    for i in range(w):
        for j in range(h):
            if table[i][j] == StaticVariables.user:
                sum += 1
            else:
                sum = 0

            if sum == rule:
                print("poziom")
                reset(table)
                return True
        sum = 0


def pionowo(table, rule):
    w = len(table)
    h = len(table[0])
    sum = 0
    for j in range(h):
        for i in range(w):
            if table[i][j] == StaticVariables.user:
                sum += 1
            else:
                sum = 0

            if sum == rule:
                print("pion")
                reset(table)
                return True
        sum = 0


def ukosSlash(table, rule):
    w = len(table)
    h = len(table[0])
    sum = 0
    for n in range(3, w):
        j = 0
        #for i in range(n, -1, -1):
        for i in myGeneratorFromNtoZero(n):
            if table[i][j] == StaticVariables.user:
                sum += 1
            else:
                sum = 0
            j += 1

            if sum == rule:
                print("slash")
                reset(table)
                return True
            if i == 0:
                sum = 0
    sum = 0

    for n in range(1, 4):
        i = w - 1
        for j in range(n, h):
            if table[i][j] == StaticVariables.user:
                sum += 1
            else:
                sum = 0
            i -= 1
            if sum == rule:
                print("slash")
                reset(table)
                return True
    return False


def ukosBackslash(table, rule):
    w = len(table)
    h = len(table[0])
    sum = 0
    for n in range(3):
        j = 0
        for i in range(n, w):
            if table[i][j] == StaticVariables.user:
                sum += 1
            else:
                sum = 0
            j += 1

            if sum == rule:
                print("backslash1")
                reset(table)
                return True
            if i == (w - 1):
                sum = 0

    sum = 0

    for n in range(1, 4):
        i = 0
        for j in range(n, h):
            if table[i][j] == StaticVariables.user:
                sum += 1
            else:
                sum = 0
            i += 1
            if sum == rule:
                print("backslash2")
                reset(table)
                return True
            if j == (h - 1):
                sum = 0

    return False
