from tkinter import *
#widget.config() modificar depois de inicializado, enquanto roda.
#try/exeption


class Pilha:
    def __init__(self):
        self.itens = []

    def vazia(self):
        return self.itens == []

    def topo(self):
        return self.itens[len(self.itens)-1]

    def inserir(self, x):
        self.itens.append(x)

    def retirar(self):
        return self.itens.pop()

    def soma(self, x):
        return float(self.topo()) + x

    def sub(self, x):
        return float(self.topo()) - x

    def mult(self, x):
        return float(self.topo()) * x

    def div(self, x):
        return float(self.topo()) / x


def visor1():
    lb["text"] = lb["text"] + "1"


def visor2():
    lb["text"] = lb["text"] + "2"


def visor3():
    lb["text"] = lb["text"] + "3"


def visor4():
    lb["text"] = lb["text"] + "4"


def visor5():
    lb["text"] = lb["text"] + "5"


def visor6():
    lb["text"] = lb["text"] + "6"


def visor7():
    lb["text"] = lb["text"] + "7"


def visor8():
    lb["text"] = lb["text"] + "8"


def visor9():
    lb["text"] = lb["text"] + "9"


def visor0():
    lb["text"] = lb["text"] + "0"


def visor():
    lb["text"] = lb["text"] + "."


def limpar():
    lb["text"] = ""


janela = Tk()
janela.title("HP 12c")
janela.geometry("400x600+710+150")
janela["bg"] = "light yellow"
lb = Label(janela, bg="white", text="", relief=SUNKEN, width=13, font="Arial 33", anchor=W)
lb.place(x=27, y=10)

p = Pilha()

but1 = Button(janela, width=4, text="1", command=visor1, font="Arial 19 bold")
but1.place(x=45, y=100)
but2 = Button(janela, width=4, text="2", command=visor2, font="Arial 19 bold")
but2.place(x=125, y=100)
but3 = Button(janela, width=4, text="3", command=visor3, font="Arial 19 bold")
but3.place(x=205, y=100)
but4 = Button(janela, width=4, text="4", command=visor4, font="Arial 19 bold")
but4.place(x=45, y=180)
but5 = Button(janela, width=4, text="5", command=visor5, font="Arial 19 bold")
but5.place(x=125, y=180)
but6 = Button(janela, width=4, text="6", command=visor6, font="Arial 19 bold")
but6.place(x=205, y=180)
but7 = Button(janela, width=4, text="7", command=visor7, font="Arial 19 bold")
but7.place(x=45, y=260)
but8 = Button(janela, width=4, text="8", command=visor8, font="Arial 19 bold")
but8.place(x=125, y=260)
but9 = Button(janela, width=4, text="9", command=visor9, font="Arial 19 bold")
but9.place(x=205, y=260)
but10 = Button(janela, width=4, text="0", command=visor0, font="Arial 19 bold")
but10.place(x=125, y=340)
but11 = Button(janela, width=4, text="+", command=lambda: [lb.config(text=p.soma(float(lb["text"]))), p.retirar(), p.inserir(float(lb["text"]))], font="Arial 19 bold")
but11.place(x=285, y=100)
but12 = Button(janela, width=4, text="-", command=lambda: [lb.config(text=p.sub(float(lb["text"]))), p.retirar(), p.inserir(float(lb["text"]))], font="Arial 19 bold")
but12.place(x=285, y=180)
but13 = Button(janela, width=4, text="x", command=lambda: [lb.config(text=p.mult(float(lb["text"]))), p.retirar(), p.inserir(float(lb["text"]))], font="Arial 19 bold")
but13.place(x=285, y=260)
but14 = Button(janela, width=4, text="÷", command=lambda: [lb.config(text=p.div(float(lb["text"]))), p.retirar(), p.inserir(float(lb["text"]))], font="Arial 19 bold")
but14.place(x=285, y=340)
but15 = Button(janela, width=4, text=".", command=visor, font="Arial 19 bold")
but15.place(x=205, y=340)
but16 = Button(janela, width=4, text="Enter", command=lambda: [p.inserir(float(lb["text"])), limpar()], font="Arial 19 bold")
but16.place(x=45, y=340)


janela.mainloop()

