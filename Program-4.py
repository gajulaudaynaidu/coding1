list_a=[1,2,3,4,5,6,7,8,9]
list_b=input().split(",")  #input comma separated integers
dict_A={}
for i in list_a:
    count=0
    for j in list_b:
        if int(j)%i==0:
            count+=1
    dict_A[i]=count
print(dict_A)