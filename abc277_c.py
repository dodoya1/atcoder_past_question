#https://atcoder.jp/contests/abc277/tasks/abc277_c
import sys
sys.setrecursionlimit(10**7)
from collections import defaultdict

edge = defaultdict(list)
N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    edge[A].append(B)
    edge[B].append(A)

ans = 1

#既に来たことがある場所を保存する変数
come = set()

def dfs(now):
    come.add(now)
    global ans
    ans = max(ans, now)
    #次に進むべき場所について探索する。
    for to in edge[now]:
        #既に来たことがある場合はスキップ
        if to in come:
            continue
        dfs(to)
    
dfs(1)
print(ans)

"""メモ
・この問題は、DFS問題である。
・DFS
    深さ優先探索。ある地点とある地点が連結であるかを調べることができる。
"""