#https://atcoder.jp/contests/abc262/tasks/abc262_b
N, M = map(int, input().split())
edge = [[False] * N for _ in range(N)]

for _ in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    edge[U][V] = True
    edge[V][U] = True

cnt = 0
    
for a in range(N):
    for b in range(a + 1, N):
        for c in range(b + 1, N):
            if edge[a][b] and edge[b][c] and edge[c][a]:
                cnt += 1

print(cnt)

"""メモ
・グラフ
・より高速に処理するために、ある頂点とある頂点の間に辺が存在するかをedgeで保存している。
"""