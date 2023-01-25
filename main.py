import time
from selenium import webdriver
from selenium.webdriver.common.by import By


navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get('https://ri.americanas.io/')
navegador.implicitly_wait(100)
navegador.find_element(By.XPATH, '//*[@id="lang-pt-br"]/div[2]/div/div').click()
navegador.find_element(By.XPATH, '//*[@id="lang-pt-br"]/section/main/label').click()
navegador.find_element(By.XPATH, '//*[@id="lang-pt-br"]/main/section/div[2]/div/div/div[2]/a/figure/img').click()
time.sleep(15)

