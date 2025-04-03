from tkinter import*
from tkinter.ttk import*

def exibe_valor():
    mensagem['text']="opacão escolhida:" +str (escolha.get())


Window= Tk()
Window.geometry("300x200+200+100")
Window.title("Radius Button")

mensagem= Label(Window,text="Opção escolhida:Nenhuma", font="arial 20 bold" )

mensagem.pack()

escolha = StringVar()

escolha1=Radiobutton(Window, text='Primeiro', value="Primeiro", variable=escolha)
escolha2=Radiobutton(Window, text="Segundo", value="Segundo",variable=escolha)
escolhe3=Radiobutton(Window, text="terceiro" , value="terceiro",variable=escolha)
escolha4=Radiobutton(Window, text="Quarto", value="Quarto",variable=escolha)
escolha5=Radiobutton(Window, text='Quinto', value='Quinto',variable=escolha)

escolha1.pack()
escolha2.pack()
escolhe3.pack()
escolha4.pack()
escolha5.pack()

botao = Button(Window, text="clique aqui",command=exibe_valor)
botao.pack()

Window.mainloop()

