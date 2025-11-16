AS = nasm
ASFLAGS = -f elf64
LD = ld
CC = gcc
CFLAGS = -Wall -g

# Binary names
ASM_BINS = stack_hello_asm stack_hello_byte_asm
BASIC_C_BINS = stack_hello_c stack_hello_simple_c
ADVANCED_C_BINS = stack_frames_c fibonacci_c stack_overflow_c stack_vs_queue_c
ALL_BINS = $(ASM_BINS) $(BASIC_C_BINS) $(ADVANCED_C_BINS)

all: $(ALL_BINS)

# Assembly versions
stack_hello_asm: stack_hello.o
	$(LD) -o $@ $<

stack_hello_byte_asm: stack_hello_byte.o
	$(LD) -o $@ $<

stack_hello.o: stack_hello.asm
	$(AS) $(ASFLAGS) -o $@ $<

stack_hello_byte.o: stack_hello_byte.asm
	$(AS) $(ASFLAGS) -o $@ $<

# Basic C versions
stack_hello_c: stack_hello.c
	$(CC) $(CFLAGS) -o $@ $<

stack_hello_simple_c: stack_hello_simple.c
	$(CC) $(CFLAGS) -o $@ $<

# Advanced C demonstrations
stack_frames_c: stack_frames.c
	$(CC) $(CFLAGS) -o $@ $<

fibonacci_c: fibonacci.c
	$(CC) $(CFLAGS) -o $@ $<

stack_overflow_c: stack_overflow.c
	$(CC) $(CFLAGS) -o $@ $<

stack_vs_queue_c: stack_vs_queue.c
	$(CC) $(CFLAGS) -o $@ $<

# Convenience targets
basic: $(ASM_BINS) $(BASIC_C_BINS)
	@echo "Built basic programs"

advanced: $(ADVANCED_C_BINS)
	@echo "Built advanced programs"

clean:
	rm -f *.o $(ALL_BINS)

# Testing targets
test: test-basic test-advanced

test-basic: $(ASM_BINS) $(BASIC_C_BINS)
	@echo "╔═══════════════════════════════════════════════════════╗"
	@echo "║           BASIC STACK OPERATIONS TESTS                ║"
	@echo "╚═══════════════════════════════════════════════════════╝"
	@echo ""
	@echo "=== Testing Assembly (word-based) ==="
	./stack_hello_asm
	@echo ""
	@echo "=== Testing Assembly (byte-by-byte) ==="
	./stack_hello_byte_asm
	@echo ""
	@echo "=== Testing C (with visualization) ==="
	./stack_hello_c
	@echo ""
	@echo "=== Testing C (simple) ==="
	./stack_hello_simple_c
	@echo ""

test-advanced: $(ADVANCED_C_BINS)
	@echo "╔═══════════════════════════════════════════════════════╗"
	@echo "║          ADVANCED STACK CONCEPTS TESTS                ║"
	@echo "╚═══════════════════════════════════════════════════════╝"
	@echo ""
	@echo "=== Testing Stack Frames (nested calls) ==="
	./stack_frames_c
	@echo ""
	@echo "=== Testing Fibonacci (recursion) ==="
	./fibonacci_c
	@echo ""
	@echo "=== Testing Stack Overflow (limits) ==="
	./stack_overflow_c
	@echo ""
	@echo "=== Testing Stack vs Queue (LIFO vs FIFO) ==="
	./stack_vs_queue_c
	@echo ""

test-frames: stack_frames_c
	./stack_frames_c

test-fib: fibonacci_c
	./fibonacci_c

test-overflow: stack_overflow_c
	./stack_overflow_c

test-queue: stack_vs_queue_c
	./stack_vs_queue_c

# Help target
help:
	@echo "Stack Operations Masterclass - Build System"
	@echo ""
	@echo "Targets:"
	@echo "  make              - Build all programs"
	@echo "  make basic        - Build basic demos only"
	@echo "  make advanced     - Build advanced demos only"
	@echo "  make test         - Run all tests"
	@echo "  make test-basic   - Run basic tests only"
	@echo "  make test-advanced - Run advanced tests only"
	@echo "  make test-frames  - Run stack frames demo"
	@echo "  make test-fib     - Run fibonacci demo"
	@echo "  make test-overflow - Run stack overflow demo"
	@echo "  make test-queue   - Run stack vs queue demo"
	@echo "  make clean        - Remove all build artifacts"
	@echo "  make help         - Show this help message"

.PHONY: all basic advanced clean test test-basic test-advanced test-frames test-fib test-overflow test-queue help
