import tkinter as tk
import time





def CountdownWindow(seconds: int):
    """Função para criar uma janela de contagem regressiva"""
    root = tk.Tk()
    root.title("Contagem Regressiva")

    label = tk.Label(root, font=("Helvetica", 30))
    label.pack()

    for remaining in range(seconds, 0, -1):
        label.config(text=f"Tempo restante: {remaining} segundos")
        root.update() 
        time.sleep(1)  

    label.config(text="Processo Concluído!")
    root.update()
    time.sleep(2)  # Exibe a mensagem por 2 segundos antes de fechar

    root.destroy() 
