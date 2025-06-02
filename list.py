nums = list()
while True:
    num = input("Enter a number: ")
    if(num == ''):break
    value = float(num)
    nums.append(value)
print(sum(nums))
print(len(nums))
average = sum(nums)/len(nums)
print("The list is :",nums)
print("The average of nums is ",average)
