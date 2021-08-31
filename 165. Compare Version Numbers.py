

解法2 投机取巧 先变成数字, 再比较
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        i = 0
        
        while i < len(v1) and i < len(v2):
            if int(v1[i]) < int(v2[i]):
                return -1
            if int(v1[i]) > int(v2[i]):
                return 1
            i += 1
            
        if len(v1) == len(v2):
            return 0
        
        if i == len(v1):
            while i < len(v2):
                if int(v2[i]) != 0:
                    return -1
                i += 1
            return 0
        if i == len(v2):
            while i < len(v1):
                if int(v1[i]) != 0:
                    return 1
                i += 1
            return 0
			
第二种解法的升级, 这个解法避免了判断完最小的以后, 接着判断剩余的

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a boolean
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        for i in range(max(len(v1), len(v2))):
            gap = (int(v1[i]) if i < len(v1) else 0) - (int(v2[i]) if i < len(v2) else 0)
            if gap != 0:
                return 1 if gap > 0 else -1
        return 0