from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

url = 'https://howlongtobeat.com/?q='

title = 'Stray'

data = {'queryString': title}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'keep-alive',
    'Referer': 'https://howlongtobeat.com/search_results',
}

## Selenium
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

driver.get(url + title)
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
url_game = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[5]/ul/li[1]/div/div[2]/h2/a').get_attribute('href')

driver.close

response = requests.get(url_game, headers=headers).text

soup = BeautifulSoup(response, 'lxml')

users_quant = soup.find('div', class_='GameHeader_profile_details__oQTrK')

print(users_quant.get_text())


url_ggdeals = f'https://gg.deals/game/stray/'

response = requests.get(url_ggdeals).text
soup = BeautifulSoup(response, 'lxml')
#print(soup)
#deals = soup.find('div', class_='header-game-prices-content-inner d-flex flex-wrap')
plataforms = soup.find('div', class_='game-header-platform-tabs')
links = plataforms.find_all('a')
for link in links:
    print(link.get('href'))
