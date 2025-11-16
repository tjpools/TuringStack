/*
 * Stack vs Queue Comparison
 * Demonstrates the difference between LIFO (stack) and FIFO (queue)
 * Shows why each data structure is useful for different problems
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

// ==================== STACK Implementation ====================

typedef struct {
    char data[MAX_SIZE];
    int top;
} Stack;

void stack_init(Stack *s) {
    s->top = -1;
}

int stack_is_empty(Stack *s) {
    return s->top == -1;
}

int stack_is_full(Stack *s) {
    return s->top == MAX_SIZE - 1;
}

void stack_push(Stack *s, char value) {
    if (!stack_is_full(s)) {
        s->data[++(s->top)] = value;
        printf("  PUSH '%c' → Stack now: ", value);
        for (int i = 0; i <= s->top; i++) {
            printf("%c ", s->data[i]);
        }
        printf("\n");
    }
}

char stack_pop(Stack *s) {
    if (!stack_is_empty(s)) {
        char value = s->data[(s->top)--];
        printf("  POP  '%c' ← Stack now: ", value);
        for (int i = 0; i <= s->top; i++) {
            printf("%c ", s->data[i]);
        }
        if (s->top == -1) printf("(empty)");
        printf("\n");
        return value;
    }
    return '\0';
}

// ==================== QUEUE Implementation ====================

typedef struct {
    char data[MAX_SIZE];
    int front;
    int rear;
    int size;
} Queue;

void queue_init(Queue *q) {
    q->front = 0;
    q->rear = -1;
    q->size = 0;
}

int queue_is_empty(Queue *q) {
    return q->size == 0;
}

int queue_is_full(Queue *q) {
    return q->size == MAX_SIZE;
}

void queue_enqueue(Queue *q, char value) {
    if (!queue_is_full(q)) {
        q->rear = (q->rear + 1) % MAX_SIZE;
        q->data[q->rear] = value;
        q->size++;
        
        printf("  ENQUEUE '%c' → Queue now: ", value);
        for (int i = 0; i < q->size; i++) {
            int idx = (q->front + i) % MAX_SIZE;
            printf("%c ", q->data[idx]);
        }
        printf("\n");
    }
}

char queue_dequeue(Queue *q) {
    if (!queue_is_empty(q)) {
        char value = q->data[q->front];
        q->front = (q->front + 1) % MAX_SIZE;
        q->size--;
        
        printf("  DEQUEUE '%c' ← Queue now: ", value);
        for (int i = 0; i < q->size; i++) {
            int idx = (q->front + i) % MAX_SIZE;
            printf("%c ", q->data[idx]);
        }
        if (q->size == 0) printf("(empty)");
        printf("\n");
        return value;
    }
    return '\0';
}

// ==================== Demonstrations ====================

void demo_basic_operations() {
    printf("=== Basic Operations Comparison ===\n\n");
    
    Stack stack;
    Queue queue;
    stack_init(&stack);
    queue_init(&queue);
    
    char *input = "ABCDE";
    
    printf("Input sequence: %s\n\n", input);
    
    // Fill both structures
    printf("--- Filling STACK (LIFO) ---\n");
    for (int i = 0; input[i]; i++) {
        stack_push(&stack, input[i]);
    }
    
    printf("\n--- Filling QUEUE (FIFO) ---\n");
    for (int i = 0; input[i]; i++) {
        queue_enqueue(&queue, input[i]);
    }
    
    // Empty both structures
    printf("\n--- Emptying STACK (Last In, First Out) ---\n");
    printf("Stack output: ");
    while (!stack_is_empty(&stack)) {
        printf("%c", stack_pop(&stack));
    }
    printf("\n");
    
    printf("\n--- Emptying QUEUE (First In, First Out) ---\n");
    printf("Queue output: ");
    while (!queue_is_empty(&queue)) {
        printf("%c", queue_dequeue(&queue));
    }
    printf("\n");
}

void demo_real_world_use_cases() {
    printf("\n\n=== Real-World Use Cases ===\n\n");
    
    printf("--- STACK Use Cases ---\n");
    printf("1. Function call stack (what we've been demonstrating!)\n");
    printf("2. Undo/Redo operations in editors\n");
    printf("3. Expression evaluation (parentheses matching)\n");
    printf("4. Backtracking algorithms (maze solving, DFS)\n");
    printf("5. Browser back button\n");
    
    printf("\n--- QUEUE Use Cases ---\n");
    printf("1. Print job spooling\n");
    printf("2. CPU task scheduling\n");
    printf("3. Breadth-First Search (BFS) in graphs\n");
    printf("4. Network packet handling\n");
    printf("5. Message queues between processes\n");
}

void demo_expression_evaluation() {
    printf("\n\n=== Stack Example: Parentheses Matching ===\n");
    
    char *expression = "(a + {b * [c - d]})";
    printf("Expression: %s\n\n", expression);
    
    Stack paren_stack;
    stack_init(&paren_stack);
    
    printf("Processing:\n");
    for (int i = 0; expression[i]; i++) {
        char ch = expression[i];
        if (ch == '(' || ch == '{' || ch == '[') {
            printf("  Found opening '%c' - pushing to stack\n", ch);
            stack_push(&paren_stack, ch);
        }
        else if (ch == ')' || ch == '}' || ch == ']') {
            char opener = stack_pop(&paren_stack);
            printf("  Found closing '%c' - matches with '%c'\n", ch, opener);
        }
    }
    
    if (stack_is_empty(&paren_stack)) {
        printf("\n✓ Expression is balanced!\n");
    } else {
        printf("\n✗ Expression is NOT balanced!\n");
    }
}

void demo_queue_simulation() {
    printf("\n\n=== Queue Example: Print Job Spooler ===\n");
    
    Queue print_queue;
    queue_init(&print_queue);
    
    printf("Simulating print jobs arriving...\n\n");
    
    char *jobs[] = {"Doc1", "Doc2", "Doc3"};
    
    for (int i = 0; i < 3; i++) {
        printf("Job '%s' submitted\n", jobs[i]);
        for (int j = 0; jobs[i][j]; j++) {
            queue_enqueue(&print_queue, jobs[i][j]);
        }
        queue_enqueue(&print_queue, '|'); // separator
    }
    
    printf("\nProcessing jobs in order received (FIFO):\n");
    printf("Printing: ");
    while (!queue_is_empty(&print_queue)) {
        char ch = queue_dequeue(&print_queue);
        if (ch == '|') {
            printf(" [DONE] ");
        } else {
            printf("%c", ch);
        }
    }
    printf("\n");
}

int main() {
    printf("╔════════════════════════════════════════════════════════╗\n");
    printf("║        STACK (LIFO) vs QUEUE (FIFO) Comparison        ║\n");
    printf("╚════════════════════════════════════════════════════════╝\n\n");
    
    demo_basic_operations();
    demo_real_world_use_cases();
    demo_expression_evaluation();
    demo_queue_simulation();
    
    printf("\n\n=== Key Differences ===\n");
    printf("┌─────────────┬──────────────────┬──────────────────┐\n");
    printf("│  Property   │      Stack       │      Queue       │\n");
    printf("├─────────────┼──────────────────┼──────────────────┤\n");
    printf("│  Order      │  LIFO            │  FIFO            │\n");
    printf("│  Add item   │  push (top)      │  enqueue (rear)  │\n");
    printf("│  Remove     │  pop (top)       │  dequeue (front) │\n");
    printf("│  Access     │  Top only        │  Front only      │\n");
    printf("│  Use case   │  Backtracking    │  Scheduling      │\n");
    printf("└─────────────┴──────────────────┴──────────────────┘\n");
    
    return 0;
}
