题目: 给了三个数组, recipes, ingredients , supplies , 问用supplies里的东西可以做recipes 上的哪些食物

一开始意味就是遍历, 后来发现recipes上的食物也可以作为一种supplies, 这样就是拓扑排序

topo need two dict, one is indegree(key is item, value is how maany item able able to reach this item) , one is neighbor (first item -> next item)



class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        #问题是转成topo sort
        #但是怎么track indegree
        
        #topo need two dict, one is indegree, one is neighbor
        indegree = defaultdict(int)
        neighbors = defaultdict(list)
        
        for i in range(len(recipes)):
            for ing in ingredients[i]:
                indegree[recipes[i]] += 1
                neighbors[ing].append(recipes[i])
        
        queue = deque(supplies)
        
        while queue:
            curr = queue.popleft()
            for ni in neighbors[curr]:
                indegree[ni] -= 1
                if indegree[ni] == 0:
                    queue.append(ni)
        
        return [k for k in indegree if indegree[k] == 0]