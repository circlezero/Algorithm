import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input())
tree = [[] for i in range(n+1)]
node = [[] for i in range(n+1)]
parent = [0 for i in range(n+1)]
check = [False for i in range(n+1)]

for i in range(n-1):
    l, r = map(int, input().split())
    node[l].append(r)
    node[r].append(l)


def gen_tree(n):
    if check[n]:
        return

    check[n] = True
    for i in node[n]:
        if check[i] is False:
            tree[n].append(i)
            parent[i] = n

    for i in tree[n]:
        gen_tree(i)


gen_tree(1)

for i in range(2, n+1):
    print(parent[i])
