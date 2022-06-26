题目: 给一串单词, 给一个最大长度, 让把这一串单词按照最大长度分发成不同的行
并且保证同一行的每次单词尽可能的分散, 如果不能平均分散, 则前面的部分尽可能分散

模拟题, 没有算法, 就是考写代码的细节处理

第一种

class Solution:
    def fullJustify(self, words, maxWidth: int) :
        
        def printLine(words, i, j, maxWidth): #将当前行单词format, 注意当前行单词包括了[i,j]
            if i == j: #如果只有一个单词, 那么直接返回
                return words[i] + ' ' * (maxWidth - len(words[i]))
            
            total = 0
            for idx in range(i, j + 1):
                total += len(words[idx])
            space = (maxWidth - total) // max(1, j - i)
            extra = maxWidth - total - space * (j - i)
            out = ''
            for idx in range(i, i + extra):
                out += words[idx] + ' ' * (space + 1)
            for idx in range(i + extra, j):
                out += words[idx] + ' ' * (space)
            
            out += words[j]
            return out
         #分配单词
        ans = []
        i = 0
        
        while i < len(words):
            cnt = 0
            j = i
            while j < len(words) and cnt <= maxWidth:
                if cnt == 0:
                    cnt += len(words[j])
                else:
                    cnt += len(words[j]) + 1
                j += 1
            
            j -= 1 #这个是减掉 已经违例后又加的那个j
            if cnt > maxWidth: #如果还是大于, 则需要减掉导致违例的那个词
                cnt -= 1 + len(words[j])
                j -= 1
            
            if j == len(words) - 1:
                tmp = ''
                for idx in range(i, j + 1):
                    tmp += words[idx] + ' '
                tmp = tmp[:-1]
                tmp += ' ' * (maxWidth - len(tmp))
                ans.append(tmp)
            else:
                ans.append(printLine(words, i, j, maxWidth))
            i = j + 1
        
        return ans
		
		
		
第二种, 明显优雅的多


class Solution:
    def fullJustify(self, words, maxWidth: int) :
        
        def justifySingleLine(line, width, max_width):
            num_words = len(line)
            total_spaces = max_width - width
            if num_words == 1:
                # if there is only word in line
                # just insert total_spaces for the remainder of line
                return line[0] + ' ' * total_spaces
            else:
                locations = num_words - 1
                # spaces_inserted[i] is the number of spaces inserted between the words line[i] and line[i+1]
                spaces_inserted = locations * [total_spaces // locations]
                # distribute the remaining spaces to the left positions
                for i in range(total_spaces % locations):
                    spaces_inserted[i] += 1
                s = ''
                for i in range(locations):
                    s += line[i] # add the word line[i]
                    s += spaces_inserted[i] * ' '# insert spaces
                s += line[-1] # add the last word
                return s

        answer = []
        line, width = [], 0
        for word in words:
            if width + len(word) + len(line) <= maxWidth: 
				#这里这个+ len(line) 非常精巧, 意思是如果想要加word 这个词, 就需要len(line) 这么多空格
                # keep adding words until we can fill out maxWidth
                # width = sum of length of all words
                # len(word) = length of current word
                # len(line) = least number of spaces needed to be inserted
                line.append(word)
                width += len(word)
            else:
                # justify the line and add it to result
                answer.append(justifySingleLine(line, width, maxWidth))
                # reset new line and new width
                line, width = [word], len(word)
        remaining_spaces = maxWidth - width - len(line)
        answer.append(' '.join(line) + (remaining_spaces + 1) * ' ')
        return answer