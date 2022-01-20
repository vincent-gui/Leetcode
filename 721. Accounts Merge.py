解法1: Union find 
思路就是用email 和id 的map

	1.  #转换成 email:idx 的map
	2. #遍历所有的email 和idx 的list, 并且union 一起
	3. #用原始id 找到root id, 再将email 全部加入到root id 的set里
	4. #返回答案
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.father = {}
        for i in range(len(accounts)):
            self.father[i] = i
            
        email_idx = {}
        #create map from email to idx
        for idx, emails in enumerate(accounts): #转换成 email:idx 的map
            for email in emails[1:]:
                email_idx[email] = email_idx.get(email, []) + [idx]
            
        for idxs in email_idx.values(): #遍历所有的email 和idx 的list, 并且union 一起
            root = idxs[0]
            for i in range(1, len(idxs)):
                self.union(root, idxs[i])
        
        id_emails = {}
        for idx, emails in enumerate(accounts): #用原始id 找到root id, 再将email 全部加入到root id 的set里
            root_id = self.find(idx)
            id_emails[root_id] = id_emails.get(root_id, set())
            for email in emails[1:]:
                id_emails[root_id].add(email)
        
        ans = []
        
        for id, emails in id_emails.items(): #返回答案
            ans.append([accounts[id][0]] + sorted(emails))
        
        return ans
    
            
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
            
        for p in path:
            self.father[p] = node
            
        return node
        
		
解法2: DFS

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_idx = {}
        for idx, emails in enumerate(accounts):
            for email in emails[1:]:
                email_idx[email] = email_idx.get(email, []) + [idx]
            
        seen = set()
        ans = []
        for idx, info in enumerate(accounts):
            if idx in seen:
                continue
            emails = set()
            self.dfs(idx, accounts, email_idx, seen, emails)
            ans.append([accounts[idx][0]] + sorted(emails))
        return ans
        
    def dfs(self, idx, accounts, email_idx, seen, emails):
        if idx in seen:
            return 
        seen.add(idx)
        for email in accounts[idx][1:]:
            emails.add(email)
            for neighbor in email_idx[email]:
                self.dfs(neighbor, accounts, email_idx, seen, emails)