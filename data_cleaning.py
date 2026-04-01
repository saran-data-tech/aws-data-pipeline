import pandas as pd

data = {
    'name':  ['Alice', 'Bob', None, 'Alice', 'Charlie', 'Saran', None],
    'age':   [25, 30, 22, 25, None, 20, 28],
    'city':  ['Chennai', 'Mumbai', 'Delhi', 'Chennai', 'Bangalore', 'chennai', 'Mumbai'],
    'salary':[50000, 60000, 55000, 50000, None, 45000, 60000]
}

df = pd.DataFrame(data)
df = df.dropna(subset=['name'])
df['age'] = df['age'].fillna(df['age'].mean())
df['salary'] = df['salary'].fillna(df['salary'].mean())
df = df.drop_duplicates()
df['city'] = df['city'].str.title()
df = df.reset_index(drop=True)
df.to_csv('cleaned_data.csv', index=False)
print("Cleaned data saved!")
print(df)