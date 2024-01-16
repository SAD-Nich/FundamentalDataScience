import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv('traditional goalkeepers/Areola.csv', encoding='windows-1252')
df2 = pd.read_csv('traditional goalkeepers/Buffon.csv', encoding='windows-1252')
df3 = pd.read_csv('traditional goalkeepers/Iker.csv', encoding='windows-1252')
df4 = pd.read_csv('traditional goalkeepers/Cech.csv', encoding='windows-1252')
df5 = pd.read_csv('traditional goalkeepers/Lloris.csv', encoding='windows-1252')
df6 = pd.read_csv('traditional goalkeepers/Navas.csv', encoding='windows-1252')
df7 = pd.read_csv('traditional goalkeepers/Pope.csv', encoding='windows-1252')
df8 = pd.read_csv('traditional goalkeepers/Trapp.csv', encoding='windows-1252')
df9 = pd.read_csv('traditional goalkeepers/Oblak.csv', encoding='windows-1252')
df10 = pd.read_csv('traditional goalkeepers/Handanovic.csv', encoding='windows-1252')
merge = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10]
df = pd.concat(merge, ignore_index = True, sort=False)
