### Invariants (configuration parameters that are the same for all runs) ###

| category   | short-name |
| ---------- | ---------- |
| platform   | pixel2     |
| input-size | medium     |
platform=pixel2,input-size=medium.csv

### Results ###

| benchmark | implementation | compiler   | environment    | mean(s) | std(s) | min(s)  | max(s)  | repetitions |
| --------- | -------------- | ---------- | -------------- | ------- | ------ | ------- | ------- | ----------- |
| backprop  | c              | wasm       | chrome-pixel2  | 1.3944  | 0.0100 | 1.3760  | 1.4140  | 30          |
| backprop  | c              | wasm       | firefox-pixel2 | 1.2553  | 0.0061 | 1.2410  | 1.2690  | 30          |
| backprop  | c              | wasm       | chrome-pixel2  | 2.7952  | 0.0080 | 2.7830  | 2.8150  | 30          |
| backprop  | js             | browserify | chrome-pixel2  | 3.7744  | 0.0217 | 3.7444  | 3.8106  | 30          |
| backprop  | js             | browserify | chrome-pixel2  | 1.9170  | 0.0251 | 1.8671  | 1.9805  | 30          |
| backprop  | js             | browserify | firefox-pixel2 | 2.7629  | 0.0661 | 2.7367  | 3.1086  | 30          |
| bfs       | cpp            | wasm       | firefox-pixel2 | 0.4359  | 0.0153 | 0.4180  | 0.4970  | 30          |
| bfs       | cpp            | wasm       | chrome-pixel2  | 0.5408  | 0.0188 | 0.5230  | 0.6240  | 30          |
| bfs       | js             | browserify | chrome-pixel2  | 0.7967  | 0.0086 | 0.7858  | 0.8174  | 30          |
| bfs       | js             | browserify | firefox-pixel2 | 0.6070  | 0.0111 | 0.5907  | 0.6466  | 30          |
| crc       | c              | wasm       | firefox-pixel2 | 2.4623  | 0.0062 | 2.4500  | 2.4840  | 30          |
| crc       | c              | wasm       | chrome-pixel2  | 3.0440  | 0.0079 | 3.0330  | 3.0680  | 30          |
| crc       | js             | browserify | chrome-pixel2  | 2.6508  | 0.0099 | 2.6270  | 2.6710  | 30          |
| crc       | js             | browserify | firefox-pixel2 | 24.0266 | 0.0536 | 23.9020 | 24.1020 | 30          |
| fft       | c              | wasm       | firefox-pixel2 | 2.2403  | 0.0112 | 2.2260  | 2.2890  | 30          |
| fft       | c              | wasm       | chrome-pixel2  | 2.6537  | 0.0064 | 2.6420  | 2.6680  | 30          |
| fft       | js             | browserify | firefox-pixel2 | 2.7188  | 0.0479 | 2.6146  | 2.8236  | 30          |
| fft       | js             | browserify | chrome-pixel2  | 13.1609 | 0.0436 | 13.0564 | 13.2481 | 30          |
| hmm       | c              | wasm       | chrome-pixel2  | 7.2646  | 0.1549 | 7.0100  | 7.6540  | 30          |
| hmm       | c              | wasm       | firefox-pixel2 | 5.6791  | 0.1740 | 5.4100  | 6.3100  | 30          |
| hmm       | js             | browserify | firefox-pixel2 | 9.8796  | 0.4718 | 9.0365  | 11.1186 | 30          |
| hmm       | js             | browserify | chrome-pixel2  | 9.2207  | 0.2069 | 8.8388  | 9.6724  | 30          |
| lavamd    | c              | wasm       | chrome-pixel2  | 2.8141  | 0.0088 | 2.7960  | 2.8310  | 30          |
| lavamd    | c              | wasm       | firefox-pixel2 | 2.8892  | 0.0098 | 2.8520  | 2.9070  | 30          |
| lavamd    | js             | browserify | firefox-pixel2 | 2.3428  | 0.0105 | 2.3292  | 2.3848  | 30          |
| lavamd    | js             | browserify | chrome-pixel2  | 3.8886  | 0.0079 | 3.8770  | 3.9089  | 30          |
| lud       | c              | wasm       | firefox-pixel2 | 4.7380  | 0.1231 | 4.4890  | 4.9740  | 30          |
| lud       | c              | wasm       | chrome-pixel2  | 4.7282  | 0.1348 | 4.4990  | 4.9550  | 30          |
| lud       | js             | browserify | chrome-pixel2  | 7.0907  | 0.1644 | 6.7520  | 7.5110  | 30          |
| lud       | js             | browserify | firefox-pixel2 | 17.5340 | 1.7671 | 14.6820 | 22.9520 | 30          |
| nqueens   | c              | wasm       | firefox-pixel2 | 7.1434  | 0.0370 | 7.0750  | 7.2120  | 30          |
| nqueens   | c              | wasm       | chrome-pixel2  | 8.8573  | 0.0179 | 8.8220  | 8.9000  | 30          |
| nqueens   | js             | browserify | firefox-pixel2 | 12.2080 | 0.2294 | 11.7610 | 12.5320 | 30          |
| nqueens   | js             | browserify | chrome-pixel2  | 12.7826 | 0.0313 | 12.6830 | 12.8280 | 30          |
| nw        | c              | wasm       | chrome-pixel2  | 0.3380  | 0.0023 | 0.3330  | 0.3420  | 30          |
| nw        | c              | wasm       | firefox-pixel2 | 0.3160  | 0.0025 | 0.3120  | 0.3210  | 30          |
| nw        | js             | browserify | chrome-pixel2  | 0.5799  | 0.0030 | 0.5754  | 0.5871  | 30          |
| nw        | js             | browserify | firefox-pixel2 | 0.4253  | 0.0043 | 0.4167  | 0.4320  | 30          |
| nw        | js             | browserify | chrome-pixel2  | 2.2506  | 0.0110 | 2.2236  | 2.2788  | 60          |
| pagerank  | c              | wasm       | chrome-pixel2  | 0.9791  | 0.0365 | 0.8880  | 1.0470  | 30          |
| pagerank  | c              | wasm       | firefox-pixel2 | 1.0493  | 0.0181 | 1.0060  | 1.0750  | 30          |
| pagerank  | js             | browserify | firefox-pixel2 | 1.6089  | 0.0720 | 1.3161  | 1.7061  | 30          |
| pagerank  | js             | browserify | chrome-pixel2  | 1.7943  | 0.0135 | 1.7408  | 1.8119  | 30          |
| spmv      | c              | wasm       | chrome-pixel2  | 2.7994  | 0.0098 | 2.7830  | 2.8320  | 30          |
| spmv      | c              | wasm       | firefox-pixel2 | 2.6166  | 0.0083 | 2.6010  | 2.6340  | 30          |
| spmv      | js             | browserify | firefox-pixel2 | 5.3136  | 0.1069 | 5.1110  | 5.5567  | 30          |
| spmv      | js             | browserify | chrome-pixel2  | 4.7509  | 0.0142 | 4.7237  | 4.7935  | 30          |
| srad      | c              | wasm       | chrome-pixel2  | 9.4108  | 0.0847 | 9.0620  | 9.4950  | 30          |
| srad      | c              | wasm       | firefox-pixel2 | 8.9935  | 0.0253 | 8.9580  | 9.0780  | 30          |
| srad      | js             | browserify | firefox-pixel2 | 15.3353 | 0.1247 | 14.8637 | 15.4664 | 30          |
| srad      | js             | browserify | chrome-pixel2  | 17.7402 | 0.1151 | 17.5265 | 17.9108 | 30          |