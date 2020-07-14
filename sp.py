#Control System
''' Profile program by Nikita Kaem'''


print ("Hello, this is program for creating your profile, answer the questions.")

#ready questions

while True:
	agex = input ("Before we start, answer two fast question. \nAre you over 18 years old?: ")
	if agex == "yes" or agex == "y" or agex == "Yes" or agex == "YES" or agex == "Y":
		break
	if agex == "no" or agex == "n" or agex == "No" or agex == "NO" or agex == "N":
		print ("Sorry, we can't continue")
		quit()
	else:
		print ("Wrong answer, please use \"Y\" or \"N\"")

while True:
	start = input ("Do you accept for collecting your data?: ")
	if start == "yes" or start == "y" or start == "Yes" or start == "YES" or start == "Y":
		print ("Ok, lets start")
		break
	if start == "no" or start == "n" or start == "No" or start == "NO" or start == "N":
		print ("Ok, see you later")
		quit()
	else:
		print ("Wrong answer, please use \"Y\" or \"N\"")

#creating file
profile = open('profile.txt', 'a', encoding="utf-8-sig")
profile.write ("\n ### \n")

#taking a time
import datetime
pd = datetime.datetime.today().strftime("%d.%m.%y \n")
profile.write (pd)


#1block (introducing)
name = input ("What is your full name?: ")
print ("Good to know, " + name + "!")
profile.write ("Name: " + name + "\n")

borndate = input ("Enter your date of born (dd.mm.yyyy): ")
profile.write ("Borndate: " + borndate + "\n")

sex = input ("What is your sex?: ")
profile.write ("Sex: " + sex + "\n")

bornplace = input ("Where your was born?: ")
profile.write ("bornplace: " + bornplace + "\n")




#Q4-5

live = input ("Where do you live right now?: ")


#Q6-7
oldwork = input("Where you work last time?: ")
work = input ("Where you work now?: ")

#Q8
info = input("Ok, tell something about you: ")

#cardclient
print ("Ok, let see what are you \n \n ")

profilex = open('profile_backup.txt', 'w')
profile.close()

xb = open('profile.txt', 'r')
profilex.write(xb.read())

xb.close()

profilex.close()


  