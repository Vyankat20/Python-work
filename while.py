#multiple table

n = int(input("enter number:"))
i = 1
while i <= 10:
    print(n * i)
    i += 1

# find number in tuple or list

nums = (1,4, 5, 2,  3, 7, 9)
i = 0
x = 5
while i < len(nums):
    if(nums[i] == x):
        print("found at index:", i)
    i += 1

# even no. between 1 to 100

n = 1
while n <= 100:
    if(n % 2 == 0):
        print(n)
    n += 1
    
    

    