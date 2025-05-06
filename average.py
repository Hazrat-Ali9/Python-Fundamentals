#To calculate an average of a list 
import math
count = 0
sum = 0
for value in [9,41,12,3,74,15]:
    count+=1
    sum+=value
    print(count, sum,value)
print(count,math.ceil(sum/count))
