import pandas as pd
import re

# info about "Sabit Disk (SSD) Boyutu" is smth like "512GB, 128GB, 1TB...". So I should make them integer like (512, 128, 1000)
def diskCap(i):
    if (str(i)[-2:] == 'GB') & (str(i) != 'nan'):
        return int(i[:-2])
    elif (str(i)[-2:] == 'TB') & (str(i) != 'nan'):
        return int(i[:-2]) * 1000
    else:
        return None
df['Sabit Disk (SSD) Boyutu'].apply(lambda x: diskCap(x))
# Conditions are little messy because column type is float and nan's are not acting like None as you know.



# info about 'Fiyat' scraped little wrong. As we see I took them with "/n", "TL", ".", "," and nans. I should make them integer or None
def ifNan(i):
    if str(i) != 'nan':
        return int(i)/100
    else:
        return None
df['Fiyat'] = [re.sub('[^0-9]', '', i) for i in df['Fiyat']]
df['Fiyat'] = df['Fiyat'].apply(lambda x: ifNan(x))

# There is only 3 type of OS but they wrote them in different types. So I should have make them in a standard.
def stdOS(i):
    if (i == 'FreeDOS') | (i == 'DOS') | (i == 'FreeDos'):
        return 'FreeDos'
    elif (i == 'Windows10') | (i == 'Windows10Pro'):
        return 'Windows10'
    else:
        return i
df['İşletim Sistemi'] = df['İşletim Sistemi'].apply(lambda x: stdOS(x))

# There is more than 50 column like these.
