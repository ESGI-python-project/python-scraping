import requests
import json
from bs4 import BeautifulSoup
import re


def request_page_html_content(params):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.46"
    }

    html_content = requests.get(f'https://www.google.com/search?q=', headers=headers, params=params).text

    return html_content


def get_resto_research_infos(nom_resto):
    #resto ="resto+plein+soleil"
    params = {'q':nom_resto}

    html_content = request_page_html_content(params)
    return html_content

def filtre_data(html_content):
    soup_content = BeautifulSoup(html_content, 'html.parser')
    search_data = soup_content.find('div', {'id': 'search'})

    data_res = search_data.find_all('div', {'class': 'g'})

    resto_note = list()

    for one_result in data_res:
        list_info = one_result.find('div', {'class': 'fG8Fp', 'class': 'uo4vr'})
        if list_info:  # avoid the search without notes
            url = one_result.find('a').attrs['href']
            note = list_info.find('span', text=re.compile("Note")).getText()

            site_name = url.split('.')[1]
            if "/" not in note:
                note = note + '/5'

            attr, note_score = note.split(':')
            data_note = {site_name: {attr: note_score}}

            resto_note.append(data_note)

    return resto_note


def get_resto_avis(nom_resto):
    html_content = get_resto_research_infos(nom_resto)
    data = filtre_data(html_content)

    return data


