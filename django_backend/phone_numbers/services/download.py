import logging

import requests
from bs4 import BeautifulSoup
import pandas as pd
import django
django.setup()

from phone_numbers.models import Range


path_to_files = './phone_numbers/services/files/'
filenames = ['ABC-3xx.csv', 'ABC-4xx.csv', 'ABC-8xx.csv', 'DEF-9xx.csv']


def download(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    for filename in filenames:
        download_button = soup.select_one(
            f'a[href^="https://opendata.digital.gov.ru/downloads/{filename}"]'
        )
        file_response = requests.get(download_button['href'], verify=False)
        with open(path_to_files + filename, 'wb') as f:
            f.write(file_response.content)


def add_to_db(filename):
    logging.info(f'add_to_db {filename=}')
    csv_data = pd.read_csv(path_to_files + filename, sep=';')
    code_startswith = str(csv_data._ixs(0)['АВС/ DEF'])[0]
    if Range.objects.filter(code_startswith=code_startswith).count():
        return
    
    ranges = [
        Range(
            code_startswith = str(row['АВС/ DEF'])[0], 
            code = row['АВС/ DEF'], 
            numbers_from = row['От'], 
            numbers_to = row['До'], 
            volume = row['Емкость'], 
            operator = row['Оператор'], 
            region = row['Регион'], 
            gar_region = row['Территория ГАР'], 
            inn = row['ИНН'] if not pd.isna(row['ИНН']) else None, 
        )
        for idr, row in csv_data.iterrows()
    ]
    Range.objects.bulk_create(ranges, batch_size=1000)


def main():
    download('https://opendata.digital.gov.ru/registry/numeric/downloads')
    for filename in filenames[1:]:
        add_to_db(filename)


if __name__ == '__main__':
    main()
