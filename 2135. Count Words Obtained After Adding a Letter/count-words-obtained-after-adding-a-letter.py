'''
Sort = sort the string in alphabetic order
O(n^2 * l)
1. Create letter sets for all words
2. Lopp targetwords, search s_word with len-1 in startwords, and check if their diff for set is 1.
(Since every ch is unique is every  word)
or 
O(n*26) 
1. Store frozenset of every s_word in startWords to all_set.
2. For sorted t_word in targetWords, check if frozenset(tword[0:i] + tword[i+1:]) (remove ith letter) is in all_set.
'''
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        '''
        Note that every ch in the word is unique, so len(set(word)) == len(word)
        '''
        all_set = set()
        for sw in startWords:
            all_set.add(frozenset(sw))

        count = 0
        for tw in targetWords:
            for i in range(len(tw)):
                if frozenset(tw[0:i] + tw[i+1:]) in all_set:
                    count += 1
                    break

        return count 
            
        