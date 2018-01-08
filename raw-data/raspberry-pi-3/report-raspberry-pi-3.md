## Device

|name   |cpu    |memory |OS     | GCC | Emscripten|
|----   |---    |-------|-------|-----|-----------|
|raspberry-pi-3  |1.2 GHz 64/32-bit quad-core ARM Cortex-A53   |  1 GB| Linux Raspbian 4.9.35-v7|4.9.2 - 10|1.37.22  |
# Environments
|environment    |version | JS Engine Version|
|---            |------- |------- |
|Node |9.3.0|6.2.414.4-node.15|
|Chromium63|56.0.2923.84|v8 5.6.326.45|
|Native |-|-|


# Node
### Invariants (configuration parameters that are the same for all runs) ###

| category    | short-name            |
| ----------- | --------------------- |
| platform    | raspberry3            |
| environment | node-remote-raspberry |
| input-size  | medium                |
platform=raspberry3,environment=node-remote-raspberry,input-size=medium.csv

### Results ###

| benchmark | implementation | compiler    | mean(s)  | std(s) | min(s)   | max(s)   | repetitions |
| --------- | -------------- | ----------- | -------- | ------ | -------- | -------- | ----------- |
| backprop  | c              | server-wasm | 5.3385   | 0.0251 | 5.2980   | 5.3930   | 30          |
| backprop  | js             | browserify  | 9.8795   | 0.1049 | 9.7590   | 10.2410  | 30          |
| bfs       | cpp            | server-wasm | 2.0264   | 0.0114 | 2.0120   | 2.0680   | 30          |
| bfs       | js             | browserify  | 7.9912   | 0.0864 | 7.8910   | 8.1120   | 30          |
| crc       | c              | server-wasm | 7.8771   | 0.0549 | 7.8190   | 7.9940   | 30          |
| crc       | js             | browserify  | 7.9768   | 0.0601 | 7.9160   | 8.0860   | 30          |
| fft       | c              | server-wasm | 10.7872  | 0.0907 | 10.6470  | 11.0100  | 30          |
| fft       | js             | browserify  | 20.2561  | 0.2716 | 19.9140  | 20.8950  | 30          |
| hmm       | c              | server-wasm | 92.9389  | 0.5207 | 91.7080  | 93.8870  | 30          |
| hmm       | js             | browserify  | 112.1745 | 0.3220 | 111.2780 | 112.8690 | 30          |
| lavamd    | c              | server-wasm | 11.9125  | 0.0277 | 11.8660  | 11.9580  | 30          |
| lavamd    | js             | browserify  | 21.4689  | 0.0493 | 21.3720  | 21.5960  | 30          |
| lud       | c              | server-wasm | 53.8421  | 0.4388 | 53.1460  | 54.8600  | 30          |
| lud       | js             | browserify  | 66.7039  | 0.6501 | 65.0290  | 67.5760  | 30          |
| nqueens   | c              | server-wasm | 22.3044  | 0.0443 | 22.2330  | 22.3710  | 30          |
| nqueens   | js             | browserify  | 46.6913  | 0.0829 | 46.6140  | 46.8170  | 30          |
| nw        | c              | server-wasm | 0.9754   | 0.0042 | 0.9700   | 0.9830   | 30          |
| nw        | js             | browserify  | 2.8672   | 0.0222 | 2.8420   | 2.9440   | 30          |
| pagerank  | c              | server-wasm | 5.9288   | 0.0264 | 5.8940   | 5.9670   | 30          |
| pagerank  | js             | browserify  | 9.3480   | 0.0362 | 9.2880   | 9.3900   | 30          |
| spmv      | c              | server-wasm | 21.0818  | 0.0754 | 20.9480  | 21.2350  | 30          |
| spmv      | js             | browserify  | 33.9186  | 0.1220 | 33.7230  | 34.2690  | 30          |
| srad      | c              | server-wasm | 34.7474  | 0.2129 | 34.4410  | 35.1720  | 30          |
| srad      | js             | browserify  | 79.6787  | 0.4355 | 79.0210  | 80.9720  | 30          |

# Native 
| Name | Version |
|------| -----|
|gcc   | 6.4.0|

### Invariants (configuration parameters that are the same for all runs) ###

| category    | short-name              |
| ----------- | ----------------------- |
| platform    | raspberry               |
| environment | remote-raspberry-native |
| input-size  | medium                  |
platform=raspberry,environment=remote-raspberry-native,input-size=medium.csv

### Results ###

| benchmark | implementation | compiler   | mean(s) | std(s) | min(s)  | max(s)  | repetitions |
| --------- | -------------- | ---------- | ------- | ------ | ------- | ------- | ----------- |
| backprop  | c              | gcc-remote | 4.7061  | 0.0135 | 4.6871  | 4.7246  | 10          |
| bfs       | cpp            | g++-remote | 1.7305  | 0.0052 | 1.7244  | 1.7389  | 10          |
| crc       | c              | gcc-remote | 3.0807  | 0.0132 | 3.0680  | 3.1006  | 10          |
| fft       | c              | gcc-remote | 9.9350  | 0.0291 | 9.9049  | 9.9816  | 10          |
| hmm       | c              | gcc-remote | 80.2364 | 0.5340 | 79.4785 | 81.3550 | 10          |
| lavamd    | c              | gcc-remote | 14.4871 | 0.0322 | 14.4470 | 14.5363 | 10          |
| lud       | c              | gcc-remote | 50.4256 | 2.8528 | 46.8266 | 53.1220 | 10          |
| nw        | c              | gcc-remote | 0.3584  | 0.0010 | 0.3568  | 0.3598  | 10          |
| pagerank  | c              | gcc-remote | 4.3809  | 0.0163 | 4.3456  | 4.3940  | 10          |
| spmv      | c              | gcc-remote | 14.0484 | 0.0440 | 13.9895 | 14.1173 | 10          |
| srad      | c              | gcc-remote | 25.2152 | 0.8966 | 24.2902 | 26.5888 | 10          |