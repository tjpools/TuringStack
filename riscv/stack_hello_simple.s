# RISC-V Stack-based Hello World (Simple Version)
# Even cleaner demonstration

.data
hello:      .asciz "Hello World!\n"

.text
.global _start

_start:
    # Simple approach: push characters in reverse, pop forward
    
    # Push characters onto stack (in reverse order)
    li      t0, 0x0A            # '\n'
    addi    sp, sp, -1
    sb      t0, 0(sp)
    
    li      t0, 0x21            # '!'
    addi    sp, sp, -1
    sb      t0, 0(sp)
    
    li      t0, 0x64            # 'd'
    addi    sp, sp, -1
    sb      t0, 0(sp)
    
    li      t0, 0x6C            # 'l'
    addi    sp, sp, -1
    sb      t0, 0(sp)
    
    li      t0, 0x72            # 'r'
    addi    sp, sp, -1
    sb      t0, 0(sp)
    
    li      t0, 0x6F            # 'o'
    addi    sp, sp, -1
    sb      t0, 0(sp)
    
    li      t0, 0x57            # 'W'
    addi    sp, sp, -1
    sb      t0, 0(sp)
    
    li      t0, 0x20            # ' '
    addi    sp, sp, -1
    sb      t0, 0(sp)
    
    li      t0, 0x6F            # 'o'
    addi    sp, sp, -1
    sb      t0, 0(sp)
    
    li      t0, 0x6C            # 'l'
    addi    sp, sp, -1
    sb      t0, 0(sp)
    
    li      t0, 0x6C            # 'l'
    addi    sp, sp, -1
    sb      t0, 0(sp)
    
    li      t0, 0x65            # 'e'
    addi    sp, sp, -1
    sb      t0, 0(sp)
    
    li      t0, 0x48            # 'H'
    addi    sp, sp, -1
    sb      t0, 0(sp)
    
    # Now stack pointer points to complete message
    # Print directly from stack!
    
    li      a7, 64              # syscall: write
    li      a0, 1               # fd: stdout
    mv      a1, sp              # buffer: stack pointer
    li      a2, 13              # length
    ecall                       # make syscall
    
    # Clean up stack
    addi    sp, sp, 13
    
    # Exit
    li      a7, 93              # syscall: exit
    li      a0, 0               # status: 0
    ecall

# Why RISC-V is Educational:
# 1. Simple, regular instruction format
# 2. No implicit operations (x86 has many)
# 3. Clean register naming (no historical baggage)
# 4. Designed for teaching and research
# 5. Open standard (not proprietary like x86/ARM)
# 6. Modern design incorporating lessons from past
