

### Invariants (configuration parameters that are the same for all runs) ###

| category    | short-name      |
| ----------- | --------------- |
| platform    | iphone10        |
| environment | chrome-iphone10 |
| input-size  | medium          |
platform=iphone10,environment=chrome-iphone10,input-size=medium.csv

### Results ###

| benchmark | implementation | compiler   | mean(s) | std(s) | min(s) | max(s) | repetitions |
| --------- | -------------- | ---------- | ------- | ------ | ------ | ------ | ----------- |
| backprop  | c              | wasm       | 0.3518  | 0.0148 | 0.3330 | 0.3790 | 10          |
| backprop  | js             | browserify | 0.6436  | 0.0221 | 0.6311 | 0.7055 | 10          |
| bfs       | cpp            | wasm       | 0.2009  | 0.0049 | 0.1920 | 0.2050 | 10          |
| bfs       | js             | browserify | 6.2034  | 0.1446 | 5.9464 | 6.5165 | 10          |
| crc       | c              | wasm       | 1.1726  | 0.0008 | 1.1710 | 1.1740 | 10          |
| crc       | js             | browserify | 1.2590  | 0.0008 | 1.2580 | 1.2600 | 10          |
| fft       | c              | wasm       | 0.8783  | 0.0093 | 0.8680 | 0.9010 | 10          |
| fft       | js             | browserify | 0.7022  | 0.0086 | 0.6918 | 0.7170 | 10          |
| hmm       | c              | wasm       | 2.7628  | 0.0106 | 2.7340 | 2.7720 | 10          |
| hmm       | js             | browserify | 1.9181  | 0.0074 | 1.9104 | 1.9339 | 10          |
| lavamd    | c              | wasm       | 1.4622  | 0.0119 | 1.4470 | 1.4760 | 10          |
| lavamd    | js             | browserify | 1.1105  | 0.0264 | 1.0741 | 1.1414 | 10          |
| lud       | c              | wasm       | 1.1122  | 0.0340 | 1.0840 | 1.2020 | 10          |
| lud       | js             | browserify | 0.8251  | 0.0468 | 0.7850 | 0.9200 | 10          |
| nqueens   | c              | wasm       | 5.4997  | 0.1839 | 5.3720 | 5.9070 | 10          |
| nqueens   | js             | browserify | 4.8143  | 0.0121 | 4.7990 | 4.8390 | 10          |
| nw        | c              | wasm       | 0.2084  | 0.0029 | 0.2040 | 0.2150 | 10          |
| nw        | js             | browserify | 0.3339  | 0.0017 | 0.3298 | 0.3360 | 10          |
| pagerank  | c              | wasm       | 0.5848  | 0.0404 | 0.5170 | 0.6310 | 10          |
| pagerank  | js             | browserify | 3.2450  | 0.0321 | 3.1800 | 3.2860 | 10          |
| spmv      | c              | wasm       | 1.6504  | 0.0195 | 1.6110 | 1.6850 | 10          |
| spmv      | js             | browserify | 2.2313  | 0.2677 | 1.8423 | 2.4019 | 10          |
| srad      | c              | wasm       | 3.3439  | 0.0017 | 3.3410 | 3.3470 | 10          |
| srad      | js             | browserify | 2.8092  | 0.0584 | 2.7658 | 2.9480 | 10          |


### Invariants (configuration parameters that are the same for all runs) ###

| category    | short-name       |
| ----------- | ---------------- |
| platform    | iphone10         |
| environment | firefox-iphone10 |
| input-size  | medium           |
platform=iphone10,environment=firefox-iphone10,input-size=medium.csv

### Results ###

| benchmark | implementation | compiler   | mean(s) | std(s) | min(s) | max(s) | repetitions |
| --------- | -------------- | ---------- | ------- | ------ | ------ | ------ | ----------- |
| backprop  | c              | wasm       | 0.3629  | 0.0238 | 0.3390 | 0.4160 | 10          |
| backprop  | js             | browserify | 0.6637  | 0.0322 | 0.6442 | 0.7518 | 10          |
| bfs       | cpp            | wasm       | 0.2009  | 0.0028 | 0.1970 | 0.2050 | 10          |
| bfs       | js             | browserify | 6.2665  | 0.1260 | 6.0460 | 6.4207 | 10          |
| crc       | c              | wasm       | 1.1730  | 0.0005 | 1.1720 | 1.1740 | 10          |
| crc       | js             | browserify | 1.2625  | 0.0016 | 1.2600 | 1.2660 | 10          |
| fft       | c              | wasm       | 0.8756  | 0.0067 | 0.8690 | 0.8880 | 10          |
| fft       | js             | browserify | 0.7126  | 0.0107 | 0.6998 | 0.7321 | 10          |
| hmm       | c              | wasm       | 2.7677  | 0.0041 | 2.7620 | 2.7730 | 10          |
| hmm       | js             | browserify | 1.9043  | 0.0303 | 1.8435 | 1.9297 | 10          |
| lavamd    | c              | wasm       | 1.4828  | 0.0335 | 1.4480 | 1.5460 | 10          |
| lavamd    | js             | browserify | 1.0931  | 0.0071 | 1.0863 | 1.1094 | 10          |
| lud       | c              | wasm       | 1.1039  | 0.0061 | 1.0940 | 1.1160 | 10          |
| lud       | js             | browserify | 0.8251  | 0.0213 | 0.7940 | 0.8750 | 10          |
| nqueens   | c              | wasm       | 5.3832  | 0.0092 | 5.3670 | 5.3920 | 10          |
| nqueens   | js             | browserify | 4.8498  | 0.0209 | 4.8180 | 4.8890 | 10          |
| nw        | c              | wasm       | 0.2070  | 0.0037 | 0.2040 | 0.2140 | 10          |
| nw        | js             | browserify | 0.2405  | 0.0027 | 0.2369 | 0.2451 | 10          |
| pagerank  | c              | wasm       | 0.6076  | 0.0288 | 0.5360 | 0.6350 | 10          |
| pagerank  | js             | browserify | 3.3085  | 0.0510 | 3.2356 | 3.3908 | 10          |
| spmv      | c              | wasm       | 1.6346  | 0.0182 | 1.6110 | 1.6560 | 10          |
| spmv      | js             | browserify | 2.2151  | 0.1070 | 2.1152 | 2.3988 | 10          |
| srad      | c              | wasm       | 3.3437  | 0.0016 | 3.3420 | 3.3470 | 10          |
| srad      | js             | browserify | 2.7791  | 0.0091 | 2.7643 | 2.7937 | 10          |