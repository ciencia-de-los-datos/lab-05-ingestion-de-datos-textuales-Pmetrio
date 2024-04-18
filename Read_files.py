import glob
import pandas as pd

def archivo_test():
    folder_list = ["negative","neutral","positive"]
    columna1=[]
    columna2=[]
    for folder in folder_list:
        filenames=glob.glob(f"data/test/{folder}"+"/*")
        for filename in filenames:
            columna1.append(pd.read_csv(filename, sep="\t",header=None, names=["phrase"]))
            columna2.append(folder)
    concatenated_col1 = pd.concat(columna1, ignore_index = True, axis=0)
    concatenated_col2=pd.DataFrame(columna2,columns=["sentiment"])
    df = pd.concat(objs=[concatenated_col1, concatenated_col2], axis=1, join="outer", ignore_index=False, sort=False)
    df.to_csv("test_dataset.csv", sep=",", index=False, header=True)
    return df

def archivo_train():
    folder_list = ["negative","neutral","positive"]
    columna1=[]
    columna2=[]
    for folder in folder_list:
        filenames=glob.glob(f"data/train/{folder}"+"/*")
        for filename in filenames:
            columna1.append(pd.read_csv(filename, sep="\t",header=None, names=["phrase"]))
            columna2.append(folder)
    concatenated_col1 = pd.concat(columna1, ignore_index = True, axis=0)
    concatenated_col2=pd.DataFrame(columna2,columns=["sentiment"])
    df = pd.concat(objs=[concatenated_col1, concatenated_col2], axis=1, join="outer", ignore_index=False, sort=False)
    df.to_csv("train_dataset.csv", sep=",", index=False, header=True)
    return df

archivo_test()
archivo_train()