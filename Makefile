AS = nasm
ASFLAGS = -f elf64
LD = ld
CC = gcc
CFLAGS = -Wall -g

# Basic programs
BASIC_TARGETS = stack_hello_asm stack_hello_byte_asm stack_hello_c stack_hello_simple_c

# Advanced programs
ADVANCED_TARGETS = stack_frames_c fibonacci_c stack_overflow_c stack_vs_queue_c

all: $(BASIC_TARGETS) $(ADVANCED_TARGETS)

# Assembly versions
stack_hello_asm: stack_hello.o
	$(LD) -o $@ $<

stack_hello_byte_asm: stack_hello_byte.o
	$(LD) -o $@ $<

stack_hello.o: stack_hello.asm
	$(AS) $(ASFLAGS) -o $@ $<

stack_hello_byte.o: stack_hello_byte.asm
	$(AS) $(ASFLAGS) -o $@ $<

# C versions
stack_hello_c: stack_hello.c
	$(CC) $(CFLAGS) -o $@ $<

stack_hello_simple_c: stack_hello_simple.c
	$(CC) $(CFLAGS) -o $@ $<

# Advanced C programs
stack_frames_c: stack_frames.c
	$(CC) $(CFLAGS) -o $@ $<

fibonacci_c: fibonacci.c
	$(CC) $(CFLAGS) -o $@ $<

stack_overflow_c: stack_overflow.c
	$(CC) $(CFLAGS) -o $@ $<

stack_vs_queue_c: stack_vs_queue.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f *.o $(BASIC_TARGETS) $(ADVANCED_TARGETS)

# Test targets
basic: $(BASIC_TARGETS)

advanced: $(ADVANCED_TARGETS)

test-basic: $(BASIC_TARGETS)
	@echo "=== Testing Assembly (word-based) ==="
	./stack_hello_asm
	@echo "\n=== Testing Assembly (byte-by-byte) ==="
	./stack_hello_byte_asm
	@echo "\n=== Testing C (with visualization) ==="
	./stack_hello_c
	@echo "\n=== Testing C (simple) ==="
	./stack_hello_simple_c

test-advanced: $(ADVANCED_TARGETS)
	@echo "=== Testing Stack Frames ==="
	./stack_frames_c
	@echo "\n=== Testing Fibonacci ==="
	./fibonacci_c
	@echo "\n=== Testing Stack Overflow ==="
	./stack_overflow_c
	@echo "\n=== Testing Stack vs Queue ==="
	./stack_vs_queue_c

test: test-basic test-advanced

# Individual test targets
test-fibonacci: fibonacci_c
	./fibonacci_c

test-stack-frames: stack_frames_c
	./stack_frames_c

test-overflow: stack_overflow_c
	./stack_overflow_c

test-queue: stack_vs_queue_c
	./stack_vs_queue_c

help:
	@echo "TuringStack Makefile"
	@echo "===================="
	@echo "Targets:"
	@echo "  all            - Build all programs (basic + advanced)"
	@echo "  basic          - Build only basic stack demos"
	@echo "  advanced       - Build advanced demos (frames, fibonacci, etc)"
	@echo "  clean          - Remove all binaries and object files"
	@echo "  test           - Run all tests (basic + advanced)"
	@echo "  test-basic     - Run basic tests only"
	@echo "  test-advanced  - Run advanced tests only"
	@echo "  test-fibonacci - Run fibonacci test only"
	@echo "  test-stack-frames - Run stack frames test only"
	@echo "  test-overflow  - Run stack overflow test only"
	@echo "  test-queue     - Run stack vs queue test only"
	@echo "  help           - Show this help message"

.PHONY: all basic advanced clean test test-basic test-advanced test-fibonacci test-stack-frames test-overflow test-queue help
