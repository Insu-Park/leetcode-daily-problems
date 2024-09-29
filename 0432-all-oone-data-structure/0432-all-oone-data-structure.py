class AllOne:

    def __init__(self):
        self.dic = defaultdict(int)
        self.key_pair = []

    def inc(self, key: str) -> None:
        self.dic[key] += 1

    def dec(self, key: str) -> None:
        if key in self.dic:
            self.dic[key] -= 1
            if self.dic[key] == 0:
                self.dic.pop(key)
        
    def getMaxKey(self) -> str:
        if not self.dic:
            return ""
        maxVal = max(self.dic.values())
        for key in self.dic.keys():
            if self.dic[key] == maxVal:
                return key

    def getMinKey(self) -> str:
        if not self.dic:
            return ""
        minVal = min(self.dic.values())
        for key in self.dic.keys():
            if self.dic[key] == minVal:
                return key
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()