import urllib.request
from bs4 import BeautifulSoup
import re
#import jsonlines

for state in ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"]:
    values = urllib.parse.urlencode({'UF': state})
    values = values.encode('ascii')

    url = "http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"

    urlResponse = urllib.request.urlopen(url,values)

    html = urlResponse.read().decode('ISO-8859-1')

    soup = BeautifulSoup(html, 'lxml')

#    tables = soup.find_all('table', "tmptabela")

    rows = soup.find_all('tr')
    
    regularExpression = r"(?:<td.*?>)(.*?)(?:</td>)"
    
    result = re.findall(regularExpression,html)
    
    print (result[:])


    #for row in rows:
    #    print (row.prettify())


    #for table in tables:
    #    print(table.prettify())
  