import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Вкажіть шлях до вашого веб-драйверу
agent_007 = webdriver.Chrome(executable_path="D:\\Programming\\hw_itstep\\Selenium\\chromedriver.exe")

agent_007.get(url="https://www.marvel.com/characters")

get_links = []
links = agent_007.find_elements(By.CLASS_NAME, "grid-base.grid__6 a.explore__link")

file = open("characters.txt", "w")
for i in links:
    get_links.append(i.get_attribute("href"))
for i in get_links:
    agent_007.get(url=i)
    name = agent_007.find_elements(By.CLASS_NAME, "masthead__headline")
    file.write(f"Hero: {name[0].text}\n")
    info_type = agent_007.find_elements(By.CLASS_NAME, "railBioInfoItem__label")
    info_content = agent_007.find_elements(By.CLASS_NAME, "railBioLinks")
    if info_content:
        for j in range(len(info_content)):
            file.write(f"{info_type[j].text}: {info_content[j].text}\n")
    else:
        file.write(f"No info found about this character")
    file.write("\n")
file.close()
agent_007.close()