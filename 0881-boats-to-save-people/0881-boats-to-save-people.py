class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        answer = 0
        c = Counter(people)
        s = sorted(set(people))
        i = len(s) - 1
        while i >= 0:
            if c[s[i]] > 0:
                c[s[i]] -= 1
                t = i
                weight = limit - s[i]
                while weight > 0:
                    if weight in c and c[weight] > 0:
                        c[weight] -= 1
                        break
                    weight -= 1
                answer += 1
            else:
                i -= 1

        return answer
                