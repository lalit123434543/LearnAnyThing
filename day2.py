# #file handling in python
f=open("file1.txt","w+")
data=f.read()
print(data)
data=str(input("enter data: "))
f.write(data)


f.close()
