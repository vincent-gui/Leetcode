题目: 一个数组里有多个string,  求模板相同的数组放在一起('ab','bc') ('ace' , 'fhj')

解法: 把每个string 转换成'a' 开头的. 放进dict


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = {} # to save all convert words
        for item in strings:
            new_item = self.convert(item)
            d[new_item] = d.get(new_item, []) + [item]
        
        return d.values()
        
    def convert(self, letters):
        diff = ord(letters[0]) - ord('a')
        out = ''

        for letter in letters:
            new_letter = chr((ord(letter) - diff + 26) % 26)
            out += new_letter
        return out