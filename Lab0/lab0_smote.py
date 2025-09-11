# Imports
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Read data
df = pd.read_csv("creditcard.csv")
y = df['Class'].astype(int)
X = df.drop(['Class','Time'], axis = 1)

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=2025
)

# Model1: Tree
tree = DecisionTreeClassifier(max_depth=5, 
                              random_state=2025,
                              class_weight='balanced')
tree.fit(X_train, y_train)
y_pred_tree = tree.predict(X_test)

print("Classification tree report:")
print(classification_report(y_test, y_pred_tree, digits=3))

# Model2: RF
rf = RandomForestClassifier(n_estimators=100, 
                            max_depth=9, 
                            random_state=2025,
                            class_weight='balanced')
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

print("Random forest report:")
print(classification_report(y_test, y_pred_rf, digits=3)) 
                            