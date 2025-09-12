# Import 
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import seaborn as sns
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

# Config
SEED = 2025 

# Read data and process
df = pd.read_csv("Wholesale customers data.csv")
df.drop(['Channel','Region'],axis = 1, inplace = True)
X_scaled = StandardScaler().fit_transform(df)

# Aux
def plot_k_dist_graph(X, k):
    # Compute the knn
    neigh = NearestNeighbors(n_neighbors=k)
    neigh.fit(X)
    distances, _ = neigh.kneighbors(X)
    # Sort distances
    k_distances = np.sort(distances[:, k-1])
    # Plot 
    plt.figure(figsize=(10, 6))
    plt.plot(k_distances)
    plt.grid(True)
    plt.yticks([0,0.5,1,1.5,2,2.5]) # Hardcoded for now
    plt.show()

for min_samples in [3,5,8]:
    plot_k_dist_graph(X_scaled,min_samples)

# 1)   
dbscan = DBSCAN(eps=1, min_samples=3)
dbscan_labels = dbscan.fit_predict(X_scaled)

unique_labels = set(dbscan_labels)
palette = sns.color_palette("Set1", len(unique_labels))
color_map = {
    label: palette[i] if label != -1 else (0.6, 0.6, 0.6)
    for i, label in enumerate(sorted(unique_labels))
}
colors_dbscan_0 = [color_map[label] for label in dbscan_labels]
score_0 = silhouette_score(X_scaled, dbscan_labels)
# 2)   
dbscan = DBSCAN(eps=1, min_samples=5)
dbscan_labels = dbscan.fit_predict(X_scaled)

unique_labels = set(dbscan_labels)
palette = sns.color_palette("Set3", len(unique_labels))
color_map = {
    label: palette[i] if label != -1 else (0.6, 0.6, 0.6)
    for i, label in enumerate(sorted(unique_labels))
}
colors_dbscan_1 = [color_map[label] for label in dbscan_labels]
score_1 = silhouette_score(X_scaled, dbscan_labels)

# 3)   
dbscan = DBSCAN(eps=1, min_samples=8)
dbscan_labels = dbscan.fit_predict(X_scaled)

unique_labels = set(dbscan_labels)
palette = sns.color_palette("Set2", len(unique_labels))
color_map = {
    label: palette[i] if label != -1 else (0.6, 0.6, 0.6) 
    for i, label in enumerate(sorted(unique_labels))
}
colors_dbscan_2 = [color_map[label] for label in dbscan_labels]
score_2 = silhouette_score(X_scaled, dbscan_labels)

print(score_0)
print(score_1)
print(score_2)

# PCA sui valori scalati

pca = PCA(n_components=3, random_state=SEED)
X_pca = pca.fit_transform(X_scaled)

# Plot 0 in 3D
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
scatter3d = ax1.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], c=colors_dbscan_0, s=50, edgecolor='k')
ax1.set_title("3D plot")
ax1.set_xlabel("Feature 1")
ax1.set_ylabel("Feature 2")
ax1.set_zlabel("Feature 3")
plt.show()

# Plot 1 in 3D
fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
scatter3d = ax1.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], c=colors_dbscan_1, s=50, edgecolor='k')
ax1.set_title("3D plot")
ax1.set_xlabel("Feature 1")
ax1.set_ylabel("Feature 2")
ax1.set_zlabel("Feature 3")
plt.show()

# Plot 2 in 3D
fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
scatter3d = ax1.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], c=colors_dbscan_2, s=50, edgecolor='k')
ax1.set_title("3D plot")
ax1.set_xlabel("Feature 1")
ax1.set_ylabel("Feature 2")
ax1.set_zlabel("Feature 3")
plt.show()