import logging
import os
import requests
import zipfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from typing import List


# Configuração
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
DOWNLOAD_DIR = "scraping/downloads/"
ZIP_FILE_NAME = "scraping/attachments.zip"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)  # Garante que o diretório existe






# Função para inicializar o driver    
def init_driver(browser: str = "chrome") -> webdriver.Remote:
    """Inicializa o WebDriver do Selenium para o navegador especificado."""
    options_dict = {
        "chrome": webdriver.ChromeOptions(),
        "firefox": webdriver.FirefoxOptions(),
        "edge": webdriver.EdgeOptions()
    }
    
    if browser not in options_dict:
        raise ValueError("Navegador não suportado! Escolha entre 'chrome', 'firefox' ou 'edge'.")
    
    options = options_dict[browser]
    options.add_argument("--headless")  # Aqui para ativar o modo sem interface gráfica
    
    driver_class = getattr(webdriver, browser.capitalize())
    return driver_class(options=options)







# Função para passar o mouse sobre os elementos e pegar os links
def hover_and_fetch_pdf_links(driver: webdriver.Remote) -> List[str]:
    """Simula o movimento do mouse e obtém os links dos PDFs Anexo I e II."""
    logging.info("Acessando o site para buscar os links dos PDFs...")
    driver.get(URL)
    
    try:
        wait = WebDriverWait(driver, 60)
        anexo_elements = wait.until(
            EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "Anexo"))
        )
        
        actions = ActionChains(driver)
        pdf_links = set()
        
        for anexo in anexo_elements:
            actions.move_to_element(anexo).perform()
            logging.info("Passando o mouse sobre: %s", anexo.text)
            
            try:
                WebDriverWait(driver, 2).until(EC.visibility_of(anexo))
                href = anexo.get_attribute("href")
                if href and href.endswith(".pdf"):
                    pdf_links.add(href)
                    logging.info("Link encontrado (PDF): %s", href)
            except StaleElementReferenceException:
                logging.warning("Elemento não encontrado, pulando...")
        
        return list(pdf_links)
    except TimeoutException:
        logging.error("Tempo de espera excedido. A página não carregou completamente.")
        return []







# Função para baixar os PDFs
def download_pdfs(pdf_links: List[str]) -> List[str]:
    """Baixa os PDFs e salva no diretório de downloads."""
    downloaded_files = []
    
    for link in pdf_links:
        file_name = os.path.join(DOWNLOAD_DIR, os.path.basename(link))
        try:
            response = requests.get(link, stream=True)
            response.raise_for_status()  # Lança erro se a resposta não for 200
            
            with open(file_name, "wb") as file:
                for chunk in response.iter_content(chunk_size=4096):
                    file.write(chunk)
            
            logging.info("Download concluído: %s", file_name)
            downloaded_files.append(file_name)
        except requests.RequestException as e:
            logging.error("Erro ao baixar %s: %s", link, str(e))
    
    return downloaded_files







# Função para criar o arquivo ZIP
def create_zip_file(files: List[str]) -> None:
    """Compacta os arquivos baixados em um único arquivo ZIP."""
    with zipfile.ZipFile(ZIP_FILE_NAME, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
            logging.info("Arquivo adicionado ao ZIP: %s", file)
    
    logging.info("Arquivo ZIP criado com sucesso: %s", ZIP_FILE_NAME)
