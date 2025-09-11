# Import delle librerie
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

# Import data and processing
df = pd.read_csv("Iris.csv")

# Scelgo le feature e la y
X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm","PetalWidthCm"]]
y = df["Species"]

# Train, val, test split
X_temp, X_test, y_temp, y_test = train_test_split(X, y,  test_size=0.15, 
                                                  stratify=y, random_state=2025)    

X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=3/17,
                                                  stratify=y_temp, random_state=2025)

# Fitto il classificatore
clf = DecisionTreeClassifier(max_depth=6, random_state=2025)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_val)
print(" VALIDATION DATA ")
print("")
print("Validation accuracy:")
print(accuracy_score(y_val,y_pred))
print("")
print("Validation data reprort:")
print(classification_report(y_val, y_pred, digits=3))

y_pred_test = clf.predict(X_test)
print(" TEST DATA ")
print("")
print("Test accuracy:")
print(accuracy_score(y_test,y_pred_test))
print("")
print("Test data report:")
print(classification_report(y_test, y_pred_test, digits=3))
