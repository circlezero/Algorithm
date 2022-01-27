import sys
input = sys.stdin.readline
n = int(input())
Tree = {}
for i in range(n):
    node, left, right = input().split()
    Tree[node] = {'l': left, 'r': right}


def pre_order(s):
    if(s == '.'):
        return
    print(s, end='')
    pre_order(Tree[s]['l'])
    pre_order(Tree[s]['r'])


def in_order(s):
    if(s == '.'):
        return
    in_order(Tree[s]['l'])
    print(s, end='')
    in_order(Tree[s]['r'])


def post_order(s):
    if(s == '.'):
        return
    post_order(Tree[s]['l'])
    post_order(Tree[s]['r'])
    print(s, end='')


pre_order('A')
print()
in_order('A')
print()
post_order('A')
print('')
