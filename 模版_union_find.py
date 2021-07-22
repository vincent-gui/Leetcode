class UnionFind:
	def __init__(self, n):
		self.father = {}
		for i in range(1, n + 1):
			self.father[i] = i 
	
	def union(self, a, b):
		root_a = self.find(a)
		root_b = self.find(b)
		if root_a != root_b:
			self.father[root_a] = root_b
	
	def find(self, node):
		path = []
		while node != self.father[node]:
			path.append(node)
			node = self.father[node]
		
		for n in path:
		self.father[n] = node 
		
		return node 