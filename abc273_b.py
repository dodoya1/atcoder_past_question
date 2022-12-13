#https://atcoder.jp/contests/abc273/tasks/abc273_b
x,k = list(map(int,input().split()))

for i in range(k):
    x//=10**i
    m=x%10
    if m<=4:
        x-=m
    else:
        x+=10-m
    x*=10**i

print(x)

"""メモ
・10**iの位以下を四捨五入する方法
"""