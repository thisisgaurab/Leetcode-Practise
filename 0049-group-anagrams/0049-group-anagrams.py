from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for word in strs:
            counter = [0]*26
            for char in word:
                counter[ord(char) - ord('a')] += 1
            counter = tuple(counter)
            dict[counter].append(word)

        return list(dict.values())
        