import pandas as pd

df = pd.read_csv('animal.csv')

group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)

data = {
    'Name': ['Alice', 'Bob', 'Roma', 'Anna'],
    'Age': [23, 45, 17, 24],
    'City': ['New York', 'LA', 'Chicago', 'Moscow']
}

df = pd.DataFrame(data)

df.to_csv('output.csv',index = False)