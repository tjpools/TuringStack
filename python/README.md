# Python Stack Operations

High-level demonstrations of stack concepts using Python's expressive syntax and built-in features.

## Programs

- `stack_hello.py` - Basic stack operations with visualization
- `stack_frames.py` - Call stack introspection with inspect module
- `fibonacci.py` - Multiple approaches including memoization
- `stack_vs_queue.py` - LIFO vs FIFO with practical examples
- `stack_overflow.py` - Recursion limits and safety

## Running

```bash
# Make executable
chmod +x *.py run_all.sh

# Run individual programs
./stack_hello.py
./stack_frames.py
./fibonacci.py
./stack_vs_queue.py
./stack_overflow.py

# Or run all at once
./run_all.sh
```

## What Python Teaches

### Higher Abstraction
- No manual memory management
- Built-in stack operations (`list.append()`, `list.pop()`)
- Dynamic typing
- Automatic safety (RecursionError)

### Pythonic Features
- **@lru_cache** - automatic memoization
- **inspect** module - runtime stack introspection
- **generators** - lazy evaluation
- **collections.deque** - efficient double-ended operations
- **queue** module - thread-safe implementations

### Safety by Default
- `sys.getrecursionlimit()` prevents stack overflow
- RecursionError exception instead of segfault
- No buffer overflows
- Automatic memory management

## Key Differences from C/Assembly

| Feature | C/Assembly | Python |
|---------|-----------|---------|
| Stack ops | Manual `push`/`pop` | `list.append()`/`pop()` |
| Memory | Manual management | Automatic GC |
| Safety | Segfaults possible | Exceptions raised |
| Recursion limit | System stack size | `sys.getrecursionlimit()` |
| Optimization | Tail call possible | No TCO |
| Introspection | Debugger only | `inspect` module |

## Learning Value

Python shows:
- **What** the algorithm does (high-level view)
- How abstractions hide complexity
- Multiple ways to solve the same problem
- Safety mechanisms in modern languages
- Functional programming approaches

Compare with C to see how high-level features are implemented!
