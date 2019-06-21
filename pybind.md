


## mac 编译
```
conda acitvate env 激活python3环境，如果不激活python3环境会出现，找不到python.h文件。

c++ -O3 -Wall -shared -std=c++11 -undefined dynamic_lookup `python3 -m pybind11 --includes` nonzero.cpp -o nonzero`python3-config --extension-suffix`
```

## linux 编译
```
conda install -c conda-forge pybind11 

$ c++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` example.cpp -o example`python3-config --extension-suffix`
```

## 例子
```cpp
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <vector>
namespace py = pybind11 ;
std::vector< std::vector<int> >find_label_coord(
    py::array_t<int32_t, py::array::c_style> label_map,
    int num_labels){

        auto pbuf_label_map = label_map.request();
        int h = pbuf_label_map.shape[0];
        int w = pbuf_label_map.shape[1];
        auto ptr_label_map = static_cast<int32_t *>(pbuf_label_map.ptr);

        std::vector<std::vector<int32_t>> pts;
        for(size_t i = 0; i < num_labels ; ++i){
            std::vector<int> pt ;
            pts.push_back(pt);
        }

        for(size_t i = 0;i < h; ++i){
            auto p_label_map = ptr_label_map + i * w ;
            for(size_t j = 0;j < w; ++j){
                int label = p_label_map[j];
                if(label > 0){
                    pts[label-1].push_back(j);
                    pts[label-1].push_back(i);
                }
            }
        }
        return pts;

    }


PYBIND11_MODULE(nonzero,m){
    m.doc() = "reimplement pse use cpp";

    m.def("find_label_coord",&find_label_coord,"a function which find lable coord",py::arg("label_map"),py::arg("num_labels"));
    
}
```