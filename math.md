# 数学

## 概率论数理统计

### 正态分布
正态分布也称高斯分布
$$
f(x)=\frac{1}{\sqrt{2\pi}\sigma} \exp-\frac{(x-\mu)^2}{2\sigma^2}
$$
![](imgs/正态分布.png)

**性质**
1. 曲线关于$x=\mu$对称
2. 当$x=\mu$时取到最大值即$f(x)=\frac{1}{\sqrt{2\pi}\sigma}$

**标准正态分布**
如果一个随机变量X服从这个分布，我们写作$  N(\mu,\sigma^2)$ 如果$\mu =0且\sigma =1$，这个分布被称为标准正态分布，这个分布能够简化为
$$
f(x)=\frac{1}{\sqrt{2\pi}} \exp \left(-\frac{x^2}{2} \right)
$$

### 极大似然估计（Maximum Likelihood Estimate，MLE）
参考浙江大学概率论与数理统计第四版 152页，整理笔记
![](imgs/mle-1.png)
极大似然估计中采样需满足一个重要的假设，就是所有的采样都是独立同分布的。
**似然函数**$L(\theta) = L(x_{1},x_{2},....,x_{n};\theta) = \prod_{i=1}^{n}f(x_{i}；\theta) $ 其中$\prod$是连乘的意思
**最大似然估计值**即最大化似然函数 $ L(x_{1},x_{2},....,x_{n};\hat{\theta}) = \max_{\theta\epsilon\Theta}L(x_{1},x_{2},....,x_{n};\theta) 则\hat{\theta}是最大似然估计值 $

求极大似然函数估计值的一般步骤：
1. 写出似然函数；
2. 对似然函数取对数(乘法变加法) ，并整理；
3. 求导数，
4. 解似然方程 。

### 条件概率
$P(B|A)$ 在事件A发生的条件下，B发生的概率。
* 条件概率公式：将一枚硬币抛掷两次，观察其出现正反面的情况。设事件A为至少有一次为H.事件B为两次抛掷为同一面。
设样本空间S = {HH,HT,TH,TT},A = {HH,HT,TH},B={HH,TT}. 求 P(B|A)
解：已知A已经发生,则 TT 不可能发生。 只有HH属于B则P(B|A) = 1/3。
P(A) = 3/4 ; P(AB)=1/4 ; $$P(B|A) = \frac{P(AB)}{P(A)}$$

* 乘法定理
$$P(AB) = P(B|A)P(A) $$
### 全概率
* 设试验E的样本空间为S,A为E的事件，B1,B2,....,Bn为S的一个划分，且$P(B_{i}) > 0 $ 则 $$P(A) = P(A|B_{1})P(B_{1}) +...... +P(A|B_{n})P(B_{n}) = \sum_{j=1}^{n}P(A|B_{j})P(B_{j})$$

### 贝叶斯 Bayes
$$P(B_{i}|A) = \frac{P(B_{i}A)}{P(A)} = \frac{P(A|B_{i})P(B_{i})}{\sum_{j=1}^{n}P(A|B_{j})P(B_{j})}$$
![](imgs/bayes_1.png)

## 微积分
### 拉格朗日乘子法
https://www.youtube.com/watch?v=aep6lwPqm6I&list=PLSQl0a2vh4HC5feHa6Rc5c0wbRTx56nF7&index=94
http://littleshi.cn/online/LagMul.html






