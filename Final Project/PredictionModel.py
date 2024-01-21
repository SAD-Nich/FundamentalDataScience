import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

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
Mdf = pd.concat(merge, ignore_index = True, sort=False)

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

Combined = [Mdf, Tdf]
Combined = pd.concat(Combined, ignore_index = True, sort=False)

Combined = Combined.rename(columns = {'Cmp.1':'SPCmp', 'Cmp.2':'MPCmp', 'Cmp.3':'LPCmp'})
Combined = Combined.rename(columns = {'Att.1':'SPAtt', 'Att.2':'MPAtt','Att.3':'LPAtt'})
Combined = Combined.rename(columns = {'Cmp%.1':'SPCmp%','Cmp%.2':'MPCmp%','Cmp%.3':'LPCmp%'})
Combined = Combined.fillna(0)
Combined['Win'] = Combined['Awards']
Combined['Win'] = Combined.apply(lambda row: 1 if row['Win']!= 0 else 0, axis =1 ).astype(int)
Combined = Combined.drop('Season', axis=1)
Combined = Combined.drop('Squad', axis=1)
Combined = Combined.drop('Country', axis=1)
Combined = Combined.drop('Comp', axis=1)
Combined = Combined.drop('LgRank', axis=1)
Combined = Combined.drop('Min', axis=1)

y = Combined['Win']
X = Combined[['Cmp','Att','Saves','CS','W']]
#X = Combined.drop('Win', axis=1)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=100)

model= LogisticRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
print (X_test) #test dataset
print (y_pred) #predicted values

print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))
print('Recall: ',metrics.recall_score(y_test, y_pred, zero_division=1))
print("Precision:",metrics.precision_score(y_test, y_pred, zero_division=1))
print("CL Report:",metrics.classification_report(y_test, y_pred, zero_division=1))

y_pred_proba= model.predict_proba(X_test) [::,1]
false_positive_rate, true_positive_rate, _ = metrics.roc_curve(y_test, y_pred_proba)
auc= metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(false_positive_rate, true_positive_rate,label="AUC="+str(auc))
plt.title('ROC Curve')
plt.ylabel('True Positive Rate')
plt.xlabel('false Positive Rate')
plt.legend(loc=4)