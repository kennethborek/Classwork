f=open("C:/Users/Student 16/PycharmProjects/Classwork/class/test.txt" )
myList = []
for line in f:
    myList.append(line)
b=len(myList)
for a in range(0,b):
    print (myList [a])