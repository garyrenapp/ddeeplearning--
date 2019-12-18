

## logistic regression 简称LR
$ z = w^T x + b $
$ \hat{y} = a = \sigma(z) $
**交叉熵损失函数**
$ costJ = -\frac{1}{m}\sum_{i=1}^{m}y^{(i)}\log(a^{(i)})+(1-y^{(i)})\log(1-a^{(i)}) $

### 这个损失函数是怎么来的？
deeplearning.ai 2.18 有讲看,过程如下
$\hat{y} = \sigma(w^T x + b) \quad when \quad \sigma(z) = \frac{1}{1+e^{-z}}$
$Interput \quad \hat{y} = p(y=1|x) $
$if \quad y=1: \quad p(y|x) = \hat{y} $
$if \quad y=0: \quad p(y|x) = 1-\hat{y} $
$so \quad p(y|x) = \hat{y}^y(1-\hat{y})^{1-y} $
$if \quad y=0 \quad p(y|x) = \hat{y}^0(1-\hat{y})^{1-0} = 1 -\hat{y}$
$if \quad y=1 \quad p(y|x) = \hat{y}^1(1-\hat{y})^{1-1} =\hat{y}$

$因为log是单调递增函数,最大化p(y|x)等价于 \log(p(y|x))$
$\log(p(y|x))
  =\log(\hat{y}^y(1-\hat{y})^{1-y}) 
  = y\log(\hat{y}) + (1-y)\log(1-\hat{y})
$
- 这一步突然加个log其实有些牵强了，后来我弄明白了，他是把他当作极大似然求解的，所以这里从极大似然估计来推比较合适。

上面说到
$ \quad p(y|x) = \hat{y}^y(1-\hat{y})^{1-y} $
转换成似然函数 为了打公式方便设$ \hat{y} = a$
$ L(w)=∏^n_{i=1}p(y^{i}|x^{i})=∏^n_{i=1}{a^{(i)}}^{y^{(i)}}(1-a^{(i)})^{1-y^{(i)}}
$
两边取对数
$ costJ = -\frac{1}{m}\sum_{i=1}^{m}y^{(i)}\log(a^{(i)})+(1-y^{(i)})\log(1-a^{(i)}) $

### 梯度下降求导
![](imgs/lr-1.jpg)
$ da = \frac{\partial J}{\partial a}= -\frac{y}{a} + \frac{1-y}{1-a}$
$ dz = \frac{\partial J}{\partial a} \frac{\partial a}{\partial z}
     =(-\frac{y}{a} + \frac{1-y}{1-a}) (a(1-a)) = a -y $
$ dw =  \frac{\partial J}{\partial a} \frac{\partial a}{\partial z} \frac{\partial z}{\partial w} = (a-y)x $
$ db =  \frac{\partial J}{\partial a} \frac{\partial a}{\partial z} \frac{\partial z}{\partial b}= (a-y) $

### 为什么不用平方损失？
平方损失函数就是最小二乘法求解，是非凸的
所以用极大似然求解
https://www.zhihu.com/question/65350200

### 逻辑回归的回归从何说起，为什么回归可以用来分类
https://zhuanlan.zhihu.com/p/39363869

### 逻辑回归与极大似然估计
上面已经解释

### 逻辑回归解决的是分类问题。为什么选择sigmoid函数呢
有人说是为了将线性回归的值压缩到0-1之间，但是符合这个条件的函数有很多，为什么偏偏选择了sigmoid函数。
https://zhuanlan.zhihu.com/p/35036985