import pandas as pd
from classes.geomeans import get_geo_means
import numpy as np
import re
files = [
"./data/total-iphone10.csv",
"./data/total-samsung8.csv",
"./data/total-pixel2.csv",
"./data/total-ipad-pro.csv",
"./data/total-samsung-tab-s3.csv",
"./data/total-mbp2013.csv",
"./data/total-ubuntu-deer.csv",
"./data/total-windows-bison.csv",
"./data/total-raspberry-pi.csv"]

environments = [
    'chrome63-wasm-c',
    'chrome63-js',
    'chromium56-js',
    'firefox57-wasm-c',
    'firefox57-js',
    'safari11-wasm-c',
    'safari11-js',
    'microsoft-edge-wasm-c',
    'microsoft-edge-js',
    'samsung-internet-js'
    # ,
    # 'node-wasm-c',
    # 'node-js'
]
environments_maps = {
    'chrome63-wasm-c': 'chrome63-wasm-c',
    'chrome63-browserify-js':'chrome63-js',
    'chromium56-browserify-js':'chromium56-js',
    'firefox57-wasm-c':'firefox57-wasm-c',
    'firefox57-browserify-js': 'firefox57-js',
    'safari11-wasm-c':'safari11-wasm-c',
    'safari11-browserify-js': 'safari11-js',
    'node-browserify-js':'node-js',
    'node-wasm-c':'node-wasm-c',
    'microsoft-edge-browserify-js':'microsoft-edge-js',
    'chrome63-wasm-cpp':"chrome63-wasm-c",
    'firefox57-wasm-cpp':'firefox57-wasm-c',
    'node-wasm-cpp': 'node-wasm-c',
    'safari11-wasm-cpp':'safari11-wasm-c',
     "samsung-internet-browserify-js":"samsung-internet-js",
    'microsoft-edge-wasm-c':'microsoft-edge-wasm-c',
    'microsoft-edge-wasm-cpp': 'microsoft-edge-wasm-c'
}
def rotate_text(name):
    return r"\rot{ "+name+" }"
rotate_column_names = np.vectorize(rotate_text)
def names_dic(name):
    if name in environments_maps:
        return environments_maps[name]
    return name

def add_missing_numbers(names, means):

    mean_means = str(np.round(np.mean(means),1))

    for i in range(len(environments)):
        if i < len(names) and names[i] != environments[i]:
            print(environments[i], names[i])
            names = list(names[:i]) + [environments[i]] + list(names[i:])
            means = list(means[:i])+ [0] + list(means[i:])

    while len(means) < len(environments):
        means.append(0)
    means = np.round(means,1).tolist()
    # means.append(mean_means)
    print(means)
    return means

df_array = []
index = 0
print(environments)
df_total = pd.DataFrame(columns=["devices"]+environments)

for file in files:
    df = pd.read_csv(file)
    print(file)
    df["config"] = (df["environment"]+"-"+df["compiler"]+"-"+df["implementation"])
    names_func = np.vectorize(names_dic)
    names = df.query("environment!= 'native'")
    names = pd.unique(names["config"].apply(names_dic))
    means, error_means =  get_geo_means(df["benchmark"],df["mean"],df["std"],index_baseline=0)
    df_total.loc[index] =[file.replace("./data/total-","").replace(".csv","")]+ add_missing_numbers(names, means)
    index+=1
    # df_array.append({"name":file,"env":environments,"geomean":add_missing_numbers(names, means)})
df_total_temp = df_total[environments]


wasm_df = df_total_temp[['chrome63-wasm-c','firefox57-wasm-c','safari11-wasm-c', 'microsoft-edge-wasm-c']]
wasm_df = wasm_df.replace(0, np.NaN)
means_wasm = np.round(wasm_df.mean(axis=1),1)
js_df = df_total_temp[['chrome63-js','chromium56-js','firefox57-js','safari11-js','samsung-internet-js', 'microsoft-edge-js']]
js_df = js_df.replace(0, np.NaN)
means_js = np.round(js_df.mean(axis=1),1)
print("means", means_wasm, means_js)
df_total["mean-wasm"] = means_wasm
df_total["mean-js"] = means_js
print(df_total)
# # print(df_total[df_total!=0])
mean_columns = ["mean"]+np.round(df_total[df_total!=0].mean(axis=0).values,1).tolist()

mean_columns[len(mean_columns)-1] = "-"
mean_columns[len(mean_columns)-2] = "-"
print(mean_columns)
df_total.loc[index] = mean_columns
# print(mean_columns)
df_total = pd.DataFrame(df_total)
df_total = df_total.replace(0, "-").replace(np.NaN, "-")
column_names = rotate_column_names(environments)
df_total.columns = ["device"]  +column_names.tolist() + ["mean-js", "mean-wasm"]
df_total.to_latex("./table-node.latex", index=False)
df_total.to_csv("./table-node.csv", index=False)


