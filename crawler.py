import urllib.request
from bs4 import BeautifulSoup
import re
import json
import jsonlines

for state in ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"]:
    values = urllib.parse.urlencode({'UF': state})
    values = values.encode('ascii')

    url = "http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"

    urlResponse = urllib.request.urlopen(url,values)

    html = urlResponse.read().decode('ISO-8859-1')

    soup = BeautifulSoup(html, 'lxml')

    regularExpression = r"(?:<td.*?>)(.*?)(?:</td>)"
    
    result = re.findall(regularExpression,html)
    
    
    """
    how I want the dict: 

    {"uf": "ac", "cep": "50000-000", "locals": [{"recife": "50000-000"}, {"olinda": "50000-0000"}]  }
    
    state_dict = {}
    
    i = 0
    
    for row in result:
        if i == 0:
            state_dict["UF"] = row
        elif i == 1:
            state_dict["faixa_cep"] = row
        print(row)
        i += 1 """
    
    to_json = json.dumps(result)
    
    print("\n========= " + state + " information =========\n" )
    print(to_json)

