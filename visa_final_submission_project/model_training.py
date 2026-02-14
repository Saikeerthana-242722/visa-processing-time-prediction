
# Model Training
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("VISA_Details_2010-2013-oct.csv")

np.random.seed(42)
df["Processing_Days"] = np.random.randint(15, 90, size=len(df))

le = LabelEncoder()
df["VISA_CLASS"] = le.fit_transform(df["VISA_CLASS"])
df["CASE_STATUS"] = le.fit_transform(df["CASE_STATUS"])
df["WORKSITE"] = le.fit_transform(df["WORKSITE"])

X = df[["VISA_CLASS","CASE_STATUS","WORKSITE","YEAR"]]
y = df["Processing_Days"]

model = RandomForestRegressor()
model.fit(X,y)

pickle.dump(model, open("visa_model.pkl","wb"))
