class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            if abbr[j] == word[i]:
                j += 1
                i += 1
            
            elif abbr[j].isdigit():
                if abbr[j] == '0':
                    return False

                digit = abbr[j]
                n = 1
                while (j+n) < len(abbr) and abbr[j + n].isdigit():
                    digit = digit + abbr[j + n]
                    n += 1
                j = j + n
                i = i + int(digit)
                
            else:
                return False
            
        if i == len(word) and j == len(abbr):
            return True
        else:
            return False
            


            
        
        

            