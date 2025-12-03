import random
import tkinter as tk
from tkinter import messagebox
import os
import subprocess

# Caminho do Git (GitHub Desktop)
GIT = r"C:\Users\LAERCIO\AppData\Local\GitHubDesktop\app-3.5.4\resources\app\git\mingw64\bin\git.exe"

# Caracteres disponíveis
caracteres = 'AEIJMNOSTUYaeijmnostuy0123456789'

# Função para gerar nome aleatório
def gerar_nome(comprimento):
    return ''.join(random.choice(caracteres) for _ in range(comprimento)) + ".html"

# Função principal para gerar arquivos
def gerar_arquivos():
    try:
        comprimento = int(entry_comprimento.get())
        link_real = entry_link.get().strip()

        if not link_real:
            messagebox.showerror("Erro", "Insira um link válido!")
            return
        
        pasta = os.getcwd()  # salva na pasta do script

        nome_arquivo = gerar_nome(comprimento)

        html_code = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redirecionando...</title>
    <meta http-equiv="refresh" content="0;url={link_real}">
    <style>
        body {{ background-color: #111; }}
    </style>
</head>
<body>
    <p style="color: #ffffff; font-size: 1.7em;">
        Redirecionando... Se não acontecer automaticamente,
        <a style="color: #ff0000;" href="{link_real}">clique aqui</a>. - JSY ANIME
    </p>
</body>
</html>"""

        caminho_completo = os.path.join(pasta, nome_arquivo)

        with open(caminho_completo, "w", encoding="utf-8") as f:
            f.write(html_code)

        # Monta a URL final
        url_final = f"https://j-s-yt.github.io/{nome_arquivo}"

        # Copiar para a área de transferência
        janela.clipboard_clear()
        janela.clipboard_append(url_final)

        messagebox.showinfo(
            "Sucesso",
            f"Arquivo gerado:\n{nome_arquivo}\n\nURL copiada:\n{url_final}"
        )

    except ValueError:
        messagebox.showerror("Erro", "Use apenas números no comprimento!")


# 🔥 Função para enviar tudo para o GitHub Pages
def enviar_para_github():
    repo = os.getcwd()

    try:
        # git add .
        subprocess.run([GIT, "-C", repo, "add", "."], check=True)

        # git commit
        subprocess.run([GIT, "-C", repo, "commit", "-m", "Envio automático de arquivos HTML"], check=True)

        # git push
        subprocess.run([GIT, "-C", repo, "push"], check=True)

        messagebox.showinfo("Sucesso", "Arquivos enviados para o GitHub Pages!")

    except FileNotFoundError:
        messagebox.showerror(
            "Erro",
            "Git não encontrado!\n\nVerifique o caminho do git.exe no topo do código."
        )

    except subprocess.CalledProcessError:
        messagebox.showerror(
            "Erro", 
            "Falha ao enviar para o GitHub.\n\nPossíveis causas:\n- Não está logado no GitHub Desktop\n- Repositório incorreto\n- Alterações já commitadas"
        )


# Interface gráfica
janela = tk.Tk()
janela.title("Gerador HTML - JSY ANIME")
janela.geometry("400x300")
janela.configure(bg="#222")

label_link = tk.Label(janela, text="Link real:", bg="#222", fg="white")
label_link.pack()
entry_link = tk.Entry(janela, width=40)
entry_link.pack()

label_comprimento = tk.Label(janela, text="Comprimento do nome:", bg="#222", fg="white")
label_comprimento.pack()
entry_comprimento = tk.Entry(janela)
entry_comprimento.pack()
entry_comprimento.insert(0, "5")

btn_gerar = tk.Button(janela, text="Gerar Arquivo", command=gerar_arquivos, bg="#ff0000", fg="white")
btn_gerar.pack(pady=10)

btn_git = tk.Button(janela, text="Enviar para GitHub Pages", command=enviar_para_github, bg="#008000", fg="white")
btn_git.pack(pady=5)

janela.mainloop()
