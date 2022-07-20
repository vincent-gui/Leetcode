
题目: 给了一串字母, 有重复, 问移除重复的字母, 并且尽可能保证字母序列从小到大

一开始想到的是用一个字点track 每个字母多少个, 然后如果没有就保留, 如果还有就skip, 但是这个并不能保证字典序

下一步就是考虑到能不能用从a 扫描到z , 然后对于每个字母, 找他前面所有字母的最大的idx(并且比当前idx 小) , 但是这个handle 不了 'zabc' 这种情况

然后最后就是考虑一个stack, 字母序递增, 字母已经在stack里, 就不需要了, 如果不在就要靠stack 最后一项的字母序是不是大于当前字母, 如果是, 最后一个字母在后边还有没有出现,如果也出现了, 就可以把stack[-1] 弹出


time: O(n)
space:O(n)
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = defaultdict(int)
        for letter in s:
            d[letter] += 1
            
        stack = []
        seen = set()
        for letter in s:
            d[letter] -= 1
            if letter in seen:
                continue
            while stack and ord(stack[-1]) > ord(letter) and d[stack[-1]] > 0: #判断是否大于curr的字母, 并且,后面还会出现stack[-1] 这个字母
                seen.remove(stack[-1])
                stack.pop()
            stack.append(letter)
            seen.add(letter)
        
        return ''.join(stack)
		
	
优化就是并不需要记录每个字母的数量, 只需要记录每个字母最后一位在哪就可以了	
time: O(n)
space:O(1)		
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = defaultdict(int)
        for i, letter in enumerate(s):
            d[letter] = i
            
        stack = []
        seen = set()
        for i, letter in enumerate(s):
            if letter in seen:
                continue
            while stack and ord(stack[-1]) > ord(letter) and d[stack[-1]] > i:
                seen.remove(stack[-1])
                stack.pop()
            stack.append(letter)
            seen.add(letter)
        
        return ''.join(stack)