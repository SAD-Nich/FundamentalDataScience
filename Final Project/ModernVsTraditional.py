import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Mdf1 = pd.read_csv('modern goalkeepers/Alisson.csv', encoding='windows-1252')
Mdf2 = pd.read_csv('modern goalkeepers/Claudio Bravo.csv', encoding='windows-1252')
Mdf3 = pd.read_csv('modern goalkeepers/Donnaruma.csv', encoding='windows-1252')
Mdf4 = pd.read_csv('modern goalkeepers/Ederson.csv', encoding='windows-1252')
Mdf5 = pd.read_csv('modern goalkeepers/Maignan.csv', encoding='windows-1252')
Mdf6 = pd.read_csv('modern goalkeepers/Neuer.csv', encoding='windows-1252')
Mdf7 = pd.read_csv('modern goalkeepers/Onana.csv', encoding='windows-1252')
Mdf8 = pd.read_csv('modern goalkeepers/terStegen.csv', encoding='windows-1252')
Mdf9 = pd.read_csv('modern goalkeepers/Raya.csv', encoding='windows-1252')
Mdf10 = pd.read_csv('modern goalkeepers/Pickford.csv', encoding='windows-1252')
merge = [Mdf1, Mdf2, Mdf3, Mdf4, Mdf5, Mdf6, Mdf7, Mdf8, Mdf9, Mdf10]
df = pd.concat(merge, ignore_index = True, sort=False)
MSaves = df.iloc[:,0:26]
MSaves = MSaves.fillna(0)
MNAdf = df.dropna()

MNAdf = MNAdf.drop('Country', axis = 1)
MNAdf = MNAdf.drop('Comp', axis =1)

MNAdf = MNAdf.rename(columns = {'Cmp.1':'SPCmp', 'Cmp.2':'MPCmp', 'Cmp.3':'LPCmp'})
MNAdf = MNAdf.rename(columns = {'Att.1':'SPAtt', 'Att.2':'MPAtt','Att.3':'LPAtt'})
MNAdf = MNAdf.rename(columns = {'Cmp%.1':'SPCmp%','Cmp%.2':'MPCmp%','Cmp%.3':'LPCmp%'})

Tdf1 = pd.read_csv('traditional goalkeepers/Areola.csv', encoding='windows-1252')
Tdf2 = pd.read_csv('traditional goalkeepers/Buffon.csv', encoding='windows-1252')
Tdf3 = pd.read_csv('traditional goalkeepers/Iker.csv', encoding='windows-1252')
Tdf4 = pd.read_csv('traditional goalkeepers/Cech.csv', encoding='windows-1252')
Tdf5 = pd.read_csv('traditional goalkeepers/Lloris.csv', encoding='windows-1252')
Tdf6 = pd.read_csv('traditional goalkeepers/Navas.csv', encoding='windows-1252')
Tdf7 = pd.read_csv('traditional goalkeepers/Pope.csv', encoding='windows-1252')
Tdf8 = pd.read_csv('traditional goalkeepers/Trapp.csv', encoding='windows-1252')
Tdf9 = pd.read_csv('traditional goalkeepers/Oblak.csv', encoding='windows-1252')
Tdf10 = pd.read_csv('traditional goalkeepers/Handanovic.csv', encoding='windows-1252')
Tmerge = [Tdf1, Tdf2, Tdf3, Tdf4, Tdf5, Tdf6, Tdf7, Tdf8, Tdf9, Tdf10]
Tdf = pd.concat(Tmerge, ignore_index = True, sort=False)
TSaves = Tdf.iloc[:,0:26]
TSaves = TSaves.fillna(0)
TNAdf = Tdf.dropna()

TNAdf = TNAdf.drop('Country', axis = 1)
TNAdf = TNAdf.drop('Comp', axis =1)

TNAdf = TNAdf.rename(columns = {'Cmp.1':'SPCmp', 'Cmp.2':'MPCmp', 'Cmp.3':'LPCmp'})
TNAdf = TNAdf.rename(columns = {'Att.1':'SPAtt', 'Att.2':'MPAtt','Att.3':'LPAtt'})
TNAdf = TNAdf.rename(columns = {'Cmp%.1':'SPCmp%','Cmp%.2':'MPCmp%','Cmp%.3':'LPCmp%'})

Tra2018 =  TNAdf['Season'] == '2018-2019'
Tra2018 = TNAdf[Tra2018].reset_index(drop=True)
Mod2018 = MNAdf['Season'] == '2018-2019'
Mod2018 = MNAdf[Mod2018].reset_index(drop=True)
Tra2022 = TNAdf['Season'] == '2021-2022'
Tra2022 = TNAdf[Tra2022].reset_index(drop=True)
Mod2022 = MNAdf['Season'] == '2021-2022'
Mod2022 = MNAdf[Mod2022].reset_index(drop=True)
TraPass2018 = Tra2018.iloc[:,[2,29,30,31,32,33,34,35,36,37]].set_index('Squad',drop=True)
ModPass2018 = Mod2018.iloc[:,[2,29,30,31,32,33,34,35,36,37]].set_index('Squad',drop=True)

Mod2018['Att'].plot(label = 'Modern Goalkeepers',title = 'Passing Attempts Made In 2018')
Tra2018['Att'].plot(label = 'Traditional Goalkeepers')
plt.legend(loc = 'upper left')
plt.show()

Mod2022['Cmp'].plot(label = 'Modern Goalkeepers',title = 'Completed Passes Made In 2022')
Tra2022['Cmp'].plot(label = 'Traditional Goalkeepers')
plt.legend(loc = 'upper left')
plt.show()

Mod2022['Saves'].plot(label = 'Modern Goalkeepers',title = 'Modern Vs Traditional Goalkeepers Saves in 2022')
Tra2022['Saves'].plot(label = 'Traditional Goalkeepers')
plt.legend(loc = 'upper left')
plt.show()

Mod2018['Save%'].plot(label = 'Modern Goalkeepers',title = 'Modern Vs Traditional Goalkeepers Save% in 2018')
Tra2018['Save%'].plot(label = 'Traditional Goalkeepers')
plt.legend(loc = 'upper left')
plt.show()