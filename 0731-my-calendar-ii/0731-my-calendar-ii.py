class MyCalendarTwo:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        tmp = 0
        for s, e in self.bookings:
            if start < e and end > s:
                new_start = max(s, start)
                new_end = min(e, end)
                
                overlap = 0
                for s, e in self.bookings:
                    if new_start < e and new_end > s:
                        overlap += 1
                        if overlap == 2:
                            return False

        self.bookings.append((start, end))        
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)