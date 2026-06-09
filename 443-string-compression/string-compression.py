"""
return only the length of the compressed array

groups that are longer than 10 will be split into 2 multiple characters

ok so we just get the latest, ake a count, convert the count to string, append each character, and return len, ez

ok so how do we do it in place, I can think of how replacing but removing... well the input is fairly small so we can just remove everythjing after a given pointer
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1: return 1
        latest = chars[0]
        count = 1
        n = len(chars)

        pointer = 0
        for i in range(1, n):
            c = chars[i]

            if c != latest:
                chars[pointer] = latest
                pointer +=1
                if count > 1:
                    strcount = str(count)
                    for countchar in strcount:
                        chars[pointer] = countchar 
                        pointer +=1
                latest = c
                count = 1

            else:
                count+=1
            
        if chars[-1] == latest:
            chars[pointer] = latest
            pointer +=1
            if count > 1:
                strcount = str(count)
                for countchar in strcount:
                    chars[pointer] = countchar 
                    pointer +=1
            latest = c
            count = 1

        remove = len(chars) - pointer 
        for i in range(remove):
            chars.pop()
        return len(chars)
        