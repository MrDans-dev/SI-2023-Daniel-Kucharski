import pandas as pd

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
