def junzhu():
    money = 0
    touzhu=100
    num = 0
    win = 0
    with open('2.txt','r')as f:
        for line in f.readlines():
            num+=1
            result,peilv = line.strip().split(',')
            print(result,peilv)
            if result=='1':
                earn = (float(peilv)-1)*touzhu
                win+=1
                money+=earn
            elif result=='0.5':
                earn = ((float(peilv)-1)/0.5)*touzhu
                win+=0.5
                money+=earn
            elif result=='-1':
                money-=touzhu
            elif result=='-0.5':
                money-=touzhu/0.5
        print("start is: "+str(money),str(win/num))

def beitou():
    money=0
    touzhu=200
    total=0
    start_touzhu=200
    num =0
    win =0
    loss = 0
    with open('2.txt','r')as f:
        for line in f.readlines():
            num+=1
            result,peilv = line.strip().split(',')
            print(result,peilv)
            if result=='1':
                win+=1
                earn = (float(peilv)-1)*touzhu
                money+=earn
                touzhu=200
                total=0
            elif result=='0.5':
                win+=0.5
                earn = ((float(peilv)-1)/0.5)*touzhu
                money+=earn
                touzhu=200
                total=0
            elif result=='-1':
                money-=touzhu
                loss+=1
                touzhu = touzhu*2
                total += touzhu
                print(touzhu,total+start_touzhu)
            elif result=='-0.5':
                loss+=0.5
                money-=touzhu/0.5
                touzhu = touzhu*2
                total+=touzhu
                print(touzhu,total+start_touzhu)
        print("start is: "+str(money),str(win/num),str(loss/num))

def feibonaqie():
    money=0
    touzhu=200
    total=0
    start_touzhu=200
    with open('2.txt','r')as f:
        for line in f.readlines():
            result,peilv = line.strip().split(',')
            print(result,peilv)
            if result=='1':
                earn = (float(peilv)-1)*touzhu
                money+=earn
                touzhu=200
                total=0
            elif result=='0.5':
                earn = ((float(peilv)-1)/0.5)*touzhu
                money+=earn
                touzhu=200
                total=0
            elif result=='-1':
                money-=touzhu
                touzhu = touzhu+touzhu
                total += touzhu
                print(touzhu,total+start_touzhu)
            elif result=='-0.5':
                money-=touzhu/0.5
                touzhu = touzhu*2
                total+=touzhu
                print(touzhu,total+start_touzhu)
        print("start is: "+str(money))

def fib_recur(n):
  	return fib_recur(n-1) + fib_recur(n-2)

beitou()