import tkinter as tk # Importa a biblioteca Tkinter para criar I1nterface Gráfica
from tkinter import ttk #Importa o ttk para widgets mais modernos
from PIL import Image, ImageTk #Importa o Pillow para trabalhar com imagens nos botões

class DashboardApp(tk.Tk):
    def __init__(self):
        super().__init__() # Inicializa a classe Tk
        #Configuração da Janela
        self.title("Dashboard") #Define o titulo da janela
        self.geometry("800x500") #Define o tamanho da janela
        self.configure(bg="FFB6C1") #Define a cor de fundo da janela
        self.iconbitmap("atividade_tkinter/img/icon.ico") #Define um icone para a janela

         #criando frames  para o mneu Lateral (Sidebar)
        self.sidebar = tk.Frame(self, bg="Linen", width=200, height=500)#cria o frame da  sidebar
        self.sidebar.pack(side="left", fill="y")## posiciona o sidebar a  esquerda e a estende verticalmente

        #Criando um frame para o conteudo principal
        self.content_frame = tk.Frame(self, bg="GhostWhite", width=600,height=500)#Cria o frame da area principal
        self.content_frame.pack(side="right", fill="both", expand=True)# Posicione o frame a direita, ocupando o espaço a disponivel
        
        ##criando  o titulo do menu lateral
        self.logo = tk.Label(self.sidebar,text="DASHBOARD", bg="#333", fg="white",font=("arial",18,"bold"))
        self.logo.pack(pady=20)

        ## carregando imagens para os botoes do menu 
        self.img_dashboard = ImageTk.PhotoImage(Image.open("atividade_tkinter/img/dashboard1.png").resize((32,32)))
        self.img_relatorio = ImageTk.PhotoImage(Image.open("atividade_tkinter/img/relatorio.png").resize((32,32)))
        self.img_configuracoes = ImageTk.PhotoImage(Image.open("atividade_tkinter/img/configuracoes.png").resize((32,32)))
        self.img_sair = ImageTk.PhotoImage(Image.open("atividade_tkinter/img/sair.png").resize((32,32)))

        # Criando botoes do Menu Lateral com Icones
        self.create_sidebar_botao("Dashboard", self.img_dashboard,self.mostrar_dashboard)
        self.create_sidebar_botao("Relatorio", self.img_relatorio,self.mostrar_relatorios)
        self.create_sidebar_botao("configurações", self.img_configuracoes,self.mostrar_configuracoes)
        self.create_sidebar_botao("Sair", self.img_sair,self.mostrar_sair)
        self.mostrar_dashboard() ##Exibe o dashboard inicial ao abrir o programa

    def create_sidebar_botao(self,text,image,comand):
        # Cria um botao estilizado no menu lateral
        btn= tk.Button(
        self.sidebar,text=text, image=image,compound="left",#Define o texto e coloca a imagem à esquerda
        bg="#555",fg="white", font=("Arial",12),anchor="w",#difine a cor do fundo,fontee alinhamento à esquerda
        command=comand, bd=0, padx=10 #define a ação do botão e remove a borda
        )
        btn.pack(fill="x", pady=5) # faz o botão ocupar toda a largura do menu e adiciona o espaçamento vertical

    def limpar_tela(self):
       #remove todos o widgets da area de conteudo antes de exibir outrar tela
       for widget in self.content_frame.winfo_children():
           widget.destroy() #Remove cada widget dentro do frame de conteudo 

    def mostrar_dashboard(self):
        #Exibe o widget do dashboard
        self.limpar_tela() # limpa o conteudo atual da tela
    
        #titulo da seção dashboard
        titulo =tk.Label(self.content_frame, text="dashboard", font=("Georgia", 16,"bold"), bg="white")
        titulo.pack(pady=20) # adiciona um espaçamento vertical

        # Criando um  Frame para armazenar os  cards informativos
        card_frame= tk.Frame(self.content_frame ,bg="white")
        card_frame.pack()

        ## Criando os cards com informações do sistema
        self.criar_card(card_frame, "BOM NÓS TENTAMOS!!!","#3498db") # Card de usuarios 

    def criar_card(self,parent,titulo, valor,cor):
        ##Cria um card  de informações colorido
        card= tk.Frame(parent , bg="#00BFFF", width=150, height=100, padx=10, pady=10)#define o tamanho e  a cor do card
        card.pack(side="left", padx="10", pady=10) #Posiciona os cards lado a lado com espaçamento


        #adiciona o titulo e o valor dentro do card
        tk.Label(card, text=titulo, font=("Arial",12, "bold"), bg=cor, fg="white").pack()
        tk.Label(card, text=valor, font=("Arial",16),bg=cor , fg="white").pack()

    def mostrar_relatorios(self):
        #exibe a area de Relatorios
        self.limpar_tela()#limpa o conteudo da tela antes de exibir os relatorios
        titulo =tk.Label(self.content_frame,text="Relatorios", font=("Arial",16, "bold"),bg="white")
        titulo.pack(pady=20) # adiciona um espaçamento vertical



    def mostrar_configuracoes(self):
        #exibe a area de configurações
        self.limpar_tela()# limpar o conteudo da tela antes de exibir os relatorios
        titulo = tk.Label(self.content_frame, text="Configuracões", font=("Arial",12,"bold"),bg="white")
        titulo.pack(pady=20)# adiciona um espaçamento vertical

        claudi=tk.Label(self.content_frame, text="Configuracões", font=("Arial",12,"bold"),bg="white")
        claudi.pack(pady=20)

    def mostrar_sair(self):
        self.limpar_tela()## limpar o conteudo da tela antes de exibir os relatorios
        titulo = tk.Label(self.content_frame, text="sair", font=("Arial",12,"bold"),bg="white")
        titulo.pack(pady=20)# adiciona um espaçamento vertical
        self.destroy()

