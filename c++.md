
# c++11
## 命名规范
* 标识符要能体现实际含义
* 变量名一般用小写字母,如index,不要使用Index或INDEX
* 用户自定义类名一般以大写字母开头,如Sales_item
* 如果标识符由多个单词组成,则单词间应有明显区分,如student_loan或者studentLoan,不要使用studentloan

## 类型别名
* 使用关键字 typedef
```cpp
typedef double wages ; //wages 是 double 的同义词
typedef wages base, *p; //base 是 double 的同义词 ，p 是double* 的同义词
```
* 使用别名声明
```cpp
using SI = Sales_item;   //SI 是 Sales_item 的同义词
wages hourly,weekly;     //等价于 double hourly,weekly
SI item;                 //等价于 Sales_item item
```

## 范围for
```cpp
int arr[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
for (int i = 0; i < 10; i++)
	cout << arr[i];


int arr[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
for (auto n : arr)
    std::cout << n;


std::vector<int> vec {1,2,3,4,5,6,7,8,9,10};
for (std::vector<int>::iterator itr = vec.begin(); itr != vec.end(); itr++)
    std::cout << *itr;

std::vector<int> vec {1,2,3,4,5,6,7,8,9,10};
for (auto n :vec)
    std::cout << n;

```
* 如果要修改元素需要声明为引用
```cpp
int arr[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
for(auto &r : arr)
    r *=2;
```

# pybind11
## mac 编译
```
conda acitvate env 激活python3环境，如果不激活python3环境会出现，找不到python.h文件。

c++ -O3 -Wall -shared -std=c++11 -undefined dynamic_lookup `python3 -m pybind11 --includes` pse.cpp -o pse`python3-config --extension-suffix`
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
using py = pybind11 ;
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