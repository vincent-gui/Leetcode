#132. Palindrome Partitioning II
def isValid(self, s):
	n = len(s)
	valid = [[False for _ in range(n)] for _ in range(n)]
	
	for mid in range(n):
		i = j = mid
		while i >= 0 and j < n and s[i] == s[j]:
			valid[i][j] = True
			i -= 1
			j += 1
		
		i, j = mid, mid + 1
		while i >= 0 and j < n and s[i] == s[j]:
			valid[i][j] = True
			i -= 1
			j += 1
	return valid