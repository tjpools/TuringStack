#!/bin/bash
# Run all Python stack demonstrations

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║              Python Stack Demonstrations                  ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

echo "=== 1. Stack Hello World ==="
python3 stack_hello.py
echo ""
echo "Press Enter to continue..."
read

echo "=== 2. Stack Frames ==="
python3 stack_frames.py
echo ""
echo "Press Enter to continue..."
read

echo "=== 3. Fibonacci Approaches ==="
python3 fibonacci.py
echo ""
echo "Press Enter to continue..."
read

echo "=== 4. Stack vs Queue ==="
python3 stack_vs_queue.py
echo ""
echo "Press Enter to continue..."
read

echo "=== 5. Stack Overflow Protection ==="
python3 stack_overflow.py
echo ""

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                All demonstrations complete!               ║"
echo "╚═══════════════════════════════════════════════════════════╝"
