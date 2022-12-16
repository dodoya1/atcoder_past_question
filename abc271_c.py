#https://atcoder.jp/contests/abc271/tasks/abc271_c
N=int(input())
a=list(map(int,input().split()))

def ok(x):
    less_than_x=[]
    for e in a:
        if e<=x:
            less_than_x.append(e)
    rem=len(set(less_than_x))
    #穴埋めに必要な巻数
    need=x-rem
    #同じ巻で複数冊あれば一冊だけ残して、それ以外は売って良い(extra=余分な巻数)
    extra=N-rem
    return extra//2>=need

bottom=0
top=333333

while top-bottom>1:
    mid=(top+bottom)//2
    if ok(mid):
        bottom=mid
    else:
        top=mid

print(bottom)

"""メモ
・二分探索
"""