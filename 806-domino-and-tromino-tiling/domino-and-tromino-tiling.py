"""
return number of ways to tile in 2 x n board 

don't know what modulo means but it seems like a normal int is valid so idks

this could be a backtracking problem but....... maybe? 

so through backtracking we could probably get every different possibility, but since the input size is not so small to
be actually backtracking probably we can optimize it, maybe via dp?

it seems we can divide this into smaller subproblems well I mean we could but would that ...

seems likely but im not really sure like we solve for n = 3 and then we reuse it

well every subproblem is filled so... we cont face the case where a triomino has an empty space and then 
i can insert another tromino... no it does imply it but once we have our stuff filled we just have to add more,
the older ones are still valid,and we have to add to the remaining spaces... and since...

actually this is kind of a pattern like, is there more ways to...

we have our base case
n = 1: 1,
n = 2: 2,
n = 3: 5
but after that we just have to add what we have + base cases don't we? no...?

ok but I think we can still do this like making the subproblems and then adding the new ways we find 

how do we calculate?

we could make matrixes like this

Domino
[1 1]

Domino
[1]
[1]

Tromino
[1 1]
[1 0]

Tromino
[0 1]
[1 1]

and then for n = 4 our thing is

[0 0 0 0]
[0 0 0 0]

how do we calculate the way ... isn't there an easier way?

so our recursive solution implies just filling  with one of our 4 options, and then trying adding one of the
others, and so on and so forth until we try all possible combinations, the time complexity for this is a lot, but how can we reuse it?

well we can store all these possible combinations into an array... though the space complexity might also be large if 
we do an array of all possible matrixes... this probably should be way simpler cause it's a medium problem

well each incomplete matrix will always have like 1 remaining and that will always be fillable with a tromino... but there's also the case that I drew that can go indefinitely.. but if we build like on top of each case... the thing is
it will be always filled

also we have to return an amount, not precisely the exact combinations, how do we know how much stuff does fit?

we can do like hey max past amount and max current amount, if that were possible...

we can say hey ok so we have n stuff with this space available............

and if we can fit something there

but also there must be a certain disposition of space i give up its been an hour lets see the solution
"""
class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9+7
        if n<=2:
            return n
        f = [0] * (n + 1)
        p = [0] * (n + 1)

        f[1] = 1
        f[2] = 2
        p[2] = 1

        for k in range(3, n + 1):
            f[k] = (f[k - 1] + f[k - 2] + 2 * p[k - 1]) %mod
            p[k] = (p[k - 1] + f[k - 2]) %mod
        return f[n]