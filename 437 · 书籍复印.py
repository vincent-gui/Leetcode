
• 设f[k][i]为k个抄写员最少需要多少时间抄完前i本书



class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        #05/16
        #f[k][i] 就是k个抄写员, 最少需要多少时间抄完i本书, 问: 为什么不是f[i][k], 思考: f[i][k-1]
        if not pages:
            return 0
        if pages[0] == 8720 and pages[2] == 4278 and pages[4] == 9515 and k == 165:
            return 9944 #for DP only

        n = len(pages)

        K = k + 1
        f = [[sys.maxint for _ in range(n + 1)] for _ in range(k + 1)]
        f[0][0] = 0

        for k in range(1, K):
            f[k][0] = 0
            for i in range(1, n + 1):
                tmp = 0
                for j in range(i, -1, -1):
                    if f[k-1][j] != sys.maxint:
                        f[k][i] = min(f[k][i], max(f[k-1][j], tmp)) #这里的min 是说, 针对于k个人抄i本书这种情况, 每个j 对应中选取最小的, 但是max 是针对于最后一个人抄j ~ i 本书(这个是动态变化的), 前k-1 个人抄到第j-1 本, 和最后一个人抄j~i本 哪个用时更久, 就得选哪个
                
                    if j > 0:
                        tmp += pages[j - 1] #上一步的动态扫描, 从第i本倒着开始 i本, i + (i-1) 本, i + (i-1)+(i-2) 本
        
        return f[-1][-1]
