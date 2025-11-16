# Stack Operations Quick Reference

## 🎯 Start Here

**Complete Beginner?** Run these in order:
```bash
make test-basic       # See basic push/pop operations
./stack_hello_c       # Most visual demonstration
./stack_vs_queue_c    # Understand LIFO vs FIFO
```

**Want to understand function calls?**
```bash
./stack_frames_c      # See how functions use the stack
```

**Want to understand recursion?**
```bash
./fibonacci_c         # See recursive stack growth
```

---

## 📋 Program Guide

| Program | What It Shows | Best For |
|---------|--------------|----------|
| `stack_hello_c` | Basic push/pop with visualization | **START HERE** |
| `stack_hello_byte.asm` | Hardware stack in assembly | Learning assembly |
| `stack_frames_c` | How function calls work | Understanding call stack |
| `fibonacci_c` | Recursive stack growth | Understanding recursion |
| `stack_overflow_c` | Stack limits and safety | Defensive programming |
| `stack_vs_queue_c` | LIFO vs FIFO comparison | Data structure choice |

---

## 🔑 Key Concepts

### Stack = LIFO (Last In, First Out)
```
Push A → [A]
Push B → [A, B]
Push C → [A, B, C]
Pop    → C (returns [A, B])
Pop    → B (returns [A])
Pop    → A (returns [])
```

### Queue = FIFO (First In, First Out)
```
Enqueue A → [A]
Enqueue B → [A, B]
Enqueue C → [A, B, C]
Dequeue   → A (returns [B, C])
Dequeue   → B (returns [C])
Dequeue   → C (returns [])
```

---

## 💡 When to Use Each

### Use STACK for:
- Function call management ✓
- Undo/Redo operations ✓
- Expression evaluation ✓
- Backtracking algorithms ✓
- Depth-First Search (DFS) ✓

### Use QUEUE for:
- Task scheduling ✓
- Print job spooling ✓
- Breadth-First Search (BFS) ✓
- Message passing ✓
- Event handling ✓

---

## 🛠️ Build Commands

```bash
make              # Build everything
make basic        # Build basic demos only
make advanced     # Build advanced demos only
make clean        # Clean build artifacts
make help         # Show all options
```

## 🧪 Test Commands

```bash
make test            # Run all tests
make test-basic      # Basic operations
make test-advanced   # Advanced concepts
make test-frames     # Function call demo
make test-fib        # Recursion demo
make test-overflow   # Stack limits demo
make test-queue      # Stack vs queue demo
```

---

## 📊 What Each Test Shows

### Basic Tests
- **Assembly versions**: Raw hardware stack operations
- **C with visualization**: See each push/pop happen
- **Simple C**: Why buffer is needed

### Advanced Tests
- **Stack frames**: How nested functions work
- **Fibonacci**: Recursive call tree visualization
- **Stack overflow**: What happens at the limits
- **Stack vs queue**: When to use each structure

---

## 🎓 Learning Path

### Level 1: Basics (30 minutes)
1. Read main README.md introduction
2. Run `./stack_hello_c`
3. Read the code in `stack_hello.c`
4. Run `./stack_vs_queue_c`

### Level 2: Understanding (1 hour)
1. Run `./stack_frames_c` - see function calls
2. Read `stack_frames.c` code
3. Run `./fibonacci_c` - see recursion
4. Read `fibonacci.c` code

### Level 3: Mastery (2+ hours)
1. Study `stack_hello_byte.asm` - assembly implementation
2. Run `./stack_overflow_c` - understand limits
3. Modify programs to experiment
4. Write your own stack-based programs

---

## 🔬 Experiments to Try

1. **Modify fibonacci.c** - add memoization to make it fast
2. **Write RPN calculator** - use stack for postfix expressions
3. **Implement undo/redo** - use two stacks
4. **Create maze solver** - use stack for backtracking
5. **Build expression evaluator** - convert infix to postfix

---

## 🐛 Common Issues

**"Segmentation fault"**
- You hit stack limit (see stack_overflow.c)
- Infinite recursion with no base case
- Stack frame too large

**"Stack smashing detected"**
- Buffer overflow protection triggered
- Writing past array bounds
- Stack canary corrupted

**"Stack pointer shows (nil)"**
- This is actually the optimizer being clever
- Stack pointer approximation in our demos
- Real SP is managed by hardware

---

## 📚 More Resources

- Full documentation: `README.md`
- Build system: `Makefile`
- All source code in this directory

---

## 🚀 Next Steps

After completing this masterclass, you should understand:
- ✓ How stacks work (LIFO)
- ✓ How function calls use the stack
- ✓ How recursion builds up stack frames
- ✓ Stack vs queue differences
- ✓ When to use each data structure
- ✓ Stack limitations and safety

**Ready to level up?** Look into:
- Stack-based virtual machines (JVM, CLR)
- Call stack in debuggers (GDB)
- Stack protection mechanisms (canaries, ASLR)
- Continuation-passing style
- Tail call optimization

---

*Happy learning! 🎉*
