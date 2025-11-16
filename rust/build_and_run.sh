#!/bin/bash
# Build and run Rust stack demonstrations

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║           Building Rust Stack Demonstrations             ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Check for rustc
if ! command -v rustc &> /dev/null; then
    echo "Error: rustc not found. Please install Rust:"
    echo "  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"
    exit 1
fi

echo "Building programs..."
rustc stack_hello.rs -o stack_hello && echo "  ✓ stack_hello"
rustc fibonacci.rs -o fibonacci && echo "  ✓ fibonacci"
rustc stack_vs_queue.rs -o stack_vs_queue && echo "  ✓ stack_vs_queue"

echo ""
echo "═══════════════════════════════════════════════════════════"
echo ""

echo "Running: stack_hello"
echo "─────────────────────────────────────────────────────────────"
./stack_hello
echo ""
echo "Press Enter to continue..."
read

echo "Running: fibonacci"
echo "─────────────────────────────────────────────────────────────"
./fibonacci
echo ""
echo "Press Enter to continue..."
read

echo "Running: stack_vs_queue"
echo "─────────────────────────────────────────────────────────────"
./stack_vs_queue
echo ""

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                All demonstrations complete!               ║"
echo "╚═══════════════════════════════════════════════════════════╝"
