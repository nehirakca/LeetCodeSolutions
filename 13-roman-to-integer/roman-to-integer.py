class Solution:
    def romanToInt(self, s: str) -> int:
        SymbolDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
        lastch = 1
        num = 0
        for ch in s[::-1]:
            if lastch > SymbolDict[ch]:
                num -= SymbolDict[ch]
            else:
                num += SymbolDict[ch]
                lastch = SymbolDict[ch]
        return num



        