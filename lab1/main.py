import pandas as pd
import numpy as np

#z3
dec_sys = []
with open("dane/car.txt") as file:
    for line in file:
        dec_sys.append(line[0:-2].split(" "))

df = pd.DataFrame(dec_sys)

#3a
symbols = []
for col in df:
    for i in df[col].unique():
        if i not in symbols:
            symbols.append(i)
print(symbols)

#3b
print("Objects/Atributes: ", df.shape)

#3c
tmp_val = []
for i in symbols:
    if i.isnumeric():
        tmp_val.append(float(i))
print("Min/Max: ", min(tmp_val), max(tmp_val))


#3d
uniq_count_val = []
for col in df:
    uniq_count_val.append(len(df[col].unique()))
print(uniq_count_val)

#3e
for col in df:
    print(df[col].unique())

#3f
tmp_df = pd.DataFrame(data=tmp_val)
print("Standard Deviation", tmp_df.std())

#4a



num_of_rows = df[0].count()
ten_percent = int(0.1*num_of_rows)
r = np.random.choice(range(num_of_rows), ten_percent, replace=False)

for r in r:
    df[0][r] = "?"
print("\n", df)

df_c = df[0].value_counts().sort_values(ascending=False)
max = df[0].value_counts().sort_values(ascending=False).max()
for i in df_c:
    if i == max:
        max_key = str(df[0].get(i))

for x in range(num_of_rows):
    if df[0][x] == "?":
        df[0][x] = max_key


# d


file = "dane/Churn_Modelling.csv"
df = pd.read_csv(file, index_col=0)
print(df.head().to_string())

df_dummied = pd.get_dummies(df, columns=['Geography'])
df_dummied.drop('Geography_Germany', inplace=True, axis=1)
print(df_dummied.head().to_string())