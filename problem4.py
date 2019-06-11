#!usr/bin/python3

name=input("Enter name of user : ")

import os
list=[]
for i in name:
	if i.isalpha()==True:
		list.append(i)
		continue

	elif i.isdigit()==True:
		print("Enter only string in name of user")
		exit()

os.system("useradd -p hello" +name+ " " +name)
