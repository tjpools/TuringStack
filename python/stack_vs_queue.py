#!/usr/bin/env python3
"""
Stack vs Queue in Python
Using collections.deque and built-in features
"""

from collections import deque
from queue import LifoQueue, Queue as FifoQueue


def demo_basic_operations():
    """Compare stack and queue operations"""
    print("=== Basic Operations Comparison ===\n")
    
    # Using lists (less efficient but simple)
    stack = []
    queue = deque()  # deque is optimized for both ends
    
    input_data = ['A', 'B', 'C', 'D', 'E']
    print(f"Input sequence: {input_data}\n")
    
    print("--- Filling STACK (LIFO) using list ---")
    for item in input_data:
        stack.append(item)
        print(f"  PUSH '{item}' → Stack: {stack}")
    
    print("\n--- Filling QUEUE (FIFO) using deque ---")
    for item in input_data:
        queue.append(item)
        print(f"  ENQUEUE '{item}' → Queue: {list(queue)}")
    
    print("\n--- Emptying STACK (Last In, First Out) ---")
    print("Output: ", end="")
    while stack:
        item = stack.pop()
        print(item, end=" ")
    print()
    
    print("\n--- Emptying QUEUE (First In, First Out) ---")
    print("Output: ", end="")
    while queue:
        item = queue.popleft()  # Remove from front
        print(item, end=" ")
    print()


def demo_thread_safe_versions():
    """Show Python's thread-safe queue implementations"""
    print("\n" + "="*60)
    print("THREAD-SAFE VERSIONS (queue module)")
    print("="*60)
    
    # LIFO Queue (Stack)
    print("\n--- LifoQueue (thread-safe stack) ---")
    stack = LifoQueue()
    
    for item in ['X', 'Y', 'Z']:
        stack.put(item)
        print(f"  Put '{item}' → Size: {stack.qsize()}")
    
    print("  Getting items (LIFO):")
    while not stack.empty():
        item = stack.get()
        print(f"    Got '{item}'")
    
    # FIFO Queue
    print("\n--- Queue (thread-safe FIFO) ---")
    queue = FifoQueue()
    
    for item in ['X', 'Y', 'Z']:
        queue.put(item)
        print(f"  Put '{item}' → Size: {queue.qsize()}")
    
    print("  Getting items (FIFO):")
    while not queue.empty():
        item = queue.get()
        print(f"    Got '{item}'")


def demo_pythonic_patterns():
    """Show Python-specific stack/queue patterns"""
    print("\n" + "="*60)
    print("PYTHONIC PATTERNS")
    print("="*60)
    
    # Stack using list comprehension
    print("\n1. Reversing with stack pattern:")
    text = "Hello"
    stack = list(text)
    reversed_text = ''.join([stack.pop() for _ in range(len(stack.copy()))])
    print(f"   Original: {text}")
    print(f"   Reversed: {reversed_text}")
    
    # Using reversed() - no stack needed!
    print("\n2. Python's built-in reversed():")
    print(f"   reversed('{text}') = {''.join(reversed(text))}")
    print("   (No explicit stack required!)")
    
    # Deque for efficient operations
    print("\n3. collections.deque - O(1) at both ends:")
    d = deque(['middle'])
    d.appendleft('left')   # Add to left
    d.append('right')       # Add to right
    print(f"   After operations: {list(d)}")
    print(f"   Pop left: {d.popleft()}")
    print(f"   Pop right: {d.pop()}")
    print(f"   Remaining: {list(d)}")


def demo_practical_examples():
    """Real-world examples"""
    print("\n" + "="*60)
    print("PRACTICAL EXAMPLES")
    print("="*60)
    
    # 1. Undo/Redo with stacks
    print("\n1. Undo/Redo System (two stacks):")
    
    class UndoRedo:
        def __init__(self):
            self.undo_stack = []
            self.redo_stack = []
        
        def do_action(self, action):
            self.undo_stack.append(action)
            self.redo_stack.clear()  # New action clears redo
            print(f"   Action: {action}")
        
        def undo(self):
            if self.undo_stack:
                action = self.undo_stack.pop()
                self.redo_stack.append(action)
                print(f"   Undo: {action}")
                return action
            print("   Nothing to undo")
        
        def redo(self):
            if self.redo_stack:
                action = self.redo_stack.pop()
                self.undo_stack.append(action)
                print(f"   Redo: {action}")
                return action
            print("   Nothing to redo")
    
    editor = UndoRedo()
    editor.do_action("Type 'Hello'")
    editor.do_action("Type ' World'")
    editor.do_action("Delete ' World'")
    editor.undo()
    editor.undo()
    editor.redo()
    
    # 2. BFS with queue
    print("\n2. Graph Breadth-First Search (queue):")
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [], 'E': [], 'F': []
    }
    
    def bfs(graph, start):
        visited = set()
        queue = deque([start])
        order = []
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                order.append(node)
                print(f"   Visiting: {node}, Queue: {list(queue)}")
                queue.extend(graph[node])
        
        return order
    
    print(f"   Graph: {graph}")
    result = bfs(graph, 'A')
    print(f"   BFS order: {' → '.join(result)}")
    
    # 3. DFS with stack
    print("\n3. Graph Depth-First Search (stack):")
    
    def dfs(graph, start):
        visited = set()
        stack = [start]
        order = []
        
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                print(f"   Visiting: {node}, Stack: {stack}")
                stack.extend(reversed(graph[node]))  # Reverse for left-to-right
        
        return order
    
    result = dfs(graph, 'A')
    print(f"   DFS order: {' → '.join(result)}")


if __name__ == "__main__":
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║       Python Stack vs Queue - Pythonic Approaches        ║")
    print("╚═══════════════════════════════════════════════════════════╝\n")
    
    demo_basic_operations()
    demo_thread_safe_versions()
    demo_pythonic_patterns()
    demo_practical_examples()
    
    print("\n" + "="*60)
    print("KEY PYTHON INSIGHTS:")
    print("="*60)
    print("• list.append()/pop() = simple stack")
    print("• collections.deque = efficient for both ends (O(1))")
    print("• queue module = thread-safe versions")
    print("• Built-in reversed() = no manual stack needed")
    print("• List comprehensions = concise stack operations")
    print("• Duck typing = same interface, different implementations")
    print("="*60)
