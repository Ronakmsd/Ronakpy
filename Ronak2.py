def prime_factorization(n):
    factors = {}
    
    # Check for number of 2s that divide n
    while n % 2 == 0:
        if 2 in factors:
            factors[2] += 1
        else:
            factors[2] = 1
        n //= 2

    # n must be odd at this point, check for odd factors from 3 onwards
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i

    # This condition is to check if n is a prime number greater than 2
    if n > 2:
        factors[n] = 1

    return list(factors.items())

# Example usage:
result = prime_factorization(60)
print(result)  # Output: [(2, 2), (3, 1), (5, 1)]