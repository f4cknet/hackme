import os
f = open('results.txt','r')
touzhu = 200
money = 0
result = [i.strip().split(',')[0] for i in f.readlines()]
index = 0
while index<1079:
    if result[index]== result[index+1]=="win":
        print("junzhu")
    else:
        print("beitou")
    index+=1


# print(f.readlines()[1])
# for line in range(0,1080):
#     print(f.readlines()[line])
    # data = line.strip().split(',')
    #
    # if data[0]== 'win':
    #     money+=touzhu
    #     touzhu = 200
    #     print()
    # else:
    #     print(touzhu)
    #     touzhu=touzhu*2