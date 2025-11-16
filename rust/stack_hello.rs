// Stack-based Hello World in Rust
// Demonstrates Rust's ownership system and memory safety

use std::fmt;

// Custom Stack implementation with generic types
struct Stack<T> {
    items: Vec<T>,
}

impl<T> Stack<T> {
    fn new() -> Self {
        Stack { items: Vec::new() }
    }
    
    fn push(&mut self, item: T) {
        self.items.push(item);
    }
    
    fn pop(&mut self) -> Option<T> {
        self.items.pop()
    }
    
    fn is_empty(&self) -> bool {
        self.items.is_empty()
    }
    
    fn size(&self) -> usize {
        self.items.len()
    }
    
    fn peek(&self) -> Option<&T> {
        self.items.last()
    }
}

impl<T: fmt::Display> Stack<T> {
    fn display(&self) {
        print!("[");
        for (i, item) in self.items.iter().enumerate() {
            if i > 0 { print!(", "); }
            print!("{}", item);
        }
        print!("]");
    }
}

fn stack_hello_basic() {
    println!("=== Basic Stack Operations ===\n");
    
    let mut stack = Stack::new();
    let message = "Hello World!";
    
    println!("BURYING (pushing to stack):");
    for ch in message.chars() {
        stack.push(ch);
        print!("  Push '{}' → Stack: ", ch);
        stack.display();
        println!();
    }
    
    println!("\nUNBURYING (popping from stack):");
    let mut buffer = Vec::new();
    while !stack.is_empty() {
        if let Some(ch) = stack.pop() {
            print!("  Pop  '{}' ← Stack: ", ch);
            if stack.is_empty() {
                print!("(empty)");
            } else {
                stack.display();
            }
            println!();
            buffer.push(ch);
        }
    }
    
    let reversed: String = buffer.iter().collect();
    let original: String = buffer.iter().rev().collect();
    
    println!("\nReversed: {}", reversed);
    println!("Original: {}", original);
}

fn demonstrate_ownership() {
    println!("\n{}", "=".repeat(60));
    println!("RUST OWNERSHIP DEMONSTRATION");
    println!("{}", "=".repeat(60));
    
    println!("\n1. Stack owns its data:");
    let mut stack1 = Stack::new();
    stack1.push(String::from("Hello"));
    stack1.push(String::from("World"));
    
    println!("  stack1 contains Strings (heap-allocated)");
    println!("  When stack1 goes out of scope, Strings are freed");
    
    println!("\n2. Moving ownership:");
    let mut stack2 = stack1;  // Ownership transferred!
    // stack1 is now invalid - can't use it!
    println!("  stack1 moved to stack2");
    println!("  Trying to use stack1 now would cause compile error");
    
    if let Some(word) = stack2.pop() {
        println!("  Popped from stack2: {}", word);
    }
    
    println!("\n3. Borrowing (immutable):");
    let stack3: Stack<i32> = Stack::new();
    let size = stack3.size();  // Immutable borrow
    println!("  Borrowed stack3 to check size: {}", size);
    println!("  stack3 still valid after borrow");
    
    println!("\n4. Borrowing (mutable):");
    let mut stack4 = Stack::new();
    stack4.push(42);  // Mutable borrow
    println!("  Mutably borrowed stack4 to push");
    println!("  Can only have ONE mutable borrow at a time!");
}

fn demonstrate_generic_stack() {
    println!("\n{}", "=".repeat(60));
    println!("GENERIC STACK - MULTIPLE TYPES");
    println!("{}", "=".repeat(60));
    
    // Stack of integers
    println!("\n1. Stack<i32>:");
    let mut int_stack = Stack::new();
    for i in 1..=5 {
        int_stack.push(i);
    }
    print!("  ");
    int_stack.display();
    println!();
    
    // Stack of strings
    println!("\n2. Stack<&str>:");
    let mut str_stack = Stack::new();
    str_stack.push("first");
    str_stack.push("second");
    str_stack.push("third");
    print!("  ");
    str_stack.display();
    println!();
    
    // Stack of tuples
    println!("\n3. Stack<(i32, &str)>:");
    let mut tuple_stack = Stack::new();
    tuple_stack.push((1, "one"));
    tuple_stack.push((2, "two"));
    println!("  Stack of tuples: size = {}", tuple_stack.size());
    
    println!("\nRust's generics are zero-cost abstractions!");
    println!("No runtime overhead like dynamic typing");
}

fn demonstrate_safety() {
    println!("\n{}", "=".repeat(60));
    println!("RUST SAFETY GUARANTEES");
    println!("{}", "=".repeat(60));
    
    println!("\n✓ No null pointers - uses Option<T>");
    let mut stack: Stack<i32> = Stack::new();
    match stack.pop() {
        Some(value) => println!("  Got: {}", value),
        None => println!("  Stack empty (None) - safe!"),
    }
    
    println!("\n✓ No buffer overflows - bounds checked");
    println!("  Vec<T> automatically resizes");
    println!("  Index access checked at runtime");
    
    println!("\n✓ No use-after-free");
    println!("  Ownership system prevents dangling pointers");
    println!("  Compiler enforces at compile time!");
    
    println!("\n✓ No data races");
    println!("  One mutable OR multiple immutable borrows");
    println!("  Enforced at compile time!");
    
    println!("\n✓ No manual memory management");
    println!("  RAII - Resource Acquisition Is Initialization");
    println!("  Automatic cleanup when out of scope");
}

fn main() {
    println!("╔═══════════════════════════════════════════════════════════╗");
    println!("║   Rust Stack Operations - Memory Safety & Ownership      ║");
    println!("╚═══════════════════════════════════════════════════════════╝\n");
    
    stack_hello_basic();
    demonstrate_ownership();
    demonstrate_generic_stack();
    demonstrate_safety();
    
    println!("\n{}", "=".repeat(60));
    println!("KEY RUST INSIGHTS:");
    println!("{}", "=".repeat(60));
    println!("• Ownership system prevents memory bugs at compile time");
    println!("• Zero-cost abstractions - as fast as C");
    println!("• Option<T> instead of null pointers");
    println!("• Generics with no runtime overhead");
    println!("• Move semantics by default (no implicit copies)");
    println!("• Borrowing rules enforced by compiler");
    println!("• Memory safety WITHOUT garbage collection");
    println!("{}", "=".repeat(60));
}
