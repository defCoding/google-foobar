from math import log
# The pattern for this one is fairly obvious -
#   - The first row will be IDs [start, start + length).
#   - Then for each column i (0-based index), there will be
#     length - i IDs in the column, with a gap of
#     length between each of the IDs.

# This one seemed a bit too straightforward, so I would like to
# see if there is a pattern I can find.

# So that solution failed, but there is another pattern
# that is separate from that previous idea. At first I was
# looking at the patterns of XORs, and I realized that
# if a number is XOR'd with itself an even amount of times,
# then the result is 0. If a number is XOR'd with itself an
# odd amount of times, then you get that number back.

# That means we can "cancel" out numbers, which helps with
# the fact that the starting ID can change. If I want the XOR
# of a range of numbers from [4, 6], I can use the XOR of all numbers
# from [1, 6] and XOR that with the range [1, 3] to cancel out
# unneeded values.

# So why is this better? We know that for each bit in position i
# starting from the least significant bit, it flips every 2^i numbers.
# This means we can calculate the XOR without having to XOR every single
# number. We just need to calculate for each bit position, if there is an
# even or odd numbers of 1s in the range [0, n].

# For every single row, we have a certain range, so we can use
# this process to calculate the XOR of each row. There are n rows, so this
# takes O(nlogn). Then we just XOR the results of our ranges.
def solution(start, length):
    """Calculates the checksum for Commander Lambda's new security checkpoint.

    Args:
        start (int): ID # of the first worker in line.
        length (int): The length of the line.

    Returns:
        int: The checksum of the line.
    """
    ret = 0
    for row in range(length):
        first = length * row + start
        last = first + length - row - 1
        ret ^= xor_range(last) ^ xor_range(first - 1)

    return ret

def xor_range(n):
    """Calculates the result of XOR'ing all integers from 0 to a given integer.

    Args:
        n (int): The inclusive end of the range to calculate the XOR of.

    Returns:
        int: The result of XOR'ing all integers from 0 to n.
    """
    if n <= 0:
        return 0

    bits = int(log(n) / log(2)) + 1
    total = 0

    for bit_pos in range(bits):
        # Check to see if there is an odd or even number of active bits at
        # position bit_pos from all numbers from 0 to n.
        if bit_pos == 0:
            is_active = (n + 1) // 2 % 2
        else:
            is_active = n // (2 ** bit_pos) % 2 and (n % (2 ** bit_pos) + 1) % 2

        if is_active:
            total += 2 ** bit_pos

    return total

ins = list(map(int, input("> ").split(" ")))
print(solution(*ins))
