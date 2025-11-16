// Fibonacci in Rust - Multiple approaches
// Shows performance, safety, and modern features

use std::time::Instant;
use std::collections::HashMap;

// 1. Naive recursive - exponential time
fn fib_recursive_naive(n: u32, depth: usize) -> u64 {
    let indent = "  ".repeat(depth);
    println!("{}→ fib({}) called", indent, n);
    
    if n <= 1 {
        println!("{}← fib({}) = {} [BASE CASE]", indent, n, n);
        return n as u64;
    }
    
    let result = fib_recursive_naive(n - 1, depth + 1) + 
                 fib_recursive_naive(n - 2, depth + 1);
    println!("{}← fib({}) = {}", indent, n, result);
    result
}

// 2. Iterative - linear time, constant space
fn fib_iterative(n: u32) -> u64 {
    if n <= 1 {
        return n as u64;
    }
    
    let (mut prev2, mut prev1) = (0u64, 1u64);
    println!("fib(0) = 0");
    println!("fib(1) = 1");
    
    for i in 2..=n {
        let current = prev1 + prev2;
        println!("fib({}) = {} + {} = {}", i, prev1, prev2, current);
        prev2 = prev1;
        prev1 = current;
    }
    
    prev1
}

// 3. Memoized with HashMap - dynamic programming
fn fib_memoized_helper(n: u32, memo: &mut HashMap<u32, u64>, depth: usize) -> u64 {
    let indent = "  ".repeat(depth);
    
    if let Some(&result) = memo.get(&n) {
        println!("{}→ fib({}) = {} [CACHED]", indent, n, result);
        return result;
    }
    
    println!("{}→ fib({}) called", indent, n);
    
    if n <= 1 {
        println!("{}← fib({}) = {} [BASE CASE]", indent, n, n);
        memo.insert(n, n as u64);
        return n as u64;
    }
    
    let result = fib_memoized_helper(n - 1, memo, depth + 1) + 
                 fib_memoized_helper(n - 2, memo, depth + 1);
    
    println!("{}← fib({}) = {} [STORING]", indent, n, result);
    memo.insert(n, result);
    result
}

fn fib_memoized(n: u32, visualize: bool) -> u64 {
    let mut memo = HashMap::new();
    let depth = if visualize { 0 } else { 1000 };  // Hide output for large n
    fib_memoized_helper(n, &mut memo, depth)
}

// 4. Const fn - compile-time fibonacci!
const fn fib_const(n: u32) -> u64 {
    if n <= 1 {
        n as u64
    } else {
        // Can't recurse in const fn easily, so use iteration
        let mut prev2 = 0u64;
        let mut prev1 = 1u64;
        let mut i = 2u32;
        
        while i <= n {
            let current = prev1 + prev2;
            prev2 = prev1;
            prev1 = current;
            i += 1;
        }
        prev1
    }
}

// Compile-time constant!
const FIB_10: u64 = fib_const(10);

// 5. Iterator-based approach (lazy evaluation)
struct FibonacciIterator {
    prev: u64,
    curr: u64,
}

impl FibonacciIterator {
    fn new() -> Self {
        FibonacciIterator { prev: 0, curr: 1 }
    }
}

impl Iterator for FibonacciIterator {
    type Item = u64;
    
    fn next(&mut self) -> Option<Self::Item> {
        let result = self.prev;
        let next = self.prev + self.curr;
        self.prev = self.curr;
        self.curr = next;
        Some(result)
    }
}

fn benchmark_approaches(n: u32) {
    println!("\n{}", "=".repeat(60));
    println!("BENCHMARK: Computing fib({})", n);
    println!("{}", "=".repeat(60));
    
    // Iterative
    println!("\n1. Iterative:");
    let start = Instant::now();
    let result = if n <= 10 {
        fib_iterative(n)
    } else {
        let mut prev2 = 0u64;
        let mut prev1 = 1u64;
        for _ in 2..=n {
            let current = prev1 + prev2;
            prev2 = prev1;
            prev1 = current;
        }
        prev1
    };
    let duration = start.elapsed();
    println!("  Result: {}", result);
    println!("  Time: {:?}", duration);
    println!("  Space: O(1) - constant");
    
    // Memoized (no visualization for large n)
    println!("\n2. Memoized:");
    let start = Instant::now();
    let result = fib_memoized(n, false);
    let duration = start.elapsed();
    println!("  Result: {}", result);
    println!("  Time: {:?}", duration);
    println!("  Space: O(n) - memoization table");
    
    // Iterator
    println!("\n3. Iterator:");
    let start = Instant::now();
    let result = FibonacciIterator::new()
        .nth(n as usize)
        .unwrap_or(0);
    let duration = start.elapsed();
    println!("  Result: {}", result);
    println!("  Time: {:?}", duration);
    println!("  Space: O(1) - iterator state only");
    
    // Const (compile-time)
    println!("\n4. Compile-time const:");
    println!("  fib(10) computed at compile time = {}", FIB_10);
    println!("  Zero runtime cost!");
}

fn demonstrate_iterator() {
    println!("\n{}", "=".repeat(60));
    println!("RUST ITERATOR - LAZY EVALUATION");
    println!("{}", "=".repeat(60));
    
    println!("\nFirst 10 Fibonacci numbers:");
    let fibs: Vec<u64> = FibonacciIterator::new()
        .take(10)
        .collect();
    println!("  {:?}", fibs);
    
    println!("\nSum of first 10:");
    let sum: u64 = FibonacciIterator::new()
        .take(10)
        .sum();
    println!("  {}", sum);
    
    println!("\nIterators are:");
    println!("  • Zero-cost abstractions");
    println!("  • Lazily evaluated");
    println!("  • Composable with .map(), .filter(), .take(), etc.");
    println!("  • As fast as hand-written loops!");
}

fn demonstrate_ownership() {
    println!("\n{}", "=".repeat(60));
    println!("OWNERSHIP IN RECURSION");
    println!("{}", "=".repeat(60));
    
    println!("\nRust's ownership prevents common recursion bugs:");
    println!("  • No use-after-free");
    println!("  • No double-free");
    println!("  • No memory leaks (without unsafe)");
    
    println!("\nEach recursive call:");
    println!("  1. Gets its own stack frame");
    println!("  2. Owns its local variables");
    println!("  3. Cleans up automatically on return");
    println!("  4. All checked at compile time!");
}

fn main() {
    println!("╔═══════════════════════════════════════════════════════════╗");
    println!("║    Rust Fibonacci - Performance & Modern Features        ║");
    println!("╚═══════════════════════════════════════════════════════════╝\n");
    
    let n = 5u32;
    
    println!("=== Naive Recursive (with visualization) ===");
    println!("Computing fib({}):", n);
    let result = fib_recursive_naive(n, 0);
    println!("\nFinal result: {}", result);
    
    println!("\n=== Iterative Approach ===");
    let result = fib_iterative(n);
    println!("Final result: {}", result);
    
    println!("\n=== Memoized Recursive ===");
    let result = fib_memoized(n, true);
    println!("\nFinal result: {}", result);
    
    benchmark_approaches(20);
    demonstrate_iterator();
    demonstrate_ownership();
    
    println!("\n{}", "=".repeat(60));
    println!("KEY RUST INSIGHTS:");
    println!("{}", "=".repeat(60));
    println!("• const fn = compile-time computation");
    println!("• Iterators = zero-cost lazy evaluation");
    println!("• No garbage collector needed");
    println!("• Type inference makes code clean");
    println!("• Ownership prevents memory bugs");
    println!("• Performance on par with C/C++");
    println!("• Modern syntax without sacrificing speed");
    println!("{}", "=".repeat(60));
}
