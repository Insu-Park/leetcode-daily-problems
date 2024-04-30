class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = 0
        n = len(word)
        
        # Iterate through all possible substrings
        for i in range(n):
            freq = [0] * 10
            for j in range(i, n):
                # Update the frequency of each character in the substring
                freq[ord(word[j]) - ord('a')] += 1
                
                # Check if the substring is wonderful
                odd_count = 0
                for f in freq:
                    if f % 2 != 0:
                        odd_count += 1
                if odd_count <= 1:
                    count += 1
        
        return count