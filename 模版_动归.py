模版1 (from 132. Palindrome Partitioning II)

f[i] = f[j] + 1, + if condition

例如: 设f[i]为S前i个字符S[0..i-1]最少可以划分成几个回文串
for i in range(1, n + 1): 
	for j in range(i):
		#do something