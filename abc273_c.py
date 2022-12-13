#https://atcoder.jp/contests/abc273/tasks/abc273_c
from collections import defaultdict

N=int(input())
A=list(map(int,input().split()))

cnt=defaultdict(int)

for a in A:
    cnt[a]+=1

cnt_list=[]

for key in cnt:
    cnt_list.append((key,cnt[key]))

cnt_list.sort(reverse=True)

for K in range(N):
    if K<len(cnt_list):
        print(cnt_list[K][1])
    else:
        print(0)

"""メモ
・連想配列、数学的考察
・https://www.youtube.com/live/kd4U4BxJLVU?feature=share
"""