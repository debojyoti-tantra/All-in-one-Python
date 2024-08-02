# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

# assume each subject has fullmarks 100, so total full marks is 300
math = int(input("Enter marks of your math exam: "))
physics = int(input("Enter marks of your physics exam: "))
chemistry = int(input("Enter marks of your chemistry exam: "))

tot_mar = math + physics + chemistry
tot_mar_per = tot_mar * 100 / 300

if (tot_mar_per>100 or math>100 or physics>100 or chemistry>100):
    print("Invalid Marks")
elif (tot_mar_per>=40 and math>=33 and physics>=33 and chemistry>=33):
    print("Total Marks:",tot_mar)
    print("Percentage:",int(tot_mar_per),"%")
    print("you are pass")
else:
    print("Total Marks:",tot_mar)
    print("Percentage:",int(tot_mar_per),"%")
    print("you are fail")
