import pandas as pd

df = pd.read_csv('hh.csv')

df['Тест'] = [new for new in range(50)]

print(df)

df.drop('Тест', axis = 1, inplace = True)
print(df)

df.drop(49, axis = 0, inplace = True)
print(df)