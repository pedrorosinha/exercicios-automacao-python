from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os
from datetime import datetime
from pathlib import Path

application_path = Path(__file__).parent

now = datetime.now()
day_month_year = now.strftime("%d-%m-%Y") # DD-MM-YYYY

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
file_name = f"data/output/headlines-{day_month_year}.csv"

final_path = os.path.join(application_path, file_name)

df_headlines.to_csv(final_path)

driver.quit()