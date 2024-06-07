class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: 
            return False

        count = Counter(hand)
        sorted_keys = sorted(count)

        for key in sorted_keys:
            if count[key] > 0:
                start_val_count = count[key]
                for i in range(groupSize):
                    if count[key + i] < start_val_count:
                        return False
                    count[key + i] -= start_val_count

        return True