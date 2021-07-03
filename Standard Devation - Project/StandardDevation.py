import math
import csv
with open("data.csv", newline="") as f:
    reader= csv.reader(f)
    file_data=list(reader)
data=file_data[0]
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+= int(x)
    mean=total/n
    return mean
Squared_list=[]
for m in data:
    a=int(m)-mean(data)
    a=a**2
    Squared_list.append(a)
sum=0
for i in Squared_list:
    sum=sum+i
result=sum/(len(data)-1)
standardDevation=math.sqrt(result)
print(standardDevation)