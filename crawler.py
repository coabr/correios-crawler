import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import json

for state in ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"]:
    values = urllib.parse.urlencode({'UF': state})
    values = values.encode('ascii')

    url = "http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"

    urlResponse = urllib.request.urlopen(url,values)

    html = urlResponse.read().decode('ISO-8859-1')

    soup = BeautifulSoup(html, 'lxml')

    table = soup.find('table')

    # for row in table.findAll("tr"):
    #     cells = row.findAll('td')
  
    print (table)
  