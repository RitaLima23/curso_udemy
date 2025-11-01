import tkinter as tk
import random

# Lista de participantes
participantes = []

# Função para adicionar participante
def adicionar_participante():
    nome = entrada_nome.get().strip()
    if nome:
        participantes.append(nome)
        lista_participantes.insert(tk.END, f"💫 {nome}")
        entrada_nome.delete(0, tk.END)

# Função para sortear
def sortear():
    if participantes:
        vencedor = random.choice(participantes)
        label_resultado.config(
            text=f"🎉 Parabéns, {vencedor}! 🎀",
            fg="#ff66b3"
        )
    else:
        label_resultado.config(text="Nenhum participante ainda! 💭", fg="#555")

# Função para limpar tudo
def limpar_tela():
    participantes.clear()  # limpa a lista
    lista_participantes.delete(0, tk.END)  # limpa a listbox
    label_resultado.config(text="Tela limpinha! 🌸", fg="#999")

# Criação da janela
janela = tk.Tk()
janela.title("🍀 Sorteio Fofo 💖")
janela.geometry("350x500")
janela.config(bg="#ffe6f2")

# Título
label_titulo = tk.Label(
    janela,
    text="✨ Sorteio Mágico ✨",
    font=("Comic Sans MS", 18, "bold"),
    bg="#ffe6f2",
    fg="#ff66b3"
)
label_titulo.pack(pady=15)

# Campo para digitar nome
entrada_nome = tk.Entry(janela, font=("Comic Sans MS", 12), width=25, justify="center")
entrada_nome.pack(pady=10)

# Botão para adicionar
botao_add = tk.Button(
    janela,
    text="🌸 Adicionar Participante 🌸",
    font=("Comic Sans MS", 10, "bold"),
    bg="#ffb3d9",
    fg="white",
    relief="ridge",
    command=adicionar_participante
)
botao_add.pack(pady=5)

# Lista de participantes
lista_participantes = tk.Listbox(
    janela,
    font=("Comic Sans MS", 10),
    bg="#fff0f5",
    width=30,
    height=8,
    fg="#ff66b3",
    selectbackground="#ffb3d9"
)
lista_participantes.pack(pady=10)

# Botão de sorteio
botao_sortear = tk.Button(
    janela,
    text="💖 Sortear Agora 💖",
    font=("Comic Sans MS", 12, "bold"),
    bg="#ff80bf",
    fg="white",
    relief="raised",
    command=sortear
)
botao_sortear.pack(pady=10)

# Botão de limpar tela
botao_limpar = tk.Button(
    janela,
    text="🧼 Limpar Tudo 🧼",
    font=("Comic Sans MS", 10, "bold"),
    bg="#ffb6c1",
    fg="#fff",
    relief="ridge",
    command=limpar_tela
)
botao_limpar.pack(pady=5)

# Resultado
label_resultado = tk.Label(
    janela,
    text="Aguardando sorteio... 🌷",
    font=("Comic Sans MS", 12),
    bg="#ffe6f2",
    fg="#666"
)
label_resultado.pack(pady=10)

# Iniciar janela
janela.mainloop()
