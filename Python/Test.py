from datetime import datetime
import csv
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

date = str(rn.day)+"/"+str(rn.month)+"/"+str(rn.year)
time = str(rn.hour)+":"+str(rn.minute)+":"+str(rn.second)
with open("data.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name","gender","date","time"])
        writer.writerow({"name" : name,"gender" : gender,"date" : date,"time" : time})
print("Data Saved")