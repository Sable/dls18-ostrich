### Invariants (configuration parameters that are the same for all runs) ###

| category | short-name |
| -------- | ---------- |
.csv

### Results ###

| benchmark | implementation | compiler   | platform       | environment               | input-size | mean(s) | std(s) | min(s)  | max(s)  | repetitions |
| --------- | -------------- | ---------- | -------------- | ------------------------- | ---------- | ------- | ------ | ------- | ------- | ----------- |
| backprop  | c              | wasm       | samsung8       | chrome-samsung8           | medium     | 1.4348  | 0.0070 | 1.4250  | 1.4590  | 30          |
| backprop  | c              | wasm       | samsung8       | firefox-samsung8          | medium     | 1.2947  | 0.0063 | 1.2830  | 1.3040  | 10          |
| backprop  | js             | browserify | samsung8       | samsung-internet-samsung8 | medium     | 2.0540  | 0.0063 | 2.0419  | 2.0637  | 11          |
| backprop  | js             | browserify | samsung8       | chrome-samsung8           | medium     | 1.9436  | 0.0306 | 1.9281  | 2.1028  | 30          |
| backprop  | js             | browserify | samsung8       | firefox-samsung8          | medium     | 2.8873  | 0.0463 | 2.8372  | 2.9524  | 10          |
| bfs       | cpp            | wasm       | samsung8       | chrome-samsung8           | medium     | 0.5465  | 0.0089 | 0.5360  | 0.5830  | 30          |
| bfs       | cpp            | wasm       | samsung8       | firefox-samsung8          | medium     | 0.4366  | 0.0047 | 0.4280  | 0.4430  | 10          |
| bfs       | js             | browserify | samsung8       | firefox-samsung8          | medium     | 0.6263  | 0.0139 | 0.6131  | 0.6662  | 40          |
| bfs       | js             | browserify | samsung8       | chrome-samsung8           | medium     | 0.8039  | 0.0107 | 0.7889  | 0.8268  | 30          |
| crc       | c              | wasm       | samsung8       | firefox-samsung8          | medium     | 2.5482  | 0.0097 | 2.5310  | 2.5680  | 10          |
| crc       | c              | wasm       | samsung8       | chrome-samsung8           | medium     | 3.1692  | 0.0103 | 3.1480  | 3.1960  | 30          |
| crc       | js             | browserify | samsung8       | chrome-samsung8           | medium     | 2.7225  | 0.0061 | 2.7130  | 2.7420  | 30          |
| crc       | js             | browserify | samsung8       | firefox-samsung8          | medium     | 24.8541 | 0.0653 | 24.7750 | 24.9720 | 10          |
| crc       | js             | browserify | samsung8       | samsung-internet-samsung8 | medium     | 5.0232  | 0.0088 | 5.0090  | 5.0340  | 10          |
| fft       | c              | wasm       | samsung8       | chrome-samsung8           | medium     | 2.7570  | 0.0093 | 2.7460  | 2.7910  | 30          |
| fft       | c              | wasm       | samsung8       | firefox-samsung8          | medium     | 2.3143  | 0.0031 | 2.3100  | 2.3190  | 10          |
| fft       | js             | browserify | samsung8       | firefox-samsung8          | medium     | 2.7769  | 0.0591 | 2.6741  | 2.8732  | 10          |
| fft       | js             | browserify | samsung8       | samsung-internet-samsung8 | medium     | 6.4997  | 0.0338 | 6.4468  | 6.5429  | 10          |
| fft       | js             | browserify | samsung8       | chrome-samsung8           | medium     | 13.7482 | 0.0422 | 13.6396 | 13.8353 | 30          |
| hmm       | c              | wasm       | samsung8       | chrome-samsung8           | medium     | 7.6045  | 0.1779 | 7.3600  | 8.0700  | 30          |
| hmm       | c              | wasm       | samsung8       | firefox-samsung8          | medium     | 6.0011  | 0.1376 | 5.7540  | 6.1570  | 10          |
| hmm       | js             | browserify | samsung8       | samsung-internet-samsung8 | medium     | 7.3050  | 0.3677 | 6.7360  | 7.9722  | 10          |
| hmm       | js             | browserify | samsung8       | chrome-samsung8           | medium     | 9.5475  | 0.3111 | 9.1715  | 10.8007 | 30          |
| hmm       | js             | browserify | samsung8       | firefox-samsung8          | medium     | 10.1018 | 0.2681 | 9.7137  | 10.4766 | 10          |
| lavamd    | c              | wasm       | samsung8       | chrome-samsung8           | medium     | 2.9505  | 0.0118 | 2.9150  | 2.9660  | 30          |
| lavamd    | c              | wasm       | samsung8       | firefox-samsung8          | medium     | 3.0070  | 0.0121 | 2.9740  | 3.0150  | 10          |
| lavamd    | js             | browserify | samsung8       | firefox-samsung8          | medium     | 2.4189  | 0.0040 | 2.4129  | 2.4269  | 10          |
| lavamd    | js             | browserify | samsung8       | chrome-samsung8           | medium     | 4.0265  | 0.0146 | 4.0005  | 4.0613  | 30          |
| lavamd    | js             | browserify | samsung8       | samsung-internet-samsung8 | medium     | 43.6090 | 0.1574 | 43.3235 | 43.8697 | 10          |
| lud       | c              | wasm       | samsung8       | chrome-samsung8           | medium     | 4.9871  | 0.2102 | 4.7280  | 5.5900  | 30          |
| lud       | c              | wasm       | samsung8       | firefox-samsung8          | medium     | 4.9979  | 0.1560 | 4.8130  | 5.3440  | 10          |
| lud       | js             | browserify | samsung8       | firefox-samsung8          | medium     | 18.6799 | 3.5601 | 15.5170 | 27.0200 | 10          |
| lud       | js             | browserify | samsung8       | chrome-samsung8           | medium     | 7.4243  | 0.1343 | 7.1590  | 7.6330  | 30          |
| lud       | js             | browserify | samsung8       | samsung-internet-samsung8 | medium     | 5.3010  | 0.5050 | 4.7920  | 6.1080  | 10          |
| nqueens   | c              | wasm       | samsung8       | firefox-samsung8          | medium     | 7.4224  | 0.0522 | 7.3650  | 7.5360  | 10          |
| nqueens   | c              | wasm       | samsung8       | chrome-samsung8           | medium     | 9.2268  | 0.0157 | 9.1910  | 9.2560  | 30          |
| nqueens   | js             | browserify | samsung8       | firefox-samsung8          | medium     | 12.3182 | 0.1657 | 12.1090 | 12.7100 | 10          |
| nqueens   | js             | browserify | samsung8       | chrome-samsung8           | medium     | 13.1981 | 0.0181 | 13.1760 | 13.2530 | 30          |
| nqueens   | js             | browserify | samsung8       | samsung-internet-samsung8 | medium     | 10.3237 | 0.0202 | 10.3070 | 10.3780 | 10          |
| nw        | c              | wasm       | samsung8       | firefox-samsung8          | medium     | 0.3218  | 0.0018 | 0.3200  | 0.3250  | 10          |
| nw        | c              | wasm       | samsung8       | chrome-samsung8           | medium     | 0.3490  | 0.0013 | 0.3470  | 0.3520  | 30          |
| nw        | js             | browserify | samsung8       | chrome-samsung8           | medium     | 0.6018  | 0.0033 | 0.5958  | 0.6087  | 30          |
| nw        | js             | browserify | samsung8       | samsung-internet-samsung8 | medium     | 0.5299  | 0.0075 | 0.5233  | 0.5460  | 10          |
| nw        | js             | browserify | samsung8       | firefox-samsung8          | medium     | 0.4423  | 0.0044 | 0.4358  | 0.4491  | 10          |
| pagerank  | c              | wasm       | samsung8       | firefox-samsung8          | medium     | 1.0502  | 0.0179 | 1.0090  | 1.0730  | 10          |
| pagerank  | c              | wasm       | samsung8       | chrome-samsung8           | medium     | 0.9968  | 0.0258 | 0.9560  | 1.0590  | 30          |
| pagerank  | js             | browserify | samsung8       | samsung-internet-samsung8 | medium     | 1.1715  | 0.0320 | 1.1357  | 1.2220  | 10          |
| pagerank  | js             | browserify | samsung8       | chrome-samsung8           | medium     | 1.8572  | 0.0273 | 1.7683  | 1.8863  | 30          |
| pagerank  | js             | browserify | samsung8       | firefox-samsung8          | medium     | 1.6393  | 0.0406 | 1.5324  | 1.6650  | 10          |
| spmv      | c              | wasm       | samsung8       | chrome-samsung8           | medium     | 2.9381  | 0.1149 | 2.8600  | 3.2050  | 10          |
| spmv      | c              | wasm       | samsung8       | firefox-samsung8          | medium     | 2.6839  | 0.0088 | 2.6750  | 2.7020  | 10          |
| spmv      | js             | browserify | samsung8       | chrome-samsung8           | medium     | 4.9122  | 0.1277 | 4.8622  | 5.2718  | 10          |
| spmv      | js             | browserify | samsung8       | firefox-samsung8          | medium     | 5.4151  | 0.5939 | 5.2030  | 7.1036  | 10          |
| spmv      | js             | browserify | samsung8       | samsung-internet-samsung8 | medium     | 4.5450  | 0.0299 | 4.5313  | 4.6292  | 10          |
| srad      | c              | wasm       | samsung8       | firefox-samsung8          | medium     | 9.2433  | 0.0117 | 9.2300  | 9.2710  | 10          |
| srad      | c              | wasm       | samsung8       | chrome-samsung8           | medium     | 9.7111  | 0.0276 | 9.6220  | 9.7570  | 30          |
| srad      | js             | browserify | samsung8       | firefox-samsung8          | medium     | 15.8590 | 0.1240 | 15.6424 | 16.0617 | 10          |
| srad      | js             | browserify | samsung8       | samsung-internet-samsung8 | medium     | 17.3862 | 0.0768 | 17.1887 | 17.4514 | 10          |
| srad      | js             | browserify | samsung8       | chrome-samsung8           | medium     | 17.7645 | 0.0890 | 17.3700 | 17.8706 | 30          |