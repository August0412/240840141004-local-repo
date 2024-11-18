def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Specify the number of terms
num_terms = 10
fibonacci_series(num_terms)