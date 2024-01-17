import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv('modern goalkeepers/Alisson.csv', encoding='windows-1252')
df2 = pd.read_csv('modern goalkeepers/Claudio Bravo.csv', encoding='windows-1252')
df3 = pd.read_csv('modern goalkeepers/Donnaruma.csv', encoding='windows-1252')
df4 = pd.read_csv('modern goalkeepers/Ederson.csv', encoding='windows-1252')
df5 = pd.read_csv('modern goalkeepers/Maignan.csv', encoding='windows-1252')
df6 = pd.read_csv('modern goalkeepers/Neuer.csv', encoding='windows-1252')
df7 = pd.read_csv('modern goalkeepers/Onana.csv', encoding='windows-1252')
df8 = pd.read_csv('modern goalkeepers/terStegen.csv', encoding='windows-1252')
df9 = pd.read_csv('modern goalkeepers/Raya.csv', encoding='windows-1252')
df10 = pd.read_csv('modern goalkeepers/Pickford.csv', encoding='windows-1252')
merge = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10]
df = pd.concat(merge, ignore_index = True, sort=False)
Saves = df.iloc[:,0:26]
Saves = Saves.fillna(0)
NAdf = df.dropna().reset_index(drop=True)

NAdf = NAdf.drop('Country', axis = 1)
NAdf = NAdf.drop('Comp', axis =1)

NAdf = NAdf.rename(columns = {'Cmp.1':'SPCmp', 'Cmp.2':'MPCmp', 'Cmp.3':'LPCmp'})
NAdf = NAdf.rename(columns = {'Att.1':'SPAtt', 'Att.2':'MPAtt','Att.3':'LPAtt'})
NAdf = NAdf.rename(columns = {'Cmp%.1':'SPCmp%','Cmp%.2':'MPCmp%','Cmp%.3':'LPCmp%'})

season2018 = NAdf['Season'] == '2017-2018'
season2018 = NAdf[season2018].reset_index(drop=True)
season2019 = NAdf['Season'] == '2018-2019'
season2019 = NAdf[season2019].reset_index(drop=True)
season2020 = NAdf['Season'] == '2019-2020'
season2020 = NAdf[season2020].reset_index(drop=True)
season2021 = NAdf['Season'] == '2020-2021'
season2021 = NAdf[season2021].sample(8).reset_index(drop=True)
season2022 = NAdf['Season'] == '2021-2022'
season2022 = NAdf[season2022].reset_index(drop=True)
season2023 = NAdf['Season'] == '2022-2023'
season2023 = NAdf[season2023].sample(8).reset_index(drop=True)

saves2016 = Saves['Season'] == '2015-2016'
saves2016 = Saves[saves2016].reset_index(drop=True)
saves2016chart = saves2016.iloc[:,[2,12,13,14]].set_index('Squad',drop=True)
CS2016 = saves2016[['MP','CS','CS%','Squad']].set_index('Squad',drop=True)

season2022chart = season2022.iloc[:,[2,29,30,31,32,33,34,35,36,37]]
season2022chart = season2022chart.set_index('Squad', drop=True)
season2019chart = season2019.iloc[:,[2,29,30,31,32,33,34,35,36,37]]
season2019chart = season2019chart.set_index('Squad', drop=True)

season2023total = season2023[['Att','Squad']].set_index('Squad', drop=True)

AlissonPass2018 = season2018['Squad'] == 'Roma'
AlissonPass2018 = season2018[AlissonPass2018]
AlissonPass2023 = season2023['Squad'] == 'Liverpool'
AlissonPass2023 = season2023[AlissonPass2023]
AlissonPass = pd.concat([AlissonPass2018, AlissonPass2023])
AlissonPass = AlissonPass.iloc[:,[2,29,30,31,32,33,34,35,36,37]].set_index('Squad', drop=True)

Neuer2019 = season2019['Squad'] == 'Bayern Munich'
Neuer2019 = season2019[Neuer2019]
Neuer2022 = season2022['Squad'] == 'Bayern Munich'
Neuer2022 = season2022[Neuer2022]
Neuer2019 = Neuer2019[['SPAtt','MPAtt','LPAtt','Season']].set_index('Season', drop=True)
Neuer2022 = Neuer2022[['SPAtt','MPAtt','LPAtt','Season']].set_index('Season', drop=True)
Neuer2019 = pd.DataFrame(Neuer2019.iloc[0])
Neuer2022 = pd.DataFrame(Neuer2022.iloc[0])

season2019chart.plot(kind='bar',title='Modern Goalkeepers Passes in 2018/2019 Season')
season2022chart.plot(kind='bar',title='Modern Goalkeepers Passes in 2021/2022 Season')

season2023total.plot(kind='line',color='red',label='2023',title='Comparison of Attempted Passes (Att) of Last 5 Years',figsize=(20,15))
season2018['Att'].plot(kind='line',color='cyan',label='Att 2018')
season2019['Att'].plot(kind='line',color='blue',label='Att 2019')
season2020['Att'].plot(kind='line',color='navy',label='Att 2020')
season2021['Att'].plot(kind='line',color='purple',label='Att 2021')
season2022['Att'].plot(kind='line',color='magenta',label='Att 2022')
plt.legend(loc='upper left')

saves2016chart.plot(kind='bar', title ='Modern Goalkeepers Save Percentages in 2015',figsize=(20,15))
saves2016chart['Save%'].plot(color='green')

AlissonPass.plot(kind='bar', title ='Alisson Passing Rate 2018 vs 2023')

CS2016.plot(kind='bar', title ='Clean Sheet Rate in 2015/2016')
plt.show()

def NeuerPassRate2019():
    Passes = Neuer2019.index
    data = Neuer2019['2018-2019']
    explode = (0.1, 0.0, 0.2,)
    colors = ( "orange", "cyan", "brown",
    		"grey", "indigo", "beige")
    wp = { 'linewidth' : 0.5, 'edgecolor' : "blue" }

    def func(pct, allvalues):
    	absolute = int(pct / 100.*np.sum(allvalues))
    	return "{:.1f}%\n({:d} PAtt)".format(pct, absolute)

    fig, ax = plt.subplots(figsize =(10, 7))
    wedges, texts, autotexts = ax.pie(data, 
    								autopct = lambda pct: func(pct, data),
    								explode = explode, 
    								labels = Passes,
    								shadow = True,
    								colors = colors,
    								startangle = 90,
    								wedgeprops = wp,
    								textprops = dict(color ="magenta"))
    ax.legend(wedges, Passes,
    		title ="Pass Types",
    		loc ="center left",
    		bbox_to_anchor =(1, 0, 0.5, 1))		
    plt.setp(autotexts, size = 8, weight ="bold")
    ax.set_title("Neuer Passing Rate 2019")
    plt.show()

def NeuerPassRate2022():
    Passes = Neuer2022.index
    data = Neuer2022['2021-2022']
    explode = (0.1, 0.0, 0.2,)
    colors = ( "orange", "cyan", "brown",
    		"grey", "indigo", "beige")
    wp = { 'linewidth' : 0.5, 'edgecolor' : "blue" }

    def func(pct, allvalues):
    	absolute = int(pct / 100.*np.sum(allvalues))
    	return "{:.1f}%\n({:d} PAtt)".format(pct, absolute)

    fig, ax = plt.subplots(figsize =(10, 7))
    wedges, texts, autotexts = ax.pie(data, 
    								autopct = lambda pct: func(pct, data),
    								explode = explode, 
    								labels = Passes,
    								shadow = True,
    								colors = colors,
    								startangle = 90,
    								wedgeprops = wp,
    								textprops = dict(color ="magenta"))
    ax.legend(wedges, Passes,
    		title ="Pass Types",
    		loc ="center left",
    		bbox_to_anchor =(1, 0, 0.5, 1))		
    plt.setp(autotexts, size = 8, weight ="bold")
    ax.set_title("Neuer Passing Rate 2023")
    plt.show()
