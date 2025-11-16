#!/usr/bin/env python3
"""
Stack-based Hello World - Turing's Bury/Unbury in Python
High-level demonstration showing Python's approach to stacks
"""

def stack_hello_simple():
    """Simple demonstration using Python list as stack"""
    stack = []  # Python list = dynamic array with stack operations
    message = "Hello World!"
    
    print("BURYING (pushing to stack):")
    for char in message:
        stack.append(char)  # append = push
        print(f"  Push '{char}' → Stack: {stack}")
    
    print("\nUNBURYING (popping from stack):")
    result = []
    while stack:
        char = stack.pop()  # pop = built-in!
        print(f"  Pop  '{char}' ← Stack: {stack if stack else '(empty)'}")
        result.append(char)
    
    print(f"\nReversed order: {''.join(result)}")
    print(f"Original order: {''.join(reversed(result))}")


def stack_hello_explicit():
    """More explicit demonstration with custom Stack class"""
    
    class Stack:
        def __init__(self):
            self.items = []
        
        def push(self, item):
            self.items.append(item)
        
        def pop(self):
            if not self.is_empty():
                return self.items.pop()
            return None
        
        def is_empty(self):
            return len(self.items) == 0
        
        def size(self):
            return len(self.items)
        
        def peek(self):
            if not self.is_empty():
                return self.items[-1]
            return None
        
        def __str__(self):
            return str(self.items)
    
    print("\n" + "="*60)
    print("EXPLICIT STACK CLASS DEMONSTRATION")
    print("="*60)
    
    stack = Stack()
    message = "Hello World!"
    
    print(f"\nPushing '{message}' character by character:")
    for i, char in enumerate(message, 1):
        stack.push(char)
        print(f"  {i:2}. Push '{char}' → Stack size: {stack.size()}, Top: '{stack.peek()}'")
    
    print(f"\n Current stack: {stack}")
    
    print("\nPopping all characters:")
    buffer = []
    count = 1
    while not stack.is_empty():
        char = stack.pop()
        buffer.append(char)
        top = stack.peek()
        print(f"  {count:2}. Pop  '{char}' → Stack size: {stack.size()}, " +
              f"Top: '{top if top else 'None'}'")
        count += 1
    
    print(f"\nFinal result (reversed): {''.join(buffer)}")
    print(f"Corrected: {''.join(reversed(buffer))}")


def demonstrate_python_features():
    """Show Python-specific stack features"""
    print("\n" + "="*60)
    print("PYTHON-SPECIFIC FEATURES")
    print("="*60)
    
    # Using collections.deque for efficient stack
    from collections import deque
    
    print("\n1. Using collections.deque (optimized for stack/queue):")
    stack = deque()
    for char in "ABC":
        stack.append(char)
        print(f"   Pushed '{char}' → {list(stack)}")
    
    while stack:
        print(f"   Popped '{stack.pop()}' ← {list(stack) if stack else '(empty)'}")
    
    # List slicing
    print("\n2. Python list slicing (no explicit loop needed):")
    message = "Hello World!"
    print(f"   Original: {message}")
    print(f"   Reversed: {message[::-1]}")
    
    # List comprehension
    print("\n3. List comprehension for stack operations:")
    chars = list("Hello")
    print(f"   Original: {chars}")
    reversed_chars = [chars.pop() for _ in range(len(chars.copy()))]
    print(f"   After pops: {reversed_chars}")
    
    # Context manager could be used for stack-based resource management
    print("\n4. Stack-based resource management (context managers):")
    print("   with open('file') as f:")
    print("       # File handle pushed onto resource stack")
    print("       # Automatically popped/closed on exit")


if __name__ == "__main__":
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║  Python Stack Operations - High-Level Abstraction Demo   ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    
    stack_hello_simple()
    stack_hello_explicit()
    demonstrate_python_features()
    
    print("\n" + "="*60)
    print("KEY PYTHON INSIGHTS:")
    print("="*60)
    print("• Lists have built-in push (append) and pop operations")
    print("• No manual memory management needed")
    print("• Dynamic typing - stack can hold any type")
    print("• Multiple ways to reverse: [::-1], reversed(), manual pop")
    print("• collections.deque more efficient for frequent push/pop")
    print("• Stack concept used in language itself (call stack, 'with')")
    print("="*60)
