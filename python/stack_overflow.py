#!/usr/bin/env python3
"""
Python Stack Recursion Limit and Safety
Demonstrates Python's protection mechanisms
"""

import sys
import resource


def demonstrate_recursion_limit():
    """Show Python's recursion limit protection"""
    print("=== PYTHON RECURSION LIMIT ===\n")
    
    current_limit = sys.getrecursionlimit()
    print(f"Current recursion limit: {current_limit}")
    print("This prevents uncontrolled stack overflow\n")
    
    # Try to exceed limit
    def infinite_recursion(depth=0):
        if depth % 100 == 0:
            print(f"  Depth: {depth}", end='\r')
        return infinite_recursion(depth + 1)
    
    print("Attempting infinite recursion...")
    try:
        infinite_recursion()
    except RecursionError as e:
        print(f"\n✓ RecursionError caught: {e}")
        print("Python prevented stack overflow!")


def safe_deep_recursion(n, limit=1000):
    """Safely demonstrate deep recursion"""
    print(f"\n=== SAFE DEEP RECURSION (limit={limit}) ===\n")
    
    call_count = [0]  # Mutable container for closure
    
    def recursive_count(depth):
        call_count[0] += 1
        if call_count[0] % 100 == 0:
            print(f"  Depth: {depth}/{limit}", end='\r')
        
        if depth >= limit:
            return depth
        return recursive_count(depth + 1)
    
    result = recursive_count(0)
    print(f"\n  Reached depth: {result}")
    print(f"  Total calls: {call_count[0]}")


def demonstrate_tail_recursion_issue():
    """Show that Python doesn't optimize tail calls"""
    print("\n=== TAIL RECURSION (Not Optimized in Python) ===\n")
    
    print("Python does NOT optimize tail calls!")
    print("This will still use O(n) stack space:\n")
    
    def factorial_tail_recursive(n, acc=1):
        """Tail recursive factorial (still uses stack in Python)"""
        if n <= 1:
            return acc
        return factorial_tail_recursive(n - 1, n * acc)
    
    # Safe version
    result = factorial_tail_recursive(5)
    print(f"  factorial(5) = {result}")
    print("\nEven though it's tail recursive, Python still")
    print("creates a new stack frame for each call.")
    print("Use iteration instead!")


def demonstrate_iterative_conversion():
    """Show converting recursion to iteration"""
    print("\n=== CONVERTING TO ITERATION ===\n")
    
    # Recursive version
    def sum_recursive(n):
        if n <= 0:
            return 0
        return n + sum_recursive(n - 1)
    
    # Iterative version
    def sum_iterative(n):
        total = 0
        for i in range(1, n + 1):
            total += i
        return total
    
    # Using Python's built-in
    def sum_pythonic(n):
        return sum(range(1, n + 1))
    
    n = 10
    print(f"Sum of 1..{n}:")
    print(f"  Recursive: {sum_recursive(n)}")
    print(f"  Iterative: {sum_iterative(n)}")
    print(f"  Pythonic:  {sum_pythonic(n)}")
    print(f"\nAll give same result, but:")
    print(f"  Recursive: O(n) stack space")
    print(f"  Iterative: O(1) stack space")
    print(f"  Pythonic:  O(1) stack space + cleaner!")


def show_stack_size():
    """Show actual stack size information"""
    print("\n=== SYSTEM STACK INFORMATION ===\n")
    
    try:
        # Get stack size on Unix systems
        soft, hard = resource.getrlimit(resource.RLIMIT_STACK)
        print(f"Stack size limits:")
        print(f"  Soft limit: {soft / (1024*1024):.1f} MB")
        print(f"  Hard limit: {'unlimited' if hard == resource.RLIM_INFINITY else f'{hard/(1024*1024):.1f} MB'}")
    except:
        print("Stack size info not available on this system")
    
    print(f"\nPython recursion limit: {sys.getrecursionlimit()}")
    print("This is much lower than system stack size")
    print("Python's own safety mechanism!")


def demonstrate_trampoline():
    """Show trampoline pattern for deep recursion"""
    print("\n=== TRAMPOLINE PATTERN (Advanced) ===\n")
    
    print("Trampoline = way to avoid deep recursion\n")
    
    class Bounce:
        """Represents a bounced (delayed) computation"""
        def __init__(self, func, *args):
            self.func = func
            self.args = args
    
    def trampoline(bouncer):
        """Execute bounced computations iteratively"""
        while isinstance(bouncer, Bounce):
            bouncer = bouncer.func(*bouncer.args)
        return bouncer
    
    def factorial_trampoline(n, acc=1):
        """Factorial using trampoline pattern"""
        if n <= 1:
            return acc
        return Bounce(factorial_trampoline, n - 1, n * acc)
    
    result = trampoline(factorial_trampoline(5))
    print(f"  factorial(5) = {result}")
    print("\nTrampoline converts recursion to iteration")
    print("But in Python, just use iteration directly!")


if __name__ == "__main__":
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║      Python Stack Safety & Recursion Protection          ║")
    print("╚═══════════════════════════════════════════════════════════╝\n")
    
    demonstrate_recursion_limit()
    safe_deep_recursion(1000)
    demonstrate_tail_recursion_issue()
    demonstrate_iterative_conversion()
    show_stack_size()
    demonstrate_trampoline()
    
    print("\n" + "="*60)
    print("KEY PYTHON INSIGHTS:")
    print("="*60)
    print("• sys.getrecursionlimit() = built-in protection")
    print("• RecursionError raised before stack overflow")
    print("• NO tail call optimization (unlike Scheme/Haskell)")
    print("• Prefer iteration over deep recursion")
    print("• Trampoline pattern available but rarely needed")
    print("• Much safer than C/assembly by default")
    print("="*60)
