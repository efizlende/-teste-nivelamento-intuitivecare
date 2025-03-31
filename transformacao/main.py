import tkinter as tk
import time
import logging
from transformacao_dados import process_pdf_to_csv, zip_csv_file, PDF_PATH, CSV_PATH, ZIP_FILE_NAME



def countdown_window(seconds: int):
    """Exibe uma janela com uma contagem regressiva."""
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









def main():
    """Função principal que integra as etapas de extração, processamento e compactação."""
    logging.info("Iniciando o processo de transformação...")

    # Exibe a janela de contagem regressiva enquanto processa o arquivo
    countdown_window(10)
    
    # Processamento do PDF para CSV
    if process_pdf_to_csv(PDF_PATH, CSV_PATH):
        # Compacta o CSV em um arquivo ZIP
        if zip_csv_file(CSV_PATH, ZIP_FILE_NAME):
            logging.info("Processo concluído com sucesso!")
        else:
            logging.error("Falha ao compactar o arquivo CSV.")
    else:
        logging.error("Falha ao processar o PDF para CSV.")

if __name__ == "__main__":
    main()
