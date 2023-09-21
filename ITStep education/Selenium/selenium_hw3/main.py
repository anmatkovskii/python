import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Вкажіть шлях до вашого веб-драйверу
agent_007 = webdriver.Chrome(executable_path="D:\\Programming\\hw_itstep\\Selenium\\chromedriver.exe")

agent_007.get(url="https://mystat.itstep.org/en/auth/login/index?returnUrl=%2Fen%2Fmain%2Fdashboard%2Fpage%2Findex")
time.sleep(1)
username = agent_007.find_element(By.NAME, "username")
username.send_keys("Matko_kq46")
time.sleep(0.4)
password = agent_007.find_element(By.NAME, "password")
password.send_keys("Andrik8989A")
time.sleep(0.4)
agent_007.find_element(By.CLASS_NAME, "login-action").click()
time.sleep(3)
agent_007.find_element(By.CLASS_NAME, "schedule-item").click()
time.sleep(2)


file = open("rozklad.txt", "w")
name = agent_007.find_elements(By.CLASS_NAME, "active-day")
month = agent_007.find_element(By.CLASS_NAME, "mount")
file.write(f"                {month.text}\n")
for i in name:
    file.write(f"Lesson scheduled: {i.text}\n")
file.close()
agent_007.close()