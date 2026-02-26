from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()

movies = []

offsets = [0, 200, 400, 600, 800]

for offset in offsets:
    url = f"https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW&offset={offset}"
    driver.get(url)
    time.sleep(3)
    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) < 4:
            continue
        rank = cols[0].text if cols[0].text else "NAN"
        title = cols[1].text if cols[1].text else "NAN"
        gross = cols[2].text if cols[2].text else "NAN"
        year = cols[3].text if cols[3].text else "NAN"

        movies.append([rank, title, year, gross])

driver.quit()

with open("movies.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Rank", "Title", "Year", "Lifetime Gross"])
    writer.writerows(movies)

print("successfully.")
