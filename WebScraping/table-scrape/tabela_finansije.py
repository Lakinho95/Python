import requests
from requests_html import HTML
import pandas as pd

url = 'https://tradingeconomics.com/country-list/external-debt'

def url_to_txt(url, filename="world.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"world-{year}.html", 'w') as f:
                f.write(html_text)
        return html_text
    return None

def izvlacenje_podataka(url):
    html_text = url_to_txt(url)
    if html_text == None:
        return False
    r_html = HTML(html=html_text)
    table_class = r_html.find('.table-hover')
    parsed_table = table_class[0]
    rows = parsed_table.find('tr')
    header_row = rows[0]
    table_data = []
    header_cols = header_row.find('th')
    header_names = [x.text for x in header_cols]
    for row in rows[1:]:
        cols = row.find('td')
        podaci = []
        for i,col in enumerate(cols,start=1):
            podaci.append(col.text)
        table_data.append(podaci)
    df = pd.DataFrame(table_data, columns=header_names)
    df.to_csv('external_debt1.csv', index=False)

izvlacenje_podataka(url)
