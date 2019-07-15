def solution(A):
    minValue = 10000
    minInd = 0
    
    for i in range(len(A)):
        sumValue = A[i]
        for j in range(i+1, len(A)):
            sumValue += A[j]
            avg = sumValue / (j-i+1)
            
            if minValue > avg:
                minValue = avg
                minInd = i
        
    return minInd