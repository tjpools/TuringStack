# Rust Stack Operations

Modern systems programming with memory safety guarantees. Shows how Rust achieves C-like performance with high-level safety.

## Programs

- `stack_hello.rs` - Stack operations with ownership demonstration
- `fibonacci.rs` - Multiple approaches including const fn and iterators  
- `stack_vs_queue.rs` - LIFO vs FIFO with pattern matching

## Building & Running

### Prerequisites
```bash
# Install Rust if not already installed
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### Build Individual Programs
```bash
rustc stack_hello.rs -o stack_hello
rustc fibonacci.rs -o fibonacci
rustc stack_vs_queue.rs -o stack_vs_queue
```

### Or Use the Script
```bash
chmod +x build_and_run.sh
./build_and_run.sh
```

### Run Programs
```bash
./stack_hello
./fibonacci
./stack_vs_queue
```

## What Rust Teaches

### Memory Safety Without GC
- **Ownership system** - each value has one owner
- **Borrowing rules** - one mutable OR many immutable references
- **Lifetime tracking** - compiler prevents dangling pointers
- **No runtime overhead** - all checks at compile time

### Modern Features
- **Option<T>** - no null pointers
- **Result<T, E>** - error handling without exceptions
- **Pattern matching** - exhaustive, compile-time checked
- **Generics** - zero-cost abstractions
- **Iterators** - lazy, composable, optimized
- **const fn** - compile-time computation

### Type System
- Strong static typing with inference
- Algebraic data types (enums, structs)
- Trait system (like interfaces but more powerful)
- No inheritance - composition over inheritance

## Key Differences from C/Python

| Feature | C | Python | Rust |
|---------|---|---------|------|
| Memory safety | Manual | GC | Ownership |
| Null pointers | Yes | No (None) | No (Option<T>) |
| Speed | Fast | Slow | Fast |
| Error handling | Return codes | Exceptions | Result<T, E> |
| Generics | Macros | Duck typing | Zero-cost |
| Concurrency | Unsafe | GIL | Safe |

## Learning Value

Rust demonstrates:
- **How** to achieve memory safety without GC
- Modern language design principles
- Systems programming without C's dangers
- Performance with safety (not a tradeoff!)
- Compile-time vs runtime guarantees

### The "Aha!" Moment

When you understand Rust's ownership system, you realize:
- Memory bugs CAN be caught at compile time
- Performance and safety aren't mutually exclusive
- The compiler can be your ally, not enemy
- Modern systems languages can be safe

## Compilation

Rust compiles directly to machine code like C/C++:
- No interpreter
- No JIT
- No runtime (except minimal for unwinding)
- As fast as C, safer than everything else

## Error Messages

Rust is famous for helpful error messages:
```rust
error[E0382]: use of moved value: `stack1`
  --> stack_hello.rs:10:5
   |
8  |     let stack2 = stack1;
   |                  ------ value moved here
9  |     
10 |     stack1.push(42);
   |     ^^^^^^^^^^^^^^ value used here after move
```

The compiler teaches you as you learn!

## Further Exploration

- Async/await for concurrent programming
- Unsafe blocks when needed (FFI, low-level)
- Macros for code generation
- Cargo package manager
- Cross-compilation support

---

**Rust bridges the gap between C and Python - safety of high-level languages, speed of low-level languages.**
