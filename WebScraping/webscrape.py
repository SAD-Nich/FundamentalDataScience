from bs4 import BeautifulSoup
import requests
import pandas as panda

url = 'https://www.rottentomatoes.com/'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
#title = soup.select('section.dynamic-poster-list a span.p--small')
#link = soup.select('section.dynamic-poster-list a ')
categorsad = soup.select('section.dynamic-poster-list h2')
####print("how many titles are available?",len(soup.select('section.dynamic-poster-list a span.p--small')))

actuallink = []
movietitle = []
category = []
image = []
scores = []
for a in soup.select('section.dynamic-poster-list a'):
    actuallink.append(a.attrs.get('href'))
for t in soup.select('section.dynamic-poster-list a span.p--small'):
    movietitle.append(t.get_text())
for c in soup.select('section.dynamic-poster-list h2'):
    category.append(c.get_text())
for i in soup.select('section.dynamic-poster-list a img'):
    image.append(i.attrs.get('src'))
for s in soup.select('section.dynamic-poster-list a score-pairs'):
    scores.append(s.attrs.get('criticsscore'))
df = panda.DataFrame({'movie' : movietitle, 'scores' : scores})
df2 = panda.DataFrame({'links':actuallink})
df3 = panda.DataFrame({'categories' : category})
df4 = panda.DataFrame({'image sources' : image})
table = panda.concat([df,df2,df3,df4], axis=0)
print(table)
table.to_csv('RottenTomatoesScraper.csv', index=False)
#print(df.head())
#print(df2.head())
#print(df3.head())
#print(df4.head())