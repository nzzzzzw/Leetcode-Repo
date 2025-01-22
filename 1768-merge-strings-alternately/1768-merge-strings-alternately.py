class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        j = 0
        merged = [] 
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged.append(word1[i])
                i = i + 1
            if j < len(word2):
                merged.append(word2[j])
                j = j + 1

        return "".join(merged)
        