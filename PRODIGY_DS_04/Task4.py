import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("sentiment_dataset_v2.xlsx")

print(df.head())
print(df.info())
print(df.isnull().sum())

sentiment_counts = df['Sentiment'].value_counts()
print(sentiment_counts)

platform_counts = df['Platform'].value_counts()
print(platform_counts)

cross = pd.crosstab(df['Platform'], df['Sentiment'])
print(cross)

likes_avg = df.groupby('Sentiment')['Likes'].mean()
print(likes_avg)

plt.figure()
sentiment_counts.plot(kind='bar')
plt.show()

plt.figure()
platform_counts.plot(kind='bar')
plt.show()

plt.figure()
cross.plot(kind='bar', stacked=True)
plt.show()

plt.figure()
likes_avg.plot(kind='bar')
plt.show()

text = " ".join(df['Content'])
words = text.split()

word_count = {}

for w in words:
    w = w.lower()
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words[:10]:
    print(word, count)