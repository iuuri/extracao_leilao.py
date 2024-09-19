############# IMPORTAÇÃO DE BIBLIOTECAS #############
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from time import sleep
import openpyxl

#################################################### AUTOMAÇÃO ####################################################

################# CONFIGURAR NAVEGADOR #################
# Configurando navegador Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Rodar o navegador em modo headless 
chrome_options.add_argument("--log-level=3")  # Desativar logs do ChromeDriver
chrome_options.add_argument("--silent")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options)

################# CRIAR E CONFIGURAR PLANILHA #################
# Criar um novo arquivo Excel
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Leilões"

# Adicionar cabeçalhos
sheet.append(["Nome do Leilão", "Data", "Mês", "Hora", "Recinto", "Cidade", "Transmissão"])

################# ACESSAR SITE PROGRAMA LEILÕES #################
try:
    print('Acessando a agenda do site Programa Leilões...')
    driver.get('https://programaleiloes.com/agenda')
    # Verifica se o elemento que indica que a página carregou está presente
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Agenda de leilões')]"))
    )
    print("Site acessado com sucesso.")
except TimeoutException:
    print("Erro ao acessar o site. Verifique sua conexão com a internet ou se o site está no ar.")
    driver.quit()

############# EXTRAIR LINKS DA AGENDA #############
print('Extraindo links da agenda...')
links_agenda = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@class = 'leiloes-area']//li//a"))
)

# Lista para armazenar os links 
links = []

# Iterar nos cards e extrair os links 
for link_agenda in links_agenda:
    link = link_agenda.get_attribute('href')
    if link:
        links.append(link)
print(f'Foram extraídos {len(links)} links da agenda.')

############# ACESSAR LINKS E EXTRAIR INFORMAÇÕES #############
for link in links:
    driver.get(link)
    print(f"Acessando: {link}")
    try:
        nome_leilao = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class = 'titulo']//h1"))
        ).text

    except:
        nome_leilao = 'N/A'

    try:
        data_leilao = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//time[@datetime]//span[@class = 'dia custom-font-color']"))
        ).text

    except:
        data_leilao = 'N/A' 
    
    try:
        mes_leilao = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class = 'mes']"))
        ).text
    except:
        mes_leilao = 'N/A'

    try:
        hora_leilao = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class = 'hora']//p"))
        ).text
    except:
        hora_leilao = 'N/A'

    try:
        recinto_leilao = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class = 'recinto']"))
        ).text
    except:
        recinto_leilao = 'N/A'

    try:
        cidade_leilao = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class = 'cidade']"))
        ).text
    except:
        cidade_leilao = 'N/A'
    
    try:
        transmissao_leilao = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='transmissao']//img"))
        )
        
        nome_transmissao_leilao = [transmissao.get_attribute('alt') for transmissao in transmissao_leilao]
            
    except:
        nome_transmissao_leilao = ['N/A']

    # Adicionar dados extraídos à planilha
    sheet.append([nome_leilao, data_leilao, mes_leilao, hora_leilao, recinto_leilao, cidade_leilao, "; ".join(nome_transmissao_leilao)])

# Salvar a planilha
workbook.save("leiloes.xlsx")

# Fechar o navegador
driver.quit()

print("Processo concluído e planilha salva como 'leiloes.xlsx'.")
