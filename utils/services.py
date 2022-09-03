from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from time import strftime
import logging
import os
import time

### Kill Process ###
try:
    os.system("taskkill /im msedge.exe /f")
    time.sleep(4)
except ValueError:
    pass

### Open WebDriver ###
s = Service(EdgeChromiumDriverManager().install())
driver_service = webdriver.Edge(service=s)
driver_service.implicitly_wait(10)

def screenshot(passo):
    name = r'C:\Users\Fabio\PycharmProjects\primeProject\output\screenshot\error_' + passo + str(
        strftime('%Y%m%d%H%M')) + str(".png")
    driver_service.get_screenshot_as_file(filename=name)
    return


def start_logging(processo, dev, modification):
    logging.basicConfig(
        filename=r'C:\Users\Fabio\PycharmProjects\primeProject\output\log\log_' + str(strftime('%Y%m%d%H%M')),
        level=logging.INFO,
        format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )
    logging.info(processo)
    logging.info(dev)
    logging.info(modification)
    logging.info('----------------------------------')
    logging.info('----------------------------------')


def finish_drive():
    driver_service.close()
    os.system("taskkill /im msedge.exe /f")