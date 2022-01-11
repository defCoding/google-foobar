import math
# My first attempt will be to solve the answer for a few small inputs to see
# if there is a pattern between input and output values.

# As I was writing out some answers, I noticed a pattern pretty quickly. This is
# a dynamic programming problem. For a given input n, you will use anywhere from
# [n - 1, ceil(n / 2)] steps on the tallest step. We'll call that amount t. Then you
# can use the solution for the subproblem of n - t sum up the number from all of the
# subproblems.

# We do not go further than ceil(n / 2) because you will end up with steps with the same height.

# So the above assumptions were incorrect after I looked at this some more.
# You do not necesssarily stop at ceil(n / 2) - for example, with an n = 15,
# I could have the first step be 7 steps (less than ceil(n / 2)), and then
# use 8 bricks for the remaining steps. However, there is a caveat in that
# I cannot use more than 6 bricks on the first step of 8. So it's like a
# subproblem of the subproblem.

# In that case, I can make a 2D cache such that the rows represent the
# total number of bricks, and the columns represent the max amount that 
# can be used on the first step.

# For dynamic programming, it's always important that you explicitly
# state what the value in each cell represents. If a value l is stored
# in cell [n][m], that means that given n bricks and a constraint that
# the tallest step can have AT MOST m bricks, there are l different
# ways you can make that staircase.

# Note, that means that for some arbitrary cell [n][m] such that
# m > n, there is 1 staircase you can make. This is for the situation
# where you are permitted to use all of the bricks for that step
# (e.g. it is not the only step). For example, if you have a total
# of 10 bricks and you spend 6 of them on the first step, then the
# next step can use up all 4 remaining bricks.

# Cell [0, 0] represents the subproblem of 0 total bricks and a maximum
# of 0 brick on the first step. Of course, this isn't ever going to be an
# input, but it makes calculations a bit simpler.

# Number of ways to make staircase with AT MOST first_step
# bricks on first step is equal to number of ways using
# first_step on first step + number of ways using
# AT MOST first_step - 1 on first step.

# If you use up first_step amount of bricks on first step, you have
# total_bricks - first_step bricks remaining, and can also only use up to
# first_step - 1 steps on the subproblem since you cannot have two steps at
# the same height.

# Once first_step == total_bricks, we simply borrow from the left cell and add 1
# (since you can now use all bricks on the step) and then just copy that into all
# remaining cells in the row.
def solution(n):
    """Calculates the total amount of staircases that can be designed using n bricks,
    assuming that there must be at least 2 steps, and that each step must be shorter
    than the previous step.
    
    Args:
        n (int): The total number of bricks.
        
    Returns:
        int: The total number of staircases that can be designed.
    """
    # Fill in some known values.
    cache = [[1 if 0 < j < 3 else 0 for i in range(n + 1)] for j in range(n + 1)] 
    cache[1][0] = 0
    cache[2][:2] = [0, 0]

    # start filling up cache from total_bricks = 3 onwards
    for total_bricks in range(3, n + 1):
        # no point in starting at 0 so starting at 1 to avoid
        # index out of bounds checks.
        for first_step in range(1, total_bricks):
            cache[total_bricks][first_step] += cache[total_bricks][first_step - 1]
            cache[total_bricks][first_step] += cache[total_bricks - first_step][first_step - 1]
            
        cache[total_bricks][total_bricks:] = [cache[total_bricks][total_bricks - 1] + 1 for i in range(n - total_bricks + 1)]

    # Return value stored in cache - remember that we can only use up to n - 1 bricks on first step.
    return cache[n][n - 1]
