import pandas as pd

data = {
    'Name': ['TJ Romack', 'Katy Zee', 'Minnie Grey'],
    'Email': ['tjromack@gmail.com', 'katy@gmail.com', 'grey@gmail.com'],
    'DOB': ['1993-12-07', '1994-07-18', '2018-06-12'],
    'SSN': [ '123-45-6789', '987-65-4321', '456-78-9123']
}

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)