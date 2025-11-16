/*
 * Simpler Stack Hello World - Direct demonstration
 * Push characters, pop into buffer, then print
 */

#include <stdio.h>

int main() {
    // We'll use the actual C stack (automatic variables)
    char stack[20];
    int sp = 0;  // stack pointer
    
    // BURY: Push each character
    char *msg = "Hello World!";
    for (int i = 0; msg[i]; i++) {
        stack[sp++] = msg[i];
    }
    
    // Buffer is REQUIRED to collect the popped characters
    char buffer[20];
    int bp = 0;  // buffer pointer
    
    // UNBURY: Pop from stack (LIFO order - comes out reversed!)
    while (sp > 0) {
        buffer[bp++] = stack[--sp];
    }
    buffer[bp] = '\0';
    
    printf("Reversed: %s\n", buffer);
    
    // To print correctly, we'd need to either:
    // 1. Push in reverse order, or
    // 2. Reverse the buffer after popping
    
    // Let's reverse the buffer:
    for (int i = 0; i < bp / 2; i++) {
        char temp = buffer[i];
        buffer[i] = buffer[bp - 1 - i];
        buffer[bp - 1 - i] = temp;
    }
    
    printf("Corrected: %s\n", buffer);
    
    return 0;
}
