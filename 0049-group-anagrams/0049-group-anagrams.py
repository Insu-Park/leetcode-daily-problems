class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        answer = []
        def dictToStr(dt: dict) -> str:
            ret = []
            for key, value in dt.items():
                ret.append("{}{}".format(key, value))
            
            ret.sort()
            return "".join(ret)

        for s in strs:
            tmp = dictToStr(Counter(s))
            for idx, an in enumerate(anagrams):
                if an == tmp:
                    answer[idx].append(s)
                    break
            else:
                anagrams.append(tmp)
                answer.append([s])
            
        return answer