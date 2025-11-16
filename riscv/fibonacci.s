# RISC-V Fibonacci Recursive
# Shows RISC-V calling convention and stack frame management

.data
result_msg: .asciz "fib(10) = "
newline:    .asciz "\n"

.text
.global _start

# Fibonacci function
# Input: a0 = n
# Output: a0 = fib(n)
# Uses stack for recursive calls
fibonacci:
    # Stack frame setup
    addi    sp, sp, -16         # Allocate stack frame
    sd      ra, 8(sp)           # Save return address
    sd      s0, 0(sp)           # Save saved register
    
    # Base case: if n <= 1, return n
    li      t0, 1
    ble     a0, t0, fib_base_case
    
    # Recursive case: fib(n-1) + fib(n-2)
    mv      s0, a0              # Save n in saved register
    
    # Call fib(n-1)
    addi    a0, s0, -1          # n-1
    call    fibonacci
    mv      t1, a0              # Save fib(n-1) result
    
    # Call fib(n-2)
    addi    a0, s0, -2          # n-2
    call    fibonacci
    
    # Add results
    add     a0, a0, t1          # fib(n-1) + fib(n-2)
    
    j       fib_return

fib_base_case:
    # n <= 1, return n (already in a0)
    
fib_return:
    # Restore stack frame
    ld      s0, 0(sp)           # Restore saved register
    ld      ra, 8(sp)           # Restore return address
    addi    sp, sp, 16          # Deallocate stack frame
    ret                         # Return

# Print integer function
# Input: a0 = number to print
print_int:
    addi    sp, sp, -16
    sd      ra, 8(sp)
    sd      s0, 0(sp)
    
    mv      s0, a0              # Save number
    
    # Convert to string (simplified - just print digit by digit)
    # For demonstration, we'll use a simple approach
    
    # Restore and return
    ld      s0, 0(sp)
    ld      ra, 8(sp)
    addi    sp, sp, 16
    ret

_start:
    # Print message
    li      a7, 64              # syscall: write
    li      a0, 1               # fd: stdout
    la      a1, result_msg      # buffer
    li      a2, 11              # length
    ecall
    
    # Calculate fib(10)
    li      a0, 10
    call    fibonacci
    
    # Result is in a0
    # For now, just exit (printing numbers requires more code)
    
    # Exit
    li      a7, 93              # syscall: exit
    mv      a0, zero            # status: 0
    ecall

# RISC-V Calling Convention:
# - a0-a7: arguments/return values
# - ra: return address
# - sp: stack pointer
# - s0-s11: saved registers (callee-saved)
# - t0-t6: temporary registers (caller-saved)
# 
# Stack frame layout (grows downward):
# sp+16: saved ra
# sp+8:  saved s0
# sp+0:  (stack grows down)
#
# Much cleaner than x86-64's complex conventions!
