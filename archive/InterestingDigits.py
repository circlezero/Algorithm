import sys

ans = []
n = int(sys.stdin.readline())

for i in range(2, n):
    if (n - 1) % i == 0:
        ans.append(i)

# -------------------------------------------------

# for i in range(2, n):
#     flag = True
#     for k1 in range(n):
#         for k2 in range(n):
#             for k3 in range(n):
#                 if (k1 + k2*n + k3*n*n) % i == 0 and (k1 + k2 + k3) % i != 0:
#                     flag = False
#                     break
#             if flag == False:
#                 break
#         if flag == False:
#             break
#     if flag == True:
#         ans.append(i)

for i in ans:
    print(i)