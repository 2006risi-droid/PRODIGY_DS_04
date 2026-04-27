import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("enhanced_population_data_1000.csv")

print("\n===== FIRST FIVE ROWS OF DATA =====\n")
print(df.head())

print("\n===== BASIC INFO =====\n")
print(df.info())

print("\n===== SUMMARY STATISTICS =====\n")
print(df.describe(include='all'))

print("\n===== MISSING VALUES =====\n")
print(df.isnull().sum())

plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="Gender", palette="viridis")
plt.title("Gender Distribution in Population", fontsize=16)
plt.xlabel("Gender", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.savefig("gender_distribution.png")
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Age", bins=30, kde=True, color="blue")
plt.title("Age Distribution in Population", fontsize=16)
plt.xlabel("Age", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.savefig("age_histogram.png")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Gender", y="Age")
plt.title("Age Spread by Gender", fontsize=16)
plt.xlabel("Gender", fontsize=14)
plt.ylabel("Age", fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.savefig("age_boxplot.png")
plt.show()

print("\n✓ All graphs generated successfully!")