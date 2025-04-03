from _tkinter import*
from tkinter import BooleanVar, Tk
from tkinter.ttk import*
def recuperarEstado():
    if botaoStatus.get() == True:
        valor = "sim"
    else:
        valor ="não"

    mensagem["text"]='valor:' +str(valor)

janela = Tk()
janela.configure(background="blue")
janela.geometry("300x200+200+100")
janela.title("aprendendo Tkinter")

mensagem  = Label(janela,text="Marcado:", font="arial 15 bold")
mensagem.pack()


botaoStatus = BooleanVar()
botaoStatus.set(False)
botaoMarcavel= Checkbutton(janela,text="Marque  aqui",var=botaoStatus)
botaoMarcavel.pack()

botao = Button(janela,text="clique",command=recuperarEstado)
botao.pack()
janela.mainloop()