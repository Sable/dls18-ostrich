import pandas as pd
import numpy as np
from classes.preprocess import new_column, new_columns
import subprocess
# constants for clean up
ubuntu_deer = True
mbp2013 = True

column_names_clean_data = ['benchmark', 'implementation', 'compiler', 'environment', 'mean', 'std',
                           'min', 'max', 'repetitions']
order_columns_environment = ["native","chrome63","firefox57","safari11","chromium56","samsung-internet","microsoft-edge"]
def sorting_order_env(env):
    return order_columns_environment.index(env)

order_columns_compilers = ["g++","gcc","wasm","browserify"]
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

# raspberry-pi
filelist = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/raspberry-pi-3/browser")
df_total_browsers = pd.read_csv(filelist[0])
df_total_browsers = new_column(df_total_browsers, size=df_total_browsers["benchmark"].size, position=1, column_name="implementation",
                       name="js")
df_total_browsers = new_column(df_total_browsers, size=df_total_browsers["benchmark"].size, position=2, column_name="compiler",
                       name="browserify")
df_total_browsers = new_column(df_total_browsers, size=df_total_browsers["benchmark"].size, position=3, column_name="environment",
                       name="chromium56")

# # raspberry-pi node
# filelist_node = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/raspberry-pi-3/server")
# df_total_node = pd.read_csv(filelist_node[0])
# df_total_node = new_column(df_total_node, size=df_total_node["benchmark"].size, position=3, column_name="environment",
#                        name="node")

# raspberry-pi native
filelist_native = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/raspberry-pi-3/native")
df_total_native_raspberry = pd.read_csv(filelist_native[0])
df_total_native_raspberry = new_column(df_total_native_raspberry, size=df_total_native_raspberry["benchmark"].size, position=3, column_name="environment",
                       name="native")

df_total = pd.concat([df_total_browsers[column_names_clean_data],
                      df_total_native_raspberry[column_names_clean_data]])
df_total = sort_dataframe(df_total)
df_total.to_csv("./data/total-raspberry-pi.csv",index=False)

# mbp-2013
# mbp-2013 browsers
filelist_browsers = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/mbp2013/browser")
df_total_browsers = pd.read_csv(filelist_browsers[0])
df_total_browsers = df_total_browsers.query("environment != 'chromium63'"
                                            " and environment != 'chromium38'"
                                            " and environment != 'firefox39'"
                                            " and environment != 'chromium63'")
# # mbp-2013 node
# filelist_node = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/mbp2013/server")
# df_total_node = pd.read_csv(filelist_node[0])
# df_total_node = new_column(df_total_node, size=df_total_node["benchmark"].size, position=3, column_name="environment",
#                        name="node")
df_total = pd.concat([df_total_browsers[column_names_clean_data],
                      df_total_native_raspberry[column_names_clean_data]])
df_total = sort_dataframe(df_total)
df_total.to_csv("./data/total-mbp2013.csv",index=False)

# windows-bison
#windows-bison browsers
filelist_browsers = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/windows-bison/browser")
df_total_browsers = pd.read_csv(filelist_browsers[0])

# #windows-bison node
# filelist_node = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/windows-bison/server")
# df_total_node = pd.read_csv(filelist_node[0])
# df_total_node = new_column(df_total_node, size=df_total_node["benchmark"].size, position=3, column_name="environment",
#                        name="node")
df_total = pd.concat([df_total_browsers[column_names_clean_data],
                      # df_total_node[column_names_clean_data],
                      df_total_native_raspberry[column_names_clean_data]])
df_total = sort_dataframe(df_total)
df_total.to_csv("./data/total-windows-bison.csv",index=False)


# ubuntu-deer

# ubuntu-deer browsers
filelist = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/ubuntu-deer/browser")
df_chrome = pd.read_csv(filelist[2])
df_firefox = pd.read_csv(filelist[4])
df_chrome = new_column(df_chrome, size=df_chrome["benchmark"].size, position=3, column_name="environment",
                       name="chrome63")
df_firefox = new_column(df_firefox, size=df_firefox["benchmark"].size, position=3, column_name="environment",
                       name="firefox57")
df_total_browsers = pd.concat([df_firefox, df_chrome])
df_total_browsers = df_total_browsers.query("environment != 'chromium63' "
                          "and environment != 'chromium38'"
                          " and environment != 'firefox39'"
                          " and environment != 'firefox34'")
# #ubuntu-deer node
# filelist_node = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/ubuntu-deer/server")
# df_total_node = pd.read_csv(filelist_node[0])
# df_total_node = new_column(df_total_node, size=df_total_node["benchmark"].size, position=3, column_name="environment",
#                        name="node")


df_total = pd.concat([df_total_browsers[column_names_clean_data],
                      # df_total_node[column_names_clean_data],
                      df_total_native_raspberry[column_names_clean_data]])
df_total = sort_dataframe(df_total)
df_total.to_csv("./data/total-ubuntu-deer.csv",index=False)

# Iphone 10
filelist = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/iphone10/browser")
df_chrome = pd.read_csv(filelist[0])
df_chrome = new_column(df_chrome, size=df_chrome["benchmark"].size, position=3, column_name="environment",name="chrome63")
df_firefox = pd.read_csv(filelist[1])
df_firefox = new_column(df_firefox, size=df_firefox["benchmark"].size, position=3, column_name="environment", name="firefox57")
df_safari = pd.read_csv(filelist[3])
df_safari = new_column(df_safari, size=df_safari["benchmark"].size, position=3, column_name="environment", name="safari11")

print(df_chrome,df_firefox,df_safari)

df_total = pd.concat([df_chrome[column_names_clean_data], df_firefox[column_names_clean_data], df_safari[column_names_clean_data],
                      df_total_native_raspberry[column_names_clean_data]])
df_total = sort_dataframe(df_total)
df_total.to_csv("./data/total-iphone10.csv",index=False)

# Samsung 8
filelist = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/samsung8")
df_total_browsers = pd.read_csv(filelist[0])
df_total = pd.concat([df_total_browsers[column_names_clean_data], df_total_native_raspberry[column_names_clean_data]])
df_total = sort_dataframe(df_total)
df_total.to_csv("./data/total-samsung8.csv",index=False)

# pixel 2
filelist = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/pixel2")
df_total_browsers = pd.read_csv(filelist[0])
df_total = pd.concat([df_total_browsers[column_names_clean_data], df_total_native_raspberry[column_names_clean_data]])
df_total = sort_dataframe(df_total)
df_total.to_csv("./data/total-pixel2.csv",index=False)

# ipad-pro
filelist = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/ipad-pro")
df_total_browsers = pd.read_csv(filelist[0])
df_total = pd.concat([df_total_browsers[column_names_clean_data], df_total_native_raspberry[column_names_clean_data]])
df_total = sort_dataframe(df_total)
df_total.to_csv("./data/total-ipad-pro.csv",index=False)

# samsung-tab-s3
filelist = list_of_files("/Users/davidherrera/Documents/Research/ostrich-updated/ecoop18-ostrich/raw-data/samsung-tab-s3")
df_total_browsers = pd.read_csv(filelist[0])
df_total = pd.concat([df_total_browsers[column_names_clean_data], df_total_native_raspberry[column_names_clean_data]])
df_total = sort_dataframe(df_total)
df_total.to_csv("./data/total-samsung-tab-s3.csv",index=False)
