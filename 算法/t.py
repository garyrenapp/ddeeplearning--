
#%%
class Quick:
    @classmethod
    def quick_sort(cls,arr):
        lo = 0 
        hi = len(arr) -1 
        cls.sort(arr,lo,hi) 

    @classmethod
    def sort(cls,arr,lo,hi):
        #终止条件
        if(lo >= hi ):
            return 
        #3-way partition
        lt,gt,i= lo,hi,lo
        v = arr[lo]
        while(i <= gt):
            if(arr[i] == v):
                i = i+1 
            elif(arr[i] < v):
                arr[i],arr[lt] = arr[lt],arr[i]
                i = i +1 
                lt = lt + 1
            else:
                arr[i],arr[gt] = arr[gt],arr[i]
                gt = gt -1 
        #左半排序
        cls.sort(arr,lo,lt-1)
        #右半排序
        cls.sort(arr,gt+1,hi)
        
        


# %%
item = [3,3,5,1,9,9,2,11,8]
#item = [1,2,3,4,5,6,7,8]
#item = [1]
Quick.quick_sort(item)

# %%
item

# %%


# %%
