n = int(input("enter nubmer:"))
for i in range(1,11):
    print(n * i)

#factorial find using while loop
g = int(input("enter another number:"))
fact = 1
i = 1
while i <= g:
    fact *= i 
    i += 1
print("factorial is:", fact)


#using for loop
h = int(input("Enter number:"))
fact = 1
for i in range(1, h + 1):
    fact *= i
print("factorial is:", fact)

