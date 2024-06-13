def sieve_of_eratosthenes(limit):
    # Create a boolean array "prime[0..limit]" and initialize all entries as True.
    # A value in prime[i] will be False if i is not a prime, True if i is a prime.
    prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        # If prime[p] is not changed, then it is a prime
        if prime[p] == True:
            # Updating all multiples of p to not prime
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1

    # Collecting all prime numbers
    prime_numbers = [p for p in range(2, limit + 1) if prime[p]]
    return prime_numbers

# Example usage
limit = 50
print(f"Prime numbers up to {limit}: {sieve_of_eratosthenes(limit)}")
