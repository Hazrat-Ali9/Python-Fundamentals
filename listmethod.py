#Declaring lists
import math # importing math module

lists = list()
print(dir(lists))
web = ['HTML','CSS','JavaScript','Bootstrap','ReactJS','Python','MongoDB', 'SQL','Nodejs']
print(web)

#Lists are mutable
web.append('Git')
web.append('Postgre')
web.append('Java')
print(web)
nums = [5,10,15,13,9,75,25,10]


#Built-in functions
print("The length of the nums lis is ",len(nums))
print("Maximum is ", max(nums))
print("Minimum is ", min(nums))
print("The sum is ", sum(nums))
print("The average is",sum(nums)/len(nums))
for i in nums:
    print(math.ceil(math.sqrt(i)))
