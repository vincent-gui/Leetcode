题目: 设计一个calender
接受一串(start, end), 当没有overlap 的时候返回true, 否则返回false

怎样判定两个interval 是否有交集 (x1, y1), (x2, y2) 

max(x1, x2) < min(y1, y2) true 说明有overlap





class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect_left(self.intervals, (start, end))  #这里用bisect_left 找到idx
        is_left_valid = idx == 0 or self.intervals[idx - 1][1] <= start #判定和前一个interval是否有交集
        is_right_valid = idx == len(self.intervals) or end <= self.intervals[idx][0] #判定和后一个interval是否有交集
        
        if is_left_valid and is_right_valid:
            self.intervals.insert(idx, (start, end))
            return True
        return False