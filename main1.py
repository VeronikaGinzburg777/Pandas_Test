import pandas as pd

df = pd.read_csv('Most Streamed Spotify Songs 2024.csv',encoding='latin1')

print("Первые 5 строк данных:")
print(df.head())

print("\nИнформация о данных:")
print(df.info())

print("\nСтатистическое описание данных:")
print(df.describe())
