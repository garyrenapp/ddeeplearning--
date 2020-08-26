# Locality Sensitive Hashing (LSH)

（局部敏感哈希）LSH的作用就是把原来高维空间上的点都映射到一个或多个hashtable的不同的位置上，这个位置术语上称作桶(buckets)。它映射的原则是：原来在高维空间中就很接近的点，会以很大的概率被映射到同一个桶中。这样，如果再给你一个高维空间上的点，你只需要按照同样的方式也把这个点映射到一个桶中，而在同一个桶中点都是有很大概率在原来高维空间中是相似的，这样就可以直接对这个桶中的元素进行查找即可，大大的提高了查找的效率。

## 具体理解
* 假设有10000个文档，每个文档用ndims=300的特征向量表示 (num , ndims) is (10000,300)
如果用最近邻进行暴力比对则需要遍历全部，LSH可以缩小搜索范围

* Each plane divides the space to  2  parts.
  ![](../imgs/../ddeeplearning--/imgs/LSH.jpg)
* So  $n$  planes divide the space into  $2^n$  hash buckets.
  ![](../imgs/../ddeeplearning--/imgs/lsh2.jpg)
* We want to organize 10,000 document vectors into buckets so that every bucket has about   16  planes. For that we need  $\frac{10000}{16}=625$  buckets.
* We're interested in  $n$ , number of planes, so that  $2^n=625$ . Now, we can calculate  $𝑛=\log{_2}{625}=9.29≈10 .$
  
### So  $n$  planes divide the space into  $2^n$  hash buckets.
* 这里plane是随机产生的一个空间向量plane
* 空间向量与特征向量相乘>=0的在一侧,<0的在另一侧
* 设planes is (300,10) 则最后就产生形如h_n is [0,1,0,1,1,0,1,1,1,1]
* 变换hash_value $$ hash\_value = \sum_{i=0}^{N-1} \left( 2^{i} \times h_{i} \right) $$
```python
def hash_value_of_vector(v, planes):
    """Create a hash for a vector; hash_id says which random hash to use.
    Input:
        - v:  vector of tweet. It's dimension is (1, N_DIMS)
        - planes: matrix of dimension (N_DIMS, N_PLANES) - the set of planes that divide up the region
    Output:
        - res: a number which is used as a hash for your vector

    """
    hash_value = 0 
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    h_n = v.dot(planes)[0]
    #>=0 在空间的一侧，<0 的在另一侧
    h_n = h_n >=0
    h_n = h_n.astype(np.int32)
    ### END CODE HERE ###
    for i,h_i in enumerate(h_n):
        hash_value = hash_value + np.power(2,i) * h_i
    # cast hash_value as an integer
    hash_value = int(hash_value)

    return hash_value
```
## 一个hashtable
hash_table = {hash_value_1:[v1,v2...],hash_value_2:[v10,v21],.....}
高维空间的相似向量会落到同一个bucket
## 多个hashtable
因为planes是随机生成的，可能会出现本来属于同相似的向量落到不同bucket，所以可以产生多组planes，生成多组hashtable 减少误差

## 相似度度量
对落到一个bucket的向量进行相似度度量。

