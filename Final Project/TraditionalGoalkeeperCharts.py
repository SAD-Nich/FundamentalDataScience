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
Saves = df.iloc[:,0:26]
Saves = Saves.fillna(0)
NAdf = df.dropna()

NAdf = NAdf.drop('Country', axis = 1)
NAdf = NAdf.drop('Comp', axis =1)

NAdf = NAdf.rename(columns = {'Cmp.1':'SPCmp', 'Cmp.2':'MPCmp', 'Cmp.3':'LPCmp'})
NAdf = NAdf.rename(columns = {'Att.1':'SPAtt', 'Att.2':'MPAtt','Att.3':'LPAtt'})
NAdf = NAdf.rename(columns = {'Cmp%.1':'SPCmp%','Cmp%.2':'MPCmp%','Cmp%.3':'LPCmp%'})

season2018 = NAdf['Season'] == '2017-2018'
season2018 = NAdf[season2018].sample(8).reset_index(drop=True)
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

season2023chart = season2023.iloc[:,[2,29,30,31,32,33,34,35,36,37]]
season2023chart = season2023chart.set_index('Squad', drop=True)
season2018chart = season2018.iloc[:,[2,29,30,31,32,33,34,35,36,37]]
season2018chart = season2018chart.set_index('Squad', drop=True)

KeylorNavas2018 = season2018['Squad'] == 'Real Madrid'
KeylorNavas2018 = season2018[KeylorNavas2018].reset_index(drop=True)
KeylorNavas2023 = season2023['Squad'] == "Nott'ham Forest"
KeylorNavas2023 = season2023[KeylorNavas2023].reset_index(drop=True)
KeylorNavas = pd.concat([KeylorNavas2018,KeylorNavas2023])
NavasPass = KeylorNavas.iloc[:,[2,29,30,31,32,33,34,35,36,37]].set_index('Squad', drop=True)

Buffon2018 = season2018['Squad'] == 'Juventus'
Buffon2018 = season2018[Buffon2018].reset_index(drop=True)
Buffon2023 = season2023['Squad'] == 'Parma'
Buffon2023 = season2023[Buffon2023].reset_index(drop=True)
Buffon = pd.concat([Buffon2018,Buffon2023])
BuffonPass = Buffon.iloc[:,[2,29,30,31,32,33,34,35,36,37]].set_index('Squad', drop=True)

Oblak2018 = season2018['Squad'] == 'Atlético Madrid'
Oblak2018 = season2018[Oblak2018].reset_index(drop=True)
Oblak2023 = season2023['Squad'] == 'Atlético Madrid'
Oblak2023 = season2023[Oblak2023].reset_index(drop=True)
Oblak = pd.concat([Oblak2018,Oblak2023])
OblakPass = Oblak2018[['SPAtt','MPAtt','LPAtt','Season']].set_index('Season',drop=True)
OblakPass = pd.DataFrame(OblakPass.iloc[0])
OblakPass2 = Oblak2023[['SPAtt','MPAtt','LPAtt','Season']].set_index('Season',drop=True)
OblakPass2 = pd.DataFrame(OblakPass2.iloc[0])

season2023total = season2023[['Att','Squad']].set_index('Squad', drop=True)

season2018chart.plot(kind='bar',title='Traditional Goalkeepers Passes in 2017/2018 Season')
season2023chart.plot(kind='bar',title='Traditional Goalkeepers Passes in 2022/2023 Season')

season2023total.plot(kind='line',color='red',label='2023',title='Comparison of Attempted Passes (Att) of Last 5 Years',figsize=(20,15))
season2018['Att'].plot(kind='line',color='cyan',label='Att 2018')
season2019['Att'].plot(kind='line',color='blue',label='Att 2019')
season2020['Att'].plot(kind='line',color='navy',label='Att 2020')
season2021['Att'].plot(kind='line',color='purple',label='Att 2021')
season2022['Att'].plot(kind='line',color='magenta',label='Att 2022')
plt.legend(loc='upper left')

NavasPass.plot(kind='bar',title='Keylor Navas 2018 Vs. 2023')
BuffonPass.plot(kind='bar',title='Gianluigi Buffon 2018 Vs. 2023')

def OblakPassRate2018():
    Passes = OblakPass.index
    data = OblakPass['2017-2018']
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
    ax.set_title("Oblak Passing Rate 2018")
    plt.show()

def OblakPassRate2023():
    Passes = OblakPass2.index
    data = OblakPass2['2022-2023']
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
    ax.set_title("Oblak Passing Rate 2023")
    plt.show()

saves2016chart.plot(kind='bar', title ='Traditional Goalkeepers Save Percentages in 2015',figsize=(20,15))
saves2016chart['Save%'].plot(color='green')

CS2016.plot(kind='bar', title ='Clean Sheet Rate in 2015/2016')
plt.show()