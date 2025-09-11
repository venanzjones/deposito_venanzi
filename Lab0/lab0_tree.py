# Import delle librerie
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score

# Load data e print prime 5 righe
df = pd.read_csv("Iris.csv")
print(df.shape)

# Scelgo le feature e la y
X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm","PetalWidthCm"]]
y = df["Species"]

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.20, random_state=2025
)

# Fitto il classificatore
clf = DecisionTreeClassifier(max_depth=5, random_state=2025)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Classification tree accuracy:")
print(accuracy_score(y_test,y_pred))
print("")
print("Classification tree report:")
print(classification_report(y_test, y_pred, digits=3))