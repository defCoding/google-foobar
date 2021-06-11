# The initial solution that comes to mind is to use something like
# inspired by the Sieve of Eratosthenes to speed up the process of
# calculating primes.

# However, the main issue with this is that it assumes that the optimal solution
# is one in which in order to calculate the 5 digits starting from the nth index,
# you need to calculate all of the digits in the string up until the nth index. I'm
# not quite sure if that's a correct assumption - if there is some way to determine
# which prime number I would be starting at, then that would be more ideal.

# Thinking about it some more, I don't think it's possible for me to determine which
# prime number I should be starting at. It would be similar to being able to quickly
# determine the nth prime, which can't be done in linear or constant time.

# Fortunately, the nature of this problem is similar to the Sieve of Eratosthenes
# in that you store all primes up to the value that you are currently checking.
# The only difference is that instead of n representing upper limit of the primes
# we are calculating, the n here is the index of our string.

# The solution I have in mind then is to slowly build up Lambda's string in a manner
# that is similar to a Segmented Sieve of Eratosthenes such that each segment is just
# of size 1.
def solution(i):
    """Given a string containing all of the primes back to back, return 5 digits starting
    from index i.
    
    Args:
        i (int): The index of the string to start at.
    
    Returns:
        str: The string containing the 5 digits starting at i.
    """
    primes = [2]
    str_length = 1
    
    while str_length <= i:
        next_prime = get_next_prime(primes)
        str_length += count_digits(next_prime)
        primes.append(next_prime)

    # Start from correct digit of starting prime (i may be in the middle of the number)
    result = str(primes[-1])[-(str_length - i):str_length - i + 3]
    
    # Start generating next primes and add to result
    while len(result) < 5:
        next_prime = get_next_prime(primes)
        primes.append(next_prime)
        result += str(next_prime)[:5 - len(result)]
    
    return result
        

def get_next_prime(primes):
    """Given a list of all primes up to some number, returns the next prime number.
    
    Args:
        primes (list of int): All prime numbers up till desired limit.
    
    Returns:
        int: The next prime number that comes after `primes[-1]`.
    """
    # We test candidates by adding 2 to skip even numbers - this works
    # for all primes except for 2, so we need a check in place for that.
    num = primes[-1] if primes[-1] != 2 else 1
    
    while True:
        num += 2 # Next candidate (can skip evens)
        
        # Primes must be exactly within one of a multiple of 6
        if num != 3 and (num + 1) % 6 != 0 and (num - 1) % 6 != 0:
            continue
        # Check for primality
        is_prime = True
        for prime in primes:
            if prime * prime > num:
                break
            if not num % prime:
                is_prime = False
                break
        if is_prime:
            return num

def count_digits(n):
    """Counts the number of digits in the given number.
    
    Args:
        n (int): The number to count the digits of.
        
    Returns:
        int: The total number of digits in n.
    """
    digits = 1
    while n >= 10:
        n /= 10
        digits += 1
    return digits

def get_nth_prime(n):
    primes = [2]

    while len(primes) < n:
        primes.append(get_next_prime(primes))

    return primes[-1]

print(get_nth_prime(int(input("> "))))
