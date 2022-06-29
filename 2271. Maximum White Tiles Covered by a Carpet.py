题目: 给了一串 interval 和一个固定长度, 问这个固定长度, 最大能cover 多少interval

解法: 同向双指针, 也称sliding window,
		稍微不同的是, 这次快指针不停往前, 满指针每次加1
		
		主要还是考察实现中的细节
https://www.youtube.com/watch?v=7R10ZSepbS4


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        
        prefix = [0]
        for i in range(len(tiles)):
            prefix.append(prefix[-1] + tiles[i][1] - tiles[i][0] + 1)
        print(prefix)
        ans = 0
        j = 0
        for i in range(len(tiles)):
            while j < len(tiles) and tiles[i][0] + carpetLen - 1 >= tiles[j][1]: #这里要检查j 是否会大于n
                j += 1

            size = prefix[j] - prefix[i]
            if j < len(tiles):
                size += max(tiles[i][0] + carpetLen - 1 - (tiles[j][0]) + 1, 0) #需要考虑到, 万一最后一个已经超过了固定长度, 减出来就是个负值, 所以要和0 比较
            ans = max(ans, size)
        
        return ans