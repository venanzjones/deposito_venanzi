# Import delle librerie
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import StratifiedKFold, cross_val_score

# Read data
df = pd.read_csv("creditcard.csv")
y = df['Class'].astype(int)
X = df.drop(['Class','Time'], axis = 1)

# K-Fold stratificato
skf = StratifiedKFold(n_splits=3, shuffle=True, random_state=2025)

# Decision Tree
tree = DecisionTreeClassifier(max_depth=5, random_state=2025)
cv_tree = cross_val_score(tree, X, y, cv=skf, scoring="roc_auc")

# Print kv_tree 
print(f"Decision Tree AUC: {cv_tree.mean():.3f} ± {cv_tree.std():.3f}")