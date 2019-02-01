# sequence to sequence 

## 机器翻译
![](imgs/seq2seq.png)
### 疑问：a<0>是什么
### 疑问：decoder的结束标记在哪里？
在编码阶段法语单词按照时序每个单词依次输入(x1,x2...xT)，最后得到一个输出。
将输出输入解码生成y1,y1作为输入生成y2,.....,那么就这样一直循环下去吗?应该有个END OF的符号吧


## beam search 集束搜索
解码出的(y1,y2,y3....)是一系列的概率,需要找出条件概率最高的的组合,而不是贪心算法求出最大概率y1,根据y1生成y2,求最大概率y2....

### 具体算法
https://www.zhihu.com/question/54356960 整理这个资料
1. 设beam withd =3,
![](imgs/beam-search1.png)

 f

![](imgs/beam-search.png)



## image captioning
**本质:** encoder编码阶段用CNN对图像就行编码

![](imgs/image-caption.png)






