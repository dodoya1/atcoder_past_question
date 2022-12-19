#https://atcoder.jp/contests/abc263/tasks/abc263_c
N, M = map(int, input().split())

ans = []

#x << n → x の n ビット左シフト(以下を参考に)
#https://qiita.com/7shi/items/41d262ca11ea16d85abc#%E3%82%B7%E3%83%95%E3%83%88
#1 << M = 2のM乗(1が立っているところの数値を使う) 
for use in range(1 << M):
    tmp = []
    #右からj番目が使用されているかどうか
    for j in range(M):
        if (use >> j) % 2 == 1:
            tmp.append(j)
    if len(tmp) == N:
        ans.append(tmp)

ans.sort()

for nums in ans:
    for i in range(N):
        nums[i] += 1
    print(*nums)

"""メモ
・ビットシフト
・1 << M = 2のM乗(1が立っているところの数値を使う)
"""