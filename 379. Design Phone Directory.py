class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.d = set(range(maxNumbers))
            

    def get(self) -> int:
        return self.d.pop() if self.d else -1
        
        

    def check(self, number: int) -> bool:
        return number in self.d
        

    def release(self, number: int) -> None:
        self.d.add(number)
        