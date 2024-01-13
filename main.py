from googlesearch import search
import random
from selenium import webdriver


websites=[]
searchQuery=input("Lūdzu ievadiet meklējamo frāzi: ")

for j in search(searchQuery, tld="co.in", num=10, stop=50, pause=2):
    websites.append(j)

randomWebsite=random.choice(websites)

driver=webdriver.Chrome()

driver.get(randomWebsite)

waitBeforeClosing=input()
while not waitBeforeClosing:
    sleep(10)