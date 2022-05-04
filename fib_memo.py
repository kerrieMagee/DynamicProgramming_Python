def fib_memo(n, memo):
    """Fibonacci with memoisation (remembering the solutions to previously computed sub-problems
    Time Complexity: Is O(n) - call to fib_memo is constant as each problem computed no more than
    once with n sub-problems
    """

    #base case
    if n <= 1:
        return n
    if memo[n] is None:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

def fib(n):
    memo = [None] * (n+1)
    return fib_memo(n, memo)

