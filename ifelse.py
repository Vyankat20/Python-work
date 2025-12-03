#if, elif, else
marks = float(input("enter you msrks:"))
if(marks>=90):
    print("You passed with grade: A")
elif(marks>=80):
    print("You passed with grade: B")
elif(marks>=70):
    print("You passed with grade: C")
elif(marks>=60):
    print("You passed with grade: D")
elif(marks<=35):
    print("You are fail better luck next time")

else:
    print("you are passed but you need to study hard")


#some practice question even or add number

num = int(input("enter your number:"))
if(num % 2 == 0):
    print("Even")
else:
    print("odd")

# find greatest number 
a = int(input("enter number1: "))
b = int(input("enter number2: "))
c = int(input("enter number3: "))

if(a > b and a > c):
    print("num1 is greater")
elif(b > c):
    print("num2 is greater")
else:
    print("num3 is greater")



