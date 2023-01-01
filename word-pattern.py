class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        match = {}
        martchReverse = {}
        words = s.split(" ")

        if len(pattern) != len(words):
            return False
        
        for c,w in zip(pattern, words):
            if c in match and match[c] != w:
                return False
            
            if w in martchReverse and martchReverse[w] != c:
                return False
            match[c] = w
            martchReverse[w] = c
        return True 