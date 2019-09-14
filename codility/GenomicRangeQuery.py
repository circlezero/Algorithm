def solution(S, P, Q):
    ans = []
    impactFactor = {'A' : 1, 'C' : 2, 'G' : 3, 'T' : 4}

    for i in range(len(P)):
        if 'A' in S[P[i] : Q[i]+1]:
            ans.append(1)
        elif 'C' in S[P[i] : Q[i]+1]:
            ans.append(2)
        elif 'G' in S[P[i] : Q[i]+1]:
            ans.append(3)
        elif 'T' in S[P[i] : Q[i]+1]:
            ans.append(4)
    return ans