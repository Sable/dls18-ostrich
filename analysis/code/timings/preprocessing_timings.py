import pandas as pd
import numpy as np
from analysis.code.classes.preprocess import new_column, new_columns
import subprocess
# constants for clean up
ubuntu_deer = True
mbp2013 = True

column_names_clean_data = ['benchmark', 'implementation', 'compiler', 'environment', 'mean', 'std',
                           'min', 'max', 'repetitions']
#============================================
# UBUNTU DEER BROWSERS
#============================================
order_columns_environment = ["native","chromium38", "firefox39","chrome63","firefox57","safari11","chromium56"
                                ,"chromium63","node","samsung-internet","microsoft-edge"]
def sorting_order_env(env):
    return order_columns_environment.index(env)

order_columns_compilers = ["wasm","browserify"]
def sorting_order_comp(name):
    return order_columns_compilers.index(name)

def list_of_files(path):
    findCMD = 'find '+path+' -name "*.csv"'
    out = subprocess.Popen(findCMD, shell=True, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Get standard out and error
    (stdout, stderr) = out.communicate()

    # Save found files to list
    return stdout.decode().split()
def sort_dataframe(df):
    df["order_env"] = df["environment"].apply(sorting_order_env)
    df["order_impl"] = df["compiler"].apply(sorting_order_comp)
    sorting_order = ["benchmark", "order_env", "order_impl"]
    return df.sort_values(by=sorting_order, axis=0)
# Find files
# Set up find command

OUTPUT_FILE_OLD_WASM_JS = "../clean-data/browsers-old-wasm-js-ubuntu-deer.csv"
OUTPUT_FILE_OLD_JS = "../clean-data/browsers-old-js-ubuntu-deer.csv"
OUTPUT_FILE_ALL_BROWSER_DATA = "../clean-data/all-browsers-ubuntu-deer.csv"

filelist = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/iphone10")
# chrome
print(filelist[0])
# Preparing chrome

# Iphone 10
df_chrome = pd.read_csv(filelist[0])
df_chrome = new_column(df_chrome, size=df_chrome["benchmark"].size, position=3, column_name="environment",
                       name="chrome63")
# df_chrome.to_csv(filelist[0].replace(".csv","-clean.csv"),index=False)
# df_chrome = sort_dataframe(df_chrome)
# df_chrome.to_csv("./data/chrome-iphone10.csv",index=False)
# Preparing firefox
print(filelist[1])
df_firefox = pd.read_csv(filelist[1])
df_firefox = new_column(df_firefox, size=df_firefox["benchmark"].size, position=3, column_name="environment", name="firefox57")
# # df_firefox.to_csv(filelist[1].replace(".csv","-clean.csv"),index=False)
# # df_firefox = sort_dataframe(df_firefox)
# df_firefox.to_csv("./data/firefox-iphone10.csv",index=False)

# Preparing safari
print(filelist[3])
df_safari = pd.read_csv(filelist[3])
df_safari = new_column(df_safari, size=df_safari["benchmark"].size, position=3, column_name="environment", name="safari11")
# df_safari.to_csv(filelist[2].replace(".csv","-clean.csv"),index=False)
# df_safari.to_csv("./data/safari-iphone10.csv",index=False)

df_total = pd.concat([df_chrome[column_names_clean_data], df_firefox[column_names_clean_data], df_safari[column_names_clean_data]])
df_total = sort_dataframe(df_total)
df_total.to_csv("./data/iphone10.csv",index=False)

# Samsung 8
filelist = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/samsung8")

df_total = pd.read_csv(filelist[0])
df_total = sort_dataframe(df_total[column_names_clean_data])
df_total.to_csv("./data/samsung8.csv",index=False)

# pixel 2
filelist = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/pixel2")
print(filelist)
df_total = pd.read_csv(filelist[0])
df_total = sort_dataframe(df_total[column_names_clean_data])
df_total.to_csv("./data/pixel2.csv",index=False)

# ipad-pro
filelist = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/ipad-pro")
df_total = pd.read_csv(filelist[0])
df_total = sort_dataframe(df_total[column_names_clean_data])
df_total.to_csv("./data/ipad-pro.csv",index=False)

# samsung-tab-s3
filelist = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/samsung-tab-s3")
print(filelist)
df_total = pd.read_csv(filelist[0])
df_total = sort_dataframe(df_total[column_names_clean_data])
df_total.to_csv("./data/samsung-tab-s3.csv",index=False)

# mbp-2013
filelist = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/mbp2013/browser")
df_total = pd.read_csv(filelist[0])
df_total = df_total.query("environment != 'chromium63'")
df_total = sort_dataframe(df_total[column_names_clean_data])
df_total.to_csv("./data/mbp2013.csv",index=False)

# windows-bison
filelist = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/windows-bison/browser")
print(filelist)
df_total = pd.read_csv(filelist[0])
df_total = sort_dataframe(df_total[column_names_clean_data])
df_total.to_csv("./data/windows-bison.csv",index=False)

# ubuntu-deer
filelist = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/ubuntu-deer/browser")
df_chrome = pd.read_csv(filelist[2])
df_firefox = pd.read_csv(filelist[4])
df_chrome = new_column(df_chrome, size=df_chrome["benchmark"].size, position=3, column_name="environment",
                       name="chrome63")
df_firefox = new_column(df_firefox, size=df_firefox["benchmark"].size, position=3, column_name="environment",
                       name="firefox57")

df_total = pd.concat([df_firefox, df_chrome])
df_total = df_total.query("environment != 'chromium63'")
df_total = sort_dataframe(df_total[column_names_clean_data])
df_total.to_csv("./data/ubuntu-deer.csv",index=False)

