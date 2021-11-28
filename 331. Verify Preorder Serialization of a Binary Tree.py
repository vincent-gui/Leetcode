思路就是一个node 可以提供两个available 的slot, 但是这个node本身自己消耗掉一个slot

解法1
1. 初始available 的slot 是1
2. 每次进入循环就要减1, 因为当前node(无论是不是null) 都消耗1个slot
3. 如果available slot 小于0, 就返回False
4. 如果当前不是'#' 那么available slot += 2


解法2 stack

每次新的元素加入stack中, 
如果len(stack) >= 3, 那么就检查最后三个是不是 num, '#', '#'.
如果是, 就意味着这是一个leaf 节点, 可以直接替换成一个 '#'
重复以上操作 直到最后. 判定最后是不是只剩下一个 '#'

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        need = 1
        nodes = preorder.split(',')
        
        for node in nodes:
            need -= 1
            if need < 0:
                return False
            if node != '#':
                need += 2
        
        return need == 0