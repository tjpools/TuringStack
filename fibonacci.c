/*
 * Recursive Fibonacci with Stack Visualization
 * Shows how recursive calls build up stack frames
 * Demonstrates why recursion uses so much stack space
 */

#include <stdio.h>
#include <string.h>

static int call_depth = 0;
static int max_depth = 0;

// Print indentation based on call depth
void print_indent() {
    for (int i = 0; i < call_depth; i++) {
        printf("  ");
    }
}

// Recursive fibonacci with visualization
int fib_recursive(int n) {
    call_depth++;
    if (call_depth > max_depth) {
        max_depth = call_depth;
    }
    
    print_indent();
    printf("→ fib(%d) called [depth=%d]\n", n, call_depth);
    
    int result;
    
    // Base cases
    if (n <= 1) {
        print_indent();
        printf("← fib(%d) = %d [BASE CASE]\n", n, n);
        call_depth--;
        return n;
    }
    
    // Recursive case
    print_indent();
    printf("  Computing fib(%d-1) + fib(%d-2)...\n", n, n);
    
    int fib1 = fib_recursive(n - 1);
    int fib2 = fib_recursive(n - 2);
    
    result = fib1 + fib2;
    
    print_indent();
    printf("← fib(%d) = %d + %d = %d\n", n, fib1, fib2, result);
    
    call_depth--;
    return result;
}

// Iterative fibonacci (no recursion, minimal stack usage)
int fib_iterative(int n) {
    if (n <= 1) return n;
    
    int prev2 = 0;
    int prev1 = 1;
    int current;
    
    printf("\nIterative calculation:\n");
    printf("  fib(0) = 0\n");
    printf("  fib(1) = 1\n");
    
    for (int i = 2; i <= n; i++) {
        current = prev1 + prev2;
        printf("  fib(%d) = %d + %d = %d\n", i, prev1, prev2, current);
        prev2 = prev1;
        prev1 = current;
    }
    
    return prev1;
}

// Count how many calls are made
int count_calls = 0;

int fib_count(int n) {
    count_calls++;
    if (n <= 1) return n;
    return fib_count(n - 1) + fib_count(n - 2);
}

void analyze_complexity(int n) {
    count_calls = 0;
    int result = fib_count(n);
    printf("\n=== Complexity Analysis for fib(%d) ===\n", n);
    printf("  Result: %d\n", result);
    printf("  Number of function calls: %d\n", count_calls);
    printf("  Maximum stack depth: ~%d frames\n", n);
    printf("  Time complexity: O(2^n) - exponential!\n");
    printf("  Space complexity: O(n) - due to call stack depth\n");
}

int main() {
    printf("=== Recursive Fibonacci with Stack Visualization ===\n\n");
    
    int n = 5;
    printf("Computing fib(%d) recursively:\n", n);
    printf("(Each indentation level = one stack frame deeper)\n\n");
    
    call_depth = 0;
    max_depth = 0;
    int result = fib_recursive(n);
    
    printf("\n=== Results ===\n");
    printf("  fib(%d) = %d\n", n, result);
    printf("  Maximum stack depth reached: %d frames\n", max_depth);
    
    printf("\n=== Compare with Iterative Approach ===\n");
    int result_iter = fib_iterative(n);
    printf("  Result: %d (same as recursive)\n", result_iter);
    printf("  Stack depth: 1 frame (constant!)\n");
    printf("  Much more efficient!\n");
    
    analyze_complexity(n);
    
    printf("\n=== Why Recursion Uses More Stack ===\n");
    printf("• Each recursive call creates a new stack frame\n");
    printf("• Frame contains: return address, parameters, local vars\n");
    printf("• All frames stay on stack until base case is reached\n");
    printf("• Then frames are popped as functions return\n");
    printf("• Fibonacci is especially inefficient - recalculates values\n");
    
    printf("\n=== Watch Out! ===\n");
    printf("Try fib(40) recursively: ~2.7 BILLION function calls!\n");
    printf("Try fib(40) iteratively: only 40 iterations\n");
    printf("This is why dynamic programming and memoization exist.\n");
    
    return 0;
}
