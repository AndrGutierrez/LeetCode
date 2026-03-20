"""
why is this hard i dont want to find out

cannot use eval

only parenthesis, additioin and substraction

+ at the left is invalid, - at the left is valid

no two consecutive operators

I mean this appearsin compilers but probably i dont want to make a grammar for this

so make a queue

push item to the q,

if opens parentheses push
if number push, 
if operator  go next

can i make like substacks in the satck

well the first thing is that you might have numbers of more than 1 digit so you
cannot split each character... just split everything and then remove spaces

ok now you have your operands

1
+
1

if finished, operate

2
-
1
+
2


(
    1
    +
    (
        4
        +
        5
        +
        2
        -
        3
    )
    +
    (
        6
        +
        8
    )

if closes parentheses, pop and operate until closed parentheses, 
add that to the q
so what if

-
1
+
2

the operations have to go backwards

traverse the string backwards,
if anything that isnt a ) parentheses, pop and sum until finding the opening parentheses,
and push to the q, remove the parentheses

(
    1
    -
    2
)
(
    -2
    +
    1
)
"""
from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        q = deque()
        number = ''

        for c in reversed(s):

            if c == ' ': continue
            if c != '(' and c != '+' and c!= ')' and c!= '-':
                number= c + number
                continue 
            if number!='':
                q.append(number)
            number = ''
            if c == '(':
                item = q.pop()

                in_parentheses = 0

                while item != ')':
                    if item == '-':
                        item = q.pop()
                        q.append(-int(item))
                        # for some reason the positive is still there and cancels out just try this in the meantime
                        q.append(-int(item))

                        continue
                    if item == '+':
                        item = q.pop()
                        continue
                    # print(item)

                    in_parentheses+=int(item)
                    item = q.pop()
                q.append(in_parentheses)
            else:
                    q.append(c)
        result = 0
        if number!='':
            q.append(number)

        while q:
            item = q.pop()

            if item == '-':
                item = q.pop()
                q.append(-int(item))
                # for some reason the positive is still there and cancels out just try this in the meantime
                # q.append(-int(item))
                continue
            if item == '+':
                continue
            # print(item
            result+=int(item)
        return result