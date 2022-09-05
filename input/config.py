import os

### Variaveis de entrada ###
url = 'https://www.itdashboard.gov/'
name_log = "log"
name_agency = 'Department of Justice'
NAME_AGENCY_OVERVIEW = 'Department of Justice'
NAME_AGENCY_FILE = r'\itpd-spending-DOJ.csv'

# Captura nome de usuario Windows #
local_user = os.environ['UserName']

# Atribui nome de usuario Windows aos caminho de saida#
path_input = fr'C:\Users\{local_user}\PycharmProjects\primeProject\input'
path_output = fr'C:\Users\{local_user}\PycharmProjects\primeProject\output'
DOWNLOAD_PATH = fr'C:\Users\{local_user}\Downloads'




