#https://atcoder.jp/contests/abc265/tasks/abc265_b
N, M, T = map(int, input().split())

A = list(map(int, input().split()))

bonus = [0] * N

for _ in range(M):
    X, Y = map(int,input().split())
    X -= 1
    bonus[X] = Y
    
for now in range(N-1):
    T += bonus[now]
    T -= A[now]
    if T <= 0:
        print("No")
        exit()

print("Yes")