import bs4


from bs4 import BeautifulSoup
import requests
import re

html_text = requests.get("https://scottsdalepublicart.org/work/don-quixote/").text

images = []

soup = BeautifulSoup(html_text, "html.parser")
bs = soup.find_all('div', class_ = "carousel-cell")
bs = list(bs)
# print(len(bs))
for image in bs: 
    img = image.find('img', {'src':re.compile('.jpg')})
    images.append(img['src'])

dsp = soup.find('div', class_ = "sa-exhibition-body-content")

# desc_txt = dsp.find_all('p').text
# print(desc_txt)
for p in dsp:
    desc_txt = p.find('p')
    print(desc_txt)


# print(images)
