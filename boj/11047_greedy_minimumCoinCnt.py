inList = input().split()
N = eval(inList[0])
total = eval(inList[1])
coinList =[]
for i in range(N):
    coinList.append(eval(input()))
resCoinList = []
cnt = 0
order = len(coinList)-1
leftMoney = total
while order >= 0 :
    if (leftMoney - coinList[order]) >=0 :
        cnt += leftMoney // coinList[order]
        leftMoney = leftMoney%coinList[order]

    # if coinList[order] <= leftMoney:
    #
    else:
        order -=1

print(cnt)
