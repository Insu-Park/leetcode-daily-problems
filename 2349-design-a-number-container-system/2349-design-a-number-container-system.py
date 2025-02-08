class NumberContainers:

    def __init__(self):
        self.mp = {}
        self.idx = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.mp[index] = number
        heappush(self.idx[number], index)
        

    def find(self, number: int) -> int:
        if number not in self.idx:
            return -1
        while self.idx[number]:
            i = self.idx[number][0]
            if self.mp[i] == number:
                return i
            heappop(self.idx[number])
        return -1
        