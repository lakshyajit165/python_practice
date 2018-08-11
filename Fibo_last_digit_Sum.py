# Uses python3
def fibonacci_last_digit_sum(n):
    sum_, a, b = 0, 0, 1
    for _ in range(n):
        a, b = b, (a + b)
        sum_ = (sum_ + b)
    return sum_

n = int(input())
print(fibonacci_last_digit_sum(n))