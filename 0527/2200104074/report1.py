#素数a
a=[]
#SAとSBに分ける
SA = []
SB = []
#SAとSBの合計値
SUMSA = 0
SUMSB = 0
#絶対値の差
dif_min=10000000000000000

#素数の書き出し
for i in range(2,100):
    flag=0
    for j in range(2,i//2+1):
        if i%j==0:
            flag=1
            break
    if flag==0:
        a.append(i)
#print(a)

a.reverse()

for i in a:
    if SUMSA <= SUMSB:
        SA.append(i)
        SUMSA = SUMSA + i
    else:
        SB.append(i)
        SUMSB = SUMSB + i

dif_min=abs(SUMSA - SUMSB)

print("dif_min:",dif_min)

print("SA:",SA)
print("SB:",SB)

