from bs4 import BeautifulSoup
import requests
import pandas as panda

url = 'https://www.channelnewsasia.com/'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

linktest = soup.select('div.media-object h6 a')

title=[]
link=[]
image=[]
category=[]
date = []
for l in soup.select('div.media-object h6 a'):
    title.append(l.get_text())
for t in soup.select('div.media-object h6 a'):
    link.append(t.attrs.get('href'))
for i in soup.select('div.media-object picture img.image'):
    image.append(i.attrs.get('src'))
for c in soup.select('div.media-object p a'):
    category.append(c.get_text())
for d in soup.select('div.media-object div.list-object__datetime-duration span'):
    date.append(d.get_text())
df = panda.DataFrame({'Titles' : title, 'Links' : link})
df2 = panda.DataFrame({'Images' : image})
df3 = panda.DataFrame({'Categories': category})
df4 = panda.DataFrame({'Time': date})

result = panda.concat([df,df2,df3,df4], axis=1)
print(result)
result.to_csv('CNAscrape.csv', index=False)
#print(df.head())
#print(df2.head())
#print(df3.head())
#print(df4.head())