import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from tkinterweb import HtmlFrame
from PIL import Image, ImageTk
import webbrowser

class EmuladorCelular:
    def __init__(self, root):
        self.root = root
        self.root.title("Emulador de Celular Avançado")
        self.root.geometry("350x600")
        self.root.configure(bg="black")

        # Criar área da tela do celular
        self.tela = tk.Frame(root, bg="white", width=300, height=500)
        self.tela.pack(pady=20, padx=10)

        # Barra de status
        self.barra_status = tk.Frame(self.tela, bg="gray", height=25)
        self.barra_status.pack(fill="x", side="top")
        self.status_texto = tk.Label(self.barra_status, text="🔋 100%   📶 Wi-Fi", font=("Arial", 10), fg="white", bg="gray")
        self.status_texto.pack(side="right", padx=10)

        # Área da tela principal (grade de apps)
        self.area_apps = tk.Frame(self.tela, bg="white")
        self.area_apps.pack(expand=True, fill="both")

        # Lista de aplicativos instalados (pré-carregados)
        self.apps_instalados = {
            "Navegador": self.abrir_navegador,
            "Loja de Apps": self.abrir_loja
        }

        self.carregar_apps()

        # Botão de menu (estilo Home Button)
        self.botao_home = tk.Button(root, text="🔙 Home", font=("Arial", 14), command=self.carregar_apps)
        self.botao_home.pack(pady=10)

    def carregar_apps(self):
        """Recarrega a tela principal com os apps instalados."""
        for widget in self.area_apps.winfo_children():
            widget.destroy()

        for nome, funcao in self.apps_instalados.items():
            botao_app = tk.Button(self.area_apps, text=nome, width=15, height=2, bg="lightgray",
                                  command=funcao, font=("Arial", 12))
            botao_app.pack(pady=5)

    def abrir_navegador(self):
        """Abre um navegador simples dentro do emulador."""
        self.limpar_tela()
        self.status_texto.config(text="🌐 Navegador Online")

        self.web_frame = HtmlFrame(self.tela)
        self.web_frame.pack(expand=True, fill="both")

        url = simpledialog.askstring("Navegador", "Digite um URL (ex: https://google.com):")
        if url:
            if not url.startswith("http"):
                url = "https://" + url
            self.web_frame.load_website(url)

        botao_voltar = tk.Button(self.tela, text="🔙 Voltar", command=self.carregar_apps)
        botao_voltar.pack(pady=10)

    def abrir_loja(self):
        """Abre a loja de aplicativos fictícia."""
        self.limpar_tela()
        self.status_texto.config(text="🛒 Loja de Aplicativos")

        label = tk.Label(self.tela, text="Escolha um app para instalar:", font=("Arial", 12))
        label.pack(pady=10)

        # Apps disponíveis para download
        apps_disponiveis = {
            "Calculadora": self.app_calculadora,
            "Bloco de Notas": self.app_notas
        }

        for nome, funcao in apps_disponiveis.items():
            botao_instalar = tk.Button(self.tela, text=f"📲 Instalar {nome}", command=lambda n=nome, f=funcao: self.instalar_app(n, f))
            botao_instalar.pack(pady=5)

        botao_voltar = tk.Button(self.tela, text="🔙 Voltar", command=self.carregar_apps)
        botao_voltar.pack(pady=10)

    def instalar_app(self, nome, funcao):
        """Simula a instalação de um novo app."""
        if nome not in self.apps_instalados:
            self.apps_instalados[nome] = funcao
            messagebox.showinfo("Instalação", f"{nome} foi instalado com sucesso!")
        self.carregar_apps()

    def app_calculadora(self):
        """Abre uma calculadora simples."""
        self.limpar_tela()
        self.status_texto.config(text="🧮 Calculadora")

        entrada = tk.Entry(self.tela, font=("Arial", 16), width=15)
        entrada.pack(pady=10)

        def calcular():
            try:
                resultado = eval(entrada.get())
                messagebox.showinfo("Resultado", f"Resultado: {resultado}")
            except:
                messagebox.showerror("Erro", "Expressão inválida")

        botao_calcular = tk.Button(self.tela, text="Calcular", command=calcular)
        botao_calcular.pack(pady=10)

        botao_voltar = tk.Button(self.tela, text="🔙 Voltar", command=self.carregar_apps)
        botao_voltar.pack(pady=10)

    def app_notas(self):
        """Abre um bloco de notas simples."""
        self.limpar_tela()
        self.status_texto.config(text="📝 Bloco de Notas")

        texto = tk.Text(self.tela, font=("Arial", 12), height=15, width=30)
        texto.pack(pady=10)

        def salvar():
            conteudo = texto.get("1.0", tk.END)
            with open("notas.txt", "w") as f:
                f.write(conteudo)
            messagebox.showinfo("Salvo", "Notas salvas!")

        botao_salvar = tk.Button(self.tela, text="💾 Salvar", command=salvar)
        botao_salvar.pack(pady=10)

        botao_voltar = tk.Button(self.tela, text="🔙 Voltar", command=self.carregar_apps)
        botao_voltar.pack(pady=10)

    def limpar_tela(self):
        """Remove todos os widgets da tela para exibir novos conteúdos."""
        for widget in self.tela.winfo_children():
            widget.destroy()

# Iniciar o emulador
if __name__ == "__main__":
    janela = tk.Tk()
    emulador = EmuladorCelular(janela)
    janela.mainloop()
