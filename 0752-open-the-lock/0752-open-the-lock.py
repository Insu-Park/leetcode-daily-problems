class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1

        de = defaultdict(bool)
        v = defaultdict(bool)
        for deadend in deadends:
            de[deadend] = True

        q = deque([["0000", 1]])
        v["0000"] = True

        while q:
            num, tries = q.popleft()
            for idx in range(4):
                next_num = str(int(num[idx]) + 1)
                next_num = "0" if next_num == "10" else next_num
                privious_num = str(int(num[idx]) - 1)
                privious_num = "9" if privious_num == "-1" else privious_num
                new_num = num[:idx] + next_num + num[idx + 1:4]
                if new_num == target:
                    return tries
                if not v[new_num] and not de[new_num]:
                    v[new_num] = True
                    q.append([new_num, tries + 1])

                new_num = num[:idx] + privious_num + num[idx + 1:4]
                if new_num == target:
                    return tries
                if not v[new_num] and not de[new_num]:
                    v[new_num] = True
                    q.append([new_num, tries + 1])

        return -1