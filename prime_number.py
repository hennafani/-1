
x = int(input('inter prime number'+'\n'))
mylist=[]
for i in range(0,x):
 mylist.append(x)
if x > 1 and x != 4:
    for i in range (2 , x //2):
        if x % i == 0:
            print('no')
            break
    else:
        print(mylist)
           
else:
    print('no')
