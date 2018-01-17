list=[10,20,20,10,10,30,50,10,20,50,70,90,70,110,90]
print("Data: ")
print(list)
datavalue=[]
delet=[]
counter=0
for i in list:
    if i not in datavalue:
        value1=i
        datavalue.append(value1)
    else:
        counter=counter+1
        index=datavalue.index(i)
        datavalue.pop(index)
print("Result is : ",counter)