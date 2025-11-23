n1 = int(input("Enter the num 1: "))
n2 = int(input("Enter the num 2: "))
op = input("What do you want ' + , - , * , / ' : ? ")
ans = 0

if op == "+":
    ans = n1+n2
elif op == "-":
    ans = n1-n2
elif op == "*":
    ans = n1*n2
elif op == "/":
    if n2 != 0:
        ans = n1/n2

if n2==0 and op=='/':
    print("Error! Cannot divide by 0")
else:
    print("Final answer : ",ans)