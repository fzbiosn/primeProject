import logging
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import utils.services

# Importando webdriver #
drive_service = utils.services.driver_service


def find_element_by_locator(locator):
    locator_type_get, locator_value_get = locator.split('=')
    locator_type = str(locator_type_get)
    locator_value = str(locator_value_get)
    logging.INFO(locator_type, locator_value)
    if locator_type == 'class':
        return drive_service.find_element(By.CLASS_NAME, locator_value)
    elif locator_type == 'css':
        drive_service.find_element(By.CSS_SELECTOR, locator_value)
    elif locator_type == 'id':
        drive_service.find_element(By.ID, locator_value)
    elif locator_type == 'link':
        drive_service.find_element(By.LINK_TEXT, locator_value)
    elif locator_type == 'name':
        drive_service.find_element(By.NAME, locator_value)
    elif locator_type == 'plink':
        drive_service.find_element(By.PARTIAL_LINK_TEXT, locator_value)
    elif locator_type == 'tag':
        drive_service.find_element(By.TAG_NAME, locator_value)
    elif locator_type == 'xpath':
        drive_service.find_element(By.XPATH, locator_value)
    else:
        raise Exception('Invalid locator')


def find_elements_by_locator(locator):
    locator_type, locator_value = locator.split('=')
    if locator_type == 'class':
        elements = drive_service.find_elements(By.CLASS_NAME, locator_value)
    elif locator_type == 'css':
        elements = drive_service.find_elements(By.CSS_SELECTOR, locator_value)
    elif locator_type == 'id':
        elements = drive_service.find_elements(By.ID, locator_value)
    elif locator_type == 'link':
        elements = drive_service.find_elements(By.LINK_TEXT, locator_value)
    elif locator_type == 'name':
        elements = drive_service.find_elements(By.NAME, locator_value)
    elif locator_type == 'plink':
        elements = drive_service.find_elements(By.PARTIAL_LINK_TEXT, locator_value)
    elif locator_type == 'tag':
        elements = drive_service.find_elements(By.TAG_NAME, locator_value)
    elif locator_type == 'xpath':
        elements = drive_service.find_elements(By.XPATH, locator_value)
    else:
        raise Exception('Invalid locator')

    return [WebElement(e) for e in elements]
