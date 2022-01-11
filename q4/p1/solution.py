from itertools import combinations
# This was an incredibly difficult problem to tackle.
# I spent the first few days trying to look for patterns between
# the input values and the output.

# It was immediately obvious to me that with n total bunnies
# and m required bunnies, there would have to be n - m + 1 duplicates
# of each key. The idea is that you need to force the picking of a key,
# and m bunnies must be picked, then we can force it by having only
# m - 1 bunnies not have that key. If m - 1 bunnies do not have that key,
# then n - (m - 1) bunnies have that key.

# However, the total number of keys I must use was not immediately obvious.
# In the previous questions, I was able to come up with a series of output
# for various inputs. However, for this particular problem, I wasn't able to
# come up with answers for some of the inputs, which made it difficult for me
# to determine the pattern.

# I decided to spend a week mulling over the problem and was finally able to come
# up with a solution that didn't require me to have multiple answers first. The
# hint was in my notes above - "if m - 1 bunnies do not have that key, then
# n - (m - 1) bunnies have that key". This means that for every group of
# m - 1 bunnies, all other bunnies have a key that the group doesn't have.

# There are n choose (m - 1) groups of bunnies, so that means there is an 
# equivalent amount of distinct keys.

# With this epiphany, I was able to start working on my solution.
# At first, my solution was a bit naive. First I would calculate every
# combination of m - 1 groups of bunnies. Then for every group, I would
# add a key to all other bunnies not in that group. Then I would move on 
# to the next group and do the same, but with a new key.

# However, this solution is a bit slow, as I would have to find bunnies not
# in the group, which would take extra calculations. Fortunately, the intuition
# here isn't too bad. I just simply have to do the reverse. For every m - 1 group
# of bunnies, there is a corresponding n - m + 1 group of bunnies. In other words,
# I can instead calculate all the groupings of n - m + 1 groups of bunnies, and
# assign all of the ones in the group a key, and then do the same for the next
# group with a new key.

def solution(num_buns, num_required):
    """Calculates the required distribution of keys to some number
    of bunnies such that a specific amount of bunnies must be picked
    in order to have all the keys.
    
    Args:
        num_buns (int): The total number of bunnies.
        num_required (int): The required number of bunnies to have all keys.
        
    Returns:
        list of list of int: The distribution of keys to each bunny.
    """
    dups = num_buns - num_required + 1
    total_keys = choose(num_buns, num_required - 1)
    bunnies = range(num_buns)
    distribution = [[] for i in bunnies]
    
    for key, grouping in enumerate(combinations(bunnies, num_buns - num_required + 1)):
        for bunny in grouping:
            distribution[bunny].append(key)
            
    return distribution
	
def choose(n, r):
    """Calculates the number of ways there are to pick r unique
    items from n total items.
    
    Args:
        n (int): The total number of items.
        r (int): The number of items to pick.
        
    Returns:
        int: The total number of ways to pick r items.
    """
    return factorial(n, r) // factorial(n - r)
    
def factorial(n, stop=0):
    """Calculates the factorial of a number, stopping at an optional
    stopping point.
    
    Args:
        n (int): The number to factorial.
        stop (int): The number to stop multiplication at if desired.
        
    Returns:
        int: The factorial of n, stopping at stop.
    """
    return 1 if n == stop else n * factorial(n - 1, stop)
    
print(solution(*list(map(int, input("> ").split(" ")))))
