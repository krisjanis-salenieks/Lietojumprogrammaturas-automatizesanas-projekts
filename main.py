from googlesearch import search
import random
from selenium import webdriver

def selectRandomWebsite(websites):
    randomWebsite=random.choice(websites)

    driver=webdriver.Chrome()
    driver.get(randomWebsite)

def selectPrompt():
    websites=[]
    searchQuery=input("Lūdzu ievadiet meklējamo frāzi: ")

    for j in search(searchQuery, tld="co.in", num=10, stop=10, pause=2):
        websites.append(j)

    return websites

while True:
    websites = selectPrompt()
    while True:
        selectRandomWebsite(websites)
        repeatWebsiteVar=input("Vai jūs vēlaties izvēlēties citu mājalapu izmantojot šo pašu meklējamo frāzi? N-Nē, Jebkas cits-Jā: ")
        if repeatWebsiteVar=="N":
            break
        while not repeatWebsiteVar:
            sleep(10)
        
    repeatSearchVar=input("Vai jūs vēlaties ievadīt citu meklējamo frāzi? N-Nē, Jebkas cits-Jā: ")
    if repeatWebsiteVar=="N":
        break
    while not repeatSearchVar:
            sleep(10)
    