a=int(input())
list_a=[]
if a==1:
    print(1)
else:
    count=1
    list_a.append(count)
    for i in range(1,a):
        count+=2
        list_a.append(count)
        
print(*list_a)