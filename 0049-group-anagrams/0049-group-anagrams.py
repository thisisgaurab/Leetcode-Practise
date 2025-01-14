from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for word in strs:
            lst = ''.join(sorted(word))
            dict[lst].append(word)

        return list(dict.values())
            
        