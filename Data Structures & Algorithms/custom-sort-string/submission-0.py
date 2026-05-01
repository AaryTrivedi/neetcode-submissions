class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderMap = {}
        sMap = {}
        for i in range(len(order)):
            orderMap[order[i]] = i
        
        for i in range(len(s)):
            sMap[s[i]] = i
        
        s = list(s)
        oLen = len(order)
        sortedS = sorted(s, key=lambda x: orderMap.get(x, oLen + 1 + sMap.get(x)))

        return ''.join(sortedS)