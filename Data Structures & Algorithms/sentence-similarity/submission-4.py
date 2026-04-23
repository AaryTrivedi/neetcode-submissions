class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        if len(sentence1) == 1:
            return sentence1[0] == sentence2[0]

        wordSimilarityLookup = defaultdict(set)
        for pair in similarPairs:
            wordSimilarityLookup[pair[0]].add(pair[1])
            wordSimilarityLookup[pair[1]].add(pair[0])
        
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i] or sentence2[i] in wordSimilarityLookup[sentence1[i]]:
                continue
            return False

        return True