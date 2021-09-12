mylist = [0, 5, 4, 3, 2, 5, 6, 4]
mylist.sort()
for i in range(0, len(mylist)):
    if mylist[i] == mylist[i - 1]:
        print(str(mylist[i]) + " Is a duplicate")
   
