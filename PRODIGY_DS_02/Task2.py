import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("Student_Performance_Task2.xlsx")

print(df.head())
print(df.info())
print(df.describe())

df.isnull().sum()

sns.countplot(x="Gender", data=df)
plt.show()

sns.histplot(df["Math_Score"], kde=True)
plt.show()

sns.boxplot(data=df[["Math_Score","Reading_Score","Writing_Score"]])
plt.show()

sns.pairplot(df[["Math_Score","Reading_Score","Writing_Score"]])
plt.show()

sns.heatmap(df[["Math_Score","Reading_Score","Writing_Score"]].corr(), annot=True)
plt.show()

sns.barplot(x="Test_Prep", y="Math_Score", data=df)
plt.show()

sns.barplot(x="Parental_Education", y="Math_Score", data=df)
plt.xticks(rotation=45)
plt.show()