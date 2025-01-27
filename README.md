# Automação de Extração de Dados de Agenda
# Descrição
Este projeto é uma automação para extrair agendamentos e informações de leilões de um site e salvar esses dados em uma planilha.
A automação é feita utilizando as bibliotecas Selenium e Openpyxl.

# Dor do Cliente
O cliente relatou que fazia manualmente o processo de acessar o site e conferir os agendamentos de leilões, registrando-os em uma planilha.
Este processo poderia levar cerca de 3 a 4 horas por dia, pois os agendamentos poderiam ser removidos ou novos poderiam ser inseridos no site, exigindo conferência diária.

# Solução
Utilizamos as bibliotecas Selenium e Openpyxl para acessar o site, extrair todos os dados necessários e salvá-los em uma planilha.
A aplicação automatizada reduz o tempo necessário para extrair os dados para aproximadamente 1 minuto.

# Requisitos do Sistema
- Python 3.6 ou superior
- Google Chrome instalado

# Bibliotecas Necessárias
As seguintes bibliotecas Python são necessárias:
- selenium
- webdriver-manager
- openpyxl
- Você pode instalá-las utilizando o seguinte comando:
- pip install -r requirements.txt
  
# Instruções de Instalação
Clone o repositório para sua máquina local:
- git clone https://github.com/seu-usuario/automacao-extracao-leilao.git
  
Navegue até o diretório do projeto:
- cd automacao-extracao-leilao

Instale as dependências:
- pip install -r requirements.txt
  
# Instruções de Execução
Para executar a automação, utilize o seguinte comando:
- python app.py
  
# Estrutura do Projeto
- app.py (Script principal que realiza a automação da extração de dados.)
- requirements.txt (Lista de dependências necessárias para o projeto.)

# Exemplos de Uso
Execute o script app.py para iniciar a automação.
Os dados extraídos serão salvos em um arquivo informacoes_leiloes.xlsx no mesmo diretório.
