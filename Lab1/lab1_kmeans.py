# Import 
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Config
SEED = 42 
MAX_K = 10

# Read data and process
df = pd.read_csv("Mall_Customers.csv")

X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
X_scaled = StandardScaler().fit_transform(X)

# Tune k using the Sum of squares error (SSE)
sse = []
k_values = range(2, MAX_K)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    sse.append(kmeans.inertia_) 

plt.figure(figsize=(8, 5))
plt.plot(k_values, sse, marker='o')
plt.xlabel('k')
plt.ylabel('SSE')
plt.xticks(k_values)
plt.grid()
plt.show()

# We not  fit the model with the optimal value
k_opt = 5
kmeans = KMeans(n_clusters=k_opt, 
                random_state=SEED,
                init="k-means++")               
labels = kmeans.fit_predict(X_scaled)

# Plot the clusters
plt.figure(figsize=(6, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], 
            kmeans.cluster_centers_[:, 1], 
            c='red', 
            marker='X', 
            s=150, 
            label='Centroids')
plt.title("Retrieved clusters")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.legend()
plt.grid(True)
plt.show()

'''
Cluster1: Customers with below-average salary and below-average spending score
Cluster2: Customers with below-average salary and above-average spending score
Cluster3: Customers with average salary and average spending score
Cluster4: Customers with above-average  salary and below-average spending score
Cluster5: Customers with above-average salary and above-average spending score
'''