from googlesearch import search

websites=[]
searchQuery = input("Lūdzu ievadiet meklējamo frāzi: ")

for j in search(searchQuery, tld="co.in", num=10, stop=100, pause=2):
    websites.append(j)

print(websites)
print(len(websites))