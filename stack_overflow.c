/*
 * Stack Overflow Demonstration
 * Shows what happens when we exceed available stack space
 * 
 * Two versions:
 * 1. Controlled - we detect and handle stack limits
 * 2. Uncontrolled - classic stack overflow (commented out for safety)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SAFE_LIMIT 10000

// Controlled recursion with depth tracking
int controlled_recursion(int depth, int limit) {
    char buffer[1024];  // 1KB per call - stack grows quickly!
    
    // Fill buffer to ensure it's actually allocated
    memset(buffer, 'A', sizeof(buffer));
    
    printf("Depth: %5d | Stack growing... (buffer at %p)\n", depth, (void*)buffer);
    
    if (depth >= limit) {
        printf("\n✓ Reached safe limit of %d calls\n", limit);
        printf("  Approximate stack usage: %d KB\n", limit);
        return depth;
    }
    
    return controlled_recursion(depth + 1, limit);
}

// Shows memory addresses getting lower (stack grows down)
void show_stack_direction() {
    int a, b, c;
    printf("\nStack Growth Direction:\n");
    printf("  Variable 'a' at: %p\n", (void*)&a);
    printf("  Variable 'b' at: %p\n", (void*)&b);
    printf("  Variable 'c' at: %p\n", (void*)&c);
    
    if ((void*)&c < (void*)&a) {
        printf("  → Stack grows DOWNWARD (toward lower addresses)\n");
    } else {
        printf("  → Stack grows UPWARD (toward higher addresses)\n");
    }
}

// WARNING: This will crash! Uncomment at your own risk
/*
void dangerous_recursion(int depth) {
    char buffer[1024];
    memset(buffer, 'X', sizeof(buffer));
    printf("Depth: %d\n", depth);
    dangerous_recursion(depth + 1);  // NO LIMIT - will crash!
}
*/

int main() {
    printf("=== Stack Overflow Demonstration ===\n\n");
    
    show_stack_direction();
    
    printf("\n--- Controlled Recursion ---\n");
    printf("Each call allocates ~1KB on stack\n");
    printf("Limit set to %d calls\n\n", SAFE_LIMIT);
    
    int final_depth = controlled_recursion(1, SAFE_LIMIT);
    
    printf("\n✓ Successfully returned from depth %d\n", final_depth);
    printf("\nNote: Actual stack overflow would cause a segmentation fault.\n");
    printf("Default stack size on Linux is typically 8MB.\n");
    
    printf("\n--- DANGEROUS (commented out) ---\n");
    printf("The dangerous_recursion() function has no limit.\n");
    printf("It would continue until:\n");
    printf("  1. Stack pointer hits guard page\n");
    printf("  2. Kernel sends SIGSEGV\n");
    printf("  3. Program crashes with 'Segmentation fault'\n");
    
    return 0;
}
