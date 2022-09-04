import logging
import time

import utils.services
import utils.page_objects
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Importando webdriver #
drive_service = utils.services.driver_service


# Iniciando variavéis #


def clicar_botao_explorer():
    logging.info('Clicando no botao Explorer - IT Portfolio')
    drive_service.find_element(By.XPATH, '//*[@id="block-views-block-domains-overview-block-1"]/div/div/div/ul/li['
                                         '1]/div[4]/div/a').click()
    if drive_service.find_element(By.XPATH, '//*[@id="header"]/nav/div/ul/li[1]/button/span'):
        logging.info('Pagina de despesas carregada')
    else:
        raise Exception('Pagina de despesas apresentou timeout')


def capturar_agencias():
    logging.info('Criando uma lista com o nome das agencias')
    dropdown = drive_service.find_element(By.ID, 'agency-select')
    selector = Select(dropdown)
    # Waiting for the values to load
    element = WebDriverWait(drive_service, 10).until(EC.element_to_be_selected(selector.options[0]))
    logging.info('Status da criacao da lista: ' + str(element))
    lista = selector.options
    return lista, selector


def percorrer_lista():
    list_agency, select = capturar_agencias()
    for index in range(1, len(list_agency) - 1):
        logging.info('Selecionando agencia: ' + list_agency[index].text)
        select.select_by_visible_text(list_agency[index].text)
        coletar_despesa()
        time.sleep(4)


def coletar_despesa():
    logging.info('Coletando as despesas')
    it_spending = drive_service.find_element_by_xpath(
        '//*[@id="agency-info-wrapper"]/div/div[1]/div[2]/div[1]/p/strong').text
    investiments_spending = drive_service.find_element_by_xpath(
        '//*[@id="agency-info-wrapper"]/div/div[1]/div[2]/div[2]/p/strong').text
    print(it_spending, investiments_spending)
