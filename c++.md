
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
## 内联函数
* 内联函数可以避免函数调用的开销
* 为什么不把所有的函数定义为内联函数？
内联函数以代码膨胀（拷贝）为代价，仅仅省去函数调用的开销，从而提高程序的执行效率。
注意：这里所说的函数调用开销并不包括执行函数体所需要的开销，而是仅指参数压栈、跳转、退栈和返回的操作。如果执行函数体内的代码的时间比函数调用的开销大很多，那么inline的效率收益会很小。
另一方面，每一处内联函数的调用都要拷贝代码，使总代码量增大，消耗更多的空间。
* 内联只是向编译器发出的一个请求，编译器可以选择忽略这个请求
一个好的编译器能够根据函数的定义体，自动取消不值得的内联，或者自动的内联一些没有inline请求的函数。

## 调试 
* NODEBUG assert
* 有帮助的调试信息
```cpp
if(word.size() < threshold){
    ceer << "Error:" << __FILE__   //文件名
         << ":in function" << __func__ //函数名
         << " at line " << __LINE__ << endl    //行号
         << "     Compiled on " << __DATE__   //编译日期
         << " at " << __TIME__ << endl;       //编译时间
}
```

## 函数指针
```cpp
bool lengthCompare(const string & , const string &);
bool (*pf)(const string & , const string &);
pf = lengthCompare
```
* 函数指针作为形参
```cpp
void useBigger(const string &s1 , const string &s2,
               bool pf(const string & , const string &));
//等价
void useBigger(const string &s1, const string & s2,
               bool(*pf)(const string & , const string &));

userBigger(s1,s2,lengthCompare);
```
直接使用函数指针类型变得冗长而繁琐，typedef和decltype能简化代码
```cpp
// Func 和 Func2 是函数类型
typdef bool Func(const string & , const string &);
typdef decltype(lengthCompare) Func2;  //等价Func
// 函数类型转自动换成函数指针
void useBigger(const string & ,const string & ,Func)

//FuncP 和 funcP2 是函数指针
typdef bool (*FuncP)(const string & , const string &);
typdef decltype(lengthCompare) * FuncP2;
void useBigger(const string & , const string & ,FuncP);
```
* 返回 函数的指针
必须要注意的是，和函数类型的形参不一样，返回类型不会自动的转换成指针。我们必须显式的返回类型指定为指针。
```cpp
using F = int(int * ,int); // F是函数类型不是指针
using PF = int(*)(int * , int ); // PF 是指针
//声明 返回函数指针的 函数
PF f1(int);  //正确，PF是只想函数的指针，f1 返回 函数指针
F f1(int);   //错误，F 是 函数类型
F *f1(int);  //正确，显式的指定返回类型是 指向函数的指针
//当然我们也可以使用下面的形式直接声明f1
int (*f1(int))(int * ,int);

//c++11的新语法尾置返回
auto f1(int) -> int (*)(int * , int);
```
* 将auto 和 decltype 用于函数指针类型
```cpp
string::size_type sumLength(const string & , const string &);'
//声明getFcn需要注意的是，decltype返回的是函数类型而非指针，因此我们显式的加上*以表明
//返回的式指针。
decltype(sumLength) * getFcn(const string &);
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