# Ecoop18-Ostrich

## Device

|name   |cpu    |memory |OS     | GCC | Emscripten|
|----   |---    |-------|-------|-----|-----------|
|mbp-2013    |  Intel(R) Core(TM) i5 @ 2.4 GHz   |  8 GB 1600 MHz DDR3      |   macOS High Sierra 10.13.1 |llvm-gcc 4.2.1   |1.37.22 |
# Web Environments
|environment    |version | JS Engine Version|Developer Build|
|---            |------- |------- |-------|
|chrome|63.0.3239.84 | 6.3.292.46|-|
|chromium63|63.0.3239.0|V8 6.3.292|508578|
|chromium38|38.0.2125.0|V8 3.28.71.2|290012|
|firefox57 |Gecko/20100101 Firefox/57.0.2|-|-|
|firefox39 |Gecko/20100101 Firefox/39.0|-|-|
|safari11 | 11.0.1 (13604.3.5)|-|-|
# Chrome 63

| category    | short-name |
| ----------- | ---------- |
| platform    | mbp2013    |
| environment | chrome     |
| input-size  | medium     |

### Results ###

| benchmark | implementation | compiler   | mean   | std    | min    | max    | repetitions |
| --------- | -------------- | ---------- | ------ | ------ | ------ | ------ | ----------- |
| bfs       | cpp            | wasm       | 0.1945 | 0.0116 | 0.1770 | 0.2240 | 30          |
| bfs       | js             | browserify | 0.3478 | 0.0148 | 0.3237 | 0.3753 | 30          |
| lud       | c              | wasm       | 2.3506 | 0.1064 | 2.2150 | 2.6370 | 30          |
| lud       | js             | browserify | 3.3140 | 0.1822 | 2.9650 | 3.6620 | 30          |
| spmv      | c              | wasm       | 1.1719 | 0.0291 | 1.1260 | 1.2620 | 30          |
| spmv      | js             | browserify | 2.1706 | 0.0300 | 2.1166 | 2.2358 | 30          |
| backprop  | c              | wasm       | 0.9994 | 0.0081 | 0.9870 | 1.0230 | 30          |
| backprop  | js             | browserify | 1.5641 | 0.0289 | 1.5470 | 1.7098 | 30          |
| crc       | c              | wasm       | 1.1880 | 0.0155 | 1.1630 | 1.2150 | 30          |
| crc       | js             | browserify | 1.0698 | 0.0494 | 1.0420 | 1.3220 | 30          |
| fft       | c              | wasm       | 1.1151 | 0.0114 | 1.0860 | 1.1340 | 30          |
| fft       | js             | browserify | 6.0469 | 0.2928 | 5.8859 | 7.2532 | 30          |
| hmm       | c              | wasm       | 2.8621 | 0.1427 | 2.6810 | 3.3920 | 30          |
| hmm       | js             | browserify | 4.9263 | 0.3509 | 4.3196 | 5.8110 | 30          |
| lavamd    | c              | wasm       | 1.4084 | 0.0299 | 1.3820 | 1.5510 | 30          |
| lavamd    | js             | browserify | 2.0787 | 0.0100 | 2.0636 | 2.0976 | 30          |
| nqueens   | c              | wasm       | 4.7775 | 0.0566 | 4.7200 | 5.0480 | 30          |
| nqueens   | js             | browserify | 7.0794 | 0.0585 | 7.0060 | 7.2790 | 30          |
| nw        | c              | wasm       | 0.6722 | 0.0119 | 0.6570 | 0.7190 | 30          |
| nw        | js             | browserify | 1.1104 | 0.0118 | 1.0897 | 1.1503 | 30          |
| pagerank  | c              | wasm       | 0.4266 | 0.0560 | 0.3750 | 0.5580 | 30          |
| pagerank  | js             | browserify | 0.7488 | 0.0937 | 0.6717 | 0.9887 | 30          |
| srad      | c              | wasm       | 3.6129 | 0.1012 | 3.5180 | 4.0850 | 30          |
| srad      | js             | browserify | 8.0752 | 0.1625 | 7.8037 | 8.6446 | 30          |

# Chromium 63


| category    | short-name |
| ----------- | ---------- |
| platform    | mbp2013    |
| environment | chromium63 |
| input-size  | medium     |
platform=mbp2013,environment=chromium63,input-size=medium.csv

### Results ###

| benchmark | implementation | compiler   | mean   | std    | min    | max    | repetitions |
| --------- | -------------- | ---------- | ------ | ------ | ------ | ------ | ----------- |
| bfs       | js             | browserify | 0.3479 | 0.0407 | 0.3168 | 0.5215 | 30          |
| lud       | c              | wasm       | 2.2904 | 0.0988 | 2.1280 | 2.5790 | 30          |
| bfs       | cpp            | wasm       | 0.1866 | 0.0078 | 0.1780 | 0.2030 | 30          |
| lud       | js             | browserify | 3.1867 | 0.2215 | 2.8530 | 3.6660 | 30          |
| spmv      | js             | browserify | 2.1661 | 0.0230 | 2.1283 | 2.2383 | 30          |
| spmv      | c              | wasm       | 1.2077 | 0.0329 | 1.1580 | 1.3100 | 30          |
| backprop  | c              | wasm       | 1.0103 | 0.0457 | 0.9810 | 1.2360 | 30          |
| backprop  | js             | browserify | 1.5705 | 0.0192 | 1.5519 | 1.6412 | 30          |
| crc       | js             | browserify | 1.0536 | 0.0121 | 1.0350 | 1.0810 | 30          |
| crc       | c              | wasm       | 1.0358 | 0.0141 | 1.0120 | 1.0610 | 30          |
| fft       | c              | wasm       | 1.0342 | 0.0218 | 1.0050 | 1.1270 | 30          |
| fft       | js             | browserify | 6.0704 | 0.1308 | 5.9700 | 6.6069 | 30          |
| hmm       | js             | browserify | 5.0262 | 0.3192 | 4.5437 | 5.7553 | 30          |
| hmm       | c              | wasm       | 2.8908 | 0.3009 | 2.6560 | 4.3420 | 30          |
| lavamd    | js             | browserify | 2.0571 | 0.0195 | 2.0256 | 2.1306 | 30          |
| lavamd    | c              | wasm       | 1.4114 | 0.0165 | 1.3860 | 1.4710 | 30          |
| nqueens   | js             | browserify | 7.1155 | 0.1145 | 7.0310 | 7.6140 | 30          |
| nqueens   | c              | wasm       | 4.7198 | 0.0190 | 4.6790 | 4.7580 | 30          |
| nw        | js             | browserify | 1.1109 | 0.0093 | 1.1003 | 1.1353 | 30          |
| pagerank  | js             | browserify | 0.6830 | 0.0487 | 0.6534 | 0.8751 | 30          |
| pagerank  | c              | wasm       | 0.3885 | 0.0197 | 0.3700 | 0.4520 | 30          |
| srad      | js             | browserify | 7.9477 | 0.2215 | 7.6390 | 8.7155 | 30          |
| nw        | c              | wasm       | 0.6737 | 0.0080 | 0.6640 | 0.7040 | 30          |
| srad      | c              | wasm       | 3.5675 | 0.0372 | 3.5190 | 3.6650 | 30          |
# Chromium 38


| category       | short-name |
| -------------- | ---------- |
| implementation | js         |
| compiler       | browserify |
| platform       | mbp2013    |
| environment    | chromium38 |
| input-size     | medium     |
implementation=js,compiler=browserify,platform=mbp2013,environment=chromium38,input-size=medium.csv

### Results ###

| benchmark | mean   | std    | min    | max    | repetitions |
| --------- | ------ | ------ | ------ | ------ | ----------- |
| bfs       | 0.3391 | 0.0759 | 0.2372 | 0.5358 | 30          |
| spmv      | 2.0246 | 0.0693 | 1.9459 | 2.2322 | 30          |
| backprop  | 1.5660 | 0.0150 | 1.5473 | 1.6056 | 30          |
| crc       | 1.4816 | 0.0139 | 1.4550 | 1.5150 | 30          |
| hmm       | 4.0216 | 0.4265 | 3.7624 | 5.6352 | 30          |
| fft       | 4.2384 | 0.0742 | 4.1603 | 4.6036 | 30          |
| lavamd    | 0.9702 | 0.0120 | 0.9480 | 1.0041 | 30          |
| nqueens   | 5.3251 | 0.0400 | 5.2280 | 5.3840 | 30          |
| nw        | 1.1371 | 0.0108 | 1.1209 | 1.1670 | 30          |
| srad      | 7.9070 | 0.1665 | 7.7597 | 8.6892 | 30          |
| pagerank  | 0.4522 | 0.0330 | 0.4309 | 0.6150 | 30          |
# Firefox 57


| category    | short-name |
| ----------- | ---------- |
| platform    | mbp2013    |
| environment | firefox57  |
| input-size  | medium     |

### Results ###

| benchmark | implementation | compiler   | mean    | std       | min     | max     | repetitions |
| --------- | -------------- | ---------- | ------- | --------- | ------- | ------- | ----------- |
| bfs       | js             | browserify | 0.3310s | +-0.0156s | 0.3083s | 0.3850s | 30          |
| bfs       | cpp            | wasm       | 0.1634s | +-0.0072s | 0.1470s | 0.1740s | 30          |
| lud       | js             | browserify | 3.2922s | +-0.1368s | 3.0630s | 3.5070s | 30          |
| lud       | c              | wasm       | 2.1307s | +-0.0705s | 1.9800s | 2.3440s | 30          |
| spmv      | js             | browserify | 1.4961s | +-0.0271s | 1.4437s | 1.5401s | 30          |
| spmv      | c              | wasm       | 1.0236s | +-0.0206s | 0.9870s | 1.0650s | 30          |
| backprop  | js             | browserify | 1.7900s | +-0.0534s | 1.7428s | 1.9857s | 30          |
| crc       | js             | browserify | 2.9793s | +-0.0205s | 2.9340s | 3.0240s | 30          |
| crc       | c              | wasm       | 1.1437s | +-0.0349s | 1.1060s | 1.3010s | 30          |
| backprop  | c              | wasm       | 0.9922s | +-0.0139s | 0.9780s | 1.0500s | 30          |
| fft       | js             | browserify | 1.3760s | +-0.0195s | 1.3421s | 1.4328s | 30          |
| fft       | c              | wasm       | 0.8661s | +-0.0110s | 0.8550s | 0.9160s | 30          |
| hmm       | js             | browserify | 4.2046s | +-0.3045s | 3.9699s | 5.1198s | 30          |
| hmm       | c              | wasm       | 2.2801s | +-0.0503s | 2.1920s | 2.4600s | 30          |
| lavamd    | c              | wasm       | 1.4189s | +-0.0154s | 1.3990s | 1.4760s | 30          |
| nqueens   | js             | browserify | 6.4014s | +-0.1091s | 6.1770s | 6.6150s | 30          |
| nw        | js             | browserify | 0.9145s | +-0.0098s | 0.8933s | 0.9350s | 30          |
| nqueens   | c              | wasm       | 4.2169s | +-0.0433s | 4.1400s | 4.3540s | 30          |
| lavamd    | js             | browserify | 1.4489s | +-0.0155s | 1.4264s | 1.5043s | 30          |
| nw        | c              | wasm       | 0.6931s | +-0.0066s | 0.6800s | 0.7080s | 30          |
| pagerank  | js             | browserify | 0.5679s | +-0.0146s | 0.5328s | 0.6067s | 30          |
| pagerank  | c              | wasm       | 0.3908s | +-0.0084s | 0.3810s | 0.4150s | 30          |
| srad      | js             | browserify | 6.4442s | +-0.1909s | 6.2207s | 6.8669s | 30          |
| srad      | c              | wasm       | 3.1112s | +-0.0299s | 3.0620s | 3.1620s | 30          |

# Firefox 39

| category       | short-name |
| -------------- | ---------- |
| implementation | js         |
| compiler       | browserify |
| platform       | mbp2013    |
| environment    | firefox39  |
| input-size     | medium     |

### Results ###

| benchmark | mean     | std       | min     | max      | repetitions |
| --------- | -------- | --------- | ------- | -------- | ----------- |
| lud       | 4.2376s  | +-0.2888s | 3.8960s | 5.2820s  | 30          |
| bfs       | 0.4150s  | +-0.0598s | 0.3836s | 0.7250s  | 30          |
| spmv      | 2.1503s  | +-0.5145s | 1.4291s | 2.5890s  | 30          |
| backprop  | 2.1421s  | +-0.1059s | 1.7518s | 2.2088s  | 30          |
| crc       | 4.6952s  | +-0.1241s | 4.5190s | 5.1210s  | 30          |
| fft       | 8.0984s  | +-0.4786s | 7.1237s | 8.8812s  | 30          |
| hmm       | 6.5387s  | +-0.2138s | 6.2643s | 7.0952s  | 30          |
| lavamd    | 1.6776s  | +-0.0878s | 1.5565s | 1.8475s  | 30          |
| nqueens   | 12.5489s | +-1.9818s | 8.4940s | 14.0070s | 30          |
| nw        | 1.3033s  | +-0.1992s | 1.0753s | 1.6843s  | 30          |
| pagerank  | 0.5286s  | +-0.1096s | 0.4376s | 0.7361s  | 30          |
| srad      | 9.4685s  | +-0.1732s | 9.2873s | 10.2938s | 30          |
# Safari 11

### Results ###

| benchmark | implementation | compiler   | mean    | std       | min     | max     | repetitions |
| --------- | -------------- | ---------- | ------- | --------- | ------- | ------- | ----------- |
| bfs       | js             | browserify | 6.0331s | +-0.4828s | 5.6491s | 7.8765s | 60          |
| bfs       | cpp            | wasm       | 0.2172s | +-0.0128s | 0.1960s | 0.2520s | 30          |
| lud       | js             | browserify | 2.6190s | +-0.1602s | 2.3760s | 3.1060s | 30          |
| lud       | c              | wasm       | 2.5538s | +-0.0540s | 2.4690s | 2.7040s | 30          |
| spmv      | js             | browserify | 1.7429s | +-0.0531s | 1.7113s | 2.0117s | 30          |
| spmv      | c              | wasm       | 1.5793s | +-0.0207s | 1.5470s | 1.6410s | 30          |
| backprop  | js             | browserify | 1.4515s | +-0.0386s | 1.4222s | 1.6238s | 30          |
| backprop  | c              | wasm       | 1.0464s | +-0.0092s | 1.0310s | 1.0690s | 30          |
| crc       | c              | wasm       | 1.0584s | +-0.0108s | 1.0380s | 1.0770s | 30          |
| crc       | js             | browserify | 1.1809s | +-0.0155s | 1.1540s | 1.2240s | 30          |
| fft       | js             | browserify | 0.8890s | +-0.0337s | 0.8086s | 0.9241s | 30          |
| fft       | c              | wasm       | 0.9166s | +-0.0346s | 0.8760s | 1.0590s | 30          |
| hmm       | js             | browserify | 3.3805s | +-0.2681s | 3.1489s | 4.2002s | 30          |
| hmm       | c              | wasm       | 3.1014s | +-0.0933s | 3.0150s | 3.4310s | 30          |
| lavamd    | js             | browserify | 1.5586s | +-0.0234s | 1.4736s | 1.6166s | 30          |
| lavamd    | c              | wasm       | 2.6738s | +-0.0192s | 2.6360s | 2.7120s | 30          |
| nqueens   | js             | browserify | 5.5401s | +-0.0550s | 5.4480s | 5.6540s | 30          |
| nqueens   | c              | wasm       | 5.0270s | +-0.1001s | 4.9190s | 5.4200s | 30          |
| nw        | js             | browserify | 0.8805s | +-0.0193s | 0.8349s | 0.9120s | 30          |
| nw        | c              | wasm       | 0.9028s | +-0.0100s | 0.8880s | 0.9390s | 30          |
| pagerank  | js             | browserify | 4.9341s | +-0.0891s | 4.7936s | 5.1834s | 30          |
| pagerank  | c              | wasm       | 0.5465s | +-0.0072s | 0.5360s | 0.5720s | 30          |
| srad      | js             | browserify | 5.5862s | +-0.0926s | 5.4519s | 5.9214s | 30          |
| srad      | c              | wasm       | 4.2460s | +-0.0390s | 4.1900s | 4.3180s | 30          |
