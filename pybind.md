


## mac 编译
```
conda acitvate env 激活python3环境，如果不激活python3环境会出现，找不到python.h文件。

c++ -O3 -Wall -shared -std=c++11 -undefined dynamic_lookup `python3 -m pybind11 --includes` example.cpp -o example`python3-config --extension-suffix`
```