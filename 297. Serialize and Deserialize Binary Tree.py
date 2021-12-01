先序遍历,进入data

deserial 的时候放入deque, popleft 继续遍历

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []
        
        def serial(root):
            if not root:
                data.append('#')
                return 
            data.append(str(root.val))
            serial(root.left)
            serial(root.right)
        
        serial(root)
        
        return ','.join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        queue = collections.deque([item for item in data.split(',')])
        
        def deserial():
            val = queue.popleft()
            if val == '#':
                return None
            node = TreeNode(val)
            node.left = deserial()
            node.right = deserial()
            
            return node
        
        return deserial()