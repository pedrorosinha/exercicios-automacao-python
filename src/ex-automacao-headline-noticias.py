from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)

driver.get(website)


containers = driver.find_elements(by="xpath", value='//div[@class="story__copy-container"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./a/h3').text
    subtitle = container.find_element(by="xpath", value='./a/p').text
    link = container.find_element(by="xpath", value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {
    "Title": titles,
    "Subtitle": subtitles,
    "Link": links
}

df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv("data/output/headlines-headless.csv")

driver.quit()