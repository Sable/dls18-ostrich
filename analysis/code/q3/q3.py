import re
import pandas as pd
import numpy as np
from classes.plots import Plots
from classes.geomeans import get_geo_means
import os

def get_speed_up_info(data):
    baselines_name = data["environment"][0]
    configs_non = len(data.query("benchmark== 'backprop' and implementation == 'js'"))-1
    baseline = data.query("environment == '"+baselines_name+"'")
    baseline_mean = np.repeat(baseline["mean"],configs_non)
    baseline_std= np.repeat(baseline["std"],configs_non)
    rest = data.query("environment != '"+baselines_name+"'")
    speedup = np.divide(baseline_mean,rest["mean"].values)
    # print(speedup.size)
    speedup_std = np.multiply(np.sqrt(np.add((rest["std"].values / rest["mean"].values) ** 2 ,
                                             (baseline_std/ baseline_mean) ** 2)),speedup)
    # print(speedup_std.size)

    df = pd.DataFrame({"benchmark": rest["benchmark"].values, "speedup":speedup,"speedup_std":speedup_std,
                       "environment":rest["environment"].values})
    return df

df = pd.read_csv("./data/proprietary-ipad-pro.csv")
get_speed_up_info(df)
# print( get_speed_up_info(df))

legends = ["Chrome63-js","Firefox57-js","Chrome63-wasm-c","Firefox57-wasm-c","Proprietary Browser"]
x_ticks = []
geomeans = []
geomean_error = []
files = [
"./data/proprietary-iphone10.csv",
"./data/proprietary-ipad-pro.csv",
"./data/proprietary-mbp2013.csv",
"./data/proprietary-windows-bison.csv",
"./data/proprietary-samsung-tab-s3.csv",
"./data/proprietary-samsung-s8.csv",
"./data/proprietary-pixel2.csv"]
sam_index = 0
df_sam = pd.DataFrame(columns=["Device","Chrome63-js-nolavamd", "Firefox57-js-nolavamd", "Chrome63-js", "Firefox57-js"])
for file in files:
    print(file)
    file = str(re.sub('.*proprietary-','',file))
    x_ticks.append(file.replace(".csv",""))
    df = pd.read_csv("./data/proprietary-"+file)
    data = get_speed_up_info(df)
    geomean, error = get_geo_means(data["benchmark"],data["speedup"],data["speedup_std"])

    if len(geomean) == 2:
        if file == 'pixel2.csv':
            geomean = np.array([0,geomean[0],0,geomean[1]])
            error = np.array([0,error[0],0,error[1]])
        else:
            geomean = np.append(geomean, np.zeros((4 - len(geomean),)))
            error = np.append(error,np.zeros((4-len(error),)))

    geomeans.append(geomean)
    geomean_error.append(error)
    if file == 'samsung-s8.csv' or file == 'samsung-tab-s3.csv':
        samng_no_lavamd = data.query("benchmark != 'lavamd'")
        geomean_no_lavamd, error_no_lavamd = get_geo_means(samng_no_lavamd["benchmark"], samng_no_lavamd["speedup"], samng_no_lavamd["speedup_std"])

        df_sam.loc[sam_index] = [file.replace(".csv","")]+np.around(geomean_no_lavamd,2).tolist() + np.around(geomean, 2)[:2].tolist()
        sam_index+=1
    print("GEO", geomean)
df_sam.to_latex("./samsung.latex", index=False)
geomeans = np.array(geomeans)
geomean_error = np.array(geomean_error)

Plots.plot_v2(y=geomeans.T,
                  output_file="../../plots/geomeans-proprietary.png",
                  x_tick=x_ticks, title=None,
                  legends=legends, random_colors=False,
                  y_label="Speedup (relative to proprietary browser)", y_lim=[0, 2.5],
                  geo_mean=False,move_xtick=0, baseline_off=4, q3a=True)


