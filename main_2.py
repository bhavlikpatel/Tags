import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=chrome_options)

def webscrap(word):
    try :
        driver.get(f"https://www.abbreviations.com/abbreviation/{word}")

        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')

        td_element = soup.find('td', class_='tal tm fsl')

        a_element = td_element.find('a')

        abbreviation = a_element.text
        return abbreviation

    except Exception as e:
        return None

def tagstandard(tagexcel):
    try:
        start_time = time.time()
        tag_list = pd.read_excel(tagexcel)
        tag_list['TagShort'] = 'Not Found'
        for index, row in tag_list.iterrows():
            cell_value = row['Tag']
            input_word = cell_value.split()
            tag_short_list = []
            for word in input_word:
                abb = webscrap(word.upper())
                if abb is not None:
                    tag_short_list.append(abb)
                else:
                    tag_short_list.append(word)              
            tag = '_'.join(tag_short_list)
            tag_list.at[index, 'TagShort'] = tag
        end_time = time.time()
        print(end_time-start_time)
        return tag_list.to_excel('Updated.xlsx', index=False)
    except Exception as e:
        print(e)

tagexcel = 'Taglist.xlsx'
tagstandard(tagexcel)
driver.quit()