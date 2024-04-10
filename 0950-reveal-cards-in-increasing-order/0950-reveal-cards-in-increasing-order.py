class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        deq = deque([deck[0]])
        for d in deck[1:]:
            last = deq.pop()
            deq.appendleft(last)
            deq.appendleft(d)
        return deq