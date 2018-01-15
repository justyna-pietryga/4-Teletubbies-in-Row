try:
    # Python2
    from Tkinter import *
    from Tkinter import ttk
    from Tkinter import messagebox
except ImportError:
    # Python3
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox

import logic_game
import threading
import pygame as pg


class UserInterface:
    def __init__(self):
        root = Tk()

        def on_closing():
            self.wlaczMuz("Track1.mp3", False)
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_closing)

        root.title("4 Teletubbies in roł!")
        # root.geometry('{}x{}'.format(323, 350))

        root.iconbitmap('ICON.ico')

        root.resizable(width=False, height=False)
        wr = 323
        # hr=350
        hr = 375
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (wr / 2)
        y = (hs / 2) - (hr / 2)
        root.geometry('%dx%d+%d+%d' % (wr, hr, x, y))

        self.style = [logic_game.EasyGame(), logic_game.NotEasyGame(), logic_game.Five_In_Row()]
        self.game = logic_game.Game(self.style[1])

        # winsound.PlaySound("telletubies.wav", winsound.SND_ASYNC)
        self.player = False
        thread = threading.Thread(target=self.wlaczMuz("telletubies.wav", True))
        thread.start()

        labelFrame = Frame(root)
        buttonFrame = Frame(root)
        canvasFrame = Frame(root)
        bottomFrame = Frame(root)
        binFrame = Frame(root)

        labelFrame.grid(column=0, row=0, sticky=(N, W))
        buttonFrame.grid(column=0, row=1, sticky=W)
        canvasFrame.grid(column=0, row=2)
        bottomFrame.grid(column=0, row=3, sticky=W)
        binFrame.grid(column=0, row=4, sticky=W)

        Label(labelFrame, text="Tura gracza:").grid(row=0, column=0)
        self.currentPlayer = 1
        self.turnLabel = Label(labelFrame, text=self.currentPlayer)
        self.turnLabel.grid(row=0, column=1)

        w, h = 7, 6
        self.matrix = [[0 for x in range(w)] for y in range(h)]
        self.matrix2 = [0 for x in range(w)]

        for i in range(7):
            self.matrix2[i] = ttk.Button(buttonFrame, text="Wrzuć", command=lambda nr=i: self.onClick(nr), width=6)
            self.matrix2[i].grid(column=i, row=0)

        self.canvas = Canvas(canvasFrame, width=400, height=275)
        self.canvas.grid(row=1, column=0)

        self.redImage = PhotoImage(file='yellow2.gif')
        self.yellowImage = PhotoImage(file='red2.gif')
        self.whiteImage = PhotoImage(file='white.gif')

        for i in range(6):
            for j in range(7):
                self.matrix[i][j] = self.canvas.create_image(23 + 46 * j, 23 + 46 * i, image=self.whiteImage)

        ttk.Button(bottomFrame, text="Wyczyść planszę", command=lambda: self.newGame(self.combo.current())).grid(
            column=0, row=0)
        Label(bottomFrame, text="Zestaw reguł:").grid(row=0, column=1)
        self.combo = ttk.Combobox(bottomFrame, values=("Easy", "Normal", "5 w rzędzie"))
        self.combo.grid(row=0, column=2)
        self.combo.current(1)
        self.combo.bind("<<ComboboxSelected>>", self.Foo)

        ttk.Button(binFrame, text="Wyłącz/włącz muzykę", command=lambda: self.wycisz()).grid(column=0, row=0)

        instructionText = self.instructionString("instruction.txt")
        messagebox.showinfo("Instrukcja", instructionText)

        root.mainloop()

    def Foo(self, event):
        # self.game.setWar(self.combo.current())
        self.newGame(self.combo.current())

    def newGame(self, nr):
        self.game = logic_game.Game(self.style[nr])

        for i in range(7):
            self.matrix2[i]["state"] = "enabled"
        for i in range(6):
            for j in range(7):
                self.canvas.itemconfig(self.matrix[i][j], image=self.whiteImage)

    def onClick(self, nr):
        move_info = self.game.move(nr)
        if logic_game.StaticVariables.user == 1:
            self.canvas.itemconfig(self.matrix[move_info[0]][nr], image=self.redImage)
        else:
            self.canvas.itemconfig(self.matrix[move_info[0]][nr], image=self.yellowImage)

        if move_info[1] != 0 and move_info[1] != -1:
            messagebox.showinfo("Wygrana", "Teletubiś nr " + str(logic_game.StaticVariables.user) + " wygrał!")
            self.newGame(self.combo.current())
        elif move_info[1] == -1:
            messagebox.showinfo("Remis", "Remis! :(")
            self.newGame(self.combo.current())

        logic_game.StaticVariables.user = (not (logic_game.StaticVariables.user - 1)) + 1
        self.turnLabel['text'] = logic_game.StaticVariables.user

        if self.game.getBoard()[0][nr] != 0:
            self.matrix2[nr]["state"] = "disabled"

    def instructionString(self, file):

        try:
            with open(file, 'r') as myfile:
                data = myfile.read()
        except IOError:
            print("File " + file + " not found!")
            return

        return data

    def wycisz(self):
        if self.player:
            pg.mixer.music.stop()
            self.player = False
        else:
            self.wlaczMuz("telletubies.wav", True)
            # pg.mixer.music.play(loops=-1)
            self.player = True

    def wlaczMuz(self, name, loop):

        pg.mixer.init()
        # pg.mixer.music.set_volume(5)
        try:
            pg.mixer.music.load(name)
        except pg.error:
            print("File " + name + " not found!")
            return

        if (loop):
            pg.mixer.music.play(loops=-1)
            self.player = True
        else:
            pg.mixer.music.play()
            self.player = False


def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
