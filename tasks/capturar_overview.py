import logging
import time
import tasks.iniciar_excel
import tasks.coletar_despesas
import utils.services
import input.config
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import csv

# Atribuindo variáveis gerais #
name_agency_overview = input.config.NAME_AGENCY_OVERVIEW
download_path = input.config.DOWNLOAD_PATH
name_agency_file = input.config.NAME_AGENCY_FILE

# Importando webdriver #
drive_service = utils.services.driver_service


# Atribuindo variavéis do Excel #
def session_excel():
    file_path_excel = tasks.iniciar_excel.FILE_PATH_EXCEL
    sheet_agency = pd.read_excel(file_path_excel)
    print(sheet_agency)
    return sheet_agency, file_path_excel


def selecionar_agencia():
    dropdown = drive_service.find_element(By.ID, 'agency-select')
    selector = Select(dropdown)
    logging.info('Selecionando a agencia: ' + name_agency_overview)
    selector.select_by_visible_text(name_agency_overview)
    time.sleep(4)


def baixar_csv():
    download_file = download_path + name_agency_file
    print(download_file)
    logging.info('Realizando download do arquivo CSV')
    #ActionChains(drive_service).click('//*[@id="agency-info-wrapper"]/div/div[1]/div[3]/div[2]/a').perform()
    if download_file:
        logging.info('Download realizado com sucesso')
    else:
        raise Exception('Falha no download')
    return download_file


def percorrer_csv():
    logging.info('Percorrendo arquivo CSV baixado')
    session_agency, path_session_excel = session_excel()
    download_file = baixar_csv()
    with open(download_file, 'rt') as ficheiro:
        reader = csv.reader(ficheiro)
        for linha in reader:
            logging.info('Capturando valores da linha')
            linha_str = str(linha)
            agency_name, spending_type, fiscal_year, spending_amount, last_updated = linha_str.split(',')
            #print(agency_name, + '|' + spending_type, + '|' + fiscal_year, + '|' + spending_amount,
            #      + '|' + last_updated)

            # Se size > 0 and < 80 #
            #if session_agency.size < 200:
            logging.info('Inserindo valores no excel')
            session_agency.at[linha, 1] = agency_name
            session_agency.at[linha, 2] = spending_type
            session_agency.at[linha, 3] = fiscal_year
            session_agency.at[linha, 4] = spending_amount
            session_agency.at[linha, 5] = last_updated

        session_agency.to_excel(path_session_excel, sheet_name=name_agency_file)
        #print(str(session_agency.size))
