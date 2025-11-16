; Stack-based Hello World - Turing's Bury/Unbury Concept
; Push characters onto stack, then pop them to print
; x86-64 Linux Assembly

section .data
    newline db 10          ; newline character

section .bss
    buffer resb 13         ; buffer to collect characters (12 + null)

section .text
    global _start

_start:
    ; Push "HelloWorld!" onto stack in REVERSE order
    ; (stack is LIFO - Last In First Out)
    push 0x0A21            ; "!\n" (exclamation + newline, with padding)
    push 0x646C726F        ; "dlro" 
    push 0x57206F6C        ; "W ol"
    push 0x6C654820        ; "leH " (note: space for alignment)
    
    ; Now pop characters from stack into buffer
    mov rdi, buffer        ; rdi points to buffer
    mov rcx, 12            ; character count
    
    ; Pop 4 bytes at a time and copy to buffer
    pop rax
    mov [rdi], eax         ; copy "leH "
    add rdi, 4
    
    pop rax
    mov [rdi], eax         ; copy "W ol"
    add rdi, 4
    
    pop rax
    mov [rdi], eax         ; copy "dlro"
    add rdi, 4
    
    pop rax
    mov byte [rdi], '!'    ; just the exclamation
    inc rdi
    mov byte [rdi], 10     ; newline
    inc rdi
    mov byte [rdi], 0      ; null terminator

    ; Print the buffer
    mov rax, 1             ; sys_write
    mov rdi, 1             ; stdout
    mov rsi, buffer        ; message buffer
    add rsi, 1             ; skip the space padding
    mov rdx, 12            ; length
    syscall

    ; Exit
    mov rax, 60            ; sys_exit
    xor rdi, rdi           ; return 0
    syscall
