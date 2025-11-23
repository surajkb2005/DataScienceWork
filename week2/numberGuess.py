import random;

rannum = random.randint(1,10)

yes = True

while yes:
    num = int(input("Enter a number between 1 to 10: "))

    if(1<=num<=10):
        if(num == rannum):
            print("Correct Answer")
            break
        elif(num<rannum):
            print("Guess to low")
        else:
            print("Guess to high")
    else:
        print("Give proper number!")
    
    ans = input("Do u want to continue y/n: ")

    if(ans=='y'):
        yes = True
    else:
        yes = False