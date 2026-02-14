
# EDA Analysis
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("VISA_Details_2010-2013-oct.csv")

np.random.seed(42)
df["Processing_Days"] = np.random.randint(15, 90, size=len(df))

df.groupby("VISA_CLASS")["Processing_Days"].mean().plot(kind="bar")
plt.title("Avg Processing Time by Visa Class")
plt.show()
