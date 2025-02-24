
def power_of_five(n):
    
    if n==0:
        return False
    
    if n==1:
        return True
    
    if n<0:
        return 1/power_of_five(n)
    
    if n%5!=0:
        return False
    
    return power_of_five(n/5)

num=4
result=power_of_five(num)
if result:
    print("Yes")
else:
    print("No")