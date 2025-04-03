import tkinter as tk
from PIL import Image, ImageTk

class DashboardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configuração da janela
        self.title("Bem vindo ao clube do livro")
        self.geometry("800x500")
        self.configure(bg="#F4f4f4")
        self.iconbitmap("atividade2_tkinter/img/icon.ico")  # Define um ícone para a janela

        # Criando frames para o menu Lateral (Sidebar)
        self.sidebar = tk.Frame(self, bg="Linen", width=200, height=500)
        self.sidebar.pack(side="left", fill="y")

        # Criando um frame para o conteúdo principal
        self.content_frame = tk.Frame(self, bg="GhostWhite", width=600, height=500)
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Criando o título do menu lateral
        self.logo = tk.Label(self.sidebar, text="DASHBOARD", bg="#333", fg="white", font=("arial", 18, "bold"))
        self.logo.pack(pady=20)

        # Carregando imagens para os botões do menu
        self.img_dashboard = ImageTk.PhotoImage(Image.open("atividade2_tkinter/img/dashboard1.png").resize((32, 32)))
        self.img_Biblioteca = ImageTk.PhotoImage(Image.open("atividade2_tkinter/img/Biblioteca.png").resize((32, 32)))
        self.img_configuracoes = ImageTk.PhotoImage(Image.open("atividade2_tkinter/img/configuracoes.png").resize((32, 32)))
        self.img_sair = ImageTk.PhotoImage(Image.open("atividade2_tkinter/img/sair.png").resize((32, 32)))

        # Criando botões do Menu Lateral com Ícones
        self.create_sidebar_botao("Dashboard", self.img_dashboard, self.mostrar_dashboard)
        self.create_sidebar_botao("Biblioteca", self.img_Biblioteca, self.mostrar_Biblioteca)
        self.create_sidebar_botao("Configurações", self.img_configuracoes, self.mostrar_configuracoes)
        self.create_sidebar_botao("Sair", self.img_sair, self.mostrar_sair)
        self.mostrar_dashboard()  # Exibe o dashboard inicial ao abrir o programa

    def create_sidebar_botao(self, text, image, comand):
        # Cria um botão estilizado no menu lateral
        btn = tk.Button(
            self.sidebar, text=text, image=image, compound="left", bg="#555", fg="white", font=("Arial", 12),
            anchor="w", command=comand, bd=0, padx=10)
        btn.pack(fill="x", pady=5)

    def limpar_tela(self):
        # Remove todos os widgets da área de conteúdo antes de exibir outra tela
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def mostrar_dashboard(self):
        # Exibe o widget do dashboard
        self.limpar_tela()
        titulo = tk.Label(self.content_frame, text="Dashboard", font=("Georgia", 16, "bold"), bg="white")
        titulo.pack(pady=20)

        # Criando um Frame para armazenar os cards informativos
        card_frame = tk.Frame(self.content_frame, bg="white")
        card_frame.pack()
        self.criar_card(card_frame, "Seja Bem-vindo ao Clube do Livro", "Onde você encontra variedades de livros!", "#3498db")

    def criar_card(self, parent, titulo, valor, cor):
        # Cria um card de informações colorido
        card = tk.Frame(parent, bg=cor, width=150, height=100, padx=20, pady=30)
        card.pack(side="left", padx=10, pady=10)
        tk.Label(card, text=titulo, font=("Arial", 12, "bold"), bg=cor, fg="white").pack()
        tk.Label(card, text=valor, font=("Arial", 16), bg=cor, fg="white").pack()

    def mostrar_Biblioteca(self):
        # Exibe a área de Biblioteca
        self.limpar_tela()
        titulo = tk.Label(self.content_frame, text="Biblioteca", font=("Arial", 16, "bold"), bg="white")
        titulo.pack(pady=30)

        card_frame = tk.Frame(self.content_frame, bg="white")
        card_frame.pack()

        self.botaob = tk.Button(card_frame, text="Fictícios", font=("Arial", 15, "bold"), bg="LightSkyBlue")
        self.aventura = tk.Button(card_frame, text="Aventura", font=("Arial", 15, "bold"), bg="LightSkyBlue")
        self.Romance = tk.Button(card_frame, text="Romance", font=("Arial", 15, "bold"), bg="LightSkyBlue")
        self.acao = tk.Button(card_frame, text="Ação", font=("Arial", 15, "bold"), bg="LightSkyBlue")
        self.infantis = tk.Button(card_frame, text="Infantis", font=("Arial", 15, "bold"), bg="LightSkyBlue")
        self.MS = tk.Button(card_frame, text="Mistério/Suspense", font=("Arial", 15, "bold"), bg="LightSkyBlue")
        self.comedia = tk.Button(card_frame, text="Comédia", font=("Arial", 15, "bold"), bg="LightSkyBlue")

        self.botaob.pack()
        self.aventura.pack()
        self.Romance.pack()
        self.acao.pack()
        self.infantis.pack()
        self.MS.pack()
        self.comedia.pack()

    def mostrar_configuracoes(self):
        # Exibe a área de configurações
        self.limpar_tela()
        titulo = tk.Label(self.content_frame, text="Configurações", font=("Arial", 12, "bold"), bg="white")
        titulo.pack(pady=20)

        card_frame = tk.Frame(self.content_frame, bg="white")
        card_frame.pack()
        self.criar_card(card_frame, "Você entrou nas configurações", "Aqui você pode modificar as preferências do app", "#3498db")

    def mostrar_sair(self):
        # Exibe a tela de saída
        self.limpar_tela()
        titulo = tk.Label(self.content_frame, text="Saindo...", font=("Arial", 12, "bold"), bg="white")
        titulo.pack(pady=20)
        self.quit()  # Finaliza o programa

app = DashboardApp()
app.mainloop()

