https://blog.csdn.net/JackyTintin/article/details/79425866

https://xiaodu.io/ctc-explained/
https://zhuanlan.zhihu.com/p/42719047

ctc 标签对齐 输入序列 X ， 标签数据是Y
* X->Y 单调递增
* X->Y 多对1 映射
* X->Y X长度大于 Y
这样出来了很多路径组合，联合概率最大用最大似然估计，多路径我们用动态规划来做，加剪枝来减少计算量。

