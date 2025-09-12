# Import
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import  confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import time

SEED = 42 

# Read data and processing
train_df = pd.read_csv("train.csv")
y = train_df['label']
X = train_df.drop('label', axis = 1)

X_scaled = StandardScaler().fit_transform(X)

# Perform PCA
pca = PCA(n_components=0.95)
X_pca = pca.fit_transform(X_scaled)

# Stampo il numero di componenti per spiegare il 95% della varianza -> 320
print("Componenti necessarie per spiegare il 0.95 della varianza: ",X_pca.shape[1])
print("")
X_train,X_test,y_train,y_test = train_test_split(X_pca,y,test_size=0.2,random_state=SEED, stratify = y)

# Fitto il classificatore sui dati proiettati
clf = DecisionTreeClassifier(max_depth=11, random_state=SEED)
start = time.time()
clf.fit(X_train, y_train)
end = time.time()
y_pred = clf.predict(X_test)
print("Tempo necessario per allenare il modello sui dati proitettati: ",end - start)
print("Accuracy sui dati trasformati:", accuracy_score(y_test,y_pred))
print("")

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, 
            annot=True,
            fmt='g',)
plt.ylabel('Actual', fontsize=13)
plt.title('Confusion matrix PCA data', fontsize=17, pad=20)
plt.gca().xaxis.set_label_position('top') 
plt.xlabel('Prediction', fontsize=13)
plt.gca().xaxis.tick_top()

plt.gca().figure.subplots_adjust(bottom=0.2)
plt.gca().figure.text(0.5, 0.05, 'Prediction', ha='center', fontsize=13)
plt.show()

# Fitto il classificatore sui dati originali
X_train,X_test,y_train,y_test = train_test_split(X_scaled,y,test_size=0.2,random_state=SEED, stratify = y)
clf = DecisionTreeClassifier(max_depth=11, random_state=SEED)
start = time.time()
clf.fit(X_train, y_train)
end = time.time()
y_pred = clf.predict(X_test)
print("Tempo necessario per allenare il modello sui dati originali: ",end - start)
print("Accuracy sui dati originali:", accuracy_score(y_test,y_pred))
print("")
# Plot confusion matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, 
            annot=True,
            fmt='g',)
plt.ylabel('Actual', fontsize=13)
plt.title('Confusion matrix: original data', fontsize=17, pad=20)
plt.gca().xaxis.set_label_position('top') 
plt.xlabel('Prediction', fontsize=13)
plt.gca().xaxis.tick_top()

plt.gca().figure.subplots_adjust(bottom=0.2)
plt.gca().figure.text(0.5, 0.05, 'Prediction', ha='center', fontsize=13)
plt.show()

'''
COMMENTO:
Il primo modello, con la sua dimensionalità ridotta di più della metà (320 su 785), ha un'accuratezza 
del 80% e impiega circa 16s per il solo training. Utilizzando i dati originali (scalati), otteniamo 
ovviamente un'accurateza maggiore (86%), visto che abbiamo tutta l'informazione del dataset. Inoltre, 
il suo training è anche più veloce (5s): ciò è dovuto alla sparsità dell'informazione nella foto (pixel neri indicano 
molti zeri nella matrice). Chiaramente preferisco il secondo modello, quello trainato sui dati originali.
'''
