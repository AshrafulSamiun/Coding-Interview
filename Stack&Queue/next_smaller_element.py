def smaller_element(arr):
    stack=[]
    n=len(arr)
    for i in range(n):
        found=False
        for j in range(i,n):
            if arr[i]>arr[j]:
                stack.append(arr[j])
                found=True
                break

        if found==False:
            stack.append(-1)
    #return stack
    print(*stack)

arr=list(map(int, input().split(" ")))
result=smaller_element(arr)
#print(*result)