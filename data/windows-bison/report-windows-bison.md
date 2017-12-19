# Ecoop18-Ostrich

## Device

|name   |cpu    |memory |OS     | GCC | Emscripten|
|----   |---    |-------|-------|-----|-----------|
|windows-bison    |  Intel(R) Core(TM) i7-3820 CPU @ 3.60GHz   | 16 GB |   Windows 10 Enterprise | llvm-gcc 4.2.1   |1.37.22 |
# Web Environments
|environment    |version | JS Engine Version|Developer Build|
|---            |------- |------- |-------|
|chrome         |63.0.3239.84 |v8 6.3.292.46|-|
|firefox        |Gecko/20100101 Firefox/57.0.2|-|-|
|microsoft-edge |38.14393.1066.0|-|-|
|Node |8.9.3 |v8 6.1.534.47| |
# All Results

| category   | short-name    |
| ---------- | ------------- |
| platform   | windows-bison |
| input-size | medium        |
| file       | platform=windows-bison,input-size=medium.csv
|

| benchmark | implementation | compiler   | environment            | mean(s) | std(s) | min(s)  | max(s)  | repetitions |
| --------- | -------------- | ---------- | ---------------------- | ------- | ------ | ------- | ------- | ----------- |
| backprop  | c              | wasm       | chrome-windows         | 0.8026  | 0.0068 | 0.7920  | 0.8170  | 31          |
| backprop  | c              | wasm       | firefox-windows        | 0.8015  | 0.0087 | 0.7860  | 0.8260  | 32          |
| backprop  | js             | browserify | firefox-windows        | 1.5464  | 0.0375 | 1.4916  | 1.6774  | 33          |
| backprop  | js             | browserify | microsoft-edge-windows | 1.7447  | 0.0904 | 1.6553  | 2.0042  | 32          |
| backprop  | js             | browserify | chrome-windows         | 1.5560  | 0.0471 | 1.4979  | 1.7008  | 31          |
| bfs       | cpp            | wasm       | firefox-windows        | 0.1222  | 0.0010 | 0.1210  | 0.1250  | 30          |
| bfs       | cpp            | wasm       | chrome-windows         | 0.1565  | 0.0040 | 0.1510  | 0.1680  | 30          |
| bfs       | js             | browserify | chrome-windows         | 0.3093  | 0.0050 | 0.2946  | 0.3260  | 30          |
| bfs       | js             | browserify | firefox-windows        | 0.2309  | 0.0020 | 0.2277  | 0.2366  | 30          |
| bfs       | js             | browserify | microsoft-edge-windows | 0.3327  | 0.0178 | 0.3182  | 0.4071  | 30          |
| crc       | c              | wasm       | chrome-windows         | 1.1413  | 0.0108 | 1.1260  | 1.1580  | 30          |
| crc       | c              | wasm       | firefox-windows        | 0.9803  | 0.0038 | 0.9750  | 0.9930  | 30          |
| crc       | js             | browserify | firefox-windows        | 2.6090  | 0.0044 | 2.6020  | 2.6190  | 30          |
| crc       | js             | browserify | microsoft-edge-windows | 9.0509  | 0.1239 | 8.8100  | 9.3160  | 30          |
| crc       | js             | browserify | chrome-windows         | 0.9319  | 0.0032 | 0.9270  | 0.9390  | 30          |
| fft       | c              | wasm       | chrome-windows         | 0.9960  | 0.0066 | 0.9850  | 1.0110  | 30          |
| fft       | c              | wasm       | firefox-windows        | 0.7858  | 0.0107 | 0.7740  | 0.8150  | 30          |
| fft       | js             | browserify | chrome-windows         | 5.7622  | 0.0409 | 5.7043  | 5.8877  | 30          |
| fft       | js             | browserify | microsoft-edge-windows | 6.7455  | 0.0286 | 6.6934  | 6.8050  | 30          |
| fft       | js             | browserify | firefox-windows        | 1.2694  | 0.0076 | 1.2584  | 1.2892  | 30          |
| hmm       | c              | wasm       | chrome-windows         | 2.5872  | 0.5377 | 2.3530  | 4.9120  | 30          |
| hmm       | c              | wasm       | firefox-windows        | 1.9575  | 0.0118 | 1.9410  | 1.9990  | 30          |
| hmm       | js             | browserify | chrome-windows         | 4.3760  | 0.6848 | 4.0265  | 6.3653  | 30          |
| hmm       | js             | browserify | microsoft-edge-windows | 4.5299  | 0.0545 | 4.4738  | 4.7083  | 30          |
| hmm       | js             | browserify | firefox-windows        | 4.2037  | 0.0293 | 4.1575  | 4.2685  | 30          |
| lavamd    | c              | wasm       | firefox-windows        | 1.2813  | 0.0181 | 1.2490  | 1.3130  | 30          |
| lavamd    | c              | wasm       | chrome-windows         | 1.2475  | 0.0207 | 1.2250  | 1.3020  | 30          |
| lavamd    | js             | browserify | microsoft-edge-windows | 2.9041  | 0.0221 | 2.8596  | 2.9853  | 30          |
| lavamd    | js             | browserify | firefox-windows        | 1.2867  | 0.0070 | 1.2756  | 1.3093  | 30          |
| lavamd    | js             | browserify | chrome-windows         | 1.8037  | 0.0172 | 1.7768  | 1.8499  | 30          |
| lud       | c              | wasm       | chrome-windows         | 1.9501  | 0.0155 | 1.9230  | 1.9900  | 30          |
| lud       | c              | wasm       | firefox-windows        | 2.0744  | 0.4090 | 1.9300  | 3.7240  | 30          |
| lud       | js             | browserify | firefox-windows        | 2.1934  | 0.5709 | 1.9590  | 4.4110  | 30          |
| lud       | js             | browserify | microsoft-edge-windows | 2.2115  | 0.5304 | 2.0480  | 4.9710  | 30          |
| lud       | js             | browserify | chrome-windows         | 1.9972  | 0.0198 | 1.9560  | 2.0450  | 30          |
| nqueens   | c              | wasm       | chrome-windows         | 3.9802  | 0.0962 | 3.8790  | 4.3140  | 30          |
| nqueens   | c              | wasm       | firefox-windows        | 3.5281  | 0.0216 | 3.4740  | 3.5610  | 30          |
| nqueens   | js             | browserify | microsoft-edge-windows | 5.7127  | 0.0628 | 5.5770  | 5.8760  | 30          |
| nqueens   | js             | browserify | chrome-windows         | 6.1237  | 0.1033 | 6.0180  | 6.4890  | 30          |
| nqueens   | js             | browserify | firefox-windows        | 5.6116  | 0.1166 | 5.3720  | 5.8420  | 30          |
| nw        | c              | wasm       | chrome-windows         | 0.5853  | 0.0037 | 0.5790  | 0.5970  | 30          |
| nw        | c              | wasm       | firefox-windows        | 0.5501  | 0.0018 | 0.5470  | 0.5540  | 30          |
| nw        | js             | browserify | microsoft-edge-windows | 4.4390  | 0.0619 | 4.3383  | 4.5955  | 30          |
| nw        | js             | browserify | chrome-windows         | 0.9619  | 0.0100 | 0.9507  | 0.9950  | 30          |
| nw        | js             | browserify | firefox-windows        | 0.7434  | 0.0109 | 0.7260  | 0.7761  | 30          |
| pagerank  | c              | wasm       | firefox-windows        | 0.7074  | 0.0173 | 0.6860  | 0.7660  | 30          |
| pagerank  | c              | wasm       | chrome-windows         | 0.7498  | 0.0039 | 0.7430  | 0.7630  | 30          |
| pagerank  | js             | browserify | microsoft-edge-windows | 0.7507  | 0.0168 | 0.7322  | 0.8096  | 30          |
| pagerank  | js             | browserify | chrome-windows         | 0.8979  | 0.0033 | 0.8925  | 0.9059  | 30          |
| pagerank  | js             | browserify | firefox-windows        | 0.8040  | 0.0250 | 0.7883  | 0.9147  | 30          |
| spmv      | c              | wasm       | chrome-windows         | 1.0561  | 0.0532 | 1.0030  | 1.2810  | 30          |
| spmv      | c              | wasm       | firefox-windows        | 0.9590  | 0.0261 | 0.9270  | 1.0290  | 30          |
| spmv      | js             | browserify | microsoft-edge-windows | 2.3218  | 0.0726 | 2.2701  | 2.6334  | 30          |
| spmv      | js             | browserify | chrome-windows         | 1.9365  | 0.0984 | 1.8871  | 2.3673  | 30          |
| spmv      | js             | browserify | firefox-windows        | 1.3776  | 0.0246 | 1.3571  | 1.4730  | 30          |
| srad      | c              | wasm       | firefox-windows        | 3.4799  | 0.0049 | 3.4720  | 3.4920  | 30          |
| srad      | c              | wasm       | chrome-windows         | 3.7429  | 0.0453 | 3.6890  | 3.9130  | 30          |
| srad      | js             | browserify | firefox-windows        | 7.3764  | 0.4099 | 5.8677  | 7.5471  | 30          |
| srad      | js             | browserify | chrome-windows         | 7.6214  | 0.0460 | 7.5330  | 7.7217  | 30          |
| srad      | js             | browserify | microsoft-edge-windows | 15.9899 | 0.3612 | 15.6939 | 17.4402 | 30          |
# Chrome 63

| category    | short-name     |
| ----------- | -------------- |
| platform    | windows-bison  |
| environment | chrome-windows |
| input-size  | medium         |
| file | platform=windows-bison,environment=chrome-windows,input-size=medium.csv |


### Results ###

| benchmark | implementation | compiler   | mean   | std    | min    | max    | repetitions |
| --------- | -------------- | ---------- | ------ | ------ | ------ | ------ | ----------- |
| backprop  | c              | wasm       | 0.8026 | 0.0068 | 0.7920 | 0.8170 | 31          |
| backprop  | js             | browserify | 1.5560 | 0.0471 | 1.4979 | 1.7008 | 31          |
| bfs       | cpp            | wasm       | 0.1565 | 0.0040 | 0.1510 | 0.1680 | 30          |
| bfs       | js             | browserify | 0.3093 | 0.0050 | 0.2946 | 0.3260 | 30          |
| crc       | c              | wasm       | 1.1413 | 0.0108 | 1.1260 | 1.1580 | 30          |
| crc       | js             | browserify | 0.9319 | 0.0032 | 0.9270 | 0.9390 | 30          |
| fft       | c              | wasm       | 0.9960 | 0.0066 | 0.9850 | 1.0110 | 30          |
| fft       | js             | browserify | 5.7622 | 0.0409 | 5.7043 | 5.8877 | 30          |
| hmm       | c              | wasm       | 2.5872 | 0.5377 | 2.3530 | 4.9120 | 30          |
| hmm       | js             | browserify | 4.3760 | 0.6848 | 4.0265 | 6.3653 | 30          |
| lavamd    | c              | wasm       | 1.2475 | 0.0207 | 1.2250 | 1.3020 | 30          |
| lavamd    | js             | browserify | 1.8037 | 0.0172 | 1.7768 | 1.8499 | 30          |
| lud       | c              | wasm       | 1.9501 | 0.0155 | 1.9230 | 1.9900 | 30          |
| lud       | js             | browserify | 1.9972 | 0.0198 | 1.9560 | 2.0450 | 30          |
| nqueens   | c              | wasm       | 3.9802 | 0.0962 | 3.8790 | 4.3140 | 30          |
| nqueens   | js             | browserify | 6.1237 | 0.1033 | 6.0180 | 6.4890 | 30          |
| nw        | c              | wasm       | 0.5853 | 0.0037 | 0.5790 | 0.5970 | 30          |
| nw        | js             | browserify | 0.9619 | 0.0100 | 0.9507 | 0.9950 | 30          |
| pagerank  | c              | wasm       | 0.7498 | 0.0039 | 0.7430 | 0.7630 | 30          |
| pagerank  | js             | browserify | 0.8979 | 0.0033 | 0.8925 | 0.9059 | 30          |
| spmv      | c              | wasm       | 1.0561 | 0.0532 | 1.0030 | 1.2810 | 30          |
| spmv      | js             | browserify | 1.9365 | 0.0984 | 1.8871 | 2.3673 | 30          |
| srad      | c              | wasm       | 3.7429 | 0.0453 | 3.6890 | 3.9130 | 30          |
| srad      | js             | browserify | 7.6214 | 0.0460 | 7.5330 | 7.7217 | 30          |

# Firefox 57

| category    | short-name      |
| ----------- | --------------- |
| platform    | windows-bison   |
| environment | firefox-windows |
| input-size  | medium          |
| file        |       platform=windows-bison,environment=firefox-windows,input-size=medium.csv |


### Results ###

| benchmark | implementation | compiler   | mean(s) | std(s) | min(s) | max(s) | repetitions |
| --------- | -------------- | ---------- | ------- | ------ | ------ | ------ | ----------- |
| backprop  | c              | wasm       | 0.8015  | 0.0087 | 0.7860 | 0.8260 | 32          |
| backprop  | js             | browserify | 1.5464  | 0.0375 | 1.4916 | 1.6774 | 33          |
| bfs       | cpp            | wasm       | 0.1222  | 0.0010 | 0.1210 | 0.1250 | 30          |
| bfs       | js             | browserify | 0.2309  | 0.0020 | 0.2277 | 0.2366 | 30          |
| crc       | c              | wasm       | 0.9803  | 0.0038 | 0.9750 | 0.9930 | 30          |
| crc       | js             | browserify | 2.6090  | 0.0044 | 2.6020 | 2.6190 | 30          |
| fft       | c              | wasm       | 0.7858  | 0.0107 | 0.7740 | 0.8150 | 30          |
| fft       | js             | browserify | 1.2694  | 0.0076 | 1.2584 | 1.2892 | 30          |
| hmm       | c              | wasm       | 1.9575  | 0.0118 | 1.9410 | 1.9990 | 30          |
| hmm       | js             | browserify | 4.2037  | 0.0293 | 4.1575 | 4.2685 | 30          |
| lavamd    | c              | wasm       | 1.2813  | 0.0181 | 1.2490 | 1.3130 | 30          |
| lavamd    | js             | browserify | 1.2867  | 0.0070 | 1.2756 | 1.3093 | 30          |
| lud       | c              | wasm       | 2.0744  | 0.4090 | 1.9300 | 3.7240 | 30          |
| lud       | js             | browserify | 2.1934  | 0.5709 | 1.9590 | 4.4110 | 30          |
| nqueens   | c              | wasm       | 3.5281  | 0.0216 | 3.4740 | 3.5610 | 30          |
| nqueens   | js             | browserify | 5.6116  | 0.1166 | 5.3720 | 5.8420 | 30          |
| nw        | c              | wasm       | 0.5501  | 0.0018 | 0.5470 | 0.5540 | 30          |
| nw        | js             | browserify | 0.7434  | 0.0109 | 0.7260 | 0.7761 | 30          |
| pagerank  | c              | wasm       | 0.7074  | 0.0173 | 0.6860 | 0.7660 | 30          |
| pagerank  | js             | browserify | 0.8040  | 0.0250 | 0.7883 | 0.9147 | 30          |
| spmv      | c              | wasm       | 0.9590  | 0.0261 | 0.9270 | 1.0290 | 30          |
| spmv      | js             | browserify | 1.3776  | 0.0246 | 1.3571 | 1.4730 | 30          |
| srad      | c              | wasm       | 3.4799  | 0.0049 | 3.4720 | 3.4920 | 30          |
| srad      | js             | browserify | 7.3764  | 0.4099 | 5.8677 | 7.5471 | 30          |

# Microsoft Edge 38
| category       | short-name             |
| -------------- | ---------------------- |
| implementation | js                     |
| compiler       | browserify             |
| platform       | windows-bison          |
| environment    | microsoft-edge-windows |
| input-size     | medium                 |
|file|implementation=js,compiler=browserify,platform=windows-bison,environment=microsoft-edge-windows,input-size=medium.csv|


### Results ###

| benchmark | mean(s) | std(s) | min(s)  | max(s)  | repetitions |
| --------- | ------- | ------ | ------- | ------- | ----------- |
| backprop  | 1.7447  | 0.0904 | 1.6553  | 2.0042  | 30         |
| bfs       | 0.3327  | 0.0178 | 0.3182  | 0.4071  | 30          |
| crc       | 9.0509  | 0.1239 | 8.8100  | 9.3160  | 30          |
| fft       | 6.7455  | 0.0286 | 6.6934  | 6.8050  | 30          |
| hmm       | 4.5299  | 0.0545 | 4.4738  | 4.7083  | 30          |
| lavamd    | 2.9041  | 0.0221 | 2.8596  | 2.9853  | 30          |
| lud       | 2.2115  | 0.5304 | 2.0480  | 4.9710  | 30          |
| nqueens   | 5.7127  | 0.0628 | 5.5770  | 5.8760  | 30          |
| nw        | 4.4390  | 0.0619 | 4.3383  | 4.5955  | 30          |
| pagerank  | 0.7507  | 0.0168 | 0.7322  | 0.8096  | 30          |
| spmv      | 2.3218  | 0.0726 | 2.2701  | 2.6334  | 30          |
| srad      | 15.9899 | 0.3612 | 15.6939 | 17.4402 | 30          |
# Node
| category    | short-name                |
| ----------- | ------------------------- |
| platform    | windows-bison             |
| environment | node-remote-windows-bison |
| input-size  | medium                    |
| file | platform=windows-bison,environment=node-remote-windows-bison,input-size=medium.csv|


### Results ###

| benchmark | implementation | compiler    | mean(s) | std(s) | min(s) | max(s) | repetitions |
| --------- | -------------- | ----------- | ------- | ------ | ------ | ------ | ----------- |
| backprop  | c              | server-wasm | 0.7662  | 0.0112 | 0.7500 | 0.7970 | 30          |
| backprop  | js             | browserify  | 1.5038  | 0.0246 | 1.4680 | 1.5780 | 30          |
| bfs       | cpp            | server-wasm | 0.1318  | 0.0079 | 0.1250 | 0.1410 | 30          |
| bfs       | js             | browserify  | 0.8924  | 0.0049 | 0.8900 | 0.9070 | 30          |
| crc       | c              | server-wasm | 0.9395  | 0.0054 | 0.9370 | 0.9530 | 30          |
| crc       | js             | browserify  | 0.9094  | 0.0063 | 0.9060 | 0.9210 | 30          |
| fft       | c              | server-wasm | 0.8932  | 0.0082 | 0.8750 | 0.9060 | 30          |
| fft       | js             | browserify  | 2.0673  | 0.0204 | 2.0460 | 2.1560 | 30          |
| hmm       | c              | server-wasm | 2.3383  | 0.0094 | 2.3130 | 2.3600 | 30          |
| hmm       | js             | browserify  | 3.9533  | 0.0126 | 3.9370 | 3.9840 | 30          |
| lavamd    | c              | server-wasm | 1.1857  | 0.0068 | 1.1720 | 1.2030 | 30          |
| lavamd    | js             | browserify  | 1.7297  | 0.0083 | 1.7180 | 1.7500 | 30          |
| lud       | c              | server-wasm | 1.9406  | 0.0388 | 1.8750 | 2.0000 | 30          |
| lud       | js             | browserify  | 2.0072  | 0.0588 | 1.9370 | 2.1870 | 30          |
| nqueens   | c              | server-wasm | 3.9290  | 0.0271 | 3.9070 | 4.0470 | 30          |
| nqueens   | js             | browserify  | 6.1319  | 0.0814 | 6.0470 | 6.3900 | 30          |
| nw        | c              | server-wasm | 0.5468  | 0.0004 | 0.5460 | 0.5470 | 30          |
| nw        | js             | browserify  | 1.0208  | 0.0106 | 1.0150 | 1.0620 | 30          |
| pagerank  | c              | server-wasm | 0.7157  | 0.0064 | 0.7030 | 0.7190 | 30          |
| pagerank  | js             | browserify  | 0.8627  | 0.0069 | 0.8590 | 0.8750 | 30          |
| spmv      | c              | server-wasm | 0.9079  | 0.0112 | 0.8900 | 0.9380 | 30          |
| spmv      | js             | browserify  | 1.9709  | 0.0532 | 1.9060 | 2.1560 | 30          |
| srad      | c              | server-wasm | 3.5789  | 0.0172 | 3.5470 | 3.6250 | 30          |
| srad      | js             | browserify  | 6.6252  | 0.0648 | 6.5150 | 6.7500 | 30          |