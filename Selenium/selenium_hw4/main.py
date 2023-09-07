import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Вкажіть шлях до вашого веб-драйверу
agent_007 = webdriver.Chrome(executable_path="D:\\Programming\\hw_itstep\\Selenium\\chromedriver.exe")

agent_007.get(url="https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1671713186&rver=7.0.6737.0&wp=MBI_SSL"
                  "&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b"
                  "-df2f57b9e44c%26RpsCsrfState%3dca251bfd-abd2-2200-6c13-70908266aa17&id=292841&aadredir=1&whr"
                  "=outlook.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c")
time.sleep(1)
username = agent_007.find_element(By.XPATH, '//*[@id="i0116"]')
username.send_keys("your email")
time.sleep(1)
agent_007.find_element(By.XPATH, '//*[@id="lightbox"]/div[3]/div/div/div/div[4]/div/div/div/div').click()
time.sleep(1)
password = agent_007.find_element(By.XPATH, '//*[@id="i0118"]')
password.send_keys("your password")
time.sleep(1)
agent_007.find_element(By.XPATH, '//*[@id="lightbox"]/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div').click()
time.sleep(1)
agent_007.find_element(By.XPATH, '//*[@id="lightbox"]/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]').click()
time.sleep(5)
agent_007.find_element(By.XPATH, '//*[@id="innerRibbonContainer"]/div[1]/div/div/div/div[2]/div/span/button[1]').click()
time.sleep(3)
address = agent_007.find_element(By.XPATH, '//*[@id="docking_InitVisiblePart_0"]/div/div[1]/div[1]/div/div['
                                           '3]/div/div/div[1]')
address.send_keys("sasha.ozerov98@gmail.com")
time.sleep(3)
content = agent_007.find_element(By.XPATH, '//*[@id="editorParent_1"]/div')
content.send_keys("Test Test Test")
time.sleep(3)
agent_007.find_element(By.XPATH, '//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[3]/div[1]/div/div/span/button[1]').click()
time.sleep(3)
agent_007.find_element(By.XPATH, '//*[@id="ok-1"]').click()
time.sleep(3)

agent_007.close()