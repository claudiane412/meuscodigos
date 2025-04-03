from tkinter import*# importando o pacote TKINTER
from tkinter.ttk import*

#def  aoClicar():
#    mensagem["text"] = "texto:  " + entrada.get()

def mostrar_biblioteca():
    mensagem['text'] = "Livros:" +combo.get()

janela = Tk()#instanciamos a classe tk
 #janela.geometry("800x600")#modificar tamanho da janela
 #janela.geometry("800x600+100+50")#modificar tamanho da janela margem esquerda+margem topo
 #janela.attributes("-fullscreen",True)#tela cheia

janela.title("Nossa primeira janela")# Definindo o titulo da janela
#criando ComboBox
combo= Combobox(janela)
combo['values'] = ("terror","mistério","Livros ficticios","Aventura","Romance","Drama")
combo.current(0)#definindo o valor a ser exibido
combo.pack()
#criando Botão
botao= Button(janela, text='Clique aqui',command=mostrar_biblioteca)
botao.pack()#adicionamos o widget  a janela


#entrada de informações
#entrada = Entry(janela,font="arial 15 bold",state="disabled")
#entrada.pack()

#fonte => nome da fonta,tamanho da fonte,efeito da fonte
mensagem = Label(janela, text="Bem vindoa a nossa biblioteca escolha uma opção para encontar seu livro!!!",font="impact 15 bold") #widget e texto que guarda a label
#alterando o texto
#texto["text"] = "este texto será exibido"
mensagem.pack()#adicionamos o widget a janela 





#entrada.focus()#focar o cursor

janela.mainloop()#Permanece aberta enquanto o mainlop estiver ativo

