def find_gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

values = raw_input().strip().split(' ')

print find_gcd(int(values[0]), int(values[1]))
