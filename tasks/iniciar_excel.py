from time import strftime
import logging
import input.config
import xlsxwriter
import os

# Atribuindo váriaveis relacionadas ao nome e diretório do Excel #
name_excel = 'Agências_' + str(strftime('%Y%m%d')) + str(".xlsx")
path_excel = input.config.path_output + r"\reports\_"
FILE_PATH_EXCEL = path_excel + name_excel


def create_excel():
    logging.info("Criando arquivo de reports 'Agencias'")
    if os.path.isfile(FILE_PATH_EXCEL):
        logging.info("Arquivo " + name_excel + " ja existente")
    else:
        workbook = xlsxwriter.Workbook(FILE_PATH_EXCEL)
        agencia = workbook.add_worksheet('Agencia')
        logging.info("Arquivo " + name_excel + " criado")
        ### Add other worksheet
        overview = workbook.add_worksheet('Spending Overview')
        logging.info("Sheet overview criada")
        #### Set Excel Header ###
        agencia.write('A1', 'Agency')
        agencia.write('B1', 'FY 2022 IT Spending')
        agencia.write('C1', 'Spending on Major Investments')
        logging.info("Cabeçalho criado")
        workbook.close()
        # currency_format = workbook.add_format({'num_format': '$#,##0'})
