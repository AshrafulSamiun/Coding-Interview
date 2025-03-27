

def binary_search(integers,h,t):
    low=0
    high=h-1
    result=-1
    check=integers[0]

    while low<=high:

        mid=(low+high)//2
        if integers[mid]<=t:                
            result=mid
            low=mid+1
        elif integers[mid]>t:
            high=mid-1

    return result+1

n,k=map(int,input().strip().split(" "))
integers=list(map(int,input().strip().split(" "))) 
quires=list(map(int,input().strip().split(" "))) 

for i in range(k):
    search=quires[i]
    max_index=binary_search(integers,n,search)
    print(max_index)

