def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        if n < 2:
            res = f'{n} - не простое и не сложное число'
        elif n == 2:
            res = f'{n} - Простое число'
        else:
            f = n ** (1 / 2)
            k = int(f + 1)
            for a in range(2, k):
                if n % a == 0:
                    res = f'{n} - Составное число'
                else:
                    res = f'{n} - Простое число'
        print(res)
        return n
    return wrapper

@is_prime
def sum_three(a: int, b: int, c: int):
    return a + b + c

result = sum_three(1, 2, 3)
print(result)