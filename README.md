# Ostrich Updated

|name   |cpu    |memory |OS     | GCC | Emscripten| Report | Data|
|----   |---    |-------|-------|-----|-----------|-----------|-----------|
| __DESKTOPS & LAPTOPS__   |    |||||||
|mbp-2013    |  Intel(R) Core(TM) i5 @ 2.4 GHz   |  8 GB 1600 MHz DDR3      |   macOS High Sierra 10.13.1 |llvm-gcc 4.2.1   |1.37.22 |[report](./data/mbp2013/report-mbp2013.md) |[mbp2013.csv](./data/mbp2013/browser/platform=mbp2013,input-size=medium.csv) |
|ubuntu-deer    |Intel(R) Core(TM) i7-3820 CPU @ 3.60GHz     |  16 GB     |   Ubuntu 16.04 xenial |5.4.0 |1.37.22  |[report](./data/ubuntu-deer/report-ubuntu-deer.md) | [ubuntu-deer.csv](./data/ubuntu-deer/browser/platform=ubuntu-deer,input-size=medium.csv)|
|windows-bison    |  Intel(R) Core(TM) i7-3820 CPU @ 3.60GHz   | 16 GB |   Windows 10 Enterprise | llvm-gcc 4.2.1   |1.37.22 |[report](./data/windows-bison/report-windows-bison.md) | [windows-bison.csv](./data/windows-bison/browser/platform=windows-bison,input-size=medium.csv)|
| __TABLETS__   |    |||||||
| ipad-pro | 2.36 GHz hexa-core Apple Fusion (3× Hurricane + 3× Zephyr) | 4GB  | OS 11.0.3 (15A432) | - | - |[report](./data/ipad-pro/report-ipad-pro.md) | [ipad-pro.csv](./data/ipad-pro/browser/platform=ipad-pro,input-size=medium.csv) |
| samsung-tab-s3|2.15GHz - 1.6Ghz Quad Core Processor | 4GB  | android 8.0.0 | - | - |[report](./data/samsung-tab-s3/report-samsung-tab-s3.md) | [samsung-tab-s3.csv](./data/samsung-tab-s3/browser/platform=samsung-tab-s3,input-size=medium.csv) |
| __SMART PHONES__   |    |||||||
| sumsung8 | Octa-core (2.3GHz Quad + 1.7GHz Quad), 64 bit, 10nm processor | 4GB | android 8.0.0 | - | - | [report](./data/samsung8/report-samsung8.md) | [sumsung8.csv](./data/samsung8/browser/platform=samsung8,input-size=medium.csv) |
| pixel2  | Qualcomm MSM8998 Snapdragon 835, Octa-core (4x2.35 GHz Kryo & 4x1.9 GHz Kryo) | 4 GB | android 8.0.0 | - | - |[report](./data/pixel2/report-pixel2.md) | [pixel2.csv](./data/pixel2/browser/platform=pixel2,input-size=medium.csv) |
| iPhone 8 | - | - | - | - | - | - | - | 
| raspberry-pi-3 | 1.2 GHZ quad-core ARM Cortex A53 (ARMv8 Instruction Set) | 1 GB | Linux Raspberry Pi 4.9.35-v7 | - | - | [report](./data/raspberry-pi-3/report-raspberry-pi-3.md) | [raspberry-pi-3.csv](./data/raspberry-pi-3/server/platform=raspberry3,environment=node-remote-raspberry,input-size=medium.csv)|

# NOTE: 
- Change of input for NW benchmark to 4096, for 8192 the memory 1.073741824GB does not work on mobile. The limit is 1GB for Chrome web assembly

- Backpropation benchmark problems running in every mobile phone. Changed size from 2850000(output 3093857) to 1425000(output 783682)

- Found bug in Samsung-browser version for all the three devices tested, Javascript BFS version.

Must run these benchmarks again in the remaining of the devices.
# Node JS Experiment
No difference performance between NodeJS
 - Get graphs on Github for those results
 - Create graph for Old vs. new
 - Create Geo-mean graph
 - Finish NodeJS
 - Explore NodeJS differences
 - Google Docs comments
 - Think about WebAssembly
 - Think about website


