from time import strftime
import logging
import input.config
import xlsxwriter
import os

### Atribuindo Váriaveis de Excel ###
name = 'Agências_' + str(strftime('%Y%m%d')) + str(".xlsx")
path = input.config.path_output + r"\reports\_"
file_path = path + name


def create_excel():
    logging.info("Criando arquivo de reports 'Agencias'")
    if os.path.isfile(file_path):
        logging.info("Arquivo " + name + " ja existente")
    else:
        workbook = xlsxwriter.Workbook(file_path)
        agencia = workbook.add_worksheet('Agencia')
        logging.info("Arquivo " + name + " criado")
        #### Set Excel Header ###
        agencia.write('A1', 'Agency')
        agencia.write('B1', 'Spending')
        logging.info("Cabeçalho criado")
        workbook.close()
        # currency_format = workbook.add_format({'num_format': '$#,##0'})
