# The approach for this solution is fairly straightforward given
# the rule that a number is divisible by 3 if the sum of its digits is
# divisible by 3.

# The idea is that we should pick as many numbers as we can, but
# if we are forced into a situation such that we can only pick one number
# or another, we pick the larger.

# The former rule means that we will pick every number divisible by
# 3 from the input.

# For the latter, we need to sort the remaining elements in descending order (so that
# we prioritize larger numbers). Then we look at the elements % 3. The numbers
# can be divided into 2 categories - either the remainder is 1 or the remainder is 2.

# Numbers with a remainder of 2 can either be paired with a number with a remainder of 1
# or two other numbers with a remainder of 2. Numbers with a remainder of 1 can either be
# paired with a number with a remainder of 2 or two other numbers with a remainder of 1.
# Since we want to pick as many numbers as possible, then the general idea is that we
# prioritize triplets, and then focus on the pairs.

def solution(l):
    """Given a list of numbers, returns the largest number divisible by 3 that uses
    those digits.
    
    Args:
        l (list of int): The list of usable digits.
        
    Returns:
        int: The largest number divisible by 3.
    """
    answer = []
    other_nums = []
    for n in l:
        (answer if n % 3 == 0 else other_nums).append(n)
    
    # We want to pick the biggest number pairs from other_nums first.
    other_nums.sort(reverse=True)
    
    # Partition non-multiples of 3 into two lists by remainder.
    ones = []
    twos = []
    for n in other_nums:
        (ones if n % 3 == 1 else twos).append(n)

    # Pick triplets from both lists first.
    for ls in [ones, twos]:
        while len(ls) >= 3:
            answer += ls[:3]
            del ls[:3]
    
    # Then create 1-2 pairings.
    answer += [n for l in list(map(list, zip(ones, twos))) for n in l]
    
    # Sort answer to get biggest number.
    answer.sort()
    total = 0
    for exp, digit in enumerate(answer):
        total += digit * 10 ** exp
        
    return total


print(solution(map(int, input("> ").split(" "))))
