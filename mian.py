import tkinter as tk
from tkinter import font
from Calculadora import Calculadora


class CalculadoraTk:

    calc = Calculadora()
    calc.setBotoes([["%","C","BCS","/"],["7","8","9","X"],["4","5","6","-"],["1","2","3","+"],["Off","0",".","="]])
    calc.setAltura(440)
    calc.setLargura(310)


    def __init__(self):
        self.jan = tk.Tk()
        self.jan.geometry(str(self.calc.getLargura())+"x"+str(self.calc.getAltura()))
        self.jan.resizable(False,False)
        self.jan.config(bg='#202020')
        self.jan.title("Calculadora Efraim")
        

        self.f1 = tk.Frame(self.jan,bg='#202020')
        self.f2 = tk.Frame(self.jan,bg='#202020')
        

        self.display = tk.Entry(self.f1,width=18,justify="right",font=("",20))
        self.display.insert(0,"0")
        self.display.grid(row=0, column=0,pady=(30,30))

        self.gerarBotoes()

        self.f1.pack()
        self.f2.pack()
        self.jan.mainloop()

    def gerarBotoes(self):
        for linha in range(len(self.calc.getBotoes())):
            for coluna in range(len(self.calc.getBotoes()[linha])):
                texto = self.calc.getBotoes()[linha][coluna]
                btn = tk.Button(self.f2,text=texto,font=("Helvetica",12),width=5,height=2,padx=5,pady=5,bd=4)
                btn.config(background='#505050')
                btn.grid(row=linha, column=coluna,pady=(3,3),padx=(3,3))
                
CalculadoraTk()
