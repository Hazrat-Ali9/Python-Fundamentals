total = 0
count = 0
while True:
    num = input('Enter a number: ')
    if(num == ''):break
    try:
        value = float(num)
    except:
        print(num, "is not a number")
        num = input('Enter a number: ')
        
    total += value
    count += 1
average = total / count
print("Average: ",average)
