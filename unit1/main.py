from bs4 import BeautifulSoup
htmlfile = open("web/index.html", encoding="utf-8")
soup = BeautifulSoup(htmlfile, "lxml")
tag = soup.find_all(class_="about")
print(tag)
print(tag[0].text)