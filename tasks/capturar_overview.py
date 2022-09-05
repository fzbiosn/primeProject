import logging
import time
from openpyxl import load_workbook
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
    sheet_overview = pd.read_excel(file_path_excel, sheet_name='Spending Overview')
    print(sheet_overview)
    return sheet_overview, file_path_excel


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

    with open(download_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t agency: {row[0]} , spending_type:  {row[1]} , fiscal_year: {row[2]},'
                      f'spending_amount: {row[3]}, last_updated: {row[4]}')
                line_count += 1

                logging.info('Inserindo valores no excel')
                session_agency.at[line_count, 1] = row[0]
                session_agency.at[line_count, 2] = row[1]
                session_agency.at[line_count, 3] = row[2]
                session_agency.at[line_count, 4] = row[3]
                session_agency.at[line_count, 5] = row[4]
        print(f'Processed {line_count} lines.')
        session_agency.to_excel(path_session_excel, sheet_name='Spending Overview', header=None, index=False)
        session_agency.save()

