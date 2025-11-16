// Stack vs Queue in Rust
// Demonstrates Rust's type system and standard library collections

use std::collections::{VecDeque, LinkedList};

// Generic Stack implementation
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
}

// Generic Queue implementation
struct Queue<T> {
    items: VecDeque<T>,
}

impl<T> Queue<T> {
    fn new() -> Self {
        Queue { items: VecDeque::new() }
    }
    
    fn enqueue(&mut self, item: T) {
        self.items.push_back(item);
    }
    
    fn dequeue(&mut self) -> Option<T> {
        self.items.pop_front()
    }
    
    fn is_empty(&self) -> bool {
        self.items.is_empty()
    }
}

fn demo_basic_operations() {
    println!("=== Basic Operations Comparison ===\n");
    
    let mut stack = Stack::new();
    let mut queue = Queue::new();
    
    let input = vec!['A', 'B', 'C', 'D', 'E'];
    println!("Input sequence: {:?}\n", input);
    
    println!("--- Filling STACK (LIFO) ---");
    for &ch in &input {
        stack.push(ch);
        println!("  PUSH '{}' → Stack", ch);
    }
    
    println!("\n--- Filling QUEUE (FIFO) ---");
    for &ch in &input {
        queue.enqueue(ch);
        println!("  ENQUEUE '{}' → Queue", ch);
    }
    
    println!("\n--- Emptying STACK (Last In, First Out) ---");
    print!("Output: ");
    while !stack.is_empty() {
        if let Some(ch) = stack.pop() {
            print!("{} ", ch);
        }
    }
    println!();
    
    println!("\n--- Emptying QUEUE (First In, First Out) ---");
    print!("Output: ");
    while !queue.is_empty() {
        if let Some(ch) = queue.dequeue() {
            print!("{} ", ch);
        }
    }
    println!();
}

fn demo_standard_collections() {
    println!("\n{}", "=".repeat(60));
    println!("RUST STANDARD LIBRARY COLLECTIONS");
    println!("{}", "=".repeat(60));
    
    println!("\n1. Vec<T> as Stack:");
    let mut vec_stack = Vec::new();
    vec_stack.push(1);
    vec_stack.push(2);
    vec_stack.push(3);
    println!("  Stack: {:?}", vec_stack);
    println!("  Pop: {:?}", vec_stack.pop());
    println!("  Remaining: {:?}", vec_stack);
    
    println!("\n2. VecDeque<T> for Queue:");
    let mut deque_queue = VecDeque::new();
    deque_queue.push_back(1);
    deque_queue.push_back(2);
    deque_queue.push_back(3);
    println!("  Queue: {:?}", deque_queue);
    println!("  Dequeue: {:?}", deque_queue.pop_front());
    println!("  Remaining: {:?}", deque_queue);
    
    println!("\n3. LinkedList<T> (also works):");
    let mut list = LinkedList::new();
    list.push_back(10);
    list.push_back(20);
    println!("  List: {:?}", list);
    println!("  Front: {:?}, Back: {:?}", list.front(), list.back());
    
    println!("\n4. Performance characteristics:");
    println!("  Vec<T>:      push/pop at end    - O(1) amortized");
    println!("  VecDeque<T>: push/pop at either - O(1) amortized");
    println!("  LinkedList:  push/pop anywhere  - O(1)");
}

fn demonstrate_ownership_with_collections() {
    println!("\n{}", "=".repeat(60));
    println!("OWNERSHIP WITH COLLECTIONS");
    println!("{}", "=".repeat(60));
    
    println!("\n1. Stack owns its elements:");
    let mut stack = Stack::new();
    let s = String::from("Hello");
    stack.push(s);  // s moved into stack
    // Can't use s here anymore!
    println!("  String moved into stack");
    
    println!("\n2. Pop returns ownership:");
    if let Some(owned_string) = stack.pop() {
        println!("  Got ownership back: {}", owned_string);
        println!("  Can now use or drop the String");
    }
    
    println!("\n3. Borrowing elements:");
    let vec = vec![1, 2, 3];
    if let Some(&last) = vec.last() {  // Immutable borrow
        println!("  Borrowed last element: {}", last);
    }
    println!("  vec still valid: {:?}", vec);
    
    println!("\n4. No dangling pointers:");
    println!("  Compiler prevents returning references");
    println!("  to elements that would be dropped!");
}

fn demonstrate_pattern_matching() {
    println!("\n{}", "=".repeat(60));
    println!("PATTERN MATCHING WITH OPTION<T>");
    println!("{}", "=".repeat(60));
    
    let mut stack = Stack::new();
    
    println!("\n1. Matching on empty stack:");
    match stack.pop() {
        Some(value) => println!("  Got value: {}", value),
        None => println!("  Stack is empty - safe!"),
    }
    
    stack.push(42);
    
    println!("\n2. Matching with value:");
    match stack.pop() {
        Some(value) => println!("  Got value: {}", value),
        None => println!("  Stack is empty"),
    }
    
    println!("\n3. Using if let:");
    stack.push(99);
    if let Some(val) = stack.pop() {
        println!("  Popped: {}", val);
    }
    
    println!("\n4. Using while let:");
    stack.push(1);
    stack.push(2);
    stack.push(3);
    println!("  Popping all:");
    while let Some(val) = stack.pop() {
        println!("    {}", val);
    }
}

// Practical example: Expression evaluation
fn evaluate_rpn(expression: &str) -> Result<i32, String> {
    let mut stack = Vec::new();
    
    for token in expression.split_whitespace() {
        match token {
            "+" => {
                let b = stack.pop().ok_or("Stack underflow")?;
                let a = stack.pop().ok_or("Stack underflow")?;
                stack.push(a + b);
            }
            "-" => {
                let b = stack.pop().ok_or("Stack underflow")?;
                let a = stack.pop().ok_or("Stack underflow")?;
                stack.push(a - b);
            }
            "*" => {
                let b = stack.pop().ok_or("Stack underflow")?;
                let a = stack.pop().ok_or("Stack underflow")?;
                stack.push(a * b);
            }
            num => {
                let value = num.parse()
                    .map_err(|_| format!("Invalid number: {}", num))?;
                stack.push(value);
            }
        }
    }
    
    if stack.len() == 1 {
        Ok(stack[0])
    } else {
        Err(format!("Invalid expression: {} values remain", stack.len()))
    }
}

fn demo_rpn_calculator() {
    println!("\n{}", "=".repeat(60));
    println!("PRACTICAL EXAMPLE: RPN CALCULATOR");
    println!("{}", "=".repeat(60));
    
    let expressions = vec![
        "3 4 +",           // 7
        "15 7 1 1 + - *",  // 75
        "5 3 * 2 +",       // 17
    ];
    
    for expr in expressions {
        match evaluate_rpn(expr) {
            Ok(result) => println!("  {} = {}", expr, result),
            Err(e) => println!("  {} → Error: {}", expr, e),
        }
    }
    
    println!("\nRPN (Reverse Polish Notation) uses a stack:");
    println!("  • Numbers pushed to stack");
    println!("  • Operators pop operands, push result");
    println!("  • Perfect stack application!");
}

fn main() {
    println!("╔═══════════════════════════════════════════════════════════╗");
    println!("║    Rust Stack vs Queue - Type Safety & Collections       ║");
    println!("╚═══════════════════════════════════════════════════════════╝\n");
    
    demo_basic_operations();
    demo_standard_collections();
    demonstrate_ownership_with_collections();
    demonstrate_pattern_matching();
    demo_rpn_calculator();
    
    println!("\n{}", "=".repeat(60));
    println!("KEY RUST INSIGHTS:");
    println!("{}", "=".repeat(60));
    println!("• Generic types work with any T");
    println!("• Option<T> = no null pointer errors");
    println!("• Pattern matching = exhaustive, safe");
    println!("• Collections optimized for different use cases");
    println!("• Ownership prevents use-after-free");
    println!("• Result<T, E> for error handling");
    println!("• Zero-cost abstractions throughout");
    println!("{}", "=".repeat(60));
}
