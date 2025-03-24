from datetime import datetime
name = input("Name : ")
gender = input("Gender : ")
d,m,y = input("Enter Birthday (DD/MM/YYYY): ").split("/")
bd = datetime(int(y),int(m),int(d))
rn = datetime.now()
if (gender.strip().lower() == "male"):
    print("Hello "+"\033[34m"+name+"\033[0m")
elif (gender.strip().lower() == "female"):
    print("Hello "+"\033[31m"+name+"\033[0m")
else:
    print("Hello "+name)
time_diff = datetime(1,1,1) + (rn - bd)
print("Your age is : "+str(time_diff.year-1)+" Years "+str(time_diff.month-1)+" Months "+str(time_diff.day-1)+" Days")
