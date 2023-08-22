import random
import pandas as pd

df = pd.read_csv('data.csv')
df['Email'] = df['Email'].apply(lambda x: x.split('@')[0] + '@' + ''.join(['*' for _ in x.split('@')[1]]))
df['SSN'] = df['SSN'].apply(lambda x: '***-**-' + x.split('-')[2])
df['Name'] = df['Name'].apply(lambda x: ''.join(random.sample(x, len(x))))
df.to_csv('anonymized_data.csv', index=False)
