题目分成三步
1. 如果root.val > key: root.left = search(root.left, key)
2. 如果root.val < key: root.right = search(root.right, key)
3. 如果root.val == key:
	a. 判断是不是leaf
	b. 判断有没有右孩子
		i. curr.val = find_successor()
		ii. 进一步递归, 因为后面的node 已经提升到前面, 后面会有一个重复的node, 需要删掉
	c.判断有没有左孩子
		i. curr.val = find_predecessor()
		ii. 进一步递归, 因为后面的node 已经提升到前面, 后面会有一个重复的node, 需要删掉

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key) #同样的条件, 放进左侧重新查找
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val) #这一步堪称 经典, 找到当前要求置换的点, 然后还完以后, 继续进行找下一个要置换的点
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val) #这一步堪称 经典, 找到当前要求置换的点, 然后还完以后, 继续进行找下一个要置换的点
                
        return root
        
        
    #smallest node bigger than curr
    def successor(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node.val
    
    
    #bigest node lower than curr
    def predecessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.val