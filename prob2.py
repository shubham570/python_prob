#!usr/bin/python3

from googlesearch import search
web = input("Enter Text : ")

print(search(web))
url= []
for i in search(web, stop=10):
	print(i)
	url.append(i)

print(url)
