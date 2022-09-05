Requisitos
====================
Para esse projeto é necessário instalar o Python versão 3.10 - https://www.python.org/downloads/

Para esse projeto é necessário instalar a versão mais recente do navegador Microsoft Edge

Para funcionamento da biblioteca webdriver é necessário instalar o msedgedriver.exe compatível 
com a versão do sistema operacional - https://developer.microsoft.com/pt-br/microsoft-edge/tools/webdriver/

O executavel msedgedriver.exe deve estar instalado em C:\webdrivers


Execução
====================
1) No terminal do IDE, navegar para diretório C:/Users/{LOCAL_USER}/PycharmProjects/primeProject/main
2) Executar o comando py main.py


Bibliotecas e Dependencias
====================
Python package selenium; 
Python package webdriver;
Python package OS;
Python package Logging;
Python package selenium.webdriver.common.by;
Python package time;
Python package selenium.webdriver.support.ui;
Python package pandas;
Python package csv;
Python package selenium.webdriver.support;
Python package xlsxwriter;
Python package selenium.webdriver.remote.webelement;

Correções Pendentes
====================
1) Necessário ajuste na função def baixar_csv() //capturar_overview.py:
	As ancoras e cliques utilizados apresentam grande instabilidade
2) Necessário a inclusão das funções xlswriter para inclusão de uma nova sheet na função session_excel() //capturar_overview.py:
	As funções nativas do pandas estão sobreescrevendo as abas da planilhas


Melhorias
====================
-Inclusão de resiliencia na task de processamento (dashboard.py), para novas tentativas de execução após qualquer exceção

-Inclusão da função timer para coleta do tempo de execução em cada step;

-Inclusão do arquivo Dotenv para utilização dos valores globais, variáveis de sistema, variáveis imutáveis e valores de configuração;

-Inclusão de classes em alguns arquivos para maior controle e privacidade das variavéis e retornos de funções;

-Padronização dos nomes de variaveis e funções;

-Inclusão das funções web no arquivo "page_objects.py" e utilização do mesmo;

-Inclusão de arquivo com requerimentos com download automatico na inicialização do projeto


Decisões Tomadas
====================
Foi considerado o uso do framework Selenium webdriver em detrenimento do rpaframework-selenium pela maior variedade de funções logadas e 
setup de configuração facilitadas no dispositivo.

O projeto foi arquitetado para que o arquivo main possa orquestrar outros robôs e testes a serem acoplados, reutilizando as tasks, módulos e funções entre si para o desenvolvimento mais perfomatico.

O modulo "robots" é onde são inseridos os diferentes testes conforme o processo elegido, a premissa é o controle do fluxo através de um processador para cada processo. Nesse projeto, o processo "dashboard_gov.py" foi criado para esse fim.

O módulo "tasks" é onde são inseridos as tasks a serem chamadas pelo processo. Esse módulo pode ser divididos em sub-módulos a depender do projeto. As tasks podem ser consumidas em diferentes testes, com interfaces ou não, caso o processo coincida.

Foram criadas os diretórios e arquivos de log e prints, para rastreio de execução, evidências de erros e reports de algumas informações que sejam relevantes para o negócio.

Se necessário, o projeto pode ser disponibilizado publicamente no GitHub.