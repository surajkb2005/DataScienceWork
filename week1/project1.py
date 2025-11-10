print("Enter your details to get your Personal Introduction ")
name = input("What is your name ? : ")
age = int(input("What is your age ? : "))
hobby = input("What is your Hobby ? : ")

print("Welcome",name)
if(age<=18):
    print("Oh! You are under 18.")
    print(hobby,"is great",". I wish you all the Best for your future!")
else:
    print("Oh! You are a responsible citizen. ")
    print("Good to have",hobby,"as a hobby. Have a great day!")

