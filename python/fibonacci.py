#!/usr/bin/env python3
"""
Fibonacci - Recursive vs Iterative in Python
With memoization demonstration
"""

import functools
import time


def fib_recursive_naive(n, depth=0):
    """Naive recursive fibonacci - exponential time"""
    indent = "  " * depth
    print(f"{indent}→ fib({n}) called")
    
    if n <= 1:
        print(f"{indent}← fib({n}) = {n} [BASE CASE]")
        return n
    
    result = fib_recursive_naive(n - 1, depth + 1) + fib_recursive_naive(n - 2, depth + 1)
    print(f"{indent}← fib({n}) = {result}")
    return result


def fib_iterative(n):
    """Iterative fibonacci - linear time, constant space"""
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    print(f"fib(0) = 0")
    print(f"fib(1) = 1")
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        print(f"fib({i}) = {prev1} + {prev2} = {current}")
        prev2, prev1 = prev1, current
    
    return prev1


@functools.lru_cache(maxsize=None)
def fib_memoized(n, depth=0):
    """Memoized recursive fibonacci - linear time and space"""
    indent = "  " * depth
    print(f"{indent}→ fib({n}) called")
    
    if n <= 1:
        print(f"{indent}← fib({n}) = {n} [BASE CASE]")
        return n
    
    result = fib_memoized(n - 1, depth + 1) + fib_memoized(n - 2, depth + 1)
    print(f"{indent}← fib({n}) = {result} [CACHED]")
    return result


def fib_generator():
    """Generator - produces infinite fibonacci sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def count_calls_decorator(func):
    """Decorator to count function calls"""
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


@count_calls_decorator
def fib_counted(n):
    """Fibonacci with call counting"""
    if n <= 1:
        return n
    return fib_counted(n - 1) + fib_counted(n - 2)


def benchmark_approaches(n):
    """Compare different fibonacci approaches"""
    print("\n" + "="*60)
    print(f"BENCHMARK: Computing fib({n})")
    print("="*60)
    
    # Iterative
    print("\n1. Iterative approach:")
    start = time.time()
    result_iter = fib_iterative(n) if n <= 10 else None
    elapsed_iter = time.time() - start
    if result_iter:
        print(f"   Result: {result_iter}")
    print(f"   Time: {elapsed_iter:.6f} seconds")
    print(f"   Space: O(1) - constant")
    
    # Naive recursive (only for small n)
    if n <= 10:
        print("\n2. Naive recursive approach:")
        fib_counted.calls = 0
        start = time.time()
        result_naive = fib_counted(n)
        elapsed_naive = time.time() - start
        print(f"   Result: {result_naive}")
        print(f"   Time: {elapsed_naive:.6f} seconds")
        print(f"   Calls: {fib_counted.calls}")
        print(f"   Space: O(n) - stack depth")
    
    # Memoized
    print("\n3. Memoized recursive approach:")
    fib_memoized.cache_clear()  # Clear cache
    start = time.time()
    result_memo = fib_memoized(n) if n <= 10 else None
    elapsed_memo = time.time() - start
    if result_memo:
        print(f"   Result: {result_memo}")
    cache_info = fib_memoized.cache_info()
    print(f"   Time: {elapsed_memo:.6f} seconds")
    print(f"   Cache: hits={cache_info.hits}, misses={cache_info.misses}")
    print(f"   Space: O(n) - cache + stack")
    
    # Generator
    print("\n4. Generator approach:")
    start = time.time()
    fib_gen = fib_generator()
    result_gen = None
    for i, val in enumerate(fib_gen):
        if i == n:
            result_gen = val
            break
    elapsed_gen = time.time() - start
    print(f"   Result: {result_gen}")
    print(f"   Time: {elapsed_gen:.6f} seconds")
    print(f"   Space: O(1) - generator state only")


def demonstrate_list_comprehension():
    """Show Python's functional approach"""
    print("\n" + "="*60)
    print("PYTHON FUNCTIONAL APPROACH")
    print("="*60)
    
    # Generate first 10 fibonacci numbers
    print("\nFirst 10 fibonacci numbers using generator:")
    fib_gen = fib_generator()
    first_10 = [next(fib_gen) for _ in range(10)]
    print(f"  {first_10}")
    
    # Using reduce (fold) - very functional!
    from functools import reduce
    print("\nUsing functools.reduce (like fold in functional languages):")
    print("  Computing fib(10) with reduce:")
    result = reduce(
        lambda acc, _: (acc[1], acc[0] + acc[1]),
        range(10),
        (0, 1)
    )[0]
    print(f"  Result: {result}")


if __name__ == "__main__":
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║   Python Fibonacci - Multiple Approaches & Optimization  ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    
    n = 5
    
    print("\n=== Naive Recursive (with visualization) ===")
    print(f"Computing fib({n}):")
    result = fib_recursive_naive(n)
    print(f"\nFinal result: {result}")
    
    print("\n=== Iterative Approach ===")
    result = fib_iterative(n)
    print(f"Final result: {result}")
    
    print("\n=== Memoized Recursive (much faster!) ===")
    fib_memoized.cache_clear()
    result = fib_memoized(n)
    print(f"\nFinal result: {result}")
    print(f"Cache info: {fib_memoized.cache_info()}")
    
    benchmark_approaches(10)
    demonstrate_list_comprehension()
    
    print("\n" + "="*60)
    print("KEY PYTHON INSIGHTS:")
    print("="*60)
    print("• @lru_cache decorator = automatic memoization!")
    print("• Generators = lazy evaluation, infinite sequences")
    print("• List comprehensions = concise iteration")
    print("• Multiple paradigms: imperative, functional, OO")
    print("• No manual memory management")
    print("• Much more expressive than C/assembly")
    print("="*60)
