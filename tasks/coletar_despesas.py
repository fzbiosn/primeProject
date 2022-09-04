import logging
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
    dropdown = drive_service.find_element(By.ID, 'agency-select')
    logging.info(dropdown)
    selector = Select(dropdown)
    logging.info(selector)
    # Waiting for the values to load
    element = WebDriverWait(drive_service, 10).until(EC.element_to_be_selected(selector.options[0]))

    options = selector.options
    for index in range(1, len(options) - 1):
        logging.info(options[index].text)

    '''def multiselect_set_selections(driver, element_id, labels):
        el = driver.find_elements_by_id(element_id)
        for option in el.find_elements_by_tag_name('option'):
            if option.text in labels:
                option.click()
#block-data-visualizer-content > div.agency-filter > div > div
#block-data-visualizer-content > div.agency-filter > div > div > label
#agency-select
select.
#agency-select > option:nth-child(1)
#agency-select > option:nth-child(2)
#agency-select > option:nth-child(3)'''
