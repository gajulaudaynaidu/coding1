a=int(input())
list_a=[]

if a%2==0:
    count=1
    list_a.append(count)
    for i in range(1,a-1):
        count+=2 
        list_a.append(count)

if a%2!=0:
    count=1
    list_a.append(count)
    for i in range(1,a):
        count+=2
        list_a.append(count)
        
print(*list_a)