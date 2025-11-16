/*
 * Nested Function Calls - Stack Frame Visualization
 * Shows how stack frames are created and destroyed
 * Demonstrates the call stack in action
 */

#include <stdio.h>
#include <stdint.h>

// Get approximate stack pointer (architecture-dependent)
void* get_stack_pointer() {
    int stack_var;
    return (void*)&stack_var;
}

void function_d() {
    void *sp = get_stack_pointer();
    printf("    [D] Executing function_d()        SP: %p\n", sp);
    printf("    [D] → Deepest in the call stack\n");
    printf("    [D] → About to return...\n");
}

void function_c() {
    void *sp = get_stack_pointer();
    printf("  [C] Executing function_c()          SP: %p\n", sp);
    printf("  [C] → Calling function_d()\n");
    function_d();
    printf("  [C] ← Returned from function_d()\n");
}

void function_b() {
    void *sp = get_stack_pointer();
    int local_b = 42;
    printf("[B] Executing function_b()            SP: %p\n", sp);
    printf("[B] → Local variable 'local_b' = %d at %p\n", local_b, (void*)&local_b);
    printf("[B] → Calling function_c()\n");
    function_c();
    printf("[B] ← Returned from function_c()\n");
}

void function_a() {
    void *sp = get_stack_pointer();
    int local_a = 100;
    char message[] = "Stack frame A";
    printf("[A] Executing function_a()            SP: %p\n", sp);
    printf("[A] → Local variable 'local_a' = %d at %p\n", local_a, (void*)&local_a);
    printf("[A] → Local array 'message' at %p\n", (void*)message);
    printf("[A] → Calling function_b()\n");
    function_b();
    printf("[A] ← Returned from function_b()\n");
}

// Demonstrate what's in a stack frame
void show_stack_frame_details() {
    printf("\n=== Stack Frame Components ===\n");
    printf("Each function call creates a stack frame containing:\n");
    printf("  1. Return address (where to resume after function returns)\n");
    printf("  2. Saved frame pointer (previous function's base pointer)\n");
    printf("  3. Local variables\n");
    printf("  4. Function parameters (passed on stack)\n");
    printf("  5. Saved registers (if needed)\n\n");
}

// Show how parameters are passed via stack
int sum_many(int a, int b, int c, int d, int e, int f) {
    void *sp = get_stack_pointer();
    printf("sum_many() called with 6 parameters\n");
    printf("  Stack pointer: %p\n", sp);
    printf("  Parameter 'a' at: %p\n", (void*)&a);
    printf("  Parameter 'f' at: %p\n", (void*)&f);
    printf("  Parameters: %d, %d, %d, %d, %d, %d\n", a, b, c, d, e, f);
    return a + b + c + d + e + f;
}

int main() {
    void *sp_main = get_stack_pointer();
    
    printf("=== Nested Function Calls - Stack Frame Visualization ===\n\n");
    printf("Main() starts execution              SP: %p\n\n", sp_main);
    
    show_stack_frame_details();
    
    printf("=== Call Chain: main → A → B → C → D ===\n");
    printf("(Watch the stack pointer move)\n\n");
    
    function_a();
    
    printf("\n[main] ← All functions returned\n");
    printf("[main] Stack unwound back to main()\n\n");
    
    printf("=== Parameter Passing Demo ===\n");
    int result = sum_many(1, 2, 3, 4, 5, 6);
    printf("  Result: %d\n\n", result);
    
    printf("=== Key Observations ===\n");
    printf("• Stack pointer changes with each function call\n");
    printf("• Stack grows DOWNWARD (toward lower addresses)\n");
    printf("• Each function has its own isolated frame\n");
    printf("• Frames are destroyed (popped) on return\n");
    printf("• Local variables are only valid within their frame\n");
    
    return 0;
}
