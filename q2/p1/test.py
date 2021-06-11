from solution import solution

fib_cache = [0, 1]
def get_next_fib():
    global fib_cache
    val = fib_cache[-1] + fib_cache[-2]
    fib_cache.append(val)
    return val

def fib_checker(n):
    total = 1
    used = [0, 1]

    while total <= n:
        val = get_next_fib()
        total += val
        used.append(val)

    return (used[1:-1], sum(used[1:-1]))

def twos(n):
    cache = [1]
    total = 1

    if n == 1:
        return (cache, sum(cache))
    elif n == 2:
        return ([1, 1], 2)

    while total <= n:
        total += cache[-1] * 2
        cache.append(cache[-1] * 2)

    total -= cache[-1]
    cache = cache[:-1]

    if n - total > cache[-1] + cache[-2]:
        cache.append(n - total)
    
    return (cache, sum(cache))

if True:
    n = int(input("> "))
    generous = twos(n)
    print("Generous:")
    print(generous)
    print(f"Paid: {len(generous[0])}\nLeftover: {n - generous[1]}")

    print()

    stingy = fib_checker(n)
    print("Stingy:")
    print(stingy)
    print(f"Paid: {len(stingy[0])}\nLeftover: {n - stingy[1]}")
else:
    for n in range(1, 1000000000):
        fib_cache = [0, 1]
        generous = len(twos(n)[0])
        stingy = len(fib_checker(n)[0])


        if stingy - generous != solution(n):
            print(n)
