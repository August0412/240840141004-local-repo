def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Specify the number of terms
num_terms = 10

print("Printing Fibonacii Series. # This print statement is the modification to the code.")

fibonacci_series(num_terms)
