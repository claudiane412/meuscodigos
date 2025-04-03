import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk #Exibir imagem no tkinter
import os
from login import*
import  bcrypt
##Arquivos onde os usuarios serão salvos
ARQUIVOS_USUARIOS = "atividade_tkinter/bd/usuarios.txt"
def salvar_usuario(usuario,cpf,telefone,senha):
    hash_senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()
    with open(ARQUIVOS_USUARIOS, "a") as f:
        f.write(f"{usuario},{cpf},{telefone},{hash_senha}\n")

def verificar_usuario(nome,cpf,telefone,senha):
    if not os.path.exists(ARQUIVOS_USUARIOS):
        return False
    
    with open (ARQUIVOS_USUARIOS, "r") as f:
        for line in f:
            user, hash_pwd = line.strip().split(",")
            if user == salvar_usuario and bcrypt.checkpw(senha.encode(),hash_pwd.encode()):
                return True


    return False

class CadrastroApp(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cadastro de Usuario")
        self.geometry("600x400")
        self.configure("bg=#09EDDF")

        frame = tk.Frame(self, bg= "blue", padx=20 , relief="raised" , borderwidth=2)
        frame.place(relx=0.5, rely=0.5, ancher="center")

        try:
            image = Image.open("atividade_tkinter/img/cadastro.png")
            imagem= imagem.resize((32,32), Image.Resampling.LANCZOS)
            self.imagem_tk = ImageTk.PhotoImage(imagem)
            self.image_label = tk.Label(self, image=self.imagem_tk, bg="white")
            self.image_label.pack()
        except Exception as e:
            print(f"erro carregar imagem;{e}")
            

        tk.Label(frame , text="Novo Usuario: ", bg="SkyBlue" , fg="white").pack()
        self.usuario_entry = tk.Entry(frame)
        self.usuario_entry.pack()

        tk.Label(frame, text="Nova Senha:", bg="turquoise",fg="white").pack()
        self.senha_entry = tk.Entry(frame, show="*")
        self.senha_entry.pack()

        self.registar_botao = tk.Button(frame, text="Cadastrar", bg="00FFFF",fg="white",command=self.cadastrar)
        self.registar_botao.pack()

        self.voltar_botao = tk.Button(frame, text="voltar", bg="#FF0000",fg="white", command=self.voltar)
        self.voltar_botao.pack()

def cadastrar(self):
    usuario= self.usuario_entry.get()
    senha= self.senha_entry.get()
    cpf = self.cpf_entry.get()
    telefone = self.telefone_entry.get()
    if usuario and senha:
        salvar_usuario(usuario,cpf,telefone,senha)
        messagebox.showinfo("Sucesso","Usuário cadastrado com sucesso.")
    else:
        messagebox.showerror("Erro","Preencha todos os campos!")

def voltar(self):
    self.destroy()# fecha a janela de cadastro
    self.master.deiconify() #mostra a tela de login



