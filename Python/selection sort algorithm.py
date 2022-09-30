
# Selection sort Algorithm:-

# NOTE:- This program means that, the elements in the given
        # list are rearranged by swapping to first place by
        # comparing of small number with adjacent numbers.

# Assending Order:

li=[10,0,1,15,3,5]
for i in range(0,len(li)):
    min_val=min(li[i:])                 # min_val=min(li[0:])       min_val=min(li[1:])         min_val=min(li[2:])
    idx=li.index(min_val)            # idx=li.index(0)=1           idx=li.index(1)=2            idx=li.index(3)=4
    li[i],li[idx]=li[idx],li[i]            # li[0],li[1]=li[1],li[0]        li[1],li[2]=li[2],li[1]         li[2],li[4]=li[4],li[2]
print(li)                                       # li=[0,10,1,15,3,5]            li=[0,1,1015,3,5]           li=[0,1,3,15,10,5]


# Desending Order:

li=[10,0,1,15,3,5]                  
for i in range(0,len(li)):          
    max_val=max(li[i:])                 # max_val=max(li[0:])
    idx=li.index(max_val)             # idx=li.index(15)=3
    li[i],li[idx]=li[idx],li[i]              # li[0],li[3]=li[3],li[0]
                                                      # li=[15,0,1,10,3,5]
print(li)

