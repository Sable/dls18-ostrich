### Invariants (configuration parameters that are the same for all runs) ###

| category | short-name |
| -------- | ---------- |
.csv

### Results ###

| benchmark | implementation | compiler   | platform       | environment               | input-size | mean(s) | std(s) | min(s)  | max(s)  | repetitions |
| --------- | -------------- | ---------- | -------------- | ------------------------- | ---------- | ------- | ------ | ------- | ------- | ----------- |
| backprop  | c              | wasm       | samsung-tab-s3 | chrome-samsung8           | medium     | 1.2169  | 0.0306 | 1.1590  | 1.2390  | 10          |
| backprop  | c              | wasm       | samsung-tab-s3 | firefox-samsung8          | medium     | 1.5613  | 0.1272 | 1.4580  | 1.8840  | 10          |
| backprop  | js             | browserify | samsung-tab-s3 | samsung-internet-samsung8 | medium     | 1.2582  | 0.0305 | 1.2251  | 1.2957  | 10          |
| backprop  | js             | browserify | samsung-tab-s3 | firefox-samsung8          | medium     | 3.2793  | 0.0969 | 3.1280  | 3.4409  | 10          |
| backprop  | js             | browserify | samsung-tab-s3 | chrome-samsung8           | medium     | 1.1236  | 0.0143 | 1.1051  | 1.1536  | 10          |
| bfs       | cpp            | wasm       | samsung-tab-s3 | firefox-samsung8          | medium     | 0.5246  | 0.0202 | 0.4900  | 0.5480  | 10          |
| bfs       | cpp            | wasm       | samsung-tab-s3 | chrome-samsung8           | medium     | 0.7589  | 0.0145 | 0.7380  | 0.7830  | 10          |
| bfs       | js             | browserify | samsung-tab-s3 | chrome-samsung8           | medium     | 1.2591  | 0.1508 | 1.0764  | 1.5810  | 20          |
| bfs       | js             | browserify | samsung-tab-s3 | firefox-samsung8          | medium     | 0.9031  | 0.0563 | 0.8451  | 0.9941  | 10          |
| crc       | c              | wasm       | samsung-tab-s3 | firefox-samsung8          | medium     | 2.1552  | 0.4372 | 1.6730  | 2.8150  | 10          |
| crc       | c              | wasm       | samsung-tab-s3 | chrome-samsung8           | medium     | 3.3094  | 0.0368 | 3.2850  | 3.4120  | 10          |
| crc       | js             | browserify | samsung-tab-s3 | samsung-internet-samsung8 | medium     | 5.4615  | 0.1399 | 5.3200  | 5.6330  | 10          |
| crc       | js             | browserify | samsung-tab-s3 | firefox-samsung8          | medium     | 39.2570 | 2.4154 | 36.3840 | 42.5880 | 10          |
| crc       | js             | browserify | samsung-tab-s3 | chrome-samsung8           | medium     | 1.8914  | 0.0781 | 1.7680  | 2.0150  | 10          |
| fft       | c              | wasm       | samsung-tab-s3 | firefox-samsung8          | medium     | 3.6642  | 0.0221 | 3.6250  | 3.6960  | 10          |
| fft       | c              | wasm       | samsung-tab-s3 | chrome-samsung8           | medium     | 4.3185  | 0.2112 | 3.8490  | 4.6410  | 10          |
| fft       | js             | browserify | samsung-tab-s3 | firefox-samsung8          | medium     | 4.3703  | 0.2850 | 3.7588  | 4.7003  | 10          |
| fft       | js             | browserify | samsung-tab-s3 | chrome-samsung8           | medium     | 23.4107 | 2.1397 | 19.5394 | 25.3420 | 10          |
| fft       | js             | browserify | samsung-tab-s3 | samsung-internet-samsung8 | medium     | 11.5877 | 0.7951 | 10.4291 | 12.5791 | 10          |
| hmm       | c              | wasm       | samsung-tab-s3 | chrome-samsung8           | medium     | 22.6071 | 1.1150 | 20.6410 | 24.2380 | 10          |
| hmm       | c              | wasm       | samsung-tab-s3 | firefox-samsung8          | medium     | 20.9048 | 0.3549 | 20.5320 | 21.5160 | 10          |
| hmm       | js             | browserify | samsung-tab-s3 | samsung-internet-samsung8 | medium     | 30.2613 | 1.6025 | 28.0967 | 32.9484 | 10          |
| hmm       | js             | browserify | samsung-tab-s3 | chrome-samsung8           | medium     | 32.3524 | 3.6874 | 26.2267 | 38.0129 | 10          |
| hmm       | js             | browserify | samsung-tab-s3 | firefox-samsung8          | medium     | 46.9167 | 0.7581 | 46.0483 | 48.7999 | 10          |
| lavamd    | c              | wasm       | samsung-tab-s3 | chrome-samsung8           | medium     | 4.5755  | 0.3736 | 4.1320  | 4.8870  | 10          |
| lavamd    | c              | wasm       | samsung-tab-s3 | firefox-samsung8          | medium     | 3.5706  | 0.3136 | 3.1230  | 4.1590  | 10          |
| lavamd    | js             | browserify | samsung-tab-s3 | samsung-internet-samsung8 | medium     | 77.8506 | 9.8676 | 62.3044 | 92.1702 | 10          |
| lavamd    | js             | browserify | samsung-tab-s3 | firefox-samsung8          | medium     | 2.9701  | 0.2603 | 2.7052  | 3.3477  | 10          |
| lavamd    | js             | browserify | samsung-tab-s3 | chrome-samsung8           | medium     | 4.9502  | 0.1547 | 4.7424  | 5.1748  | 10          |
| lud       | c              | wasm       | samsung-tab-s3 | chrome-samsung8           | medium     | 10.8337 | 0.7457 | 9.7000  | 11.6570 | 10          |
| lud       | c              | wasm       | samsung-tab-s3 | firefox-samsung8          | medium     | 11.4719 | 1.1035 | 10.0510 | 14.0690 | 10          |
| lud       | js             | browserify | samsung-tab-s3 | chrome-samsung8           | medium     | 13.5368 | 0.8249 | 12.4800 | 14.6820 | 10          |
| lud       | js             | browserify | samsung-tab-s3 | samsung-internet-samsung8 | medium     | 7.5571  | 0.4532 | 7.0820  | 8.2960  | 10          |
| lud       | js             | browserify | samsung-tab-s3 | firefox-samsung8          | medium     | 19.7935 | 1.1246 | 18.1100 | 21.8370 | 10          |
| nqueens   | c              | wasm       | samsung-tab-s3 | firefox-samsung8          | medium     | 10.0006 | 0.1074 | 9.9020  | 10.2200 | 10          |
| nqueens   | c              | wasm       | samsung-tab-s3 | chrome-samsung8           | medium     | 10.1132 | 0.7690 | 9.4360  | 11.1060 | 10          |
| nqueens   | js             | browserify | samsung-tab-s3 | firefox-samsung8          | medium     | 17.9965 | 2.3416 | 15.5290 | 21.5040 | 10          |
| nqueens   | js             | browserify | samsung-tab-s3 | chrome-samsung8           | medium     | 15.8656 | 1.0839 | 14.1740 | 16.7770 | 10          |
| nqueens   | js             | browserify | samsung-tab-s3 | samsung-internet-samsung8 | medium     | 11.2575 | 0.8097 | 10.0840 | 12.9480 | 10          |
| nw        | c              | wasm       | samsung-tab-s3 | firefox-samsung8          | medium     | 0.4537  | 0.0063 | 0.4470  | 0.4660  | 10          |
| nw        | c              | wasm       | samsung-tab-s3 | chrome-samsung8           | medium     | 0.3738  | 0.0383 | 0.3210  | 0.4180  | 10          |
| nw        | js             | browserify | samsung-tab-s3 | chrome-samsung8           | medium     | 0.6806  | 0.0196 | 0.6470  | 0.7152  | 10          |
| nw        | js             | browserify | samsung-tab-s3 | firefox-samsung8          | medium     | 0.6057  | 0.0188 | 0.5795  | 0.6418  | 10          |
| nw        | js             | browserify | samsung-tab-s3 | samsung-internet-samsung8 | medium     | 0.7620  | 0.1362 | 0.5718  | 0.9137  | 10          |
| pagerank  | c              | wasm       | samsung-tab-s3 | chrome-samsung8           | medium     | 2.5898  | 0.1745 | 2.2450  | 2.7870  | 10          |
| pagerank  | c              | wasm       | samsung-tab-s3 | firefox-samsung8          | medium     | 2.8710  | 0.0842 | 2.7160  | 3.0390  | 10          |
| pagerank  | js             | browserify | samsung-tab-s3 | firefox-samsung8          | medium     | 2.1467  | 0.3690 | 1.8976  | 3.1267  | 10          |
| pagerank  | js             | browserify | samsung-tab-s3 | samsung-internet-samsung8 | medium     | 2.7284  | 0.3249 | 2.0429  | 3.0552  | 10          |
| pagerank  | js             | browserify | samsung-tab-s3 | chrome-samsung8           | medium     | 2.7661  | 0.1583 | 2.6215  | 3.1240  | 10          |
| spmv      | c              | wasm       | samsung-tab-s3 | firefox-samsung8          | medium     | 3.4940  | 0.0574 | 3.4560  | 3.6470  | 10          |
| spmv      | c              | wasm       | samsung-tab-s3 | chrome-samsung8           | medium     | 5.9554  | 0.4161 | 5.5180  | 6.8200  | 10          |
| spmv      | js             | browserify | samsung-tab-s3 | samsung-internet-samsung8 | medium     | 11.7258 | 0.7293 | 10.8606 | 13.4477 | 10          |
| spmv      | js             | browserify | samsung-tab-s3 | chrome-samsung8           | medium     | 14.7521 | 0.8192 | 13.1731 | 15.5317 | 10          |
| spmv      | js             | browserify | samsung-tab-s3 | firefox-samsung8          | medium     | 6.2681  | 0.2301 | 5.7161  | 6.5394  | 10          |
| srad      | c              | wasm       | samsung-tab-s3 | firefox-samsung8          | medium     | 15.0093 | 0.9413 | 13.7300 | 15.9000 | 10          |
| srad      | c              | wasm       | samsung-tab-s3 | chrome-samsung8           | medium     | 12.8557 | 0.0477 | 12.7890 | 12.9200 | 10          |
| srad      | js             | browserify | samsung-tab-s3 | chrome-samsung8           | medium     | 37.9503 | 1.4565 | 36.4998 | 40.6546 | 10          |
| srad      | js             | browserify | samsung-tab-s3 | firefox-samsung8          | medium     | 32.2638 | 2.0853 | 30.1671 | 35.4862 | 10          |
| srad      | js             | browserify | samsung-tab-s3 | samsung-internet-samsung8 | medium     | 30.0305 | 4.3233 | 24.4734 | 35.7192 | 10          |