from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pandas import DataFrame as df
# import pandas as pd
import time

opt = Options()
opt.add_argument("start-maximized")
# opt.add_argument("--headless")
# opt.add_argument("--no-sandbox")
# opt.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=opt)

web = 'https://fortune.com/fortune500/2021/search/'

driver.get(web)

table = []

table_head = []
head_value = driver.find_elements(By.CLASS_NAME,"searchResults__columnTitle--1Brf4")

ranks = driver.find_elements(By.XPATH,".//div[@class='rt-td searchResults__cell--2Y7Ce searchResults__rank--1sTfo']/a/div/span")
country_name = driver.find_elements(By.XPATH,".//div[@class='rt-td searchResults__cell--2Y7Ce searchResults__title--3LyRA']/a/div/span/div")
revenues = driver.find_elements(By.XPATH,".//div[@class='rt-td searchResults__cell--2Y7Ce'][1]/a/div/span")
revenues_precent = driver.find_elements(By.XPATH,".//div[@class='rt-td searchResults__cell--2Y7Ce'][2]/a/div/span") 
profits = driver.find_elements(By.XPATH,".//div[@class='rt-td searchResults__cell--2Y7Ce'][3]/a/div/span")
profits_precent = driver.find_elements(By.XPATH,".//div[@class='rt-td searchResults__cell--2Y7Ce'][4]/a/div/span")
Assets = driver.find_elements(By.XPATH,".//div[@class='rt-td searchResults__cell--2Y7Ce'][5]/a/div/span")
market_value = driver.find_elements(By.XPATH,".//div[@class='rt-td searchResults__cell--2Y7Ce'][6]/a/div/span")
change_rank_1000 = driver.find_elements(By.XPATH,".//div[@class='rt-td searchResults__cell--2Y7Ce'][7]/a/div/span")
employees = driver.find_elements(By.XPATH,".//div[@class='rt-td searchResults__cell--2Y7Ce'][8]/a/div/span")
change_rank_500 = driver.find_elements(By.XPATH,".//div[@class='rt-td searchResults__cell--2Y7Ce'][9]/a/div/span")
measure_rank = driver.find_elements(By.XPATH,".//div[@class='rt-td searchResults__cell--2Y7Ce'][10]/a/div/span")

for table_value in head_value:
    table_head.append(table_value.text)
table.append(table_head)

for i in range(len(ranks)):
    table_body = []

    table_body.append(ranks[i].text)
    table_body.append(country_name[i].text)
    table_body.append(revenues[i].text)
    table_body.append(revenues_precent[i].text)
    table_body.append(profits[i].text)
    table_body.append(profits_precent[i].text)
    table_body.append(Assets[i].text)
    table_body.append(market_value[i].text)
    table_body.append(change_rank_1000[i].text)
    table_body.append(employees[i].text)
    table_body.append(change_rank_500[i].text)
    table_body.append(measure_rank[i].text)

    table.append(table_body)

# print(table)

dataframe = df(table)
dataframe.to_csv("fotune_10.csv",index=False,encoding='utf-8')


driver.implicitly_wait(10)
driver.quit()
