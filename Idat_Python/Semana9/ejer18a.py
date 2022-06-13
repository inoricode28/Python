sum4,sum5=0,0
for i in range(5,126):
    if(i%20==0):
        sum4+=i
        sum5+=i
        print(i,sum4,sum5)
    elif(i%4==0):
        sum4+=i
        print(i,sum4)
    elif(i%5==0):
        sum5+=i
        print(i,sum5)
print(sum4,sum5)