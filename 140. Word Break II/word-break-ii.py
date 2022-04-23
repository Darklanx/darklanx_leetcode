class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        s_l = []
        wordDict = set(wordDict)
        @cache
        def helper(start):
            nonlocal s_l, s, wordDict     
            ans = []
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict:
                    if end == len(s):
                        ans.append(s[start:end])
                    else:
                        for next_str in helper(end):
                            ans.append(s[start:end] + " " + next_str)
                    
            return ans
            
        return helper(0)