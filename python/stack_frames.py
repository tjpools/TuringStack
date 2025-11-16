#!/usr/bin/env python3
"""
Stack Frames Visualization in Python
Shows how Python's call stack works with frame introspection
"""

import sys
import inspect


def show_frame_info(label):
    """Display information about the current stack frame"""
    frame = inspect.currentframe()
    caller_frame = frame.f_back
    
    print(f"\n[{label}] Frame Information:")
    print(f"  Function: {caller_frame.f_code.co_name}")
    print(f"  Line number: {caller_frame.f_lineno}")
    print(f"  Local variables: {list(caller_frame.f_locals.keys())}")
    print(f"  Stack depth: {len(inspect.stack())}")


def function_d():
    """Deepest function in the call chain"""
    local_d = "deep"
    print("\n    [D] Executing function_d()")
    print(f"    [D] Local variable: local_d = '{local_d}'")
    show_frame_info("D")
    
    # Show full call stack
    print("\n    [D] Full call stack:")
    for i, frame_info in enumerate(inspect.stack()):
        print(f"        {i}. {frame_info.function}() at line {frame_info.lineno}")
    
    print("    [D] → About to return...")


def function_c():
    """Third level function"""
    local_c = [1, 2, 3]
    print("\n  [C] Executing function_c()")
    print(f"  [C] Local variable: local_c = {local_c}")
    print("  [C] → Calling function_d()")
    function_d()
    print("  [C] ← Returned from function_d()")


def function_b(param1, param2):
    """Second level function with parameters"""
    local_b = {"key": "value"}
    print("\n[B] Executing function_b()")
    print(f"[B] Parameters: param1={param1}, param2={param2}")
    print(f"[B] Local variable: local_b = {local_b}")
    show_frame_info("B")
    print("[B] → Calling function_c()")
    function_c()
    print("[B] ← Returned from function_c()")


def function_a():
    """First level function"""
    local_a = 42
    message = "Stack frame A"
    print("\n[A] Executing function_a()")
    print(f"[A] Local variables: local_a = {local_a}, message = '{message}'")
    show_frame_info("A")
    print("[A] → Calling function_b()")
    function_b("hello", 99)
    print("[A] ← Returned from function_b()")


def demonstrate_recursion_depth():
    """Show Python's recursion limit"""
    print("\n" + "="*60)
    print("PYTHON RECURSION LIMIT")
    print("="*60)
    
    limit = sys.getrecursionlimit()
    print(f"\nDefault recursion limit: {limit}")
    print("This is Python's stack depth protection")
    print("(Prevents stack overflow like C/assembly can have)")
    
    # Safe recursive function
    def count_down(n, max_depth=10):
        if n <= 0 or n > max_depth:
            return n
        print(f"  Depth {max_depth - n + 1}: count_down({n})")
        return count_down(n - 1, max_depth)
    
    print(f"\nSafe recursion (limited to 10 levels):")
    count_down(5)


def demonstrate_exception_stack():
    """Show how exceptions capture the call stack"""
    print("\n" + "="*60)
    print("EXCEPTION STACK TRACE")
    print("="*60)
    
    def level_3():
        raise ValueError("Intentional error to show stack trace")
    
    def level_2():
        level_3()
    
    def level_1():
        level_2()
    
    print("\nCalling level_1() → level_2() → level_3() (raises exception):")
    try:
        level_1()
    except ValueError as e:
        print(f"\nCaught exception: {e}")
        print("\nStack trace shows the call chain:")
        import traceback
        traceback.print_exc()


def demonstrate_closure_stack():
    """Show closures - functions that capture their enclosing scope"""
    print("\n" + "="*60)
    print("CLOSURES - STACK FRAMES THAT PERSIST")
    print("="*60)
    
    def make_counter(start):
        """Factory that creates counter functions"""
        count = start  # This variable captured in closure
        
        def increment():
            nonlocal count  # Reference to outer scope
            count += 1
            return count
        
        return increment
    
    print("\nCreating counter starting at 10:")
    counter = make_counter(10)
    
    print(f"  counter() = {counter()}")
    print(f"  counter() = {counter()}")
    print(f"  counter() = {counter()}")
    
    print("\nThe 'count' variable is kept alive in closure")
    print("It's like a mini-stack frame that persists!")


if __name__ == "__main__":
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║     Python Stack Frames - Call Stack Introspection       ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    
    print("\n=== Nested Function Calls ===")
    print("Watch the call stack grow and shrink:")
    function_a()
    
    demonstrate_recursion_depth()
    demonstrate_exception_stack()
    demonstrate_closure_stack()
    
    print("\n" + "="*60)
    print("KEY PYTHON INSIGHTS:")
    print("="*60)
    print("• inspect module lets you examine stack frames at runtime")
    print("• sys.getrecursionlimit() shows Python's stack protection")
    print("• Exception tracebacks capture the entire call stack")
    print("• Closures = stack frames that persist after function returns")
    print("• Much safer than C/asm - automatic bounds checking")
    print("="*60)
