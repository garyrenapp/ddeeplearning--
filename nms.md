
https://zhuanlan.zhihu.com/p/50126479
## 标准nms
* 按score做降序排列 list_k
* 从头list_k的top 1开始，计算与其他box的IOU，若大于阈值则删除

## 局部感知nms - LNMS
为了形成最终结果，阈值化后的几何图形应该由NMS合并。一个简单的NMS算法在O（n2）中运行，其中n是候选几何体的数量，这是不可接受的，因为我们正面临来自密集预测的成千上万个几何体。

在假定来自附近像素的几何图形倾向于高度相关的情况下，我们提出将行几何图形逐行合并，并且在合并同一行中的几何图形时，我们将迭代地合并当前遇到的几何图形。这种改进的技术在O（n）中以最佳方案运行。即使最坏的情况与最初的情况一样，只要局部性假设成立，算法在实践中运行得足够快。