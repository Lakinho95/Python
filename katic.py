import requests
import datetime
from requests_html import HTML

url = 'https://nkatic.wordpress.com/category/medjunarodna-ekonomija/'
def url_to_txt(url,filename='world.html', save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f'world-{year}.html', 'w') as f:
                f.write(html_text)
        return html_text
    return ""

html_text = url_to_txt(url)
r_html = HTML(html=html_text)
a = r_html.find('.category-medjunarodna-ekonomija')
a = a[0]
podnaslovi = a.find('.posttitle')
tekst = [ ]
ostatak = ''
for podnaslov in podnaslovi:
    tekst.append(podnaslov.find('h2')[0].text)
    ostatak +=podnaslov.find('p')[0].text
opisi = a.find('.entry')
paragraf = []
for opis in opisi:
    paragraf.append(opis.find('p')[0].text)
import pandas as pd
import re
datumi = re.findall('\d{1,2}.\d{1,2}.\d{4}', ostatak)
a = 0
broj_kometara = []
for sekcija in re.findall('\d{4}\|\s?(\d?\d?\d?)',ostatak):
    if len(sekcija) > 0:
        broj_kometara.append(sekcija)
    else:
        sekcija = 0
        broj_kometara.append(sekcija)

Tabela = pd.DataFrame({
    'naslov':tekst,
    'size' : paragraf,
    'datum': datumi,
    'broj_komenatara' : broj_kometara
})
Tabela.to_csv('katic1.csv',index=False)




