from time import strftime
import logging
import input.config
import xlsxwriter
import os

# Atribuindo váriaveis relacionadas ao nome e diretório do Excel #
name = 'Agências_' + str(strftime('%Y%m%d')) + str(".xlsx")
path = input.config.path_output + r"\reports\_"
_FILE_PATH = path + name


def create_excel():
    logging.info("Criando arquivo de reports 'Agencias'")
    if os.path.isfile(_FILE_PATH):
        logging.info("Arquivo " + name + " ja existente")
    else:
        workbook = xlsxwriter.Workbook(_FILE_PATH)
        agencia = workbook.add_worksheet('Agencia')
        logging.info("Arquivo " + name + " criado")
        #### Set Excel Header ###
        agencia.write('A1', 'Agency')
        agencia.write('B1', 'FY 2022 IT Spending')
        agencia.write('C1', 'Spending on Major Investments')
        logging.info("Cabeçalho criado")
        workbook.close()
        # currency_format = workbook.add_format({'num_format': '$#,##0'})
