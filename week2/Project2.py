#student marks

marks = int(input("Enter your marks: "))

if marks<0 or 100<marks:
    print("Enter marks between 0 to 100!!")
elif 90<=marks<=100:
    print("A Grade! Very good , keep it up")
elif 75<=marks<90:
    print("B Grade: Keep it up")
elif 40<=marks<75:
    print("C Grade: Good")
else:
    print("F Grade: Do hard work and score better!")
