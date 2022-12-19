#https://atcoder.jp/contests/abc263/tasks/abc263_b
N = int(input())
P = [-1, -1] + list(map(int, input().split()))

now = N
back = 0

while now != 1:
    now = P[now]
    back += 1

print(back)

"""メモ
・木
"""