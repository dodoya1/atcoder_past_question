#https://atcoder.jp/contests/abc265/tasks/abc265_c
H, W = map(int, input().split())
G = [input() for _ in range(H)]
#その場所に来たことがあるか(無限ループの場合のために使用する)
come = [[False] * W for _ in range(H)]

nowx, nowy = 0, 0

while True:
    come[nowx][nowy] = True
    c = G[nowx][nowy]
    nxtx, nxty = nowx, nowy
    if c == 'U':
        nxtx -= 1
    if c == 'D':
        nxtx += 1
    if c == 'L':
        nxty -= 1
    if c == 'R':
        nxty += 1
    #マス外で移動することができない場合。　
    if nxtx < 0 or H <= nxtx or nxty < 0 or W <= nxty:
        print(nowx + 1, nowy + 1)
        exit()
    nowx, nowy = nxtx, nxty
    if come[nowx][nowy]:
        print(-1)
        exit()
"""メモ
・マス問題
"""