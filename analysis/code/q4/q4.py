import re
import pandas as pd
import numpy as np
from classes.plots import Plots
from classes.geomeans import get_geo_means
import os
def get_speed_up_info_native(data):
    baseline = data.query("environment == 'native'")
    baseline_mean = np.repeat(baseline["mean"],2)
    baseline_std = np.repeat(baseline["std"],2)
    rest = data.query("environment != 'native'")
    speedup = np.divide(baseline_mean,rest["mean"].values)
    speedup_std = np.multiply(np.sqrt(np.add((rest["std"].values / rest["mean"].values) ** 2 ,
                                             (baseline_std/ baseline_mean) ** 2)),speedup)
    df = pd.DataFrame({"benchmark": rest["benchmark"].values, "speedup":speedup,"speedup_std":speedup_std,
                       "environment":rest["environment"].values})
    return df

def get_speed_up_info(data,file):
    print(file)
    if file == 'raspberry-pi':
        data = data.query("compiler != 'wasm'")
        baseline = data.query("environment == 'node'")
        baseline_mean = baseline["mean"]
        baseline_std = baseline["std"]
        rest = data.query("environment != 'node'")

        speedup = np.divide( rest["mean"].values,baseline_mean)
        # print(speedup.size)
        speedup_std = np.multiply(np.sqrt(np.add((rest["std"].values / rest["mean"].values) ** 2,
                                                 (baseline_std / baseline_mean) ** 2)), speedup)

        rest.loc[data["compiler"] == 'browserify', 'compiler'] = 'js'
        df = pd.DataFrame({"benchmark": rest["benchmark"].values, "speedup": speedup, "speedup_std": speedup_std,
                           "environment": rest["environment"].values,"compiler":rest["compiler"].values})
        return df
    else:
        if file == 'ubuntu-deer':
            repeat_js = 2
            repeat_wasm = 2
        elif file == 'mbp2013':
            repeat_js = 3
            repeat_wasm = 3
        elif file == 'windows-bison':
            repeat_js = 3
            repeat_wasm = 3

        node_wasm = data.query("compiler == 'wasm' and environment == 'node'")
        node_wasm_mean = np.repeat(node_wasm["mean"],repeat_wasm)
        node_wasm_std = np.repeat(node_wasm["std"], repeat_wasm)
        rest_wasm = data.query("compiler == 'wasm' and environment != 'node'")
        speedup_wasm = np.divide(rest_wasm["mean"].values, node_wasm_mean)
        speedup_std_wasm = np.multiply(np.sqrt(np.add((rest_wasm["std"].values / rest_wasm["mean"].values) ** 2,
                                                 (node_wasm_std / node_wasm_mean) ** 2)), speedup_wasm)
        data.loc[data.eval("compiler == 'wasm' and environment != 'node'"), 'speedup'] = speedup_wasm.values
        data.loc[data.eval("compiler == 'wasm' and environment != 'node'"), 'speedup_std'] = speedup_std_wasm.values

        # Javascript
        node_js = data.query("compiler == 'browserify' and environment == 'node'")


        node_js_mean = np.repeat(node_js["mean"], repeat_js)
        node_js_std = np.repeat(node_js["std"], repeat_js)

        rest_js = data.query("compiler == 'browserify' and environment != 'node'")
        speedup_js = np.divide(rest_js["mean"].values,node_js_mean)
        speedup_std_js = np.multiply(np.sqrt(np.add((rest_js["std"].values / rest_js["mean"].values) ** 2,
                                                      (node_js_std / node_js_mean) ** 2)), speedup_js)
        data.loc[data.eval("compiler == 'browserify' and environment != 'node'"), 'speedup'] = speedup_js.values
        data.loc[data.eval("compiler == 'browserify' and environment != 'node'"), 'speedup_std'] = speedup_std_js.values

        data.loc[data["compiler"] == 'browserify', 'compiler'] = 'js'
        df = pd.DataFrame({"benchmark": data["benchmark"].values, "speedup":data["speedup"].values,
                           "speedup_std":data["speedup_std"].values,"compiler":data["compiler"].values,
                           "environment":data["environment"].values})
        return df.query("environment != 'node'")
# df = pd.read_csv("./data/node-browsers-windows-bison.csv")
# get_speed_up_info(df)
# print( get_speed_up_info(df))

#
files_node = ["./data/node-browsers-mbp2013.csv",
"./data/node-browsers-windows-bison.csv",
"./data/node-browsers-ubuntu-deer.csv",
"./data/node-browsers-raspberry-pi.csv",
  "./data/node-native-mbp2013.csv",
  "./data/node-native-windows-bison.csv",
  "./data/node-native-ubuntu-deer.csv",
  "./data/node-native-raspberry-pi.csv"]
legends_node = []
legends_native = []
x_ticks_node = []
x_ticks_node_wasm = ["mbp2013","windows-bison","ubuntu-deer"]
x_ticks_native = []
geomeans_wasm_js = []
geomeans_node_js = []
geomeans_node_error_js = []
geomeans_node_wasm = []
geomeans_node_error_wasm = []
geomeans_native = []
geomeans_native_error = []


for file in files_node:
    if re.match('.*node-browsers', file):
        file = str(re.sub('.*node-browsers-', '', file))
        df = pd.read_csv("./data/node-browsers-" + file)
        legends_node = pd.unique(df["environment"])
        name = file.replace(".csv", "")
        data = get_speed_up_info(df, name)
        geomean_wasm_js,_ =  get_geo_means(data["benchmark"],data["speedup"],data["speedup_std"])
        geomeans_wasm_js.append(geomean_wasm_js)

        data_js = data[data["compiler"] == 'js']
        geomean_js, error_js = get_geo_means(data_js["benchmark"],data_js["speedup"],data_js["speedup_std"])


        if data_js["compiler"].values[0] == 'js':
            x_ticks_node.append(name)

            if name == 'mbp2013':

                geomean_js = np.concatenate([geomean_js, np.array([0,0])])

                error_js = np.array([error_js,np.array([0,0])])
            elif name == 'ubuntu-deer':
                geomean_js = np.concatenate([geomean_js, np.array([0,0,0])])
                error_js = np.array([error_js, np.array([0, 0])])
            elif name == 'windows-bison':
                geomean_js = np.concatenate([[ geomean_js[0],geomean_js[1],0,geomean_js[2]], np.array([0])])
                error_js = np.concatenate([[ error_js[0],error_js[1],0,error_js[2]], np.array([0])])

            elif name == 'raspberry-pi':
                geomean_js = np.concatenate([[0, 0, 0, 0], geomean_js])
                error_js = np.array([np.array([0, 0, 0, 0]), error_js])

        geomeans_node_js.append(geomean_js)
        geomeans_node_error_js.append(error_js)

        if name != 'raspberry-pi':
            data_wasm = data[data["compiler"] == 'wasm']
            geomean_wasm, error_wasm = get_geo_means(data_wasm["benchmark"], data_wasm["speedup"], data_wasm["speedup_std"])
            if name == 'ubuntu-deer':
                geomean_wasm = np.concatenate([geomean_wasm, np.array([0, 0])])
                error_wasm = np.array([error_wasm, np.array([0, 0])])
            elif name == 'mbp2013':
                geomean_wasm = np.concatenate([geomean_wasm, np.array([0])])
                error_wasm = np.array([error_wasm, np.array([0])])
            elif name == 'windows-bison':
                geomean_wasm = np.array(geomean_wasm[:2].tolist() + [0] + [geomean_wasm[2]])
                error_wasm = np.array(error_wasm[:2].tolist() + [0] + [error_wasm[2]])
            print(name, geomean_wasm)
            geomeans_node_wasm.append(geomean_wasm)
            geomeans_node_error_wasm.append(error_wasm)
    else:
        file = str(re.sub('.*node-native-', '', file))
        df = pd.read_csv("./data/node-native-" + file)
        legends = ["wasm","js"]
        name = file.replace(".csv", "")
        x_ticks_native.append(name)
        data = get_speed_up_info_native(df)
        geomean_native, geomean_error = get_geo_means(data["benchmark"],data["speedup"],data["speedup_std"])
        geomeans_native.append(geomean_native)
        geomeans_native_error.append(geomean_error)
legends_node_browsers_js = ["Chrome63-js","Firefox57-js","Safari11-js","Microsoft-Edge-js","Chromium56-js"]
legends_node_browsers = ["Chrome63-js","Chrome63-wasm-c","Firefox57-js","Firefox57-wasm-c","Safari11-js","Safari11-wasm-c","Microsoft-Edge-js","Microsoft-Edge-wasm-c","Chromium56-js"]
legends_node_browsers_wasm = ["Chrome63-wasm-c","Firefox57-wasm-c","Safari11-wasm-c","Microsoft-Edge-wasm-c"]




geomeans_node_wasm.append(np.array([0,0,0,0]))
df_table = pd.DataFrame(columns=["Device"]+legends_node_browsers)
df_table["Device"] = np.array(["mbp2013",  "windows-bison", "ubuntu-deer","raspberry-pi"]).T
df_table[legends_node_browsers_js] = np.round(geomeans_node_js,1)
df_table[legends_node_browsers_wasm] = np.round(geomeans_node_wasm,1)
print(df_table[legends_node_browsers_js])
print(df_table[legends_node_browsers_wasm])

mean_browsers = np.round(df_table[legends_node_browsers].replace(0, np.NaN).mean(axis=0),1)
mean_device_js = np.round(df_table[legends_node_browsers_js].replace(0, np.NaN).mean(axis=1),1)
mean_device_wasm = np.round(df_table[legends_node_browsers_wasm].replace(0, np.NaN).mean(axis=1),1)

print("MEANS",mean_device_js,"wasm",mean_device_wasm )
df_table["mean-js"] = mean_device_js
df_table["mean-wasm"] = mean_device_wasm
print( ["Mean Browser"] + mean_browsers.tolist() + ["-"])
df_table.loc[len(df_table)] = ["Mean Browser"] + mean_browsers.tolist() + ["-","-"]
df_table = df_table.replace(np.nan, "-")
df_table = df_table.replace(0, "-")
df_table.to_latex("./q4.latex", index=False)
df_table.to_csv("./q4.csv", index=False)

# df_table = df_table.append(  + geomeans_node_js)

# Plots.plot_v2(y=np.array(geomeans_node_js).T,
#               output_file="../../plots/geomeans-node-browsers-js.png",
#               x_tick=x_ticks_node, title="Geometric Mean Browsers - Node JS",
#               legends=["chrome","firefox","safari","microsoft-edge","chromium56","node "], random_colors=False,
#               y_label="Speedup", geo_mean=False, move_xtick=0, baseline_off=5)
# Plots.plot_v2(y=np.array(geomeans_node_wasm).T,
#               output_file="../../plots/geomeans-node-browsers-wasm.png",
#               x_tick=x_ticks_node_wasm, title="Geometric Mean Browsers - Node Wasm",
#               legends=["chrome","firefox","safari","node"], random_colors=False,
#               y_label="Speedup", geo_mean=False, move_xtick=0, baseline_off=3)

# print(geomeans_native)
# Plots.plot_v2(y=np.array(geomeans_native).T,
#               output_file="../../plots/geomeans-node-native.png",
#               x_tick=x_ticks_native, title=None,
#               legends=["Wasm-c","JS","C"], random_colors=False,
#               y_label="Speedup (relative to C)",y_lim=[0,2], geo_mean=False, move_xtick=0, baseline_off=4, font_size=20)




#     else:
#
#     print(file)
#     file = str(re.sub('.*proprietary-','',file))
#     x_ticks.append(file.replace(".csv",""))
#     df = pd.read_csv("./data/proprietary-"+file)
#     data = get_speed_up_info(df)
#     print(data)
#     geomean, error = get_geo_means(data["benchmark"],data["speedup"],data["speedup_std"])
#     print(geomean)
#     if len(geomean) == 2:
#         if file == 'pixel2.csv':
#             geomean = np.array([0,geomean[0],0,geomean[1]])
#             error = np.array([0,error[0],0,error[1]])
#         else:
#             geomean = np.append(geomean, np.zeros((4 - len(geomean),)))
#             error = np.append(error,np.zeros((4-len(geomean),)))
#     geomeans.append(geomean)
#     geomean_error.append(error)
# geomeans = np.array(geomeans)
# geomean_error = np.array(geomean_error)
# Plots.plot_v2(y=geomeans.T,
#                   output_file="../../plots/geomeans_proprietary.png",
#                   x_tick=x_ticks, title="Geometric Mean Proprietary",
#                   legends=legends, random_colors=False,
#                   y_label="Speedup", y_lim=[0, 2.5], geo_mean=False,move_xtick=0, baseline_off=4)
