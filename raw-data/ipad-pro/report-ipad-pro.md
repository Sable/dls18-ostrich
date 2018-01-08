### Invariants (configuration parameters that are the same for all runs) ###

| category   | short-name |
| ---------- | ---------- |
| platform   | ipad-pro   |
| input-size | medium     |
platform=ipad-pro,input-size=medium.csv

### Results ###

| benchmark | implementation | compiler   | environment      | mean(s) | std(s) | min(s) | max(s) | repetitions |
| --------- | -------------- | ---------- | ---------------- | ------- | ------ | ------ | ------ | ----------- |
| backprop  | c              | wasm       | safari-ipad-pro  | 0.4030  | 0.0088 | 0.3970 | 0.4270 | 10          |
| backprop  | c              | wasm       | firefox-ipad-pro | 0.4009  | 0.0016 | 0.3980 | 0.4040 | 10          |
| backprop  | c              | wasm       | chrome-ipad-pro  | 0.3985  | 0.0027 | 0.3950 | 0.4040 | 10          |
| backprop  | js             | browserify | chrome-ipad-pro  | 0.7520  | 0.0748 | 0.7032 | 0.9422 | 10          |
| backprop  | js             | browserify | safari-ipad-pro  | 0.7141  | 0.0172 | 0.6982 | 0.7550 | 10          |
| backprop  | js             | browserify | firefox-ipad-pro | 0.7097  | 0.0055 | 0.7023 | 0.7183 | 10          |
| bfs       | cpp            | wasm       | safari-ipad-pro  | 0.2847  | 0.0018 | 0.2820 | 0.2890 | 10          |
| bfs       | cpp            | wasm       | chrome-ipad-pro  | 0.2911  | 0.0106 | 0.2830 | 0.3140 | 10          |
| bfs       | cpp            | wasm       | firefox-ipad-pro | 0.2856  | 0.0016 | 0.2840 | 0.2900 | 10          |
| bfs       | js             | browserify | safari-ipad-pro  | 8.4173  | 0.1235 | 8.2828 | 8.7223 | 10          |
| bfs       | js             | browserify | firefox-ipad-pro | 8.3668  | 0.0290 | 8.3369 | 8.4187 | 10          |
| bfs       | js             | browserify | chrome-ipad-pro  | 8.6003  | 0.4903 | 8.3186 | 9.8662 | 10          |
| crc       | c              | wasm       | firefox-ipad-pro | 1.6385  | 0.0018 | 1.6360 | 1.6410 | 10          |
| crc       | c              | wasm       | safari-ipad-pro  | 1.6448  | 0.0262 | 1.6310 | 1.7010 | 10          |
| crc       | c              | wasm       | chrome-ipad-pro  | 1.6315  | 0.0028 | 1.6290 | 1.6370 | 10          |
| crc       | js             | browserify | safari-ipad-pro  | 1.4519  | 0.0757 | 1.3660 | 1.6230 | 10          |
| crc       | js             | browserify | firefox-ipad-pro | 1.3770  | 0.0058 | 1.3660 | 1.3860 | 10          |
| crc       | js             | browserify | chrome-ipad-pro  | 1.3564  | 0.0013 | 1.3540 | 1.3580 | 10          |
| fft       | c              | wasm       | safari-ipad-pro  | 1.2625  | 0.0054 | 1.2580 | 1.2730 | 10          |
| fft       | c              | wasm       | firefox-ipad-pro | 1.2685  | 0.0041 | 1.2630 | 1.2740 | 10          |
| fft       | c              | wasm       | chrome-ipad-pro  | 1.2669  | 0.0060 | 1.2610 | 1.2810 | 10          |
| fft       | js             | browserify | firefox-ipad-pro | 0.8809  | 0.0071 | 0.8660 | 0.8898 | 10          |
| fft       | js             | browserify | chrome-ipad-pro  | 0.9171  | 0.1126 | 0.8596 | 1.2202 | 10          |
| fft       | js             | browserify | safari-ipad-pro  | 1.0323  | 0.1119 | 0.8619 | 1.1548 | 10          |
| hmm       | c              | wasm       | chrome-ipad-pro  | 3.7444  | 0.0102 | 3.7260 | 3.7590 | 10          |
| hmm       | c              | wasm       | firefox-ipad-pro | 3.8085  | 0.0140 | 3.7810 | 3.8320 | 10          |
| hmm       | c              | wasm       | safari-ipad-pro  | 3.7560  | 0.0177 | 3.7340 | 3.7830 | 10          |
| hmm       | js             | browserify | chrome-ipad-pro  | 2.8820  | 0.0102 | 2.8725 | 2.9094 | 10          |
| hmm       | js             | browserify | safari-ipad-pro  | 3.0316  | 0.0851 | 2.8923 | 3.1799 | 10          |
| hmm       | js             | browserify | firefox-ipad-pro | 2.9158  | 0.0134 | 2.8973 | 2.9328 | 10          |
| lavamd    | c              | wasm       | chrome-ipad-pro  | 2.5959  | 0.0650 | 2.5640 | 2.7790 | 10          |
| lavamd    | c              | wasm       | firefox-ipad-pro | 2.5932  | 0.0691 | 2.5620 | 2.7890 | 10          |
| lavamd    | c              | wasm       | safari-ipad-pro  | 2.5895  | 0.0632 | 2.5530 | 2.7680 | 10          |
| lavamd    | js             | browserify | chrome-ipad-pro  | 1.4646  | 0.0559 | 1.4183 | 1.5654 | 10          |
| lavamd    | js             | browserify | safari-ipad-pro  | 1.5878  | 0.0623 | 1.5232 | 1.7012 | 10          |
| lavamd    | js             | browserify | firefox-ipad-pro | 1.4183  | 0.0063 | 1.4051 | 1.4264 | 10          |
| lud       | c              | wasm       | firefox-ipad-pro | 7.0219  | 0.0312 | 6.9490 | 7.0560 | 10          |
| lud       | c              | wasm       | safari-ipad-pro  | 7.0261  | 0.0465 | 6.9830 | 7.1370 | 10          |
| lud       | c              | wasm       | chrome-ipad-pro  | 7.0495  | 0.1514 | 6.9640 | 7.4740 | 10          |
| lud       | js             | browserify | chrome-ipad-pro  | 6.3634  | 0.1454 | 5.9580 | 6.4690 | 10          |
| lud       | js             | browserify | firefox-ipad-pro | 6.4241  | 0.2147 | 6.0360 | 6.8800 | 10          |
| lud       | js             | browserify | safari-ipad-pro  | 6.5447  | 0.0613 | 6.4850 | 6.6970 | 10          |
| nqueens   | c              | wasm       | safari-ipad-pro  | 6.8290  | 0.0242 | 6.7900 | 6.8720 | 10          |
| nqueens   | c              | wasm       | chrome-ipad-pro  | 6.8299  | 0.0203 | 6.7930 | 6.8460 | 10          |
| nqueens   | c              | wasm       | firefox-ipad-pro | 6.8241  | 0.0140 | 6.8040 | 6.8490 | 10          |
| nqueens   | js             | browserify | safari-ipad-pro  | 5.9283  | 0.0636 | 5.8080 | 6.0220 | 10          |
| nqueens   | js             | browserify | firefox-ipad-pro | 5.7766  | 0.0210 | 5.7380 | 5.8030 | 10          |
| nqueens   | js             | browserify | chrome-ipad-pro  | 5.7435  | 0.0311 | 5.6710 | 5.7830 | 10          |
| nw        | c              | wasm       | chrome-ipad-pro  | 0.2530  | 0.0011 | 0.2510 | 0.2540 | 10          |
| nw        | c              | wasm       | safari-ipad-pro  | 0.2532  | 0.0011 | 0.2520 | 0.2560 | 10          |
| nw        | c              | wasm       | firefox-ipad-pro | 0.2531  | 0.0014 | 0.2510 | 0.2560 | 10          |
| nw        | js             | browserify | safari-ipad-pro  | 0.3299  | 0.1029 | 0.2294 | 0.5666 | 10          |
| nw        | js             | browserify | chrome-ipad-pro  | 0.3957  | 0.0017 | 0.3937 | 0.3986 | 10          |
| nw        | js             | browserify | firefox-ipad-pro | 0.2360  | 0.0032 | 0.2311 | 0.2409 | 10          |
| pagerank  | c              | wasm       | safari-ipad-pro  | 0.7992  | 0.0758 | 0.7680 | 1.0140 | 10          |
| pagerank  | c              | wasm       | firefox-ipad-pro | 0.7694  | 0.0050 | 0.7560 | 0.7740 | 10          |
| pagerank  | c              | wasm       | chrome-ipad-pro  | 0.7758  | 0.0059 | 0.7650 | 0.7840 | 10          |
| pagerank  | js             | browserify | chrome-ipad-pro  | 4.6803  | 0.0118 | 4.6623 | 4.6984 | 10          |
| pagerank  | js             | browserify | firefox-ipad-pro | 4.6948  | 0.0078 | 4.6878 | 4.7108 | 10          |
| pagerank  | js             | browserify | safari-ipad-pro  | 4.7647  | 0.0671 | 4.6768 | 4.8362 | 10          |
| spmv      | c              | wasm       | firefox-ipad-pro | 2.3039  | 0.0011 | 2.3020 | 2.3060 | 10          |
| spmv      | c              | wasm       | safari-ipad-pro  | 2.2928  | 0.0106 | 2.2800 | 2.3020 | 10          |
| spmv      | c              | wasm       | chrome-ipad-pro  | 2.2986  | 0.0013 | 2.2970 | 2.3010 | 10          |
| spmv      | js             | browserify | firefox-ipad-pro | 1.9400  | 0.0016 | 1.9380 | 1.9431 | 10          |
| spmv      | js             | browserify | chrome-ipad-pro  | 1.9398  | 0.0051 | 1.9320 | 1.9483 | 10          |
| spmv      | js             | browserify | safari-ipad-pro  | 1.9364  | 0.0030 | 1.9334 | 1.9437 | 10          |
| srad      | c              | wasm       | chrome-ipad-pro  | 6.4474  | 0.0162 | 6.4240 | 6.4780 | 10          |
| srad      | c              | wasm       | safari-ipad-pro  | 6.4089  | 0.0139 | 6.3960 | 6.4340 | 10          |
| srad      | c              | wasm       | firefox-ipad-pro | 6.4272  | 0.0235 | 6.3910 | 6.4750 | 10          |
| srad      | js             | browserify | chrome-ipad-pro  | 5.5553  | 0.0373 | 5.5014 | 5.6174 | 10          |
| srad      | js             | browserify | firefox-ipad-pro | 5.5712  | 0.0458 | 5.5131 | 5.6300 | 10          |
| srad      | js             | browserify | safari-ipad-pro  | 5.7087  | 0.0596 | 5.6260 | 5.7847 | 10          |