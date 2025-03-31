import os
import pandas as pd
import zipfile
import pdfplumber
import logging
from typing import List, Optional



PDF_PATH = "/home/uanicode/Documents/Entrevistas/Intuitive-care/-teste-nivelamento-intuitivecare/scraping/scraping/downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
CSV_PATH = "transformacao/Rol_de_Procedimentos.csv"
ZIP_FILE_NAME = "transformacao/Ernesto_Orlando_Uanicela.zip"


os.makedirs("transformacao", exist_ok=True)

# Configuração do Logger
LOG_FILE = "transformacao/logs.txt"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Dicionário de abreviações
ABREVIACOES = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial"
}








# Funcao para extração de tabelas de PDF
def extract_table_from_pdf(pdf_path: str) -> List[List[str]]:
    """Extrai a tabela de um arquivo PDF e retorna os dados em formato de lista de listas."""
    data = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    data.extend(table)  
        logging.info("Tabela extraída com sucesso do PDF.")
    except Exception as e:
        logging.error(f"Erro ao extrair tabela do PDF: {e}")
        raise
    return data









#Funcao para processar PDF para CSV
def process_pdf_to_csv(pdf_path: str, csv_path: str) -> bool:
    """Processa o PDF, converte para CSV e substitui abreviações."""
    try:
        # Extração da tabela
        table_data = extract_table_from_pdf(pdf_path)

       
        df = pd.DataFrame(table_data)

        # Substituição das abreviações
        df.replace(ABREVIACOES, inplace=True)

        # Salvando o CSV
        df.to_csv(csv_path, index=False, header=False, sep=";")
        logging.info(f"CSV salvo em {csv_path}")
        return True
    except Exception as e:
        logging.error(f"Erro ao processar PDF para CSV: {e}")
        return False








#Funcao para compactar CSV em ZIP
def zip_csv_file(csv_path: str, zip_file_name: str) -> bool:
    """Compacta o CSV em um arquivo ZIP."""
    try:
        with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(csv_path, os.path.basename(csv_path))
        logging.info(f"Arquivo ZIP salvo em {zip_file_name}")
        return True
    except Exception as e:
        logging.error(f"Erro ao compactar o CSV: {e}")
        return False
