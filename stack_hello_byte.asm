; Stack-based Hello World - Character by Character
; Demonstrates Turing's Bury/Unbury concept more explicitly
; Push each character individually, then pop to print
; x86-64 Linux Assembly

section .bss
    buffer resb 13         ; buffer for the message

section .text
    global _start

_start:
    ; BURY: Push each character of "HelloWorld!" onto stack
    ; Push in REVERSE order (LIFO)
    xor rax, rax           ; clear rax
    
    mov al, 10             ; newline
    push rax
    mov al, '!'
    push rax
    mov al, 'd'
    push rax
    mov al, 'l'
    push rax
    mov al, 'r'
    push rax
    mov al, 'o'
    push rax
    mov al, 'W'
    push rax
    mov al, ' '
    push rax
    mov al, 'o'
    push rax
    mov al, 'l'
    push rax
    mov al, 'l'
    push rax
    mov al, 'e'
    push rax
    mov al, 'H'
    push rax
    
    ; UNBURY: Pop each character from stack into buffer
    mov rdi, buffer        ; point to buffer
    mov rcx, 13            ; number of characters
    
.pop_loop:
    pop rax                ; pop character from stack
    mov [rdi], al          ; store in buffer
    inc rdi                ; move to next position
    loop .pop_loop         ; decrement rcx and loop
    
    ; Print the buffer
    mov rax, 1             ; sys_write
    mov rdi, 1             ; stdout
    mov rsi, buffer        ; our message
    mov rdx, 13            ; length
    syscall
    
    ; Exit
    mov rax, 60            ; sys_exit
    xor rdi, rdi           ; return 0
    syscall
