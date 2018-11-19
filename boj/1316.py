n = int(input())
res = 0
for i in range(n):
	s = input()
	c = [0]*26
	flag = True
	for j in range(1, len(s)):
		ind1 = ord(s[j-1]) - ord('a')
		ind2 = ord(s[j]) - ord('a')

		if s[j] != s[j-1]:
			if c[ind1] != 0 or c[ind2] != 0:
				flag = False
				break
			c[ind1] = 1
		else: continue
	if flag: res += 1
print(res)
