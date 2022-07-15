# %%
import io
import sharepy
import getpass
import pandas as pd
import sys
import os
from pathlib import Path
import numpy as np
import csv

# %%
# lists with the name of the folder where the different files to be uploaded are contained
lista_dir1 = ['1_CPC']
lista_dir2 = ['2_CPC']
lista_dir3 = ['3_CPC']
lista_dir4 = ['4_CPC']
lista_dir5 = ['5_CPC']
lista_dir6 = ['6_CPC']
lista_dir7 = ['7_CPC']
lista_dir8 = ['8_CPC']
lista_dir9 = ['1_IPC']


# %%
# path to the first folder
path_base = r"C:\Users\bincoletto\OneDrive - Area Science Park\Documenti\green classification"
path_dati = path_base + "\\ENV-TECH codes\\"
lista_dd = []
for x in lista_dir1:
    lista_dd.append(path_dati + x + "\\")
print(f'directory dati: {lista_dd}')

# %%
# function to open every .csv file in every folders
def lista_file_csv(dd):
    lista_file = []
    for root, dirs, files in os.walk(dd):
        for name in files:
            if 'csv' in name:
                lista_file.append(os.path.join(root, name))
    n = len(lista_file)
    print(f'la directory contiene {n} file')
    return (lista_file)


# %%
for dd in lista_dd:
    print(f'>>> inizio elaborazione {dd}')
    file_da_elaborare = lista_file_csv(dd)

# %%
# function to read the .csv files in the folder
def carica_dati_da_csv(ff):
    print(f'Elaborazione dei file {ff} \n ')
    df = pd.read_csv(ff, sep = ',', encoding='utf-8-sig', dtype=str)
    return(df)

# %%
# concatenation of all .csv files in the first folder
lista_df = []
for ff in file_da_elaborare:
    df = carica_dati_da_csv(ff)
    lista_df.append(df)
df_code_1 = pd.concat(lista_df)

# %%
# second folder
path_base = r"C:\Users\bincoletto\OneDrive - Area Science Park\Documenti\green classification"
path_dati = path_base + "\\ENV-TECH codes\\"
lista_dd = []
for x in lista_dir2:
    lista_dd.append(path_dati + x + "\\")
print(f'directory dati: {lista_dd}')

for dd in lista_dd:
    print(f'>>> inizio elaborazione {dd}')
    file_da_elaborare = lista_file_csv(dd)

lista_df = []
for ff in file_da_elaborare:
    df = carica_dati_da_csv(ff)
    lista_df.append(df)
df_code_2 = pd.concat(lista_df)

# %%
# third folder
path_base = r"C:\Users\bincoletto\OneDrive - Area Science Park\Documenti\green classification"
path_dati = path_base + "\\ENV-TECH codes\\"
lista_dd = []
for x in lista_dir3:
    lista_dd.append(path_dati + x + "\\")
print(f'directory dati: {lista_dd}')

for dd in lista_dd:
    print(f'>>> inizio elaborazione {dd}')
    file_da_elaborare = lista_file_csv(dd)

lista_df = []
for ff in file_da_elaborare:
    df = carica_dati_da_csv(ff)
    lista_df.append(df)
df_code_3 = pd.concat(lista_df)

# %%
# fourth folder
path_base = r"C:\Users\bincoletto\OneDrive - Area Science Park\Documenti\green classification"
path_dati = path_base + "\\ENV-TECH codes\\"
lista_dd = []
for x in lista_dir4:
    lista_dd.append(path_dati + x + "\\")
print(f'directory dati: {lista_dd}')

for dd in lista_dd:
    print(f'>>> inizio elaborazione {dd}')
    file_da_elaborare = lista_file_csv(dd)

lista_df = []
for ff in file_da_elaborare:
    df = carica_dati_da_csv(ff)
    lista_df.append(df)
df_code_4 = pd.concat(lista_df)

# %%
# fifth folder
path_base = r"C:\Users\bincoletto\OneDrive - Area Science Park\Documenti\green classification"
path_dati = path_base + "\\ENV-TECH codes\\"
lista_dd = []
for x in lista_dir5:
    lista_dd.append(path_dati + x + "\\")
print(f'directory dati: {lista_dd}')

for dd in lista_dd:
    print(f'>>> inizio elaborazione {dd}')
    file_da_elaborare = lista_file_csv(dd)

lista_df = []
for ff in file_da_elaborare:
    df = carica_dati_da_csv(ff)
    lista_df.append(df)
df_code_5 = pd.concat(lista_df)

# %%
# sixth folder
path_base = r"C:\Users\bincoletto\OneDrive - Area Science Park\Documenti\green classification"
path_dati = path_base + "\\ENV-TECH codes\\"
lista_dd = []
for x in lista_dir6:
    lista_dd.append(path_dati + x + "\\")
print(f'directory dati: {lista_dd}')

for dd in lista_dd:
    print(f'>>> inizio elaborazione {dd}')
    file_da_elaborare = lista_file_csv(dd)

lista_df = []
for ff in file_da_elaborare:
    df = carica_dati_da_csv(ff)
    lista_df.append(df)
df_code_6 = pd.concat(lista_df)

# %%
# seventh folder
path_base = r"C:\Users\bincoletto\OneDrive - Area Science Park\Documenti\green classification"
path_dati = path_base + "\\ENV-TECH codes\\"
lista_dd = []
for x in lista_dir7:
    lista_dd.append(path_dati + x + "\\")
print(f'directory dati: {lista_dd}')

for dd in lista_dd:
    print(f'>>> inizio elaborazione {dd}')
    file_da_elaborare = lista_file_csv(dd)

lista_df = []
for ff in file_da_elaborare:
    df = carica_dati_da_csv(ff)
    lista_df.append(df)
df_code_7 = pd.concat(lista_df)

# %%
# eighth folder
path_base = r"C:\Users\bincoletto\OneDrive - Area Science Park\Documenti\green classification"
path_dati = path_base + "\\ENV-TECH codes\\"
lista_dd = []
for x in lista_dir8:
    lista_dd.append(path_dati + x + "\\")
print(f'directory dati: {lista_dd}')

for dd in lista_dd:
    print(f'>>> inizio elaborazione {dd}')
    file_da_elaborare = lista_file_csv(dd)

lista_df = []
for ff in file_da_elaborare:
    df = carica_dati_da_csv(ff)
    lista_df.append(df)
df_code_8 = pd.concat(lista_df)

# %%
# ninth folder
path_base = r"C:\Users\bincoletto\OneDrive - Area Science Park\Documenti\green classification"
path_dati = path_base + "\\ENV-TECH codes\\"
lista_dd = []
for x in lista_dir9:
    lista_dd.append(path_dati + x + "\\")
print(f'directory dati: {lista_dd}')

for dd in lista_dd:
    print(f'>>> inizio elaborazione {dd}')
    file_da_elaborare = lista_file_csv(dd)

lista_df = []
for ff in file_da_elaborare:
    df = carica_dati_da_csv(ff)
    lista_df.append(df)
df_code_9 = pd.concat(lista_df)

# %%
CPC_code = df_code_1.append([df_code_2, df_code_3, df_code_4, df_code_5, df_code_6, df_code_7, df_code_8])
CPC_code.shape

# %%
CPC_code_univoci = CPC_code.drop_duplicates(subset=['Code'])
CPC_code_univoci.shape

# %%
# append
df_code = df_code_1.append([df_code_2, df_code_3, df_code_4, df_code_5, df_code_6, df_code_7, df_code_8, df_code_9])
df_code.shape

# %%
# no duplicates
df_code_univoco = df_code.drop_duplicates(subset=['Code'])
df_code_univoco.shape

# %%
path = "C:\\Users\\bincoletto\\OneDrive - Area Science Park\\Documenti\\green classification\\ENV-TECH codes\\finale\\ENV_TECH_univoco.csv"
#df_code_univoco.to_csv(path, sep=';', encoding='utf-8', index=False)
df_code_univoco.to_csv(path, sep='|',encoding='utf-8-sig', index=False)

# %%
# Add a column with the name of the .csv file to each dataframe for the first folder

# path_base = r"C:\Users\bincoletto\OneDrive - Area Science Park\Documenti\green classification"
# path_dati = path_base + "\\ENV-TECH codes\\"

path = os.path.join(path_dati, '1_CPC')
files = [os.path.join(path,i) for i in os.listdir(path) if os.path.isfile(os.path.join(path,i))]

df_1 = pd.DataFrame()

for file in files:
    _df = pd.read_csv(file)
    _df['level_2'] = os.path.split(file)[-1]
    df_1 = df_1.append(_df)

df_1['sublevel'] = df_1['level_2'].str.replace('.csv', '', regex=True)
df_1 = df_1.drop(columns=[
    'level_2'
])
df_1 = df_1.rename(columns={
    'sublevel': 'level_2'
})

df_1["Fonte"] = 'CPC'

df_1.value_counts('level_2')

# %%
# Add a column with the name of the .csv file to each dataframe for the second folder
path = os.path.join(path_dati, '2_CPC')
files = [os.path.join(path,i) for i in os.listdir(path) if os.path.isfile(os.path.join(path,i))]

df_2 = pd.DataFrame()

for file in files:
    _df = pd.read_csv(file)
    _df['level_2'] = os.path.split(file)[-1]
    df_2 = df_2.append(_df)

df_2['sublevel'] = df_2['level_2'].str.replace('.csv', '', regex=True)
df_2 = df_2.drop(columns=[
    'level_2'
])
df_2 = df_2.rename(columns={
    'sublevel': 'level_2'
})

df_2["Fonte"] = 'CPC'

df_2.value_counts('level_2')

# %%
# Add a column with the name of the .csv file to each dataframe for the third folder
path = os.path.join(path_dati, '3_CPC')
files = [os.path.join(path,i) for i in os.listdir(path) if os.path.isfile(os.path.join(path,i))]

df_3 = pd.DataFrame()

for file in files:
    _df = pd.read_csv(file)
    _df['level_2'] = os.path.split(file)[-1]
    df_3 = df_3.append(_df)

df_3['sublevel'] = df_3['level_2'].str.replace('.csv', '', regex=True)
df_3 = df_3.drop(columns=[
    'level_2'
])
df_3 = df_3.rename(columns={
    'sublevel': 'level_2'
})

df_3["Fonte"] = 'CPC'

df_3.value_counts('level_2')

# %%
# Add a column with the name of the .csv file to each dataframe for the fourth folder
path = os.path.join(path_dati, '4_CPC')
files = [os.path.join(path,i) for i in os.listdir(path) if os.path.isfile(os.path.join(path,i))]

df_4 = pd.DataFrame()

for file in files:
    _df = pd.read_csv(file)
    _df['level_2'] = os.path.split(file)[-1]
    df_4 = df_4.append(_df)

df_4['sublevel'] = df_4['level_2'].str.replace('.csv', '', regex=True)
df_4 = df_4.drop(columns=[
    'level_2'
])
df_4 = df_4.rename(columns={
    'sublevel': 'level_2'
})

df_4["Fonte"] = 'CPC'

df_4.value_counts('level_2')

# %%
# Add a column with the name of the .csv file to each dataframe for the fifth folder
path = os.path.join(path_dati, '5_CPC')
files = [os.path.join(path,i) for i in os.listdir(path) if os.path.isfile(os.path.join(path,i))]

df_5 = pd.DataFrame()

for file in files:
    _df = pd.read_csv(file)
    _df['level_2'] = os.path.split(file)[-1]
    df_5 = df_5.append(_df)

df_5['sublevel'] = df_5['level_2'].str.replace('.csv', '', regex=True)
df_5 = df_5.drop(columns=[
    'level_2'
])
df_5 = df_5.rename(columns={
    'sublevel': 'level_2'
})

df_5["Fonte"] = 'CPC'

df_5.value_counts('level_2')

# %%
# Add a column with the name of the .csv file to each dataframe for the sixth folder
path = os.path.join(path_dati, '6_CPC')
files = [os.path.join(path,i) for i in os.listdir(path) if os.path.isfile(os.path.join(path,i))]

df_6 = pd.DataFrame()

for file in files:
    _df = pd.read_csv(file)
    _df['level_2'] = os.path.split(file)[-1]
    df_6 = df_6.append(_df)

df_6['sublevel'] = df_6['level_2'].str.replace('.csv', '', regex=True)
df_6 = df_6.drop(columns=[
    'level_2'
])
df_6 = df_6.rename(columns={
    'sublevel': 'level_2'
})

df_6["Fonte"] = 'CPC'

df_6.value_counts('level_2')

# %%
# Add a column with the name of the .csv file to each dataframe for the seventh folder
path = os.path.join(path_dati, '7_CPC')
files = [os.path.join(path,i) for i in os.listdir(path) if os.path.isfile(os.path.join(path,i))]

df_7 = pd.DataFrame()

for file in files:
    _df = pd.read_csv(file)
    _df['level_2'] = os.path.split(file)[-1]
    df_7 = df_7.append(_df)

df_7['sublevel'] = df_7['level_2'].str.replace('.csv', '', regex=True)
df_7 = df_7.drop(columns=[
    'level_2'
])
df_7 = df_7.rename(columns={
    'sublevel': 'level_2'
})

df_7["Fonte"] = 'CPC'

df_7.value_counts('level_2')

# %%
# Add a column with the name of the .csv file to each dataframe for the eighth folder
path = os.path.join(path_dati, '8_CPC')
files = [os.path.join(path,i) for i in os.listdir(path) if os.path.isfile(os.path.join(path,i))]

df_8 = pd.DataFrame()

for file in files:
    _df = pd.read_csv(file)
    _df['level_2'] = os.path.split(file)[-1]
    df_8 = df_8.append(_df)

df_8['sublevel'] = df_8['level_2'].str.replace('.csv', '', regex=True)
df_8 = df_8.drop(columns=[
    'level_2'
])
df_8 = df_8.rename(columns={
    'sublevel': 'level_2'
})

df_8["Fonte"] = 'CPC'

df_8.value_counts('level_2')

# %%
# Add a column with the name of the .csv file to each dataframe for the IPC folder
path = os.path.join(path_dati, '1_IPC')
files = [os.path.join(path,i) for i in os.listdir(path) if os.path.isfile(os.path.join(path,i))]

df_9 = pd.DataFrame()

for file in files:
    _df = pd.read_csv(file)
    _df['level_2'] = os.path.split(file)[-1]
    df_9 = df_9.append(_df)

df_9['sublevel'] = df_9['level_2'].str.replace('.csv', '', regex=True)
df_9 = df_9.drop(columns=[
    'level_2'
])
df_9 = df_9.rename(columns={
    'sublevel': 'level_2'
})

df_9["Fonte"] = 'IPC'

df_9.value_counts('level_2')

# %%
# append of the results
Code_level_all = df_1.append([df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9])
Code_level_all.shape

# %%
# Groupby to add a column with the source:
# - CPC
# - CPC&IPC
# - IPC
fonte_all_subset = Code_level_all.copy()
fonte_all_subset= fonte_all_subset.groupby('Code')['Fonte'].apply(';'.join).reset_index()
print(f"I progetti del dataframe sono: {fonte_all_subset.shape}")
print(fonte_all_subset.head(5))
print(fonte_all_subset.tail(5))

# %%
conteggio = fonte_all_subset.value_counts('Fonte')
print('Le righe della colonna "Fonte" sono categorizzate nel seguente modo:')
print(f'{conteggio}')

# Find the presence of the CPC and IPC values and replace the values correctly according to the categories identified above:

fonte_riclassification = fonte_all_subset.copy()
fonte_riclassification['Fonte'] = fonte_riclassification['Fonte'].map({
    'CPC': 'CPC',
    'CPC;IPC': 'CPC & IPC',
    'CPC;CPC': 'CPC',
    'CPC;CPC;CPC': 'CPC',
    'IPC': 'IPC',
    'CPC;CPC;IPC;IPC': 'CPC & IPC',
    np.nan:'Null'
}, na_action=None)

conteggio = fonte_riclassification.value_counts('Fonte')
print(conteggio)

# %%
# Groupby to put all values in the 'level_2' column in one cell for the single code
# (che dovrà apparire solo una volta per riga)
level_all_subset = Code_level_all.copy()
level_all_subset= level_all_subset.groupby('Code')['level_2'].apply('; '.join).reset_index()
level_all_subset = level_all_subset.rename(columns={
    'level_2':'Level_2'
})
print(level_all_subset.head(10))
print(f"I progetti del dataframe sono: {level_all_subset.shape}")

# %%
# merge
df_final = pd.merge(level_all_subset, fonte_riclassification, how="left", on='Code')
df_final

# %%
path = "C:\\Users\\bincoletto\\OneDrive - Area Science Park\\Documenti\\green classification\\ENV-TECH codes\\finale\\ENV_TECH_final.csv"
#df_code_univoco.to_csv(path, sep=';', encoding='utf-8', index=False)
df_final.to_csv(path, sep='|',encoding='utf-8-sig', index=False)


