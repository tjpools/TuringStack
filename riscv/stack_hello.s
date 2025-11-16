# RISC-V Stack-based Hello World
# Demonstrates RISC-V's clean, consistent instruction set
# Compare with x86-64 complexity!

.data
message:    .asciz "Hello World!\n"
buffer:     .space 20

.text
.global _start

_start:
    # RISC-V uses simple, orthogonal instructions
    # All instructions are 32 bits (unlike x86's variable length)
    
    # Push "Hello World!\n" to stack character by character
    # RISC-V uses sp (stack pointer) register
    
    # Load address of message
    la      a0, message         # Load address
    li      t0, 0               # Counter
    
push_loop:
    add     t1, a0, t0          # Calculate address
    lb      t2, 0(t1)           # Load byte
    beqz    t2, push_done       # If zero, done
    
    # Push character onto stack
    addi    sp, sp, -1          # Decrement stack pointer
    sb      t2, 0(sp)           # Store byte on stack
    
    addi    t0, t0, 1           # Increment counter
    j       push_loop           # Continue
    
push_done:
    # Now pop characters from stack into buffer
    la      a1, buffer          # Buffer address
    li      t0, 0               # Counter
    
pop_loop:
    lb      t2, 0(sp)           # Load byte from stack
    addi    sp, sp, 1           # Increment stack pointer (pop)
    
    add     t1, a1, t0          # Calculate buffer address
    sb      t2, 0(t1)           # Store in buffer
    
    addi    t0, t0, 1           # Increment counter
    
    # Check if we've popped everything (compare sp with start)
    li      t3, 13              # We pushed 13 chars
    blt     t0, t3, pop_loop    # Continue if counter < 13
    
    # Null terminate buffer
    sb      zero, 0(t1)
    
    # Print buffer (using RISC-V syscall)
    li      a7, 64              # syscall: write
    li      a0, 1               # fd: stdout
    la      a1, buffer          # buffer address
    li      a2, 13              # length
    ecall                       # make syscall
    
    # Exit
    li      a7, 93              # syscall: exit
    li      a0, 0               # status: 0
    ecall

# RISC-V Architecture Notes:
# - 32 general-purpose registers (x0-x31)
# - x0 is always zero
# - sp (x2) is stack pointer
# - a0-a7 (x10-x17) are arguments/return values
# - a7 is syscall number
# - Clean, simple instruction encoding
# - No status flags (unlike x86's EFLAGS)
# - Load/store architecture (RISC philosophy)
# - Instructions are orthogonal - easy to learn!
