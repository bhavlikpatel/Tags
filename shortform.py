from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def webscrap(word):
    try :
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(options=chrome_options)

        driver.get(f"https://www.abbreviations.com/abbreviation/{word}")

        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')

        td_element = soup.find('td', class_='tal tm fsl')

        a_element = td_element.find('a')

        abbreviation = a_element.text
        driver.quit()
        return abbreviation

    except Exception as e:
        return None