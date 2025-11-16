# RISC-V Architecture Comparison with x86-64

## Why RISC-V for Education?

### 1. **Simplicity**
- Fixed 32-bit instruction format (base ISA)
- No variable-length instructions like x86
- Easy to decode and understand

### 2. **Orthogonality**
- Instructions don't have special cases
- All registers can be used for all operations
- Consistent behavior

### 3. **Modern Design**
- Designed in 2010s with decades of lessons learned
- No historical baggage from 1970s (like x86)
- Clean separation of concerns

### 4. **Open Standard**
- Free to use, no licensing
- Growing ecosystem
- Used in education worldwide

## Programs

- `stack_hello.s` - Full stack demonstration with loop
- `stack_hello_simple.s` - Simplified version, character by character
- `fibonacci.s` - Recursive fibonacci with proper stack frames

## Register Comparison

### x86-64 Registers
```
rax, rbx, rcx, rdx - historical names, special purposes
rsi, rdi - source/destination for string operations
rsp, rbp - stack/base pointers
r8-r15 - "new" registers (added in 64-bit)
```

### RISC-V Registers
```
x0 - always zero (hardware enforced!)
x1 (ra) - return address
x2 (sp) - stack pointer
x8 (s0/fp) - saved register / frame pointer
x10-x17 (a0-a7) - arguments/return values
x5-x7, x28-x31 (t0-t6) - temporaries
x8-x9, x18-x27 (s0-s11) - saved registers
```

**RISC-V wins**: Consistent naming, clear purpose

## Instruction Comparison

### Pushing to Stack

**x86-64:**
```asm
push rax        ; Implicit sp decrement, 8 bytes
```

**RISC-V:**
```asm
addi sp, sp, -1    ; Explicit decrement
sb   t0, 0(sp)     ; Store byte
```

RISC-V is more explicit but more flexible (any size, any register)

### Function Calls

**x86-64:**
```asm
call func       ; Push ra, jump
ret             ; Pop ra, jump
```

**RISC-V:**
```asm
call func       ; Store ra in x1, jump (same concept!)
ret             ; Jump to ra
```

Similar, but RISC-V exposes what's happening

## Stack Frame Management

### x86-64 Prologue/Epilogue
```asm
push rbp
mov  rbp, rsp
sub  rsp, 16
; ... function body ...
mov  rsp, rbp
pop  rbp
ret
```

### RISC-V Prologue/Epilogue
```asm
addi sp, sp, -16
sd   ra, 8(sp)
sd   s0, 0(sp)
; ... function body ...
ld   s0, 0(sp)
ld   ra, 8(sp)
addi sp, sp, 16
ret
```

**RISC-V wins**: More explicit, easier to understand

## Building RISC-V Programs

### Prerequisites

**RISC-V requires either real hardware or CPU emulation.** Since most systems are x86-64, you'll need QEMU to emulate a RISC-V processor.

```bash
# Install RISC-V toolchain and QEMU emulator
# On Fedora/RHEL:
sudo dnf install qemu-user-static-riscv riscv64-linux-gnu-binutils riscv64-linux-gnu-gcc

# On Ubuntu/Debian:
sudo apt install qemu-user-static gcc-riscv64-linux-gnu binutils-riscv64-linux-gnu

# Verify installation:
qemu-riscv64-static --version
riscv64-linux-gnu-as --version
```

### Assembling
```bash
cd riscv/
riscv64-linux-gnu-as stack_hello_simple.s -o stack_hello_simple.o
riscv64-linux-gnu-ld stack_hello_simple.o -o stack_hello_simple
```

### Running with QEMU Emulation
```bash
# QEMU translates RISC-V instructions to your native CPU on-the-fly
qemu-riscv64-static ./stack_hello_simple
```

**Note**: QEMU emulates the RISC-V CPU, registers, and syscalls. Programs run slower than native but are functionally identical to running on real RISC-V hardware.

### Educational Value Without Running

Even without QEMU, the **source code itself** is educational! Compare:
- Instruction encoding (fixed 32-bit vs x86's 1-15 bytes)
- Register naming (logical x0-x31 vs historical rax/rbx)
- Stack operations (explicit vs implicit)
- Calling conventions (cleaner than x86-64)

## Learning Value

### What RISC-V Teaches

1. **Load-Store Architecture**
   - Only load/store access memory
   - All computation in registers
   - Clear separation of concerns

2. **Fixed Instruction Format**
   - Makes decoding simple
   - Shows why RISC is "Reduced"
   - Compare to x86's 1-15 byte instructions!

3. **No Flags Register**
   - Comparisons set registers, not flags
   - More explicit data flow
   - Easier to understand

4. **Modern ISA Design**
   - Vector extensions (RVV)
   - Atomic operations
   - Modular design

### Comparison Table

| Feature | x86-64 | RISC-V |
|---------|--------|---------|
| Instruction length | Variable (1-15 bytes) | Fixed (32-bit) |
| Registers | 16 general purpose | 31 general + x0 |
| Register x0 | N/A | Always zero |
| Stack | Implicit ops | Explicit |
| Flags | Yes (EFLAGS) | No |
| Design era | 1970s+ | 2010s |
| Licensing | Proprietary (Intel/AMD) | Open |
| Complexity | CISC | RISC |
| Teaching | Complex | Simple |

## The "Aha!" Moment

When you see RISC-V after x86-64, you realize:
- **ISA complexity matters** for understanding
- **Modern designs** are cleaner (hindsight is 20/20)
- **Open standards** enable innovation
- **Teaching-focused** design makes learning easier

## Side-by-Side: Push 'A'

### x86-64
```asm
mov al, 'A'
push rax
```
(2 instructions, implicit size, historical register names)

### RISC-V
```asm
li   t0, 0x41
addi sp, sp, -1
sb   t0, 0(sp)
```
(3 instructions, explicit everything, clear names)

**Both work**, but RISC-V shows exactly what's happening!

## Future of RISC-V

- Growing adoption (Western Digital, NVIDIA, Google)
- Linux kernel support
- GCC, LLVM support
- Educational standard
- Open hardware movement

---

**RISC-V represents a clean slate in ISA design, incorporating 50+ years of lessons. Perfect for learning computer architecture.**
