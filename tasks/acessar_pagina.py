from selenium.webdriver.common.by import By
import logging
import utils.services

# Capability #
drive_service = utils.services.driver_service


def acessar_url(page):
    logging.info('Acessando a url: ' + page)
    drive_service.get(page)
    drive_service.maximize_window()
    drive_service.set_page_load_timeout(25)


def validar_pagina():
    logging.info('Validando se a URL foi aberta com sucesso')
    if drive_service.find_element(By.XPATH, '//*[@id="logo"]/em/a[1]/img'):
        logging.info('URL carregada')
    else:
        raise Exception('URL apresentou timeout')
