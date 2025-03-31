import logging
import threading
from scraper import init_driver, hover_and_fetch_pdf_links, download_pdfs, create_zip_file
from countdown_window import CountdownWindow  # Importa a classe da janela de contagem regressiva

# Configuração de logging
logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_scraper() -> None:
    """
    Executa o scraper para capturar links de PDFs, baixar e compactá-los.
    Garante fechamento seguro do WebDriver e log detalhado do processo.
    """
    logging.info("Iniciando o processo de scraping...")
    
    # Inicializa a janela de contagem regressiva em uma thread separada
    countdown_thread = threading.Thread(target=CountdownWindow, args=(10,))  # 10 segundos de contagem regressiva
    countdown_thread.daemon = True  # Permite que a thread de contagem seja finalizada quando o programa principal terminar
    countdown_thread.start()
    
    driver = init_driver()
    
    try:
        # Aqui está obtendo os links dos pdf
        pdf_links = hover_and_fetch_pdf_links(driver)
        
        if not pdf_links:
            logging.info("Nenhum link de PDF encontrado.")
            return  

        logging.info(f"Total de links encontrados: {len(pdf_links)}")

        # Baixa os PDFs em paralelo para melhorar o desempenho
        downloaded_files = download_pdfs(pdf_links)
        
        if downloaded_files:
            create_zip_file(downloaded_files)
    
    except Exception as e:
        logging.error(f"Erro durante a execução do scraper: {e}", exc_info=True)
    
    finally:
        driver.quit()  # Garante que o WebDriver será fechado corretamente

if __name__ == "__main__":
    run_scraper()
