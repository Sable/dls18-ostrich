import pandas as pd
import numpy as np
from classes.plots import Plots
from classes.speedup import histogram_plot

from classes.geomeans import get_geo_means
import re
from classes.helper_q2 import get_speed_up_info,get_speed_up_info_native

legends = ["Chrome63-wasm-c","Firefox57-wasm-c","Safari11-wasm-c","Microsoft-Edge-wasm-c","JS"]
geomeans = []
geomean_error = []
x_ticks = []
files = [
"./data/iphone10.csv",
"./data/samsung-s8.csv",
"./data/pixel2.csv",
"./data/samsung-tab-s3.csv",
"./data/ipad-pro.csv",
"./data/mbp2013.csv",
"./data/ubuntu-deer.csv",
"./data/windows-bison.csv"]
for name in files:
    file = re.sub('.*/data/','',name)
    name = file.replace(".csv","")
    x_ticks.append(name)
    df = pd.read_csv("./data/"+file)
    data = get_speed_up_info(df)
    geomean, error = get_geo_means(data["benchmark"],data["speedup"],data["speedup_std"])
    if name == 'iphone10' or name == 'ipad-pro' or name == 'mbp2013':
        geomean = np.append(geomean, [0])
        error = np.append(error, [0])
    elif len(geomean) == 2:
        geomean = np.append(geomean,[0,0])
        error = np.append(error, [0,0])
    elif name == 'windows-bison':
        geomean = geomean[:2].tolist() + [0] + [geomean[2]]
        error = error[:2].tolist() + [0] + [error[2]]
    geomeans.append(geomean)
    geomean_error.append(error)
geomeans = np.array(geomeans)
geomean_error = np.array(geomean_error)
# print(len(geomeans))
Plots.plot_v2(y=geomeans.T,
                  output_file="../../plots/geomeans-wasm-vs-js.png",
                  x_tick=x_ticks, title=None,
                  legends=legends, random_colors=False,
                  y_label="Speedup (relative to JavaScript)", y_lim=[0, 3], geo_mean=False,
              move_xtick=0, baseline_off=4, q2a=True)

# histogram_plot("./data/native-vs-all-mbp2013.csv",
#                "../../plots/native-vs-all-mbp2013.png",
#                12, 4, name_plot="Wasm vs. Native mbp2013", include_name=False, y_lim=[0, 2])

files_native = [
"./data/native-browsers-mbp2013.csv",
"./data/native-browsers-windows-bison.csv",
"./data/native-browsers-ubuntu-deer.csv"
]
geomeans_native_browsers = []
geomeans_native_browsers_error = []
x_ticks_native = []
for name in files_native:
    df = pd.read_csv( name)
    file = re.sub('.*/data/native-browsers-','',name)
    name = file.replace(".csv","")
    x_ticks_native.append(name)
    data = get_speed_up_info_native(name, df)
    geomean, error = get_geo_means(data["benchmark"],data["speedup"],data["speedup_std"])
    if name == 'ubuntu-deer':
        geomean = np.append(geomean, [0,0])
        error = np.append(error, [0,0])
    elif name == 'mbp2013':
        geomean = np.append(geomean,[0])
        error = np.append(error, [0])
    elif name == 'windows-bison':
        geomean = geomean[:2].tolist() + [0] + [geomean[2]]
        error = error[:2].tolist() + [0] + [error[2]]
    geomeans_native_browsers.append(geomean)
    geomeans_native_browsers_error.append(error)
geomeans_native_browsers = np.array(geomeans_native_browsers)
x_ticks_native = ["mbp2013","windows-bison","ubuntu-deer"]
legends_native =  ["Chrome63-wasm-c","Firefox57-wasm-c","Safari11-wasm-c","Microsoft-Edge-wasm-c","C"]

Plots.plot_v2(y=geomeans_native_browsers.T,
                  output_file="../../plots/geomeans-wasm-vs-c.png",
                  x_tick=x_ticks_native, title=None,
                  legends=legends_native, random_colors=False,
                  y_label="Speedup (relative to C)", y_lim=[0, 2], geo_mean=False,
              move_xtick=0, baseline_off=3, q2c=True)
