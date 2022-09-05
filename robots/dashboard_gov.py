import logging
import input.config
import input.config
import tasks.acessar_pagina
import tasks.coletar_despesas
import tasks.iniciar_excel
import tasks.capturar_overview
import utils.services


### Variables Pre Process ###
nome_agencia = input.config.name_agency
page = input.config.url
log = input.config.name_log


### Set up logging to file ###
utils.services.start_logging('Process Name - ITdashboard', 'Dev Name - Fabio Neves', 'Last Modification - 02/09/2022')


# run_tasks()
def run_tasks():
    step = '01_Iniciar_Excel'
    logging.info('Iniciando o step: ' + step)
    try:
        tasks.iniciar_excel.create_excel()
    except Exception as x:
        logging.error("Erro no step: " + step + " - " + str(x))
        utils.services.screenshot(step)
        utils.services.finish_drive()
    logging.info('-----------------------------')

    step = '02_Acessar_Pagina'
    logging.info('Iniciando o step: ' + step)
    try:
        tasks.acessar_pagina.acessar_url(page)
        tasks.acessar_pagina.validar_pagina()
    except Exception as x:
        logging.error("Erro no step: " + step + " - " + str(x))
        utils.services.screenshot(step)
        utils.services.finish_drive()
    logging.info('-----------------------------')

    step = '03_Coletar_Despesas'
    logging.info('Iniciando o step: ' + step)
    try:
        tasks.coletar_despesas.clicar_botao_explorer()
        tasks.coletar_despesas.capturar_agencias()
        tasks.coletar_despesas.percorrer_lista()
    except Exception as x:
        logging.error("Erro no step: " + step + " - " + str(x))
        utils.services.screenshot(step)
        # utils.services.finish_drive()
    logging.info('-----------------------------')

    step = '04_Capturar_Overview'
    logging.info('Iniciando o step: ' + step)
    try:
        tasks.capturar_overview.selecionar_agencia()
        tasks.capturar_overview.baixar_csv()
        tasks.capturar_overview.percorrer_csv()
    except Exception as x:
        logging.error("Erro no step: " + step + " - " + str(x))
        utils.services.screenshot(step)
        # utils.services.finish_drive()
        # utils.services.finish_drive()
    logging.info('-----------------------------')

    utils.services.finish_drive()


run_tasks()
