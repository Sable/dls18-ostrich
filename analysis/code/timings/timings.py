import pandas as pd
import numpy as np
from classes.plots import Plots
import re
from classes.helper_timings import get_timing_data

files = [
"./data/iphone10.csv",
"./data/samsung8.csv",
"./data/pixel2.csv",
"./data/samsung-tab-s3.csv",
"./data/ipad-pro.csv",
"./data/mbp2013.csv",
"./data/ubuntu-deer.csv",
"./data/windows-bison.csv"]
x_ticks = ['backprop','bfs', 'crc', 'fft', 'hmm', 'lavamd', 'lud', 'nqueens', 'nw',
 'pagerank', 'spmv', 'srad']
possible_legends = ['chrome63-browserify', 'chrome63-wasm', 'firefox57-browserify',
 'firefox57-wasm', 'microsoft-edge-browserify','safari11-browserify' 'safari11-wasm']
def sort_legends(df):

        df["order_env"] = (df["environment"] + "-" + df["compiler"] ).apply(sorting_order_env)
        sorting_order = ["order_env"]
        return df.sort_values(by=sorting_order, axis=0)
for name in files:
    print(name)
    name = re.sub('.*/data/','',name).replace(".csv","")

    df = pd.read_csv("./data/"+name + ".csv")
    legends = pd.unique(df["environment"] + "-" + df["compiler"])
    if name == 'samsung8' or name == 'samsung-tab-s3':
        data, error = get_timing_data(df["benchmark"], df["mean"], df["std"], samsung_internet=True)
    else:
        data, error = get_timing_data(df["benchmark"], df["mean"], df["std"])

    Plots.plot_v2(data, y_error=error,output_file="../../plots/timings-"+name+".png",
                  x_tick=x_ticks, title="Timings - "+name, legends=legends,
                                  random_colors=False,width = None,
                                y_label="Time (s)", y_lim=None, geo_mean=False,
                                move_xtick = 0,baseline_off=2,move=None, speedup=False)
    # print(data, data.size, error, error.size, legends, x_ticks)



