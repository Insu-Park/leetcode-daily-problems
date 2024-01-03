class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = []
        for row in bank:
            tmp = row.count('1')
            if tmp != 0:
                beams.append(tmp)

        answer = 0
        for idx in range(1, len(beams)):
            answer += beams[idx] * beams[idx - 1]

        return answer