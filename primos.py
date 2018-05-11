def get_prime_numbers(max_number):
    numbers = [True, True] + [True] * (max_number-1)
    last_prime_number = 2
    i = last_prime_number
    
    while last_prime_number**2 <= max_number:
        i += last_prime_number
        while i <= max_number:
            numbers[i] = False
            i += last_prime_number
        j = last_prime_number + 1
        while j < max_number:
            if numbers[j]:
                last_prime_number = j
                break
            j += 1
        i = last_prime_number
    
    return [i + 2 for i, not_crossed in enumerate(numbers[2:]) if not_crossed]
if __name__ == "__main__":
    import timeit
    print("Python", timeit.timeit("get_prime_numbers(20)", number=100000, globals=globals()))
    from cprime import get_prime_numbers as get_prime_numbers_fast
    print("Cython", timeit.timeit("get_prime_numbers_fast(20)", number=100000, globals=globals()))
