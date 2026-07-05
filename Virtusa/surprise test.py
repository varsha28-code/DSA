def powers(n):
    power_set = set()
    base = 2

    while base * base <= n:
        value = base * base

        while value <= n:
            power_set.add(value)
            value *= base

        base += 1

    return n - len(power_set)

n = int(input())
print(powers(n))
