#!usr/bin/python3

import time
a=input("Enter your name : ")

import datetime
b=int(datetime.datetime.now().strftime('%H%M%S'))

if b>215959 & b<=55959 :
	print("Good Night, " +a)
elif b>55959 & b<=115959 :
	print("Good Morning, " +a)
elif b>115959 & b<=165959 :
	print("Good Afternoon, " +a)
elif b>165959 & b<=215959 :
	print("Good Evening, " +a)

