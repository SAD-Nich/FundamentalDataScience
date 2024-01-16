import pandas as pd

df1 = pd.read_csv('modern goalkeepers/Alisson.csv', encoding='windows-1252')
df2 = pd.read_csv('modern goalkeepers/Claudio Bravo.csv', encoding='windows-1252')
df3 = pd.read_csv('modern goalkeepers/Ederson.csv', encoding='windows-1252')
df4 = pd.read_csv('modern goalkeepers/Neuer.csv', encoding='windows-1252')
df5 = pd.read_csv('modern goalkeepers/Onana.csv', encoding='windows-1252')
df6 = pd.read_csv('modern goalkeepers/terStegen.csv', encoding='windows-1252')
df7 = pd.read_csv('modern goalkeepers/Maignan.csv', encoding='windows-1252')
df8 = pd.read_csv('modern goalkeepers/Raya.csv', encoding='windows-1252')
df9 = pd.read_csv('modern goalkeepers/Pickford.csv', encoding='windows-1252')
df10 = pd.read_csv('modern goalkeepers/Donnaruma.csv', encoding='windows-1252')
merge = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10]
df = pd.concat(merge, ignore_index = True, sort=False)