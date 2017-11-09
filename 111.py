num=[];
i=2
for i in range(2,100):
    j=2
    for j in range(2,i):
        if(i%j==0):
            print(i,"可以被",j,"整除","不是质数")
    else:
        print(num)
