#!usr/bin/python3

adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
u= []
for i in adhoc:
	if i>5:
		u.append(i)
print("List of numbers that are greater than 5 : ")
print(u)

v=[]
for i in adhoc:
	if i<=2:
		v.append(i)
print("List of numbers that are less than or equal to 2 : ")
print(v)






