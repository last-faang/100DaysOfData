class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        result = []

        for str in strs:
            key = ''.join(sorted(str))
            word_map[key] = word_map.get(key, []) + [str]

        for k, v in word_map.items():
            result.append(v)

        return result 
