import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, Birch, DBSCAN
from sklearn.metrics import calinski_harabasz_score, silhouette_score, davies_bouldin_score

data = pd.read_csv('Bayern.csv',encoding='latin1')
data = data.dropna()
data = data.drop(['Nation','Pos','Age','Player'],axis=1)
data.index = data.index + 1

datascaler = StandardScaler()
scaled_data = datascaler.fit_transform(data)

dbscandata = DBSCAN(eps=1,min_samples=2)
with pd.option_context('mode.chained_assignment', None):
    data.loc[:,'cluster']=dbscandata.fit_predict(scaled_data)

birchdata = Birch(threshold=1, branching_factor=50, n_clusters=2)
with pd.option_context('mode.chained_assignment', None):
    data.loc[:,'cluster']=birchdata.fit_predict(scaled_data)

agglomerativedata = AgglomerativeClustering(n_clusters=2,linkage='ward')
with pd.option_context('mode.chained_assignment', None):
    data.loc[:,'cluster']=agglomerativedata.fit_predict(scaled_data)

with pd.option_context('mode.chained_assignment', None):
    kmeans = KMeans(n_clusters=2,random_state=21,n_init=5)
    data['cluster']=kmeans.fit_predict(scaled_data)

# KMeans clustering
kmeans = KMeans(n_clusters=2)
kmeans_labels = kmeans.fit_predict(scaled_data)
kmeans_silhouette = silhouette_score(scaled_data, kmeans_labels)
kmeans_davies_bouldin = davies_bouldin_score(scaled_data, kmeans_labels)
kmeans_calinski_harabasz = calinski_harabasz_score(scaled_data, kmeans_labels)

# DBSCAN clustering
dbscan = DBSCAN(eps=1, min_samples=2)
dbscan_labels = dbscan.fit_predict(scaled_data)
dbscan_silhouette = silhouette_score(scaled_data, dbscan_labels)
dbscan_davies_bouldin = davies_bouldin_score(scaled_data, dbscan_labels)
dbscan_calinski_harabasz = calinski_harabasz_score(scaled_data, dbscan_labels)

# Agglomerative Clustering
agg_cluster = AgglomerativeClustering(n_clusters=2)
agg_labels = agg_cluster.fit_predict(scaled_data)
agg_silhouette = silhouette_score(scaled_data, agg_labels)
agg_davies_bouldin = davies_bouldin_score(scaled_data, agg_labels)
agg_calinski_harabasz = calinski_harabasz_score(scaled_data, agg_labels)

# BIRCH clustering
birch = Birch(threshold=1, branching_factor=50, n_clusters=2)
birch_labels = birch.fit_predict(scaled_data)
birch_silhouette = silhouette_score(scaled_data, birch_labels)
birch_davies_bouldin = davies_bouldin_score(scaled_data, birch_labels)
birch_calinski_harabasz = calinski_harabasz_score(scaled_data, birch_labels)

# Displaying scores
print("Silhouette Scores     :", [kmeans_silhouette, agg_silhouette, dbscan_silhouette, birch_silhouette])
print("Davies Bouldin Indices:", [kmeans_davies_bouldin, agg_davies_bouldin, dbscan_davies_bouldin, birch_davies_bouldin])
print("Calinski-Harabasz Score:", [kmeans_calinski_harabasz, agg_calinski_harabasz, dbscan_calinski_harabasz, birch_calinski_harabasz])