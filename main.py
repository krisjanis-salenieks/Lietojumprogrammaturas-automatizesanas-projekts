from googlesearch import search
import random
from selenium import webdriver
import time

def selectRandomWebsite(websites):
    randomWebsite=random.choice(websites)

    driver=webdriver.Chrome()
    driver.get(randomWebsite)
    time.sleep(2)
    input("Uzspiediet ENTER lai aizvērtu pārlūka logu")

def selectPrompt():
    websites=[]
    searchQuery=input("Lūdzu ievadiet meklējamo frāzi: ")

    for j in search(searchQuery, tld="co.in", num=10, stop=10, pause=2):
        websites.append(j)

    return websites

repeatWebsitePrompt=True
randomizeWebsite=True

while repeatWebsitePrompt:
    websites = selectPrompt()
    randomizeWebsite=True
    while randomizeWebsite:
        selectRandomWebsite(websites)
        repeatWebsiteVar=input("Vai jūs vēlaties izvēlēties citu mājalapu izmantojot šo pašu meklējamo frāzi? (j/n): ")
        while not repeatWebsiteVar:
            time.sleep(10)
        if repeatWebsiteVar=="n":
            randomizeWebsite=False
        
    repeatSearchVar=input("Vai jūs vēlaties ievadīt citu meklējamo frāzi? (j/n): ")
    while not repeatSearchVar:
            time.sleep(10)
    if repeatSearchVar=="n":
        repeatWebsitePrompt=False