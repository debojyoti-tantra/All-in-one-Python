marks = int(input("Enter your marks: "))

if (marks>=90 and marks<=100):
    print("Very Good")

elif (marks>=75 and marks<90):
    print("Good")

elif (marks>=50 and marks<75):
    print("Normal")

elif (marks>=25 and marks<50):
    print("Poor")

elif (marks>0 and marks<25):
    print("Very Poor")

elif (marks == 0):
    print("Shame On You")

else:
    print("Invalid Marks")
