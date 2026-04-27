import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(10)
rows=1000

data={
    "Road_Condition":np.random.choice(["Dry","Wet","Snow","Ice","Under Construction"],rows),
    "Weather":np.random.choice(["Clear","Rain","Fog","Snow","Storm"],rows),
    "Time_of_Day":np.random.choice(["Morning","Afternoon","Evening","Night"],rows),
    "Severity":np.random.randint(1,6,rows),
    "City":np.random.choice(["New York","Los Angeles","Chicago","Houston","Phoenix"],rows)
}

df=pd.DataFrame(data)
df.to_excel("traffic_accidents.xlsx",index=False)

df=pd.read_excel("traffic_accidents.xlsx")

print(df.head(20))
print(df.shape)

print(df["Road_Condition"].value_counts())
print(df["Weather"].value_counts())
print(df["Time_of_Day"].value_counts())
print(df["City"].value_counts())

print(df.groupby("Road_Condition")["Severity"].mean())
print(df.groupby("Weather")["Severity"].mean())
print(df.groupby("Time_of_Day")["Severity"].mean())
print(df.groupby("City")["Severity"].mean())

plt.figure()
sns.countplot(x=df["Road_Condition"])
plt.title("Accidents by Road Condition")
plt.show()

plt.figure()
sns.countplot(x=df["Weather"])
plt.title("Accidents by Weather")
plt.show()

plt.figure()
sns.countplot(x=df["Time_of_Day"])
plt.title("Accidents by Time of Day")
plt.show()

plt.figure()
sns.countplot(x=df["City"])
plt.title("Accident Hotspots by City")
plt.show()

plt.figure()
sns.boxplot(x="Road_Condition",y="Severity",data=df)
plt.title("Severity vs Road Condition")
plt.show()

plt.figure()
sns.boxplot(x="Weather",y="Severity",data=df)
plt.title("Severity vs Weather")
plt.show()

plt.figure()
sns.boxplot(x="Time_of_Day",y="Severity",data=df)
plt.title("Severity vs Time of Day")
plt.show()

pivot=df.pivot_table(values="Severity",index="Road_Condition",columns="Weather",aggfunc="mean")

plt.figure()
sns.heatmap(pivot,annot=True)
plt.title("Heatmap Road Condition vs Weather")
plt.show()