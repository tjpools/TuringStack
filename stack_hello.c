/*
 * Stack-based Hello World - Turing's Bury/Unbury Concept
 * Demonstrates pushing characters to stack, then popping to print
 * 
 * Yes, we need a buffer! The stack is ephemeral - we need to collect
 * the characters somewhere before printing them all at once.
 */

#include <stdio.h>
#include <string.h>

#define STACK_SIZE 100

// Simple stack implementation
typedef struct {
    char data[STACK_SIZE];
    int top;
} Stack;

void stack_init(Stack *s) {
    s->top = -1;
}

void stack_push(Stack *s, char c) {
    if (s->top < STACK_SIZE - 1) {
        s->data[++(s->top)] = c;
    }
}

char stack_pop(Stack *s) {
    if (s->top >= 0) {
        return s->data[(s->top)--];
    }
    return '\0';
}

int main() {
    Stack stack;
    stack_init(&stack);
    
    // BURY: Push "Hello World!" character by character
    printf("BURYING (pushing to stack):\n");
    char *message = "Hello World!";
    for (int i = 0; message[i] != '\0'; i++) {
        printf("  Pushing: '%c'\n", message[i]);
        stack_push(&stack, message[i]);
    }
    
    // Buffer needed to collect characters
    char buffer[STACK_SIZE];
    int buf_index = 0;
    
    // UNBURY: Pop from stack into buffer
    printf("\nUNBURYING (popping from stack):\n");
    while (stack.top >= 0) {
        char c = stack_pop(&stack);
        printf("  Popped: '%c'\n", c);
        buffer[buf_index++] = c;
    }
    buffer[buf_index] = '\0';  // null terminate
    
    // Print the result
    printf("\nFinal message: %s\n", buffer);
    
    return 0;
}
