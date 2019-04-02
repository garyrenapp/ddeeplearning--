

## 排序
### 快速排序
快速排序是图灵奖得主 C. R. A. Hoare 于 1960 年提出的一种划分交换排序。它采用了一种分治的策略，通常称其为分治法(Divide-and-ConquerMethod)。

分治法的基本思想是：将原问题分解为若干个规模更小但结构与原问题相似的子问题。递归地解这些子问题，然后将这些子问题的解组合为原问题的解。

利用分治法可将快速排序的分为三步：

1.在数据集之中，选择一个元素作为”基准”（pivot）。

2.所有小于”基准”的元素，都移到”基准”的左边；所有大于”基准”的元素，都移到”基准”的右边。这个操作称为分区 (partition) 操作，分区操作结束后，基准元素所处的位置就是最终排序后它的位置。

3.对”基准”左边和右边的两个子集，不断重复第一步和第二步，直到所有子集只剩下一个元素为止。

这个一步步讲解http://bubkoo.com/2014/01/12/sort-algorithm/quick-sort/

```python
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def quick_sort(lst):
            if not lst:
                return []
            pivot = lst[0]
            #这里开辟了空间，而且遍历了两次，这个代码只是为了理解思想吧
            left = quick_sort([x for x in lst[1:] if x < pivot])
            right = quick_sort([x for x in lst[1:] if x>=pivot])
            return left + [pivot] + right 
    
        if(tinput==[] or k >len(tinput)):
            return []
        tinput = quick_sort(tinput)
        return tinput[:k]

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        def quick_sort(arr):
            less = [] 
            pivot = []
            more =[]

            #这个只遍历了一次但是还是开辟了空间
            if(len(arr)<=1):
                return arr
            else:
                p = arr[0]
                for i in arr:
                    if(i<p):
                        less.append(i)
                    elif(i>p):
                        more.append(i)
                    else:
                        pivot.append(i)
            less = quick_sort(less)
            more = quick_sort(more)
            return less + pivot + more
        
        if(len(tinput)<k):
            return []
        arr = quick_sort(tinput)
        return arr[:k]

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # 未开辟空间，标准的快速排序
        if(len(tinput)<k):
            return []
        arr = self.quick_sort(tinput)
        return arr[:k]
    
    def quick_sort(self,arr):
        def swap(arr,i,k):
            tmp = arr[i]
            arr[i] = arr[k]
            arr[k] = tmp
            
        def partition(arr,left,right):
            storeIndex = left
            pivot = arr[right] #直接选取最右边的元素为基准元素
            for i in range(left,right):
                if(arr[i] < pivot):
                    swap(arr,storeIndex,i)
                    storeIndex +=1
                    
            swap(arr,right,storeIndex)  #交换基准元素和 storeIndex 位置的元素的位置
            return storeIndex
            
        def sort(arr,left,right):
            if(left > right):
                return 
            storeIndex = partition(arr,left,right)
            sort(arr,left,storeIndex-1)
            sort(arr,storeIndex+1,right)
            
        sort(arr,0,len(arr)-1)
        return arr

```
