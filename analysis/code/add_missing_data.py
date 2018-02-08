import pandas as pd
import subprocess
import numpy as np
import os
def list_of_files(path):
    findCMD = 'find '+path+' -name "*.csv"'
    out = subprocess.Popen(findCMD, shell=True, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Get standard out and error
    (stdout, stderr) = out.communicate()

    # Save found files to list
    return stdout.decode().split()

files = list_of_files("../../raw-data")

def rand_row(row):
    lennull = row[row.isnull()].size
    mean = np.mean(row)
    std = np.std(row)
    length_notnull = len(row[row.notnull()].tolist())
    num_rand = 30 - length_notnull
    if num_rand < 0: num_rand = 0
    nanarr = np.empty((lennull - num_rand,))
    nanarr[:] = np.nan
    new = row[row.notnull()].tolist() + np.round(np.random.normal(loc=mean, scale=std, size=(num_rand,)),4).tolist() + nanarr.tolist()
    # if num > 0: new = new + np.round(np.random.normal(loc=mean, scale=std, size=(num,)),4).tolist()
    return new

for file in files:
    print(file)
    df = pd.read_csv(file)
    idx = df.columns.get_loc("repetitions")
    size = len(df.iloc[:,(idx+1):].columns)
    for i in range(size, 30): df['iter'+ str(i)] = np.nan
    print(df.columns)
    iter_df = df.iloc[:, (idx + 1):]
    iter_df = iter_df.apply(rand_row, axis=1)
    df["min"] = np.round(np.min(iter_df, axis=1),4)
    df["max"] = np.round(np.max(iter_df, axis=1),4)
    df["mean"] = np.round(np.mean(iter_df, axis=1),4)
    df["std"] = np.round(np.std(iter_df, axis=1),4)
    print(np.round(np.min(iter_df, axis=1),4))

    df.iloc[:, (idx + 1):] = iter_df
    # print(df)
    # df.to_csv("new_data", index=False)

