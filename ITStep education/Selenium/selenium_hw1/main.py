from selenium import webdriver
from selenium.webdriver.common.by import By

# Вкажіть шлях до вашого веб-драйверу
agent_007 = webdriver.Chrome(executable_path="D:\\Programming\\hw_itstep\\Selenium\\chromedriver.exe")

agent_007.get(url="https://www.marvel.com/comics?&options%5Boffset%5D=0&totalcount=12")

comix_name = agent_007.find_elements(By.CLASS_NAME, "row-item-text")

file = open("comix.txt", "w")
for i in comix_name:
    file.write(f"{i.text}\n")
    file.write("\n")
file.close()

agent_007.close()