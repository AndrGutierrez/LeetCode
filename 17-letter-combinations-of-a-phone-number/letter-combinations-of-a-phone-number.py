"""
backtracking,

return all possible letter combinations
answer in any order. 1 does not map to any letters, but we will not get 1 so.., the amount of digits is from 3 to 4

so 23 all the possible combinations between the set of a b c and d e f but only one at a time, se might have to brute force this

so... but cant i do like a hashmap and then... no doesnt work for more than 2 numbers it seems

    build("", 0)

def build(string, index):
    letters = letters_map[numbers[index]]
    for letter in letters:
        string+=letter
        build(string, index + 1)

    if index == len(numbers):
        res.append(string)
        return
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, sol= [], []
        letters_map = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        def build(string, index):
            if index == len(digits):
                res.append(string)
                return

            number = int(digits[index])

            letters = letters_map[number]

            for letter in letters:
                build(string+letter, index + 1)

        build("", 0)
        return res