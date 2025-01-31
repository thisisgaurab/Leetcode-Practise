from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = defaultdict(list)

        for word in strs:
            lst = [0]*26

            for char in word:
                lst[ord(char)-ord('a')] += 1

            lst = tuple(lst)

            dict[lst].append(word)

        return list(dict.values())
        
