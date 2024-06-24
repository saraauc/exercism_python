def find_pythagorean_triplets(N):
    triplets = []
    for a in range(1, N // 3):
        for b in range(a + 1, N // 2):
            c = N - a - b
            if c > b and a**2 + b**2 == c**2:
                triplets.append([a, b, c])
    return triplets
