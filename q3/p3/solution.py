from math import log, ceil
# So my immediate thought is that this is a dynamic programming
# problem. However, there is one issue here - dynamic programming
# relies specifically on subproblems. This problem, however, relies
# both on subproblems (removing one and dividing in half), and also
# on super-problems (adding one). This means that a general approach
# simply will not work.

# I did have one idea of using dynamic programming in which I would divide
# the problem into two parts:
#   - first we assume we can only either remove 1 or divide by half.
#   - then we would focus on being able to add 1

# I spent a lot of time working on the dynamic programming solution, eventually
# realizing a flaw in my solution. When I first ran into the errors and failed tests,
# I had thought my solution was correct, so I thought maybe there was something wrong
# with the test cases. Of course, that is almost never the answer, so I instead redid
# everything from scratch and tried again, which led me to a different pattern.

# I started writing out some sample solutions and noticed a pattern. If we modulo
# the input by 4, we see the following patterns depending on the remainder:
#
#   remainer | pattern
#          0 | Just divide by 2 and recurse on subproblem
#          1 | Subtract 1 and recurse on subproblem
#          2 | Just divide by 2 and recurse on subproblem
#          3 | Add 1 and recurse on superproblem
#
# What's interesting about numbers with a remainder of 3 is for most numbers,
# subtracting 1 and recursing is equally efficient - however, if the number above
# is a power of 2, then adding 1 is better. (subtracting 1 will never be a power of 2
# because only multiples of 4 can be powers of 2, except for 2, which is why
# this rule doesn't apply to n = 3).

# This makes sense. If a number can be divided in half (remainder 0/2),
# then it will always require at least 2 additions or subtractions to be
# brought to another even number (possible power of 2). That means that
# dividing in half will always be better or as good at getting you to 
# another even number (either dividing in half gets you to an even number,
# or dividing in half brings you to an odd number and you just need one more
# step to go to an even number).

# If a number has a remainder of 1 or 3, it can't be divided in half.
# We simply need to bring it to an even number then. If the remainder is 1,
# we need to subtract 1 to get to an even number (no sense in going up).
# If the remainder is 3, then we add 1 to get to an even number.

# This time complexity is then much better, looking at O(log n) instead of the
# O(n) from before. Space complexity is also now much better, being O(1).

def solution(n):
    """Calculates the minimum operations to turn a positive integer to 1
    using only +1, -1, or // 2 (only if even) operations.
    
    Args:
        n (int): The starting number.
        
    Returns:
        int: The minimum steps required to turn n into 1 using above operations.
    """
    n = int(n)
    operations = 0
        
    while n > 1:
        # Rule doesn't work for 3, so put check here.
        if n == 3:
            operations += 2
            break
            
        remainder = n % 4
        if remainder == 0 or remainder == 2:
            n //= 2
        else:
            n += -1 if remainder == 1 else 1
            
        operations += 1
        
    return operations

print(solution(input("> ")))
