# %% [markdown]
# # Make a full list of Green codes

# %% [markdown]
# Autori: Fabio Morea, Leyla Vesnic, Andrea Bincoletto
# Data: 20 giugno 2022
# Versione 1.0
# GitHub: https://github.com/areasciencepark/CodiciGreen 

# %% [markdown]
# ## load libraries

# %%
import pandas as pd 
import re

# %% [markdown]
# ## Load data
# 

# %%
# reading data and selecting only the column we are interested in
raw_data = pd.read_excel("../2IPCGreenInventoryList_2022WIPO.xlsx", dtype=str)
raw_data = raw_data[[ "IPC"]]
raw_data.dropna(inplace=True)
raw_data.head(5)

# %%
codes = pd.read_excel("../IPC WIPO unione.xlsx", dtype=str)
codes = list(codes["ipc_class_symbol"])


# %% [markdown]
# ## scan eaach row of the dataframe to generate a list of results
# 
# "," is the separator for lists of codes
# "-" is the separator for sequences
# and add individual results in a codes_list[]

# %%
codes_list = []
i=0

for index, row in raw_data.iterrows():
    parts = row['IPC'].split(" ")
    first_part  = parts[0]
    for p in range(0,len(parts)):
        parts[p] = re.sub("\xa0"," ",parts[p]) 
        if parts[p][-1]==",": 
            print("issue with final comma", parts[p])
            parts[p] = parts[p][:-1]
            print("solved issue with final comma", parts[p])
            
    print("PARTS: ",parts, len(parts))
    
    if len(parts) == 1:
        print(i,j, "this is a short code ", parts[0])
        i+=1
        codes_list.append(parts[0])
    else:
        other_parts=[]
        for p in range(0,len(parts)):
            other_parts = other_parts + parts[p].split(",")
                
        print("PROCESSING the parts ",other_parts,len(other_parts))
        for j in range(0,len(other_parts)):
            print("FOR loop ", j, other_parts[j])
            this_part = re.sub(" ", "",other_parts[j]) #remove whitespaces
            this_part = re.sub('"',"",this_part) # 



            full_code = first_part + this_part
            
            if (len(this_part))==0:
                print("this part is EMPTY!", full_code)
            elif not("-" in this_part):
                i+=1
                codes_list.append(full_code)
                print(i,j,"Adding a single code ", full_code)
            
            else:#sequenza
                sequence_start = first_part + this_part.split("-")[0]
                sequence_end   = first_part + this_part.split("-")[1]
                print(i,j, "** This is a sequence from ", sequence_start, " to " , sequence_end)
                # scan the full list of codes and add everything from sequence_start to sequence_end
                get_also_next_code = False
                found_any_code = False
                for cod in codes:
                    if (cod == sequence_start): 

                        print("ADDING the sequence start",cod)
                        i+=1
                        found_any_code = True
                        codes_list.append(cod)
                        get_also_next_code = True
                    elif (cod == sequence_end): 
                        print("ADDING end of the sequence end",cod)
                        i+=1
                        found_any_code = True
                        codes_list.append(cod)
                        get_also_next_code = False
                        break #don't need to search in the rest of the list
                    elif (get_also_next_code==True):
                        print("ADDING A PART OF the sequence",cod)
                        i+=1
                        found_any_code = True
                        codes_list.append(cod)
                if found_any_code == False: print("WARNING no codes found for the given sequence")
print("Done :-D")

codes_list = sorted(list(set(codes_list)))
print(len(codes_list), " codes found")


        

    

# %%
print(codes_list) 

# %%
codes_list

# %% [markdown]
# # write the results to a CSV file

# %%
pd.DataFrame(codes_list).to_csv("GreenCodes.csv", index=False, header=False)


